# Fundamentos Linux - Parte 3

Ah, o `echo "conteúdo" > arquivo.txt`. Um clássico, né? Mas, vamo combinar, quando você precisa lidar com várias linhas ou colar aquele textão pra mandar pra namorada, esse método é tipo cortar um bife com uma colher de plástico. Felizmente, o Linux oferece alternativas bem melhores para isso.

## Editores de Texto no Terminal

Agora entra o herói que você nem sabia que precisava: o editor de texto do terminal. Imagina poder editar arquivos sem sair do seu precioso terminal. Parece mágica, né? E é quase isso! Neste curso, vamos nos concentrar no *nano*, o editor que é tipo o cachorro-quente dos editores de texto – simples, gostoso, e todo mundo gosta.

### Nano: O Canivete Suíço dos Editores

Se o *nano* fosse uma pessoa, ele seria aquele amigo que sempre tem um chiclete e sabe as piadas certas. Usar o *nano* é fácil que nem descascar uma banana. Para começar, é só abrir um arquivo usando:

```bash
nano nome_do_arquivo
```

E aí, prontinho, preparado para você editar o que quiser. Quer navegar entre as linhas? Simples, use as setas. Quer salvar? Beleza, aperta Ctrl + O. Quer sair? Fácil demais, Ctrl + X.

Aqui está um gostinho da interface:

```
root@linux3:/tmp# nano arquivo
  GNU nano 4.8                                             meu_arquivo                                                       

^G Obter Ajuda    ^O Escrever    ^W Onde Está    ^K Cortar Texto    ^J Justificar     ^C Posição Atual     M-U Desfazer       M-A Marcar Texto
^X Sair        ^R Ler Arquivo   ^\ Substituir     ^U Colar Texto  ^T Verificar Ortografia    ^_ Ir Para Linha  M-E Refazer       M-6 Copiar Texto
```

É muita opção! E sabe o que é melhor? Tudo isso com combinações de teclas super fáceis de lembrar. Por exemplo, para sair do nano, é só usar Ctrl + X. Simples assim!

### Vim: O Mestre Jedi dos Editores
Existe outro editor, o nome dele é Vim. Ele é mais avançado, perfeito pras pessoas que já hackearam o governo e não estão presas ainda (opcional). Mas, por enquanto, vamos deixar ele de lado e nos concentrar no nosso nano.

## Baixando Arquivos com o Wget
Já se perguntou como seria baixar arquivos direto pelo terminal? Com o wget, isso é fácil. É como se você tivesse um navegador invisível, baixando tudo o que você precisa. Você só precisa saber o link completinho, tipo:
`wget https://XXXXX.XXXXXX/XXXXX.XXXXXX/XXXXXXXXXXX-XXXXXX/XXXX/XXX/arquivo.txt`

"Aí, mas se eu tenho o link eu tive que abrir o google pra encontrar", se você pensou isso, para de ser chato e aceita

## Transferindo Arquivosa Usando o SCP
O SCP (Não os monstro, o Secure copy) é tipo o correios da internet. Quer enviar um arquivo do seu computador para outro? Ou pegar algo de uma máquina remota? SCP é o cara certo para o trabalho, e faz isso tudo usando uma camada de segurança que impediria até o ladrão mais esperto. E quer saber o melhor? Diferente dos correios ele não trava os prodoutos na alfandega e ele vem sem NENHUMA, exatamente, NENHUMA taxa (por enquanto)

Por exemplo, para transferir um arquivo da sua máquina para outra

`scp flag.txt ubuntu@192.168.1.30:/home/ubuntu/transfer.txt`

Esse comando é útil quando você precisa tacar um payload destruidor pra ferrar com 100% do pc do cara e roubar todos os dados dele, ou quando você quiser uma flag da tryhackme (esse é bem menos legal)

Ou, se você estiver na outra máquina e quiser se vingar do cara que pegou seu ip depois de você clicar num link muito suspeito num site mais suspeito ainda

`scp ubuntu@192.168.1.30:/home/ubuntu/documents.txt nota.txt`

## Fazendo seu PC ser um Servidor com o Python
Imagine que seu PC pode virar um servidor, tipo aqueles que você acessa o toda hora e nem repara. Com um comando, você pode servir arquivos para serem baixados

`python3 -m http.server`

Boom! Seu PC é um servidor web. Só toma cuidado: esse server vai rodar na porta 8000 e só vai funcionar enquanto a janela do terminal estiver aberta, então, não esquece de abrir um novo terminal para fazer outras coisas enquanto ele está rodando.

## Espionando Processos no Linux
Você já quis saber o que está acontecendo no seu PC enquanto você joga lol? Com o comando ps, você pode espiar todos os processos lá dentro. É tipo ter uma visão de raio-x do sistema. Quer mais detalhes? O comando ps aux vai te mostrar tudo – do quanto de RAM o Chrome está devorando (spoiler: é muito) até o ID dos processos.

```bash
$ ps aux
      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
     1491    1470    1491      13536  pty0     2177803 15:57:44 /usr/bin/ps
     1469       1    1469      25932  ?        2177803 15:57:41 /usr/bin/mintty
     1470    1469    1470      21004  pty0     2177803 15:57:41 /usr/bin/bash
```

Se você quer ver tudo acontecendo em tempo real, o comando top é tipo assistir um filme atualizando a página cada 10 segundos.

### Matando Processos: O Jogo do Poder

Os processos não querem que você saiba disso, mas se você usar o comando `kill`, você pode encerrar qualquer processo, tudo isso com 4 letras e um enter

existem 3 tipos de desligamentos:

SIGTERM: Desliga o processo gentilmente, você despeja ele e dá 24h para ele arrumar as malas.
SIGKILL: Um chute na porta, encerra o processo sem nenhuma dó e sem conversa.
SIGSTOP: Coloca o processo em pausa, como se você desse mais um mês pra ele pagar o aluguel.

## Iniciando Processos na Inicialização
Alguns programas são tão importantes que você quer que eles comecem junto com o sistema. O systemctl é seu mordomo para esses casos. Quer iniciar um servidor Apache assim que ligar o PC?

`systemctl start apache2`

quer desligar quando terminar?

`systemctl stop apache2`

## Segundo Plano, Primeiro Plano: Onde Rodar os Comandos?
No Linux, você pode escolher se quer um comando que rode em segundo plano (para não ficar olhando pra tela enquanto ele carrega) ou em primeiro plano. Por exemplo:

`echo "hello, World!" &`

Esse "&" no final é tipo mandar o comando trabalhar enquanto você vai fazer outra coisa.

## Crontabs: O Relógio Suíço do Linux
Crontabs são tipo despertadores para comandos. Quer rodar um backup todo dia às 2 da manhã (por mais que não faça sentido)? Uma atualização semanal? Eu odiaria precisar ficar fazendo isso toda hora, crontabs são a solução pra isso! Cada linha de comando em uma crontab tem seis parâmetros, controlando quando e como ela vai funcionar:

MIN: Minuto
HOUR: Hora
DOM: Dia do mês
MON: Mês
DOW: Dia da semana
CMD: O comando que vai ser executado

`0 */12 * * * cp -R /home/usuario/documentos/ /var/backups`

Simples, direto ao ponto, e você nunca mais vai esquecer de fazer aquele backup!

Wildcards: O poder dos Asteriscos
Wildcards (ou curingas) são literalmente um asterisco (*), ele significa "qualquer coisa vai aqui", então:

```
* * * * * * executa o comando a cada minuto.
0 0 * * * * executa o comando todo dia à meia-noite.
```
Simples, né? E se você acha que ainda precisa de uma ajudinha, existem geradores de crontabs online que fazem o trabalho pesado para você!

###### Recursos para iniciantes
Tem umas ferramentas para facilitar a criação desses carinhas, essas ferramentas são boas pra quem tá começando e não lembra sempre da sintaxe, um deles é o [crontab-generator](https://crontab-generator.org/)
