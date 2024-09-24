import hashlib
from arg_parser import parse_args

args = parse_args()

def print_result(hash_value, word, success=True):
    if success:
        print(f"""
            [+] Senha crackeada com sucesso
            [+] Resultado - {hash_value}:{word}
            [+] Status: finish
            [+] Número de correspondencias: 1
            [+] Password cracked
            [-] Exiting...
        """)
    else:
        print(f"[-] Não foi possível crackear a senha: {hash_value}")

def exec_hash(hash_function, wordlist, hash_value):
    for word in wordlist:
        if hash_function(word.encode()).hexdigest() == hash_value:
            print_result(hash_value, word)
            return
    print_result(hash_value, "", success=False)

def execMd5(wordlist, hash_value):
    exec_hash(hashlib.md5, wordlist, hash_value)

def execSha1(wordlist, hash_value):
    exec_hash(hashlib.sha1, wordlist, hash_value)

def execSha224(wordlist, hash_value):
    exec_hash(hashlib.sha224, wordlist, hash_value)

def execSha256(wordlist, hash_value):
    exec_hash(hashlib.sha256, wordlist, hash_value)

def execSha384(wordlist, hash_value):
    exec_hash(hashlib.sha384, wordlist, hash_value)

def execSha512(wordlist, hash_value):
    exec_hash(hashlib.sha512, wordlist, hash_value)

def execSha3_224(wordlist, hash_value):
    exec_hash(hashlib.sha3_224, wordlist, hash_value)

def execSha3_256(wordlist, hash_value):
    exec_hash(hashlib.sha3_256, wordlist, hash_value)

def execSha3_384(wordlist, hash_value):
    exec_hash(hashlib.sha3_384, wordlist, hash_value)

def execSha3_512(wordlist, hash_value):
    exec_hash(hashlib.sha3_512, wordlist, hash_value)

def execShake128(wordlist, hash_value):
    exec_hash(lambda x: hashlib.shake_128(x).hexdigest(32), wordlist, hash_value)

def execShake256(wordlist, hash_value):
    exec_hash(lambda x: hashlib.shake_256(x).hexdigest(32), wordlist, hash_value)

def execBlake2b(wordlist, hash_value):
    exec_hash(hashlib.blake2b, wordlist, hash_value)

def execBlake2s(wordlist, hash_value):
    exec_hash(hashlib.blake2s, wordlist, hash_value)

def execRipemd160(wordlist, hash_value):
    exec_hash(lambda x: hashlib.new('ripemd160', x).hexdigest(), wordlist, hash_value)

def execWhirlpool(wordlist, hash_value):
    exec_hash(lambda x: hashlib.new('whirlpool', x).hexdigest(), wordlist, hash_value)

def execMd4(wordlist, hash_value):
    exec_hash(lambda x: hashlib.new('md4', x).hexdigest(), wordlist, hash_value)

def execMd5Sha1(wordlist, hash_value):
    for word in wordlist:
        combined_hash = hashlib.md5(word.encode()).hexdigest() + hashlib.sha1(word.encode()).hexdigest()
        if combined_hash == hash_value:
            print_result(hash_value, word)
            return
    print_result(hash_value, "", success=False)

def execSm3(wordlist, hash_value):
    exec_hash(lambda x: hashlib.new('sm3', x).hexdigest(), wordlist, hash_value)

def execMdc2(wordlist, hash_value):
    exec_hash(lambda x: hashlib.new('mdc2', x).hexdigest(), wordlist, hash_value)
