from algorithms import *
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))
from scripts.arg_parser import parse_args 

args = parse_args()

def choose(wordlist, hash):
    match args.hash_type:
        case "1":
            execMd5(wordlist, hash) 
        case "2":
            execSha1(wordlist, hash)
        case "3":
            execSha224(wordlist, hash)
        case "4":
            execSha256(wordlist, hash)
        case "5":
            execSha384(wordlist, hash)
        case "6":
            execSha512(wordlist, hash)
        case "7":
            execSha3_224(wordlist, hash)
        case "8":
            execSha3_256(wordlist, hash)
        case "9":
            execSha3_384(wordlist, hash)
        case "10":
            execSha3_512(wordlist, hash)
        case "11":
            execShake128(wordlist, hash)
        case "12":
            execShake256(wordlist, hash)
        case "13":
            execBlake2b(wordlist, hash)
        case "14":
            execBlake2s(wordlist, hash)
        case "15":
            execRipemd160(wordlist, hash)
        case "16":
            execWhirlpool(wordlist, hash)
        case "17":
            execMd4(wordlist, hash)
        case "18":
            execMd5Sha1(wordlist, hash)
        case "19":
            execSm3(wordlist, hash)
        case "20":
            execMdc2(wordlist, hash)
        case _:
            print(f"O hash número {args.hash_type} nao existe, tente novamente")