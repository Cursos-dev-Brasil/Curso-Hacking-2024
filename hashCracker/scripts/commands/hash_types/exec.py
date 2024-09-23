from md5 import exec_md5
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))
from scripts.arg_parser import parse_args 
args = parse_args

def choose(wordlist, hash):
    match args.hash_type:
        case "1":
            exec_md5(wordlist, hash) 
        case _:
            print(f"O hash número {args.hash_type} nao existe, tente novamente")