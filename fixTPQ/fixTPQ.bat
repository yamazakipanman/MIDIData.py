@echo off
cls
if "%1"=="" (
exit /b 1
) else (
py fixTPQ.py %1
)
