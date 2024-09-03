# Termos comuns

Quando tiver no meio de um pentest, você vai encontrar 400 girias diferentes e 500 termos, não vou falar de tudo aqui, mas é o suficiente pra começar

# Shell

Vamo começar pelo shell (Não é as conchinhas que você encontra na praia). Um shell no TI é uma palavra que você vai ouvir tantas vezes, mais tantas vezes, que a palavra shell vai começar a ecoar na sua cabeça. No linux, o shell é um programa que recebe os comandos do usuário (no caso você sherlock) e passa pro OS fazer alguma coisa de útil (nem sempre é útil mas releva essa parte) como rodar scripts que você baixou e esqueceu o caminho (sem julgamento)

Nos primórdios da humanidade, quando os dinossauros ainda eram vivos e a rainha elizabeth era só uma princesa, o shell era a única interface pra interagir com o computador. Hoje em dia as interfaces gráficas de 20g deixam os botõeszinhos coloridos e bonitinhos mas o shell continua na ativa, lutando pra recuperar sua popularidade ele é tipo o seu pai falando "no meu tempo....", ele existe em qualquer sistema que você imaginar, só o Windows tem 2 shells (não me pergunta por que, é vício em dificultar as coisas)

A maioria dos sistemas Unix/like usam o bash (Bourne Again Shell) como o shell principal, pensa no bash como a versão melhorada do sh "mas eu não gosto do bash", sem problema meu pequeno gafanhoto, existem milhares de alternativas pro bash, Zsh, Tcsh, Ksh, tem até um Fish, "Por que tem um shell chamado fish?" Por que não teria?

# Shell(s)

Existem 3 tipos de shells, explicando de uma forma preguiçosa é o seguinte:

Reverse shell: É tipo convidar alguém pra sua casa só que ao contrário, você obriga o computador alvo a se conectar ao seu pc (em outras palavras você comete uma invasão de domicilio informal)

Bind Shell: É como se você deixasse a porta da sua casa aberta e esperasse alguém entrar nela. o shell "te amarra" numa porta do alvo e espera conexão

Web shell: É como se você tivesse esquecido a chave do portão em casa e gritasse pra sua mãe pegar pra você. Você dá comandos a partir do navegador

A definição completa de todos os shells tá na aula de [shells](../../hacking/geral/shell/shell.md)
Caso você ainda não saiba oque é uma porta, uma porta é basicamente a janela (ou uma porta, o que faz mais sentido) de uma casa, se a porta estiver aberta, qualquer um pode passar por ela. No TI, uma porta é onde uma conexão começa e termina

portas tem números, da 0 até a 1023 são portas reservadas

