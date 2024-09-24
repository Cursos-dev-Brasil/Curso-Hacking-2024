import sys
import os

# Adiciona diretórios ao path do Python para permitir a importação de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts/commands"))
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts/commands/hash_types"))

# Importação de funções e arquivos externos
from exec import choose
from scripts.commands.help_command import *
from arg_parser import parse_args

# Captura os argumentos passados na execução
args = parse_args()

# Função para verificar a wordlist
def wordlist(wordlistFile):
    # Verifica se o arquivo da wordlist existe
    if os.path.exists(wordlistFile):
        # Verifica se o usuário tem permissão de leitura
        if os.access(wordlistFile, os.R_OK):
            # Verifica se a wordlist é um arquivo de texto
            if wordlistFile.lower().endswith(".txt"):
                # Verifica se a wordlist tem conteúdo
                if os.path.getsize(wordlistFile) > 0:
                    # Lê o conteúdo da wordlist e separa em linhas
                    with open(wordlistFile, "r", encoding="utf-8") as file:
                        return file.read().splitlines()
                else:
                    print("ERRO: O arquivo de texto está vazio")
                    exit()
            else:
                print("ERRO: O script não suporta outro tipo de arquivo, converta para .txt")
                exit()
        else:
            print("ERRO: O arquivo está inacessível")
            exit()
    else:
        print("ERRO: O arquivo não existe, Adeus...")
        exit()

# Função para verificar o arquivo de hash
def hash_fileVerify(hash_file):
    if os.path.exists(hash_file):
        if os.access(hash_file, os.R_OK):
            if hash_file.lower().endswith(".txt"):
                if os.path.getsize(hash_file) > 0:
                    with open(hash_file, "r", encoding="utf-8") as file:
                        return file.read()
                else:
                    print("ERRO: O arquivo de texto está vazio")
                    exit()
            else:
                print("ERRO: O script não suporta outro tipo de arquivo, converta para .txt")
                exit()
        else:
            print("ERRO: O arquivo está inacessível")
            exit()
    else:
        print("ERRO: O arquivo não existe, Adeus...")
        exit()

# Função principal que inicia outras funções
def main():
    global wordlist_data, hash_data
    # Pega os dados dos argumentos
    wordlist_data = wordlist(args.wordlist)
    hash_data = hash_fileVerify(args.file)
    choose(wordlist_data, hash_data)
    return wordlist_data, hash_data

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Verifica se argumentos necessários foram passados
    if not args.wordlist or not args.hash_type or not args.file and not args.help:
        print("Erro ao processar os argumentos, preencha os argumentos necessários '-w/--wordlist', '--hash_type' e '-f/--file' Ou use o comando --help")
    else:
        # Atribui os valores retornados da função main a wordlist_data e hash_data
        wordlist_data, hash_data = main()
