@echo off
rem launch venv
echo Creando virtual environment
rem Chequea su venv esta instalado

python -m venv --help >nul 2>&1

if errorlevel 1 (
    echo virtualenv no esta instalado. Por favor installe utilizando 'pip install virtualenv'. 
    pause
    exit /b 1
)

rem Actualiza pip a la ultima version
echo Actualizando PIP a la ultima version
call .venv\Scripts\python.exe -m pip install --upgrade pip >> run.log

for /d %%D in (*) do (
    if exist "%%D\Scripts\activate" (
        call "%%D\Scripts\activate"
        echo Virtual Environment activado "%%D"

        echo Instalando dependencias de requirements.txt

        rem revisar si requirements.txt existe...

        if not exist requirements.txt (
            echo requirements.txt no existe. Saltando instalación...
        ) else (
            rem instalando paquetes de requirements.txt
            pip install -r requirements.txt
            echo Paquetes de requirements.txt instalados correctamente
        )

        rem Ejecutando musicblog desde este directorio 
        echo :: Ejecutando MusicBlog ::
        python app_core\manage.py runserver
        rem exit 0
    )


)