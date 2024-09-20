from hashCracker.lib import *

# Função principal para inicializar a verificação dos arquivos
def main():
    if len(sys.argv) < 3:
        print("ERRO: Argumentos insuficientes. Uso: script.py <wordlist> <hash_file>")
        exit()
    for args in sys.argv:
        if args.startswith("-h") or args.startswith("--help"):
            commands.helpFun(sys.argv)
        if args.startswith("-w") or args.startswith("--wordlist"):
            commands.wordlist(file)

if __name__ == "__main__":
    main()
