# Antes de começar com o hacking, é preciso saber como um sistema Linux funciona e por que ele é útil no hacking

**O linux é um dos Sistemas operacionais mais utilizados do mundo e é um sistema altamente flexível, além de ser leve, o requisito minimo de um linux são 512Mb de ram dependendo da distro. Provavelmente você já usou um linux, seja em um sistema de um carro, ou até nos semáforos da cidade, obviamente, o linux também tem suas desvantagens, ao mesmo tempo que é flexível e leve, não é tão simples de aprender, entender e até usar**

**Para fazer o linux mais leve possível, muitas coisas devem ser sacrificadas, como GUI's, portanto, uma boa parte das interfaces Windows ou Mac, podem não estar disponiveis no Linux, a maioria dos linux são altamente customizáveis pelo usuário ou já são pré-definidas para um público alvo**

**Como foi dito, o Linux pode não ter as mesmas GUI's de outros sistemas, e para anular isso, o *Terminal* é usado para personalizar o sistema, usar comandos, criar scripts ou até mesmo obter acesso remoto a um sistema, seja por *SSH*, *FTP*, etc...**

## Comandos básicos de navegação

O terminal tem alguns comandos básicos que vão ser indispensáveis em um pentest ou qualquer coisa do tipo. alguns desses incluem:

| Comando  | Descrição                          | Exemplo                                 |
|----------|------------------------------------|-----------------------------------------|
| echo     | Exibe qualquer texto fornecido na tela|`root@linux1:~$ echo "Hello, world!` <br> output: `Hello, world!`|
| whoami   | Verifica qual é o usuário logado atualmente | `root@linux1:~$ whoami` <br> output: `root` |
| ls       | Listagem de diretórios e arquivos | `root@linux1:~$ ls` <br> output:  `a.txt` <br> `text.txt` `documents` <br> `folder` |
| cd <diretório> | Altera de um diretório pra outro | `root@linux1:~$ cd documents` <br> output: `root@linux1:~/documents $`|
| cat <arquivo>  | concatenar arquivos | `root@linux1:~$ cat text.txt` <br> output: `Conteúdo do arquivo text.txt`|
| pwd            | imprime o diretório de trabalho | `root@linux1:~/documents $ pwd` <br> output: `~/documents`|

- ls: **antes de descobrir o conteúdo de pastas e arquivos, você precisa saber o nome e localização deles. Isso é possível usando ls**
```
root@linux1:~$ ls
a.txt text.txt documents folder access.log
```

Com o nome das pastas, você pode ter uma ideia do que esperar de cada uma e abrir as com mais potencial primeiro

*Dica profissional: Você pode listar o conteúdo de um diretório sem ter que navegar até ele usando ls e o nome do diretório. Ou seja, ls documents*

- cd: **Agora que você sabe as pastas disponiveis, podemos usar cd (abreviação de *change directory*) para acessa-las, para fazer isso, você precisa usar cd e o diretório, depois disso, podemos combinar com ls:**
```
root@linux1:~$ cd documents
root@linux1:~/documents $ ls
"Arquivos secretos" imagem.jpeg "Confidencial" clientes.txt
```

*Dica profissional: Você não precisa necessáriamente navegar para o próximo diretório disponivel, você por exemplo usar cd documents/"arquivos secretos" para ir direto para arquivos secretos*
- cat: **Saber da existência de um arquivo é útil, mas não ajuda em nada se você não puder abri-lo, por enquanto você vai aprender a ler arquivos, mas no futuro vai aprender a transferi-lo de uma máquina para outra também, enquanto isso, vamos usar o comando cat (Abreviação de concatenar) para para exibir o conteúdo de arquivos (não necessáriamente .txt)**

```

root@linux1:~/documents $ ls
"Arquivos secretos" imagem.jpeg "Confidencial" clientes.txt
root@linux1:~/documents $ cat clientes.txt
cliente 1. Almir        email: almirAzevedo@hotmail.com
cliente 2. Gabriel      email: gabriel__@gmail.com
cliente 3. júlio        email: Ju__l_io@yahoo.com
```

As vezes senhas, usuários, credenciais ou até mesmo flags (em CTF's) ou configurações são armazenadas em arquivos que suportam o cat, no nosso caso, descobrimos o E-mail do que parecem ser 3 clientes de alguma empresa, isso pode ser útil para técnicas de engenharia social ou phishing

*Dica profissional: no mesmo estilo do ls e cd, você pode usar cat para exibir o conteúdo de um arquivo dentro de diretórios sem ter que navegar até ele usando cat e o nome do diretório. Ou seja, cat /Documents/tarefas.txt*

- pwd: **É fácil se perder enquanto você navega em uma máquina, principalmente no começo, por isso o comando pwd (abreviação de print work directory). Nos comandos anteriores, navegamos até o diretório documents, mas qual é o path completo?**

```
root@linux1:~/documents $ pwd
/home/ubuntu/Documents
```

Antes, o terminal informava que o diretório atual era documents, mas até agora não sabiamos aonde documents estava armazenado, sabendo disso, fica mais fácil voltar lá no futuro

## Comandos básicos de pesquisa de arquivos

O linux é um sistema muito eficiente se você estiver familiarizado. a medida que você executa os comandos mais comuns, eles acabam se torando memória muscular

uma das maneiras de ser eficiente nesse tipo de OS é combinando comandos para procurar arquivos em todo o sistema, sem cd e sem ls consistentemente nesse caso, ao invés disso, podemos usar *find* para automatizar isso

- find: **O comando find pode ser usado de forma simples ou muito complexa, dependendo do objetivo. É normal que uma máquina tenham um diretório dentro do outro dentro do outro e por aí vai, e isso acaba tornando a busca muito chata e complexa**

Vamos criar uma situação em que você sabe o nome do arquivo que está procurando, mas não lembra a sua localização exata, vamos procurar o arquivo passwd.txt com find

```
root@linux1:~$ find -name passwd.txt
./documents/.senhas.txt
```
Ótimo, encontramos o arquivo dentro de documents.

*dica: Observe que tem um "." antes do nome do arquivo, isso significa que ele não será listado para o explorador de arquivos ou no próprio terminal, para corrigir isso você pode usar o comando ls -a ou ls -Hidden para exibir os arquivos ocultos*

Para encontrar o arquivo que sabemos usamos -name, mas e se não soubermos o nome ou queremos pesquisar todos os arquivos com extensão .txt

Podemos usar o curinga(*) para procurar qualquer coisa com .txt no diretório atual.

```
root@linux1:~$ find -name *.txt
./documents/.senhas.txt
./Documents/clientes.txt
```

- Grep: **Outro comando ótimo é o *grep*, que nos permite pesquisar arquivos por valores especificos. Por exemplo procurar alguma frase em um arquivo especifico**

```
root@linux1:~/documents $ grep "senha" passwd.txt
senha 1 - - !4CFF0

[....]
```

Aqui o comando grep filtra a palavra senha no arquivo passwd.txt

## Operadores do terminal

Os operadores do terminal são muito importantes para garantir um melhor aproveitamento e uma melhor produtividade em ambiente Linux 
| Operador | Descrição                                                                                       | Exemplo                          |
|----------|-------------------------------------------------------------------------------------------------|----------------------------------|
| `&`      |  executar comandos em segundo plano no terminal.                                         | `comando &`                      |
| `&&`     | Combina múltiplos comandos em uma linha ; o segundo comando só executa se o primeiro for bem-sucedido. | `comando1 && comando2`           |
| `>`      | Redireciona a saída de um comando para outro lugar, como um arquivo, sobrescrevendo seu conteúdo se o arquivo já existir. | `echo "conteúdo" > arquivo.txt`  |
| `>>`     | Redireciona a saída de um comando para outro lugar, como um arquivo, adicionando ao final do conteúdo existente no arquivo. | `echo "mais conteúdo" >> arquivo.txt` |


- `&`: **esse operador executa comandos em segundo plano, se quisermos copiar um arquivo grande, levaria muito tempo e travaria nosso terminal. O operador "&" adicionado ao comando executa a tarefa a segundo plano, sem precisar interromper outros processoa**

- `&&`: **Esse comando é enganador por se parecer muito com o operador "&",só que ao contrário dele, o operador de "&&" é usado para rodar mais de um comando de uma vez, `comando 1 &&,comando 2`. Vale lembrar ar que o comando 2 só será executado se o comando 1 for bem sucessido**

- `>`: **Esse operador é conhecido como redirecionamento de saída,  ou seja, pegamos a saída de um comando que executamos e enviamos a saída para outro lugar. Um bom exemplo disso é usar o comando echo para redirecionar a string para outro arquivo, por exemplo.**

*Nota: se o arquivo existir, o conteúdo é sobre escrito, caso contrário o arquivo é criado*

- '>>': **Esse operador também é um direcionamento de saída, o que diferencia ele do,">". Em vez de sobreescrever o arquivo, ele adiciona o novo conteúdo ao final do arquivo, mantendo o resto do conteúdo