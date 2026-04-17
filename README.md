<<<<<<< HEAD
# Security+ SY0-701 - Material de Preparación Completo

> **Objetivo:** Aprobar CompTIA Security+ SY0-701 con 85%+ antes de mayo 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status: Production](https://img.shields.io/badge/Status-Production-green.svg)
![Version: 2.0](https://img.shields.io/badge/Version-2.0-blue.svg)

---

## 📋 Descripción

Repositorio completo de materiales de estudio para la certificación **CompTIA Security+ SY0-701**, incluyendo:

- ✅ **382 flashcards** priorizadas (220 ALTA + 162 MEDIA)
- ✅ **Sistema de simulacros** con 2292 preguntas reales
- ✅ **15 laboratorios prácticos** (~17 horas)
- ✅ **20 ejemplos de análisis de logs**
- ✅ **12 ejercicios de cálculos** (RTO, RPO, ALE, etc.)
- ✅ **Glosarios interactivos** con errores comunes
- ✅ **Plan de estudio de 8 semanas** estructurado
- ✅ **Sincronización multiplataforma** (PC + Android)

---

## 📁 Estructura del Proyecto

```
Sec+/
├── 📂 programa_simulacros/          # Sistema de simulacros (PRINCIPAL)
│   ├── SimulacroSecPlusmegabank.html
│   ├── mega_bank.json               # 2292 preguntas
│   ├── INICIAR.bat                  # Windows launcher
│   ├── iniciar_android.sh           # Android launcher
│   ├── iniciar_api.py               # API con sincronización
│   ├── secplus_progress.json        # Progreso Round-Robin
│   └── README.md                    # Guía completa (PC + Android)
│
├── 📂 01_Errores_Simulacros/        # Análisis de errores por simulacro
│   ├── Simulacro_#22_Errores.md
│   ├── Simulacro_#23_Errores.md
│   └── ...                          # 11 simulacros analizados
│
├── 📂 Simulacros/                   # Simulacros realizados
│   └── (Resultados históricos)
│
├── 📂 segundachance/                # Preguntas para repasar
│   └── (Errores recurrentes)
│
├── 📂 00_Archivo/                   # Material legacy/backup
│   ├── SecPlus_SY0-701_COMPLETO.pdf
│   ├── SecPlus_SY0-701_Diccionario_Completo.json
│   ├── SecPlus_SY0-701_SOC_COMPLETO.json
│   └── ...                          # Material de referencia
│
├── 📄 Glosario_Errores_Simulacros.html  # Términos de errores frecuentes
├── 📄 GUIA_TIPOS_PREGUNTAS.md           # Estrategias por tipo de pregunta
├── 📄 .project-context.json             # Contexto del proyecto (auto-carga)
└── 📄 README.md                         # Este archivo
```

---

## 🚀 Quick Start

### Opción 1: Sistema de Simulacros (Recomendado)

**En Windows:**
```bash
cd programa_simulacros
# Doble clic en INICIAR.bat
```

**En Android:**
- Ver guía completa: [`programa_simulacros/README.md`](programa_simulacros/README.md)
- Configuración widget Termux (1 tap → listo)

### Opción 2: Glosarios y Flashcards

1. **Abrir glosarios HTML:**
   - `Glosario_Errores_Simulacros.html` - Errores comunes

2. **Importar flashcards** (si usas Anki/Quizlet):
   - Los archivos JSON en `00_Archivo/` son compatibles con importación

---

## 📊 Sistema de Simulacros

### Características principales

- **2292 preguntas** de los 5 dominios Security+ SY0-701
- **Sistema Round-Robin** (evita repeticiones hasta agotar el banco)
- **5 tipos de pregunta:** Single, Multi-select, Ordering, Matching, True/False
- **Temporizador configurable** (0 = sin límite)
- **Filtrado por dominio y tipo** (personaliza tu simulacro)
- **Exportación de errores a Markdown** (repasa solo lo que fallaste)
- **100% offline** (no requiere Internet)
- **Sincronización de progreso** entre dispositivos (Syncthing)

### Dominios cubiertos

| Dominio | % Examen | Preguntas |
|---------|----------|-----------|
| 1.0 General Security Concepts | 12% | ~275 |
| 2.0 Threats, Vulnerabilities & Mitigations | 22% | ~504 |
| 3.0 Security Architecture | 18% | ~413 |
| 4.0 Security Operations | 28% | ~642 |
| 5.0 Security Program Management | 20% | ~458 |

### Uso rápido

```bash
# Windows
cd programa_simulacros
INICIAR.bat

# Linux/Mac
cd programa_simulacros
python iniciar_api.py
```

**Guía detallada:** [`programa_simulacros/README.md`](programa_simulacros/README.md)

---

## 📚 Recursos Incluidos

### Material de Estudio

| Recurso | Descripción | Ubicación |
|---------|-------------|-----------|
| **Flashcards** | 382 flashcards (220 ALTA prioridad) | `00_Archivo/*.json` |
| **Diccionario** | Términos técnicos completos | `00_Archivo/SecPlus_SY0-701_Diccionario_Completo.json` |
| **Material SOC** | Enfoque SOC Analyst | `00_Archivo/SecPlus_SY0-701_SOC_COMPLETO.json` |
| **PDF Completo** | Temario completo español | `00_Archivo/SecPlus_SY0-701_COMPLETO.pdf` |
| **Guía Dominios** | Resumen 5 dominios | `00_Archivo/Guia_Completa_5_Dominios.pdf` |

### Herramientas de Repaso

| Herramienta | Propósito | Archivo |
|-------------|-----------|---------|
| **Glosario Errores** | Términos de errores frecuentes | `Glosario_Errores_Simulacros.html` |
| **Guía Tipos** | Estrategias por tipo de pregunta | `GUIA_TIPOS_PREGUNTAS.md` |
| **Análisis Errores** | Revisión de simulacros previos | `01_Errores_Simulacros/*.md` |

---

## 🎯 Plan de Estudio

### Resumen de 8 Semanas

**Ver plan completo:** `00_Archivo/SecPlus_Plan_Estudio_8_Semanas.md`

| Semana | Enfoque | Actividades |
|--------|---------|-------------|
| 1-2 | **Fundamentos** | Dominios 1.0 + Laboratorios básicos |
| 3-4 | **Amenazas y Mitigación** | Dominio 2.0 + Análisis de logs |
| 5-6 | **Arquitectura y Operaciones** | Dominios 3.0 y 4.0 + Labs avanzados |
| 7 | **Gestión de Seguridad** | Dominio 5.0 + Cálculos (RTO, ALE) |
| 8 | **Repaso Final** | Simulacros + Flashcards ALTA |

### Estrategia Recomendada

1. **Días 1-5 por semana:** Teoría + Flashcards (2-3 horas/día)
2. **Día 6:** Laboratorios prácticos (4-5 horas)
3. **Día 7:** Simulacro completo + Análisis de errores (3-4 horas)
4. **Repaso nocturno:** 30 min de flashcards ALTA prioridad

---

## 🔧 Requisitos Técnicos

### Windows
- Python 3.8+ (para simulacros con sincronización)
- Navegador moderno (Chrome, Firefox, Edge)

### Android
- **Termux** + **Termux:Widget** (F-Droid)
- Python en Termux: `pkg install python`
- Navegador (Chrome recomendado)

### Opcional
- **Syncthing** (sincronización de progreso entre dispositivos)
- **Git** (control de versiones de tus notas)

---

## 📱 Sincronización Multiplataforma

El sistema de simulacros permite sincronizar tu progreso entre dispositivos usando **Syncthing**.

**Archivo sincronizado:** `programa_simulacros/secplus_progress.json`

**Guía completa:** [`programa_simulacros/SINCRONIZACION.md`](programa_simulacros/SINCRONIZACION.md)

### Ventajas

- ✅ Mismo progreso Round-Robin en PC y móvil
- ✅ Evita repetir preguntas ya vistas
- ✅ Sincronización automática en tiempo real
- ✅ No requiere Internet (sincronización local)

---

## 🎓 Áreas de Enfoque Prioritarias

Basado en errores comunes en simulacros:

1. **Controles de seguridad** (preventivo/detective/correctivo/compensatorio)
2. **Criptografía** (PKI, certificados, algoritmos, key exchange)
3. **Network security** (firewalls, IDS/IPS, VPN, NAC)
4. **Cloud security** (IaaS/PaaS/SaaS, responsabilidad compartida)
5. **Incident response** (fases PICERL, chain of custody)
6. **Risk management** (ALE, SLE, ARO, RTO, RPO, MTBF, MTTR)

---

## 🤝 Contribución

Este es un repositorio personal de estudio, pero si encuentras errores o mejoras:

1. **Errores en preguntas:** Documentar en `01_Errores_Simulacros/`
2. **Mejoras en flashcards:** Usar formato estándar (ver `.project-context.json`)
3. **Nuevas nemotecnias:** Añadir en flashcards con campo `nemo`

---

## 📝 Notas Importantes

### ⚠️ Advertencias

- **NO borrar** flashcards ALTA prioridad sin verificar
- **NO modificar** estructura de `mega_bank.json` (rompe el HTML)
- **SIEMPRE** validar JSON antes de guardar
- **BACKUP** antes de cambios masivos

### 💡 Tips

- Flashcards ALTA son de errores reales → Revisar primero
- Nemotecnias visuales funcionan mejor
- Usar patrones de examen para predecir trampas
- Relacionar conceptos nuevos con conocimientos previos
- **Priorizar razonamiento sobre memorización**

---

## 📊 Progreso Actual

- ✅ Material de estudio completo
- ✅ Sistema de simulacros operativo
- ✅ 382 flashcards priorizadas
- ✅ 11 simulacros analizados
- ⏳ En preparación activa (Semana X de 8)
- 🎯 **Objetivo:** 85%+ en examen real

---

## 📜 Licencia

Este proyecto está bajo licencia MIT - ver [LICENSE](LICENSE) para detalles.

---

## 📞 Contacto

**Proyecto:** Preparación Security+ SY0-701
**Objetivo:** Aprobar antes de mayo 2026
**Última actualización:** Abril 2026

---

**¡Éxito en tu certificación! 🚀**
=======
# Sec-Preparation

>>>>>>> 1f53cec6d73604458ec8095e7ab9c4d8173c8a78
