# Antes de começar com o hacking, é preciso saber como um sistema Linux funciona e por que ele é útil no hacking

**O linux é um dos Sistemas mais manjados do mundo e é um sistema flexível, ele é leve, o requisito minimo de um linux é de 512Mb de ram dependendo da distribuição, é bem leve, então você vai ter bastante espaço pra guardar aqueles arquivos seus arquivos pesados. Provavelmente você já usou um linux, como eu disse ele é muito manjado, então todo mundo já usou linux, seja em um carro, ou até nos semáforos da cidade, obviamente, o linux tem suas desvantagens, ele não é tão simples de aprender, entender e usar**

**Para fazer o linux mais leve, cagaram pra um monte de funções dos concorrentes, tipo as GUIs, a maioria dos linux são customizáveis pelo usuário ou são pré-definidas para um público alvo, então relaxa, você não precisa esperar 4 horas pra baixar um sistema cheio de aplicativo louco que você nem vai usar**

**o Linux pode ter GUIs a menos comparado a alguns sistemas lotados de GUIs bugadas ou inúteis, por isso, graças ao gênio que inventou o *Terminal* você tem uma interface que faz as mesmas coisas que as trocentas GUIs dos outros sistemas, mas é 30 vezes mais leve e mais fácil de usar (literalmente algumas palavras e pronto, você invadiu o blog da sua mãe) você pode usar o terminal para usar comandos, criar scripts ou ganhar acesso remoto a um sistema, por *SSH*, *FTP*, etc...**

## Comandos básicos de navegação

O terminal tem alguns comando que se você não souber você não vai conseguir nem descobrir o nome de um arquivo (literalmente):

| Comando  | Descrição                          | Exemplo                                 |
|----------|------------------------------------|-----------------------------------------|
| echo     | Exibe qualquer texto fornecido na tela|`root@linux1:~$ echo "Hello, world!` <br> output: `Hello, world!`|
| whoami   | Verifica qual é o usuário logado atualmente | `root@linux1:~$ whoami` <br> output: `root` |
| ls       | Listagem de diretórios e arquivos | `root@linux1:~$ ls` <br> output:  `a.txt` <br> `text.txt` `documents` <br> `folder` |
| cd <diretório> | Altera de um diretório pra outro | `root@linux1:~$ cd documents` <br> output: `root@linux1:~/documents $`|
| cat <arquivo>  | concatenar arquivos | `root@linux1:~$ cat text.txt` <br> output: `Conteúdo do arquivo text.txt`|
| pwd            | imprime o diretório de trabalho | `root@linux1:~/documents $ pwd` <br> output: `~/documents`|

- ls: **antes de descobrir o conteúdo de pastas e arquivos, você precisa saber o nome e localização deles. Isso é possível usando ls (abreviação de list)**
```
root@linux1:~$ ls
a.txt text.txt documents folder access.log
```

Com o nome das pastas, você pode ter uma ideia do que esperar de cada uma e abrir as com mais potencial primeiro

*Dica: Você pode listar o conteúdo de um diretório sem ter que navegar até ele usando ls e o nome do diretório. Ou seja, ls documents*

- cd: **Agora que você sabe as pastas que você pode abrir, use cd (abreviação de *change directory*) para acessa-las, para fazer isso, você precisa usar `cd <directory>`, depois, você pode combinar com ls:**
```
root@linux1:~$ cd documents
root@linux1:~/documents $ ls
"Arquivos secretos" imagem.jpeg "Confidencial" clientes.txt
```

*Dica: Você não precisa navegar para o próximo diretório disponivel, você pode por exemplo usar cd documents/"arquivos secretos" para ir direto para arquivos secretos*
- cat: **Saber da existência de um arquivo é útil, mas não ajuda em nada se você não puder abrir ele, por enquanto você vai aprender a ler arquivos, mas no futuro vai aprender a transferi-lo de uma máquina para outra também, enquanto isso, vamos usar o comando cat (Abreviação de concatenar) para exibir o conteúdo de arquivos (não necessáriamente .txt)**

```shell

root@linux1:~/documents $ ls
"Arquivos secretos" imagem.jpeg "Confidencial" clientes.txt
root@linux1:~/documents $ cat clientes.txt
cliente 1. Almir        email: almirAzevedo@hotmail.com
cliente 2. Gabriel      email: gabriel__@gmail.com
cliente 3. júlio        email: Ju__l_io@yahoo.com
```

As vezes senhas (sim, as pessoas guardam senhas em arquivos), usuários, credenciais ou configurações são armazenadas em arquivos que suportam o cat, no nosso caso, descobrimos o E-mail do que parecem ser 3 clientes de alguma empresa, isso pode ser útil para técnicas de engenharia social ou phishing

*Dica: no mesmo estilo do ls e cd, você pode usar cat para exibir o conteúdo de um arquivo dentro de diretórios sem ter que navegar até ele usando cat e o nome do diretório. Ou seja, cat /Documents/tarefas.txt*

- pwd: **É fácil se perder enquanto você navega em uma máquina, principalmente no começo, por isso o comando pwd (abreviação de print work directory). Nos comandos anteriores, navegamos até o diretório documents, mas qual é o path completo?**

```
root@linux1:~/documents $ pwd
/home/ubuntu/Documents
```

Antes, o terminal mostrava que o diretório atual era documents, mas até agora não sabiamos aonde documents estava armazenado, sabendo disso, fica mais fácil voltar lá

## Comandos básicos de pesquisa de arquivos

O linux é um sistema bom se você não for do tipo usuário fiel de Windows. a medida que você executa os comandos mais simples, você acaba usando eles até quando não é pra usar (experiência própria)

uma das melhores formas de usar esse sistema DO JEITO CERTO é combinando comandos no terminal para procurar arquivos no sistema, sem cd e sem ls a cada 4 segundos nesse caso, ao invés disso, podemos usar *find* para não ficar repetindo a meesma coisa 400 vezes

- find: **O comando find pode ser usado de forma simples ou muito complexa, dependendo do objetivo. É normal que uma máquina tenham um diretório dentro do outro dentro do outro e por aí vai, e isso acaba tornando a busca muito chata e complexa**

Vamos imaginar que você sabe o nome do arquivo que está procurando, mas não lembra aonde ele está exatamente, vamos procurar o arquivo passwd.txt com find

```
root@linux1:~$ find -name passwd.txt
./documents/.senhas.txt
```
Boa, você achou o arquivo dentro de documents.

*dica: Se você diver 40% de visão, deve ter visto um "." antes de passwd.txt, então ele não vai ser listado normalmente, para ler arquivos ocultos você pode usar `ls -a` ou `ls -Hidden` para powershell, sim usuário de powershell, você digita mais e tem um terminal feio, parabéns*

Para encontrar o arquivo usamos -name, mas e se não soubermos o nome ou queremos pesquisar todos os arquivos com uma extensão especifica? Podemos usar o curinga(*) para procurar qualquer coisa com .txt no diretório atual.

```
root@linux1:~$ find -name *.txt
./documents/.senhas.txt
./Documents/clientes.txt
```

- Grep: **Outro comando ótimo é o *grep*, que permite pesquisar arquivos por valores. Por exemplo procurar alguma frase em um arquivo**

```
root@linux1:~/documents $ grep "senha" passwd.txt
senha 1 - - !4CFF0

[....]
```

Aqui o comando grep filtra a palavra senha no arquivo passwd.txt (o arquivo passwd existe em sistemas linux mas nem perde seu tempo procurando a palavra senha dentro)

## Operadores do terminal

Os operadores do terminal são importantes para você perder menos tempo executando comandos e perder mais tempo lembrando o quee cada operador faz 
| Operador | Descrição                                                                                       | Exemplo                          |
|----------|-------------------------------------------------------------------------------------------------|----------------------------------|
| `&`      |  executar comandos em segundo plano no terminal.                                         | `comando &`                      |
| `&&`     | Combina múltiplos comandos em uma linha ; o segundo comando só executa se o primeiro for bem-sucedido. | `comando1 && comando2`           |
| `>`      | Redireciona a saída de um comando para outro lugar, como um arquivo, sobrescrevendo seu conteúdo se o arquivo já existir. | `echo "conteúdo" > arquivo.txt`  |
| `>>`     | Redireciona a saída de um comando para outro lugar, como um arquivo, adicionando ao final do conteúdo existente no arquivo. | `echo "mais conteúdo" >> arquivo.txt` |


- `&`: **esse operador executa comandos em segundo plano, se quisermos copiar um arquivo grande, levaria uma eternidade seu terminal viraria uma pedra em quanto isso. O operador "&" no fim do comando executa a tarefa a segundo plano, sem interromper seus cyber crimes**

- `&&`: **Esse comando é enganador por se parecer muito com o operador "&",só que ao contrário dele, o operador de "&&" é usado para rodar mais de um comando de uma vez, `comando 1 &&,comando 2`. Vale lembrar ar que o comando 2 só será executado se o comando 1 for bem sucessido**

- `>`: **Esse operador é conhecido como redirecionamento de saída,  ou seja, pegamos a saída de um comando que executamos e enviamos a saída para outro lugar. Um bom exemplo disso é usar o comando echo para redirecionar a string para outro arquivo, por exemplo.**

*Nota: se o arquivo existir, o conteúdo é sobre escrito, caso contrário o arquivo é criado*

- `>>`: **Esse operador também é um direcionamento de saída, o que diferencia ele do,">". Em vez de sobreescrever o arquivo, ele adiciona o novo conteúdo ao final do arquivo, mantendo o resto do conteúdo
