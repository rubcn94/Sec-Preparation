#!/usr/bin/env python3
import http.server
import socketserver
import os
import subprocess
import time
import threading

PORT = 8000
FOLDER = os.path.dirname(os.path.abspath(__file__))

os.chdir(FOLDER)

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Silenciar logs para mejor rendimiento en móvil
        pass

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

print("=" * 50)
print(" SIMULACRO SECURITY+ SY0-701")
print("=" * 50)
print(f"\nServidor iniciado en puerto {PORT}")
print(f"Presiona Ctrl+C para detener")
print("=" * 50)

def open_browser():
    """Espera 2 segundos y abre el navegador"""
    time.sleep(2)
    url = f"http://localhost:{PORT}/SimulacroSecPlusmegabank.html"
    try:
        # Intentar abrir con termux-open (Termux en Android)
        subprocess.run(['termux-open-url', url], check=False)
        print(f"\nNavegador abierto automaticamente")
    except FileNotFoundError:
        # Si no está en Termux, intentar webbrowser normal (PC)
        try:
            import webbrowser
            webbrowser.open(url)
            print(f"\nNavegador abierto automaticamente")
        except:
            print(f"\nAbre manualmente: {url}")

# Abrir navegador en segundo plano
threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido")
