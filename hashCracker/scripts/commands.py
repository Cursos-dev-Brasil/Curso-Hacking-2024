from hashCracker import lib
from lib import *

# Função para exibir a mensagem de ajuda personalizada
def helpFun():
    help_message = """
    Comando de ajuda personalizado:
    
    Argumentos:
    -w, --wordlist     Especifica a wordlist a ser utilizada.
    -t, --threads      Número de threads a ser utilizado (padrão: 1).
    --tipo-hash        Especifica o tipo de hash a ser quebrado.
                       Formatos disponíveis: sha256, md5-sha1, sha512, md5sha1, blake2b, blake2s,
                       ripemd160, sha3_224, sha384, md4, shake_128, sha224, mdc2, sha3_256,
                       sha512_224, sha3_384, sha512_256, shake_256, sha3_512, sm3, whirlpool
                       
    Exemplo de uso:
    python helpCommand.py -w wordlist.txt -t 10 --tipo-hash sha256
    """
    print(help_message)
    lib.sys.exit()


parser = lib.argparse.ArgumentParser(add_help=False) 


parser.add_argument('-w', '--wordlist', type=str, help="Especifica a wordlist a ser utilizada.")
parser.add_argument('-t', '--threads', type=int, default=1, help="Número de threads a ser utilizado (padrão: 1).")
parser.add_argument('-h', '--hash-type', type=str, help="Especifica o tipo de hash a ser quebrado.")

parser.add_argument('help', nargs='?', default=None, help="Exibe este comando de ajuda personalizado.")

parser.add_argument('-a', '--arquive', type=str, required=True)

args = parser.parse_args()

if args.help == 'help':
    helpFun()

if not args.wordlist or not args.hash_type:
    print("Erro: Os argumentos '-w/--wordlist' e '-h/--tipo-hash' são obrigatórios.")
    lib.sys.exit(1)

def wordlist(wordlistFile):
    if lib.os.path.exists(wordlistFile):
        if lib.os.access(wordlistFile, lib.os.R_OK):
            if wordlistFile.lower().endswith(".txt"):
                if lib.os.path.getsize(wordlistFile) > 0:
                    with open(wordlistFile, "r", encoding="utf-8") as file:
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

def hash_fileVerify(hash_file):
    if lib.os.path.exists(hash_file):
        if lib.os.access(hash_file, lib.os.R_OK):
            if hash_file.lower().endswith(".txt"):
                if lib.os.path.getsize(hash_file) > 0:
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

hashContent = hash_fileVerify(args.arquive)
wordlistContent = wordlist(args.wordlist)