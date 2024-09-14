# Windows (eca)

Eu vou ser bem sincero, minha última vontade era precisar fazer uma aula sobre linux, esse sistema é tão ruim que não existe quase nenhum conteúdo, eu vou fazer o possível pra criar algum conteúdo em cima desse sistema horroroso, se não vão achar que eu tô dando prioridade pro linux (eu tô)

## Fundamentos Windows

Como eu disse antes, não tem conteúdo suficiente pra fazer 4 aulas só sobre fundamentos de windows, então uma já serve

Durante essa aula, vou tentar ser o mais imparcial possível com o windows (mesmo que seja difícil)

O Windows foi lançado pela primeira vez no dia 20 de novembro de 1985, foi uma resposta ao computador Macintosh da Apple. Eu não posso mentir, o windows foi muito importante pro desenvolvimento dos sistemas operacionais, ele foi o primeiro sistema a ter GUI, que apesar de ser reduzida no Linux, ainda existe

O Windows é útil para pessoas que não trabalham na área da Tecnologia, por ele ter mais GUI's ele acaba sendo mais intuitivo para pessoas sem conhecimento e para pessoas que gerenciam / usam sistemas de gestão de empresas (ERP), como o SAP, Oracle NetSuite, Microsoft Dynamics 365 ou até um sistemas de VPN como o Open VPN ou o Ivanti SAC

MASSS, como eu não suporto falar bem do windows isso tem uma desvantagem, uma interface gráfica pode na maioria das vezes desperdiçar uma boa  dos recursos, como RAM para carregar gráficos e CPU para renderizar, o que não é necessário em ferramentas de linhas de comando que compõe grante parte do linux, o que faz o Windows 11 ser 8x mais pesado do que por exemplo o Parrot OS

### Comandos e ferramentas  

Por incrível que pareça o Windows tem um terminal, no windows o terminal (Comand prompt / cmd) é mais uma pedra do que um terminal, você não pode adicionar outros comandos, você só tem os comandos do windows e pronto

| Comando          | Descrição                                                      | Exemplo de Uso                        | Saída Exemplo                     |
| ---------------- | -------------------------------------------------------------- | ------------------------------------- | --------------------------------- |
| `echo`           | O Windows copiou esses comandos do linux. Então é a mesma coisa que no Linux        | `root@windows1:~$ echo "Hello, world!"` | `Hello, world!`                   |
| `whoami`         | O Windows copiou esses comandos do linux. Então é a mesma coisa que no Linux | `root@windows1:~$ whoami`               | `root`                            |
| `dir`            | Esse daqui foi pra não copiar 100%, é tipo o primo excluído da familia         | `root@windows1:~$ dir`                 | `a.txt text.txt documents folder` |
| `cd <diretório>` | O Windows copiou esses comandos do linux. Então é a mesma coisa que no Linux                               | `root@windows1:~$ cd documents`        | `root@windows1:~/documents $`     |
| `type <arquivo>` | Esse daqui é equivalente ao cat   | `root@windows1:~$ type text.txt`       | `Conteúdo do arquivo text.txt`    |
| `pwd`            | O Windows copiou esses comandos do linux. Então é a mesma coisa que no Linux           | `root@windows1:~/documents $ pwd`      | `/home/ubuntu/Documents`          |

Você pode até me falar "Mas o linux é 6 anos mais novo que o windows" a primeira coisa que eu vou fazer é te fazer devolver o curso, defensor de windows não tem lugar aqui, depois disso eu vou te dizer que você tá completamente enganado, já que o linux é um sistema baseado no UNIX-Like, O modelo UNIX-Like por sua vez é do ano de 1971

#### Localização de arquivos

| Comando | Descrição | Exemplo | Saída |
|---------|-----------|---------|-------|
| `find`  | Também é igual ao linux | `find -name passwd.txt` | `./documents/.senhas.txt` |
| `findstr`  | Adivinha? não é igual ao linux, é o aquivalente ao grep. | `findstr "senha" passwd.txt` | `senha 1 - - !4CFF0` |

#### Operadores de terminal
| Operador | Descrição | Exemplo | Observação |
|----------|-----------|---------|------------|
| `&`      | Linux | `comando &` | 
| `&&`     | Linux | `comando1 && comando2` |
| `>`      | Linux | `echo "conteúdo" > arquivo.txt` |
| `>>`     | Linux denovo | `echo "mais conteúdo" >> arquivo.txt` |

### Ferramentas e Hacking no windows

Algumas ferramentas "úteis" para hacking no windows são:

1. Powershell: Ajuda na automação e em scripts, o comando `Get-Command` te mostra os comandos

2. Sysinternals Suite: Ferramentas de analise e diagnóstico de sistemas. Inclui `Process Explorer`, `Autoruns` e `Sysmon`

3. Metasploit Framework: É nativa do Linux (pra variar, você precisa baixar o código fonte pré-compilado ou arrumar outro jeito)





