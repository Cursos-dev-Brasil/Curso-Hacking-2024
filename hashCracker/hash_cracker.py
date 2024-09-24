import sys
import os

# adiciona outros scripts ao path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts/commands"))
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts/commands/hash_types"))

# importação de funções e arquivos externos
from exec import choose
from scripts.commands.help_command import *
from arg_parser import parse_args

# captura os argumentos passados na execução
args = parse_args()
# Verificação de wordlist
def wordlist(wordlistFile):
				# verifica se o arquivo da wordlist existe
    if os.path.exists(wordlistFile):
									# verifica se o usuário tem permissão de leitura na wordlist
        if os.access(wordlistFile, os.R_OK):
        # verifica se a wordlist é um arquivo de texto

									if wordlistFile.lower().endswith(".txt"):
																		# verifica se a wordlist tem conteúdo
                if os.path.getsize(wordlistFile) > 0:
																						# abre a wordlist
                    with open(wordlistFile, "r", encoding="utf-8") as file:
                        return
# Le o conteúdo da wordlist e separa em linhas
 file.read().splitlines()
          

# Erros...              
                else:
                    print("ERRO: O arquivo de texto está vazio")
                    exit()
            else:
                print(
                    "ERRO: O script não suporta outro tipo de arquivo, converta para .txt"
                )
                exit()
        else:
            print("ERRO: O arquivo está inacessível")
            exit()
    else:
        print("ERRO: O arquivo não existe, Adeus...")
        exit()


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
                print(
                    "ERRO: O script não suporta outro tipo de arquivo, converta para .txt"
                )
                exit()
        else:
            print("ERRO: O arquivo está inacessível")
            exit()
    else:
        print("ERRO: O arquivo não existe, Adeus...")
        exit()


def main():
    global wordlist_data, hash_data
    wordlist_data = wordlist(args.wordlist)
    hash_data = hash_fileVerify(args.file)
    choose(wordlist_data, hash_data)
    return wordlist_data, hash_data

if __name__ == "__main__":
    if (
        not args.wordlist
        or not args.hash_type
        or not args.file
        and not args.help
    ):
        print(
            "Erro ao processar os argumentos, preencha os argumentos necessários '-w/--wordlist', '--hash_type' e '-f/--file' Ou use o comando help"
    )
    else:
        wordlist_data, hash_data = main()
