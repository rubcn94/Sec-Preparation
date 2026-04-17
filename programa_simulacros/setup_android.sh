#!/data/data/com.termux/files/usr/bin/bash

# Script para lanzar GymTracker en Termux (Android)
# Uso: Termux:Widget o ejecutar manualmente en Termux

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Ruta al proyecto (ADAPTADA para Termux/Android)
# En Android, la ruta equivalente sería algo como:
# /storage/emulated/0/Proyectos/Acabado/programa_simulacros
PROJECT_DIR="/storage/emulated/0/Documents/Acabado/programa_simulacros"

# Verificar que existe la carpeta
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${YELLOW}⚠️  Carpeta no encontrada: $PROJECT_DIR${NC}"
    echo -e "${YELLOW}Verifica que Syncthing haya sincronizado los archivos${NC}"
    echo -e "${BLUE}📁 Las carpetas en Android están en /storage/emulated/0/${NC}"
    exit 1
fi

# Buscar cualquier archivo HTML en el directorio
HTML_FILE=$(find "$PROJECT_DIR" -maxdepth 1 -name "*.html" -type f | head -n 1)

# Verificar que existe algún HTML
if [ -z "$HTML_FILE" ]; then
    echo -e "${YELLOW}⚠️  No se encontraron archivos HTML en el directorio${NC}"
    echo -e "${BLUE}📄 Buscando: ${PROJECT_DIR}/*.html${NC}"
    exit 1
fi

# Obtener solo el nombre del archivo
HTML_NAME=$(basename "$HTML_FILE")

# Matar servidor previo si existe
pkill -f "python.*http.server.*8001" 2>/dev/null

# Cambiar al directorio del proyecto
cd "$PROJECT_DIR" || exit 1

# Mostrar info
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}💪 GymTracker - Entrenamiento${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📂 Proyecto:${NC} $PROJECT_DIR"
echo -e "${BLUE}📄 Archivo:${NC} $HTML_NAME"
echo -e "${BLUE}🌐 URL:${NC} http://localhost:8001/$HTML_NAME"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Iniciar servidor HTTP en background
echo -e "${YELLOW}🚀 Iniciando servidor...${NC}"
python -m http.server 8001 --bind 127.0.0.1 > /dev/null 2>&1 &
SERVER_PID=$!

# Esperar a que el servidor esté listo
sleep 2

# Verificar que el servidor está corriendo
if ps -p $SERVER_PID > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Servidor corriendo (PID: $SERVER_PID)${NC}"
    
    # Intentar abrir en navegador de Termux
    echo -e "${YELLOW}🌐 Abriendo navegador...${NC}"
    termux-open-url "http://localhost:8001/$HTML_NAME"
    
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}✅ Todo listo!${NC}"
    echo -e "${BLUE}ℹ️  El servidor seguirá corriendo en segundo plano${NC}"
    echo -e "${BLUE}ℹ️  Para detenerlo:${NC} pkill -f 'python.*http.server.*8001'"
    echo -e "${BLUE}ℹ️  Si no abre el navegador, accede manualmente a la URL${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
else
    echo -e "${YELLOW}❌ Error al iniciar el servidor${NC}"
    echo -e "${BLUE}Verifica que Python esté instalado:${NC} pkg install python"
    exit 1
fi