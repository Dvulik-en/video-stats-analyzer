@echo off
chcp 65001 >nul

:: Указываем путь к python внутри твоего venv
set VENV_PYTHON=venv\Scripts\python.exe

echo Проверка наличия библиотек...
"%VENV_PYTHON%" -c "import tabulate; import pytest" >nul 2>&1

if %errorlevel% neq 0 (
    echo Библиотеки не найдены в виртуальном окружении. Установка...
    "%VENV_PYTHON%" -m pip install -r requirements.txt
) else (
    echo Все зависимости уже установлены.
)

echo.
echo Запуск программы...
"%VENV_PYTHON%" main.py --files stats1.csv stats2.csv
pause