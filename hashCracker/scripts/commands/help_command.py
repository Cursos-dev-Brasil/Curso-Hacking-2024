import sys

def helpFun():
    # Mensagem de ajuda que será exibida
    help_message = """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Comando de ajuda =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    Argumentos:
    -w, --wordlist     Especifica a wordlist a ser utilizada.
    -t, --threads      Número de threads a ser utilizado (padrão: 1).
    --hash_type        Especifica o tipo de hash a ser quebrado.
                       Formatos disponíveis: sha256, md5-sha1, sha512, ...

    Exemplo de uso:
    python hash_cracker.py -w wordlist.txt -t 10 --hash_type sha256 -f test.txt

    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Tipos de hash =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        - md5 = 1
        - sha1 = 2
        - sha224 = 3
        - sha256 = 4
        - sha384 = 5
        - sha512 = 6
        - sha3_224 = 7
        - sha3_256 = 8
        - sha3_384 = 9
        - sha3_512 = 10
        - shake_128 = 11
        - shake_256 = 12
        - blake2b = 13
        - blake2s = 14
        - ripemd160 = 15
        - whirlpool = 16
        - md4 = 17
        - md5-sha1 = 18
        - sm3 = 19
        - mdc2 = 20
    """
    print(help_message)
    sys.exit()  # Encerra o programa após exibir a ajuda
