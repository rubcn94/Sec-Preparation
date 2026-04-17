#!/usr/bin/env python3
"""
Security+ Simulacro - Servidor con API REST para sincronización de progreso
Guarda el progreso Round-Robin en secplus_progress.json (sincronizable con Syncthing)
"""

import http.server
import socketserver
import os
import subprocess
import time
import threading
import json
from urllib.parse import urlparse, parse_qs
from datetime import datetime

PORT = 8000
FOLDER = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(FOLDER, 'secplus_progress.json')

os.chdir(FOLDER)

# Inicializar archivo de progreso si no existe
if not os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            'ask_counts': {},
            'last_updated': datetime.utcnow().isoformat() + 'Z',
            'version': '1.0'
        }, f, indent=2)

class SecPlusAPIHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        """Handle preflight CORS requests"""
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests for progress data"""
        parsed = urlparse(self.path)

        if parsed.path == '/api/progress':
            # Leer progreso desde archivo
            try:
                with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            # Servir archivos estáticos normalmente
            super().do_GET()

    def do_POST(self):
        """Handle POST requests to save progress"""
        parsed = urlparse(self.path)

        if parsed.path == '/api/progress':
            try:
                # Leer datos del body
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                data = json.loads(body.decode('utf-8'))

                # Actualizar timestamp
                data['last_updated'] = datetime.utcnow().isoformat() + 'Z'
                data['version'] = '1.0'

                # Guardar en archivo
                with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok', 'saved': True}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Silenciar logs excepto errores
        if '500' in str(args) or '404' in str(args):
            super().log_message(format, *args)

def find_free_port(start_port=8000, max_attempts=10):
    import socket
    for port in range(start_port, start_port + max_attempts):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("", port))
            sock.close()
            return port
        except OSError:
            continue
    return 8000

PORT = find_free_port()

socketserver.TCPServer.allow_reuse_address = True

print("=" * 60)
print(" 🔐 SECURITY+ SY0-701 SIMULACRO")
print("=" * 60)
print(f"\n✅ Servidor con API REST iniciado en puerto {PORT}")
print(f"📂 Progreso guardado en: {PROGRESS_FILE}")
print(f"🔄 Sincronizable con Syncthing")
print(f"\n⚠️  Presiona Ctrl+C para detener")
print("=" * 60)

def open_browser():
    """Espera 2 segundos y abre el navegador"""
    time.sleep(2)
    url = f"http://localhost:{PORT}/SimulacroSecPlusmegabank.html"
    try:
        # Intentar abrir con termux-open (Termux en Android)
        subprocess.run(['termux-open-url', url], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"🌐 Navegador abierto automáticamente")
    except FileNotFoundError:
        # Si no está en Termux, intentar webbrowser normal (PC)
        try:
            import webbrowser
            webbrowser.open(url)
            print(f"🌐 Navegador abierto automáticamente")
        except:
            print(f"\n🌐 Abre manualmente: {url}")

# Abrir navegador en segundo plano
threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), SecPlusAPIHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor detenido")
