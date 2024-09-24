import hashlib
from arg_parser import parse_args

args = parse_args()

def execMd5(wordlist, hash_value):
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha1(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha224(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha224(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha256(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha384(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha384(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha512(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha3_224(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha3_224(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha3_256(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha3_256(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha3_384(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha3_384(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSha3_512(wordlist, hash_value):
    for word in wordlist:
        if hashlib.sha3_512(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execShake128(wordlist, hash_value):
    for word in wordlist:
        if hashlib.shake_128(word.encode()).hexdigest(32) == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execShake256(wordlist, hash_value):
    for word in wordlist:
        if hashlib.shake_256(word.encode()).hexdigest(32) == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execBlake2b(wordlist, hash_value):
    for word in wordlist:
        if hashlib.blake2b(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execBlake2s(wordlist, hash_value):
    for word in wordlist:
        if hashlib.blake2s(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execRipemd160(wordlist, hash_value):
    for word in wordlist:
        if hashlib.new('ripemd160', word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execWhirlpool(wordlist, hash_value):
    for word in wordlist:
        if hashlib.new('whirlpool', word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execMd4(wordlist, hash_value):
    for word in wordlist:
        if hashlib.new('md4', word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execMd5Sha1(wordlist, hash_value):
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() + hashlib.sha1(word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execSm3(wordlist, hash_value):
    for word in wordlist:
        if hashlib.new('sm3', word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

def execMdc2(wordlist, hash_value):
    for word in wordlist:
        if hashlib.new('mdc2', word.encode()).hexdigest() == hash_value:
            print(f"""
                [+] Senha crackeada com sucesso
                [+] Resultado - {hash_value}:{word}
                [+] Status: finish
                [+] Número de correspondencias: 1
                [+] Password cracked
                [-] Exiting...
            """)
            return
    print(f"[-] Não foi possível crackear a senha: {hash_value}")

