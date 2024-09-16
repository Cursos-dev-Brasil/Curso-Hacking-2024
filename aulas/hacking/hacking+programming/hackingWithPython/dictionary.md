# Dicionários

Um dicionário python é uma lista com dois valores relacionados, por exemplo um nome e idade respectivamente

```py
>>> names = {}
>>> names = {"Eduardo": 25}
>>> print (names)
{'Eduardo': 25} 
```

Dicionários são extremamente úteis no hacking, imagina que você tá fazendo um software para explorar vulnerabilidades em um determinado host usando portas TCP abertas. Então você pode usar um dicionário pra exibir o nome do serviço e a porta que ele roda. Isso é só um exemplo. Mas exemplifica bem a utilidade dos dicionários. Exemplificando ainda mais, você pode criar um dicionário que exiba na tela o serviço ftp junto com a porta dele (21). Além disso você pode usar dicionários para ataques de brute force ou cracking de senha

Quando você cria um dicionário, você precisa separar os valores por ":" e os itens por ","

```
$ python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> services = {"ftp": 21, "smb": 139, "http": 80, "ssh": 22, "rdp": 3389}
>>> services.items()
dict_items([('ftp', 21), ('smb', 139), ('http', 80), ('ssh', 22), ('rdp', 3389)])
>>> services["ftp"]
21  
>>> print("[+] Vulnerabilidade encontrada no serviço {0} na porta {1}".format(
... "ftp", services["ftp"]
... )
... )
[+] Vulnerabilidade encontrada no serviço ftp na porta 21
```

Faça isso no seu interpretador e pronto, você terminou seu primeiro script python (Tecnicamente não é um script)

**OBS: Isso é super importante, NUNCA cole código, se fizer isso você NUNCA vai aprender, você só vai estar copiando código**

