from hashlib import md5
def exec_md5(wordlist, hash):
    from arg_parser import args
    if args.hash_type == 1:
        wordlist_dataEncrypt = md5(wordlist)
        print(wordlist_dataEncrypt)