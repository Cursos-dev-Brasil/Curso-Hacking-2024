# Escalada de privilégios (privilege escalation)

Normalmente você entra no sistema como um usuário padrão, ou seja, sem privilégio administrativo, o que normalmente não te da acesso completo ao dispositivo. Pra obter acesso total você precisa encontrar uma vulnerabilidade interna pra escalar seus privilégios para o root do linux ou SYSTEM/administrator do outro sistema. 

## Lista de verificação PrivEsc

Depois de conseguir acesso você pode enumerar a máquina para explorar escalada de privilégios (eu sei, é muita enumeração) você pode encontrar listas e dicas com verificações e comandos que você pode usar para executar essas verificações. O melhor recurso pra isso é o [HackTricks](https://book.hacktricks.xyz/), que tem uma lista gigante para verificação de escalação deprivilégios. Escalar privilégios se traduz em testar comandos e mais comandos até encontrar alguma fraqueza na segurança

## Scripts de enumeração

Muitos comandos da hacktricks (ou da payload all the things, eles estão em todo lugar) podem ser executados usando um script pra isso. Alguns scripts de enumeração são o LinEnum e o linuxprivchecker, invadir um windows é tão fácil que isso é inútil na maioria das vezes

Outra ferramenta útil é a Privilege Escalation Awesome Scripts SUITE, PEASS pros mais intimos, ele sempre é atualizado e funciona no windows e linux

Esses scripts criam muito "ruído" na máquina, o que pode acionar o antivirus. Isso pode impedir que os scripts sejam executados ou até alertar o dono do pc (em alguns casos coloca o pc em quarentena ou ativa o firewall). As vezes ser preguiçoso não é o melhor caminho

```bash
[!bash!]$ ./linpeas.sh
...

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEYEND:
  RED/YELLOW: 99% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)
  LightMangenta: Your username


====================================( Basic information )=====================================
OS: Linux version 3.9.0-73-generic
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
...
```

### Exploit de kernel

Sempre que você encontrar um pc com SO antigo, você precisa procurar vulnerabilidades no kernel desse sistema, por exemplo, se o servidor não for atualizado com patches ou/e atualizações de segurança ele provavelmente é vulnerável a alguma vulnerabilidade de kernel, como você vai descobrir isso? Enumerando pra variar

no script de exemplo, o linux é um Linux 3.9.0-73-generic, se você usar o searchexploit para vulnerabilidades nesse sistema você vai encontrar um CVE-2016-5195, ou o dirtyCow, você pode executar esse exploit no servidor e conseguir privilégios de administração

**Nota: Exploits de kernel podem causar instabilidade no sistema onde é executado, então não sai usando exploit de kernel sem testar antes**

### Software vulnerável

no linux você pode usar o comando pkgd -l para  listar todos os softwares instalados

### Privilégios do usuário

Outro ponto importante é você entender os seus limites no sistema as três maneiras mais comuns são:

1. Sudo
2. Suid
3. Privilégios de token do windows

**obs: como sempre o windows tem o nome maior**

no linux um usuário comum pode usar o comando `sudo` para executar comandos como superusuário (root) sem dar privilégios de superusuário para o usuário, você pode descobrir que comandos você pode utilizar com o sudo usando o comando

```bash
[!bash!]$ sudo -l

[sudo] password for user1:

User user1 may run the following commands on ExampleServer:
    (ALL : ALL) ALL

```

Você pode executar qualquer comando com sudo e você pode usar o comando `su -` para trocar para o usuário root

```bash
[!bash!]$ sudo su -

[sudo] password for user1:
whoami
root
```

nesse caso você precisaria da senha do user1 para executar qualquer comando com sudo, as vezes você pode executar certos aplicativos sem essa senha

```
[!bash!]$ sudo -l

(user : user) NOPASSWD: /bin/echo
```

isso indica que o comando echo pode ser executado sem uma senha (é meio óbvio)

Depois de encontrar um app que você possa executar sem senha você pode explorar ele usando o GTFOBins (eu sei, tudo usa uma ferramenta, é difícil decorar) para conseguir um shell do usuário root

### Crontabs

No linux, você pode executar comandos de tempos em tempos, existem 2 maneiras de usar crontabs para escalar privilégios

1. Enganar as tarefas para executar software malicioso

pra isso você precisa de permissão para escrever em pelo menos um dos diretórios de crontabs

```
/etc/crontab
/etc/cron.d
/var/spool/cron/crontabs/root
```

Se puder gravar em um desses, você pode escrever um script bash com um reverse shell que nos envia o reverse shell quando é executado

### Credenciais expostas

Alguns arquivos tem credenciais expostas, como arquivos de configuração, log, histórico do usuaário

Os Scripts de enumeração procuram por senhas nesses arquivos e fornecem de volta pra vc

```
[+] Searching passwords in config PHP files
[+] Finding passwords inside logs (limit 70)
...
/var/www/html/config.php: $conn = new mysqli(localhost, 'db_user', 'password123');
```

A senha do banco de dados (extremamente segura) é exposta, qualquer pessoa com 5 neurônios sabe que colocar as credenciais diretamente na consulta é uma péssima ideia mas isso não vem ao caso

As vezes usuários burros reutilizam senhas, então se você descobrir uma senha pode tentar a sorte em outros protocolos ou usuários

```
[!bash!]$ su -

Password: password123
whoami

root
```

### Chaves SSH

Essa aula vai estar [aqui](/aulas/linux/ferramentas/ssh/chavesSSH.md)