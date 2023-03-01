from cx_Freeze import setup, Executable

setup(
    name="Excute admin cmd",
    version="1.0",
    description="Simple script que ejecuta codigo en el cmd en modo administrador.",
    executables=[Executable("start.py")]
)