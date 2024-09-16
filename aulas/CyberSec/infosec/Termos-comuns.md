# Termos comuns
scripts que você baixou e esqueceu o caminho (sem julgamento)

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


# Tipos de "chapéus"

hack é uma palavra controversa, se você falar pra alguém que entende de computadores que é um hacker, a pessoa não vai saber se você é um ladrão de dados ou um desenvolvedor bom no que faz

## "O cara mal"

Nem tudo são flores, o hack pode ser usado pro bem mas também pro mal. No geral, a palavra hacking tomou o significado negativo de invadir sistemas ou redes com uma má intenção, e isso tá errado, quem entende sabe que essa função é do Cracking não o hacking. Isso não quer dizer que se alguém te falar que a conta do roblox dele foi hackeada você vai corrigir ele, a não ser que você queira parecer um idiota desesperado pra mostrar que entende do assunto. Você sabe o que ele quis dizer. De qualquer forma a mídia (que só faz bosta) saiu associando o ato de invadir um sistema ao hacking quando o certo seria o cracking levar essa fama. Alguém que se considera ou é um cracker é chamado de Black hat. Como tudo que é ruim viraliza, esse tipo é o que a gente mais vê em filmes. A partir de agora sempre que eu citar um cracker eu vou usar o termo black hat. Eu não tô aqui pra ser seu professor de dramática. isso é só pra você diferenciar o bem do mal da forma mais simples possível

## "O cara legal"

Hackers Éticos são os bonzinhos. São apelidados de white hats. São os que usam as habilidades pra ajudar os outros. Normalmente white hats são ou pentesters ou bug bounty hunter

Normalmente você protege seu pc vendo reviews da tech tudo ou acreditando no vendedor da pichau. Alguém com conhecimento em invasão de sistemas pode preferir pagar alguém para te invadir e roubar seus dados (normalmente empresas ou pessoas jurídicas). Se der certo você corrige, documenta e tenta de novo. Isso é o básico do pentest. O processo é repetido até o white hat não conseguir acesso ao sistema. Quando isso acontece, a empresa citada pode contratar freelancers pra ter certeza que não faltou nada, esses freelancers são chamados de consultores de segurança, seguindo a nomenclatura, esses consultores podem ser chamados de blue hats

Infelizmente, sempre tem alguém com muito tempo livre, muito recurso e muito treino pra rir na cara do seu sistema "infalível" pra crackear qualquer sistema. Sempre tem novos ataques cybernéticos manuais ou vírus extremamente fortes que praticamente forçam seu pc a conceder acesso ao seu sistema e consequentemente tomar seus dados. A intenção do white hat é permitir que seu sistema seja o mais difícil de invadir possível


## O meio a meio

Se você invadir um sistema pra ganhos pessoais sem autorização, você seria um black hat. Essa parte é bem delicada, tem vários tipos de interpretações sobre o que é o meio e o que ultrapassa esse meio. Existem pessoas que ganham a vida invadindo sistemas de forma não autorizada. E depois notificando a vítima e se oferecendo pra consertar o sistema

Esse tipo de invasor é um grey hat. Por que ele sabe que o que ele tá fazendo é errado porém a intenção dele não é te roubar ou espalhar essa vulnerabilidade por aí

A maioria das pessoas não gostaria de ter seu sistema invadido sem seu conhecimento, mas o fato da pessoa te alertar isso pode acabar despertando um certo sentimento de gratidão pelo atacante (não, não é tipo síndrome de estocolmo)

Se você fosse colocar isso no mundo real: Imagina que você descobriu uma vulnerabilidade num site do governo, essa vulnerabilidade por sorte não foi explorada por ninguém (ainda) e pode ser fatal, já que envolve a captura de informações civis. Nesse caso, o tempo seria um fator crítico e que você provavelmente não teria, mas acontece que conseguir autorização de invasão é um processo demorado, principalmente quando se trata de um governo (principalmente quando se trata do brasil). Nesse caso um hacker pode invadir, deixar bem claro que ele invadiu e disponibilizar a solução. Ele cometeu um crime, mas salvou dados super sigilosos, ele tá certo ou errado? 


Sem esses caras, provavelmente a intenet hoje seria só um projeto que não foi pra frente ou uma terra sem lei


# Tipos de hacking

## Website Hacking

Quando o controle de um website (ou servidor que hospeda esse website) é passado para outra pessoa sem o consentimento e consequentemente sem o conhecimento do dono original

## Network hacking

Quando um hacker usa ferramentas como ping, arp, tracert ou qualquer outra pra capturar informações sobre dominios da internet

## Computer hacking

Quando um computador independente é alvo de um ataque, isso é hacking de um computador. Quando um computador é comprometido, o atacante tem acesso à cópia, instalação, edição ou remoção de arquivos e diretórios

## Password hacking

O mais comum no dia a dia e o que tem maior chance de te afetar, é quando um atacante recupera credenciais de um banco de dados ou da própria rede

