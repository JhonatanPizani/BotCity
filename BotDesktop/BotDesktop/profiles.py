import os
import logging
import platform

# Configuração do logging para exibir as mensagens no terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para determinar o diretório de perfis do Google Chrome com base no sistema operacional
def determinar_diretorio_perfis():
    sistema_operacional = platform.system()
    diretorio_home = os.path.expanduser("~")
    
    if sistema_operacional == "Windows":
        return os.path.join(diretorio_home, "AppData", "Local", "Google", "Chrome", "User Data")
    elif sistema_operacional == "Linux":
        return os.path.join(diretorio_home, ".config", "google-chrome")
    elif sistema_operacional == "Darwin":  # macOS
        return os.path.join(diretorio_home, "Library", "Application Support", "Google", "Chrome")
    else:
        raise Exception("Sistema operacional não suportado")

# Função para listar os perfis do Google Chrome
def listar_perfis(diretorio_perfis):
    try:
        # Lista todos os diretórios no diretório de perfis
        perfis = [perfil for perfil in os.listdir(diretorio_perfis) if os.path.isdir(os.path.join(diretorio_perfis, perfil))]
    except FileNotFoundError:
        logging.error(f"Diretório de perfis não encontrado: {diretorio_perfis}")
        return []
    
    # Filtra apenas os diretórios que começam com "Profile"
    perfis = [perfil for perfil in perfis if perfil.startswith("Profile")]
    return perfis


# Função para salvar os nomes dos perfis em um arquivo de texto
def salvar_perfis_arquivo(perfis, caminho_arquivo):
    with open(caminho_arquivo, "w") as arquivo:
        # Escreve cada nome de perfil no arquivo
        for perfil in perfis:
            arquivo.write(perfil + "\n")
    logging.info(f"Perfis salvos no arquivo '{caminho_arquivo}': {perfis}")

# Determina o diretório de perfis do Google Chrome
diretorio_perfis = determinar_diretorio_perfis()

# Obtém os nomes dos perfis
perfis = listar_perfis(diretorio_perfis)

if perfis:
    # Caminho do arquivo de texto onde os nomes dos perfis serão salvos
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "perfis.txt")
    
    # Salva os nomes dos perfis em um arquivo
    salvar_perfis_arquivo(perfis, caminho_arquivo)
else:
    logging.warning("Nenhum perfil encontrado para salvar")
