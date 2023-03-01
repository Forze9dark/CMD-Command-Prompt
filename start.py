import subprocess
import ctypes, sys

logo = """
#####################################################################################################


       d8888 8888888b.  888b     d888 8888888 888b    888      .d8888b.  888b     d888 8888888b.  
      d88888 888  "Y88b 8888b   d8888   888   8888b   888     d88P  Y88b 8888b   d8888 888  "Y88b 
     d88P888 888    888 88888b.d88888   888   88888b  888     888    888 88888b.d88888 888    888 
    d88P 888 888    888 888Y88888P888   888   888Y88b 888     888        888Y88888P888 888    888 
   d88P  888 888    888 888 Y888P 888   888   888 Y88b888     888        888 Y888P 888 888    888 
  d88P   888 888    888 888  Y8P  888   888   888  Y88888     888    888 888  Y8P  888 888    888 
 d8888888888 888  .d88P 888   "   888   888   888   Y8888     Y88b  d88P 888   "   888 888  .d88P 
d88P     888 8888888P"  888       888 8888888 888    Y888      "Y8888P"  888       888 8888888P"  


#####################################################################################################

"""
print(logo)

NewCommand = input("Ingrese el comando que desea ejecutar en la terminal: ")


def run_as_admin(cmd):
    try:
        if sys.platform == "win32":
            # Se asegura de que el proceso se ejecute como administrador en Windows
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", "cmd.exe", f"/k {cmd}", None, 1
            )

        else:
            subprocess.call(["sudo", "sh", "-c", cmd])

    except Exception as e:
        print(e)


# Llama a la función "run_as_admin" para ejecutar la terminal cmd en modo administrador con el respectivo comando.
run_as_admin(
    NewCommand
)
