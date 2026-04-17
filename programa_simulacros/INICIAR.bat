@echo off
title Simulacro Security+
cls
echo ========================================
echo   Iniciando Simulacro Security+
echo   Con sincronizacion de progreso
echo ========================================
echo.
cd /d "%~dp0"
python iniciar_api.py
pause
