# Simulacro Security+ SY0-701

Sistema de simulacros de examen con 2292 preguntas.

---

## 🖥️ Uso en PC (Windows)

**Doble clic en `INICIAR.bat`**

Se abre automáticamente el navegador con el simulacro.

---

## 📱 Uso en Android

### Opción 1: Widget en pantalla de inicio (RECOMENDADO)

**Un solo tap para lanzar todo** - Ver guía completa: **[ANDROID_SETUP.md](ANDROID_SETUP.md)**

**Instalación rápida:**
1. Instalar **Termux** + **Termux:Widget** + **Termux:API** desde F-Droid
2. En Termux:
   ```bash
   pkg update && pkg install python termux-api
   termux-setup-storage
   mkdir -p ~/.shortcuts
   cp /storage/emulated/0/Documents/Acabado/programa_simulacros/iniciar_android.sh ~/.shortcuts/SecPlus-Simulacro
   chmod +x ~/.shortcuts/SecPlus-Simulacro
   ```
3. Añadir widget **Termux:Widget** a la pantalla de inicio
4. ✅ **Tap en el widget** → Servidor lanzado + Navegador abierto

### Opción 2: Manual (método tradicional)

```bash
cd /storage/emulated/0/Documents/Acabado/programa_simulacros
python iniciar.py
```

### Opción 3: Auto-inicio al arrancar (opcional)

Para que el servidor esté **siempre disponible** sin tocar nada → Ver **[ANDROID_AUTOSTART.md](ANDROID_AUTOSTART.md)**

⚠️ **Solo recomendado si estudias todos los días** (consume batería en segundo plano)

---

## 📦 Archivos incluidos

**Core:**
- `SimulacroSecPlusmegabank.html` - Interfaz web del simulacro
- `mega_bank.json` - Base de datos (2292 preguntas)

**Lanzadores:**
- `INICIAR.bat` - Windows (usa iniciar_api.py con sincronización)
- `iniciar.py` - Servidor simple (sin sincronización)
- `iniciar_api.py` - Servidor con API REST (sincronización de progreso) ⭐
- `iniciar_android.sh` - Android (Termux:Widget)

**Datos sincronizables:**
- `secplus_progress.json` - Progreso Round-Robin (sincronizable con Syncthing) ⭐

**Documentación:**
- `README.md` - Guía principal
- `SINCRONIZACION.md` - Cómo sincronizar progreso entre dispositivos ⭐
- `ANDROID_SETUP.md` - Configuración Android con widget
- `ANDROID_AUTOSTART.md` - Auto-inicio opcional (avanzado)

**Extras:**
- `secplus_completo.json` - Banco adicional (220 preguntas)
- `secplus_nemotecnia.json` - Banco nemotécnico (84 preguntas)

**Total:** ~2.5 MB

---

## ✨ Características

- ✅ **2292 preguntas** de los 5 dominios Security+ SY0-701
- ✅ **Sistema Round-Robin** (evita repetir preguntas hasta agotar todo el banco)
- ✅ **5 tipos de pregunta:** Single, Multi-select, Ordering, Matching, True/False
- ✅ **Temporizador configurable** (0 = sin límite)
- ✅ **Filtrado por dominio y tipo** (personaliza tu simulacro)
- ✅ **Exportación de errores a Markdown** (repasa solo lo que fallaste)
- ✅ **100% offline** (no requiere Internet una vez descargado)
- ✅ **Compatible PC y Android** (mismo banco, mismas funciones)
- ✅ **Acceso directo Android** vía Termux:Widget (1 tap → listo)
- ✅ **Sincronización de progreso** entre dispositivos vía Syncthing ⭐ NUEVO

---

## 📊 Notas técnicas

### Sistema de persistencia

**Nuevo:** El progreso Round-Robin se guarda en `secplus_progress.json` (sincronizable)

- ✅ **Prioridad:** API REST → `secplus_progress.json` (archivo sincronizable)
- ✅ **Fallback:** localStorage del navegador si el servidor no está disponible
- ✅ **Sincronización:** Usa Syncthing para tener el mismo progreso en todos tus dispositivos

Ver guía completa: **[SINCRONIZACION.md](SINCRONIZACION.md)**

### Configuración

- Puerto por defecto: 8000 (encuentra automáticamente uno libre si está ocupado)
- Para resetear estadísticas: Click en "reset" en la pantalla de inicio o borrar `secplus_progress.json`
- No requiere conexión a Internet una vez descargado

---

## 🔧 Troubleshooting

**Problema:** El navegador no se abre automáticamente en Android

**Solución:** Abre Chrome manualmente y ve a:
```
http://localhost:8000/SimulacroSecPlusmegabank.html
```

**Problema:** Puerto 8000 ocupado

**Solución:** El script encuentra automáticamente un puerto libre (8001, 8002, etc.)

---

---

## 🎯 Flujo de trabajo recomendado

### En PC (Windows)
1. Doble clic `INICIAR.bat`
2. Estudiar
3. Descargar errores (.md)
4. Cerrar navegador (servidor se detiene automáticamente)

### En Android (con widget)
1. **Tap** en widget "SecPlus-Simulacro"
2. Estudiar en el navegador
3. Cerrar navegador cuando termines
4. El servidor sigue corriendo (si quieres detenerlo: tap en widget "SecPlus-Stop")

---

**Última actualización:** 2026-04-12
