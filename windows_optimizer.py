import os
import shutil
import psutil
import subprocess
import sys
import ctypes

def limpar_arquivos_temporarios():
    temp_dirs = [
        os.environ.get("TEMP"),
        os.environ.get("TMP"),
        os.path.join(os.environ.get("SystemRoot"), "Temp"),
        os.path.join(os.environ.get("LOCALAPPDATA"), "Temp")
    ]
    
    for temp_dir in temp_dirs:
        if temp_dir and os.path.exists(temp_dir):
            for root, dirs, files in os.walk(temp_dir, topdown=False):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except (PermissionError, FileNotFoundError):
                        pass
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                    except (PermissionError, FileNotFoundError):
                        pass
    print("✔ Arquivos temporários limpos!")

def liberar_memoria_ram():
    try:
        # Esvaziar cache do sistema
        ctypes.windll.ntdll.NtSetSystemInformation(0x50, None, 0)
        # Forçar paginação para liberar RAM
        subprocess.run("wmic process where \"WorkingSetSize>10000000\" CALL SetPriority 64", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✔ Memória RAM otimizada sem EmptyStandbyList.exe!")
    except Exception as e:
        print(f"⚠ Falha ao liberar memória RAM: {e}")

def otimizar_servicos():
    services_to_disable = ["DiagTrack", "WSearch"]
    
    for service in services_to_disable:
        try:
            subprocess.run(["sc", "stop", service], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["sc", "config", service, "start=disabled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✔ Serviço {service} desativado!")
        except subprocess.SubprocessError:
            print(f"⚠ Não foi possível desativar {service}.")

def restaurar_servicos():
    services_to_enable = ["DiagTrack", "WSearch"]
    for service in services_to_enable:
        try:
            subprocess.run(["sc", "config", service, "start=auto"], check=True)
            subprocess.run(["sc", "start", service], check=True)
            print(f"✔ Serviço {service} restaurado!")
        except subprocess.SubprocessError:
            print(f"⚠ Falha ao restaurar {service}.")

def exibir_uso_de_cpu_ram():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"🔹 Uso atual: CPU {cpu}% | RAM {ram}%")

def otimizar_sistema():
    exibir_uso_de_cpu_ram()
    limpar_arquivos_temporarios()
    liberar_memoria_ram()
    otimizar_servicos()
    print("✅ Otimização concluída!")

def main():
    print("🔧 Iniciando otimização...")
    if len(sys.argv) > 1 and sys.argv[1] == "--restore":
        restaurar_servicos()
    else:
        otimizar_sistema()

if __name__ == "__main__":
    main()
