#!/usr/bin/env python3
"""
小說翻譯器 - 本地伺服器
雙擊啟動，或在命令列執行 python server.py
預設監聽 http://localhost:5678
"""

import os
import json
import shutil
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

PORT = 5678
ALLOWED_ORIGIN = "*"

class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", ALLOWED_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # 健康檢查
        if path == "/ping":
            self._json({"ok": True, "version": "v2"})

        # 列出資料夾內的 txt 檔案
        elif path == "/list":
            from urllib.parse import parse_qs
            params = parse_qs(parsed.query)
            folder = params.get("folder", [None])[0]
            if not folder or not os.path.isdir(folder):
                self._error(400, "資料夾不存在或路徑錯誤")
                return
            files = [
                f for f in os.listdir(folder)
                if f.lower().endswith(".txt") and os.path.isfile(os.path.join(folder, f))
            ]
            files.sort()
            self._json({"files": files, "count": len(files)})

        # 讀取單一 txt 檔案內容
        elif path == "/read":
            from urllib.parse import parse_qs
            params = parse_qs(parsed.query)
            filepath = params.get("file", [None])[0]
            if not filepath or not os.path.isfile(filepath):
                self._error(400, "檔案不存在")
                return
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                self._json({"content": content, "size": len(content)})
            except Exception as e:
                self._error(500, str(e))

        else:
            self._error(404, "未知端點")

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        # 檢查輸出資料夾是否已存在
        if path == "/check":
            folder = body.get("folder", "")
            if not folder:
                self._error(400, "未提供資料夾路徑")
                return
            parent = os.path.dirname(folder.rstrip("/\\"))
            base   = os.path.basename(folder.rstrip("/\\"))
            output_name = base + "_翻譯"
            output_path = os.path.join(parent, output_name)
            exists = os.path.exists(output_path)
            self._json({
                "exists": exists,
                "output_path": output_path,
                "output_name": output_name
            })

        # 建立輸出資料夾
        elif path == "/mkdir":
            folder = body.get("folder", "")
            if not folder:
                self._error(400, "未提供資料夾路徑")
                return
            try:
                os.makedirs(folder, exist_ok=False)
                self._json({"ok": True, "created": folder})
            except FileExistsError:
                self._error(409, f"資料夾已存在：{folder}")
            except Exception as e:
                self._error(500, str(e))

        # 寫入翻譯結果
        elif path == "/write":
            filepath = body.get("file", "")
            content  = body.get("content", "")
            if not filepath:
                self._error(400, "未提供檔案路徑")
                return
            try:
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                self._json({"ok": True, "written": filepath})
            except Exception as e:
                self._error(500, str(e))

        else:
            self._error(404, "未知端點")

    def _json(self, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_cors()
        self.end_headers()
        self.wfile.write(body)

    def _error(self, code, msg):
        body = json.dumps({"error": msg}, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_cors()
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("=" * 50)
    print("  小說翻譯器 本地伺服器")
    print(f"  監聽位址：http://localhost:{PORT}")
    print("  關閉請按 Ctrl+C")
    print("=" * 50)
    server = HTTPServer(("localhost", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n伺服器已關閉")
