# Importando as bibliotecas necessárias
import os
import zipfile
import datetime

# Definindo o diretório de origem e o diretório de destino
source_dir = "C:/Users/bruno/Downloads"
target_dir = "D:/"

# Definindo a função de backup
def backup_files(source_dir, target_dir):
    # Obtendo a data e hora atual
    now = datetime.datetime.now()

    # Formatando a data e hora atual
    now_format = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Definindo o nome do arquivo de backup
    backup_file = os.path.join(target_dir, f"backup_{now_format}.zip")

    # Criando o arquivo zip
    with zipfile.ZipFile(backup_file, 'w') as zipf:
        # Caminhando por todos os arquivos no diretório de origem
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Adicionando cada arquivo ao arquivo zip
                zipf.write(os.path.join(root, file))

    # Imprimindo uma mensagem de sucesso
    print(f"Backup de {source_dir} concluído com sucesso. O backup está armazenado em {backup_file}.")

# Chamando a função de backup
backup_files(source_dir, target_dir)
