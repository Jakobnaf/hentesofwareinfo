
import socket
import platform
import shutil
import windows_tools
import windows_tools.installed_software

# Funksjon for å hente informasjon om operativsystemet (navn og versjon)
def var_getosinfo():
    return platform.system(), platform.version()

# Funksjon for å hente IP-adressen til maskinen
def var_getipaddressse():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Funksjon for å hente diskplass (total, brukt og ledig) i GB
def var_getdiskspace():
    total, used, free = shutil.disk_usage("/")
    return f"Total: {total // (2**30)} GB, Used: {used // (2**30)} GB, Free: {free // (2**30)} GB"

# Funksjon for å hente listen over installerte programmer
def var_getinstalledsoftware():
    return windows_tools.installed_software.get_installed_software()

# Funksjon for å hente listen over installerte programmer
def var_gethostname():
    return socket.gethostname()

# Funksjon for å lagre all informasjon til en fil
def save_info_to_file(filename):
     with open(filename, 'a') as file:
        file.write(f"OS info: {var_getosinfo()}\n")
        file.write(f"Ledig plass: {var_getdiskspace()}\n")
        file.write(f"ipadresse: {var_getipaddressse()}\n")
        file.write(f"Hostname: {var_gethostname()}\n")
        file.write(f"instalerte apper: {var_getinstalledsoftware()}\n")

# Kaller funksjonen for å lagre informasjonen til filen "system_info.txt"
save_info_to_file("system_info.txt")