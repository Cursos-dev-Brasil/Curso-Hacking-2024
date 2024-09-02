# Introdução ao linux

Antes de Começar a escrever naqueles terminais de filme você precisa entender o Linux e por que ele é tão maravilhoso

Ah, o Linux! O sistema operacional que dá uma surra bem dada no Windows. Leve, rápido e bonito. Se você já se perguntou por que o Linux é tão amado por hackers e gente do ti, a resposta é simples: ele é poderoso e não exige muito. Você pode instalar uma versão com 512MB de RAM. Isso mesmo, menos do que o chrome consome a cada 2 abas!

Embora o Linux seja útil, ele tem suas diferenças. Pode ser mais complicado aprender, mas é tipo aprender a andar de bicicleta sem rodinhas – um pouco difícil no começo, mas depois você voa. O Linux é tipo o amigo que não se importa de não ter um guarda-roupa cheio de roupas chamativas. Ele é minimalista e, quando você aprende a usar, fica claro que não precisa de todo aquele luxo.

Ao invés de GUIs com bugs e opções que você nunca usa, o Linux tá lá pra te dar o poder com menos bagunça. E se você gosta de escrever, então você vai amar. O Terminal é tipo o superpoder dos hackers – uma interface que pode fazer quase tudo com uns comandos. É tipo transformar seu pc numa máquina de combate com um simples toque no teclado (só que sem a parte do combate).

## Comandos de Navegação: Sua Primeira Aula no Terminal

Vamo ver alguns comandos que vão ajudar a navegar no Linux

| Comando          | Descrição                                                      | Exemplo de Uso                        | Saída Exemplo                     |
| ---------------- | -------------------------------------------------------------- | ------------------------------------- | --------------------------------- |
| `echo`           | Quer exibir uma mensagem na tela? echo é o seu amigo.          | `root@linux1:~$ echo "Hello, world!"` | `Hello, world!`                   |
| `whoami`         | tá achando que logou no user errado? whoami te fala a verdade. | `root@linux1:~$ whoami`               | `root`                            |
| `ls`             | O comando que revela todos os segredos (do diretório).         | `root@linux1:~$ ls`                   | `a.txt text.txt documents folder` |
| `cd <diretório>` | pular de diretório em diretório que nem um besta.    | `root@linux1:~$ cd documents`         | `root@linux1:~/documents $`       |
| `cat <arquivo>`  | Quer ver o que tá dentro de um arquivo? cat dá uma olhada por você.  | `root@linux1:~$ cat text.txt`         | `Conteúdo do arquivo text.txt`    |
| `pwd`            | Se perdeu no caminho? pwd te mostra a saída.                   | `root@linux1:~/documents $ pwd`       | `/home/ubuntu/Documents`          |

## Comandos de Pesquisa de Arquivos: Caçando Tesouros
Se você acha que procurar arquivos é tipo procurar uma agulha no palheiro, pensa denovo, e você acertou. O Linux tem ferramentas pra te poupar tempo de vida:

| Comando | Descrição | Exemplo | Saída |
|---------|-----------|---------|-------|
| `find`  | O comando para caçar arquivos em qualquer lugar. | `find -name passwd.txt` | `./documents/.senhas.txt` |
| `grep`  | Vai procurar o texto que você pedir pra você não ficar 30 minutos fazendo isso. | `grep "senha" passwd.txt` | `senha 1 - - !4CFF0` |

**Dica:** Se você encontrar arquivos ocultos, use `ls -a` para revelá-los. Sim, alguns arquivos são tímidos!

## Operadores do Terminal: Seus Superpoderes Digitais
Os operadores do terminal são quase truques pra tornam sua vida mais fácil economizando 0.7 segundos.

| Operador | Descrição | Exemplo | Observação |
|----------|-----------|---------|------------|
| `&`      | Executa comandos em segundo plano. | `comando &` | (Porque você não precisa ficar esperando um comando gigante terminar) |
| `&&`     | Combina comandos, onde o segundo só roda se o primeiro der certo. | `comando1 && comando2` | (Pra que fazer uma coisa de cada vez, se você pode fazer duas, uma depois da outra?) |
| `>`      | Redireciona a saída pra um arquivo, substituindo o conteúdo se o arquivo já existir. | `echo "conteúdo" > arquivo.txt` | (Sobre escreve sem dor de cabeça!) |
| `>>`     | Adicione a saída ao final de um arquivo sem apagar o que já estava lá. | `echo "mais conteúdo" >> arquivo.txt` | (Porque você pode querer adicionar, não apagar!) |

Agora você tá  pronto para explorar o Linux e começar a hackear sistemas bancários com ferramentas prontas (contém ironia). 


6