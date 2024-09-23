import argparse, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "commands"))

from help_command import helpFun

def parse_args():
    parser = argparse.ArgumentParser(add_help=False) 
    parser.add_argument('-w', '--wordlist', type=str, help="Especifica a wordlist a ser utilizada.")
    parser.add_argument('-t', '--threads', type=int, default=1, help="Número de threads a ser utilizado (padrão: 1).")
    parser.add_argument('-h', '--hash_type', type=str, help="Especifica o tipo de hash a ser quebrado.")
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument("--help", action="store_true")
    args = parser.parse_args()

    if args.help:
        helpFun()
        exit(1)

    if not args.wordlist or not args.hash_type or not args.file:
        print("Erro: Os argumentos '-w/--wordlist', '--hash_type' e '-f /--file' são obrigatórios.")
        sys.exit(1)

    return args
