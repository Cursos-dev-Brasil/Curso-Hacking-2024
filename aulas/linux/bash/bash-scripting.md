# Bash
## Oque é bash?

Bash é uma linguagem de script que roda no terminal na maioria das distribuições Linux e no MacOS. Scripts shell são uma sequência de comandos bash dentro de um arquivo, combinados para realizar tarefas mais complexas do que simples comandos de uma linha, e são especialmente úteis para automatizar tarefas de administração de sistemas, como backups.

Algumas coisas básicas do bash são:

- Sintaxe
- Variáveis
- Parâmetros
- Arrays
- Condicionais

Um script bash **sempre começa com a mesma linha de código no topo do script**

`#!/bin/bash`

Isso é para o shell saber que precisa usar o bash para iniciar seu arquivo no terminal

Você pode executar comandos padrão do Linux dentro do script bash, e eles são executados e formatados. Por exemplo, você pode usar o comando `ls` dentro de um script bash, você vai ver a saída ao executar o arquivo

Antes de executar o script bash, você precisa atribuir a ele a permissão de execução

`chmod +x script.sh`

ele é executado usando:

`./script.sh`

crie um script bash com esse conteúdo:

```
echo "HELLO WORLD"
ls
whoami
id
```

agora execute usando ./nome_do_script.sh (não esqueça que a primeira linha deve ser `#!/bin/bash`)

### Variáveis

a forma de escrever variáveis em bash é:
`name="phantom"`

Nesse caso, você atribuiu o valor phantom a variável name

**lembrete: em bash, você não pode ter espaços entre o nome, o sinal de igual (recebe na programação) e o valor**

#### Usando sua variável

É muito simples usar as variáveis em um script bash, a única coisa que você precisa é colocar um `$` e o nome da variável (sem espaços)

por exemplo:
```
name="phantom"
echo $name
```

Caso você teste isso, você deverá ver **phantom** na saída

Variáveis tornam seu código muito mais simples, elas ajudam você a guardar dados e permite que você não fique repetindo o mesmo código centenas de vezes

Você pode usar quantas variáveis quiser no código, e quantas variáveis quiser em cada comando, por exemplo: 
```
name="Billy"
age=21
echo "$name tem $age anos de idade"
```

### Parametros

Uma das principais funcionalidade do bash são os parametros

Primeiro, vamos usar os parametros especificados usando a cli (command line interface) para executar o arquivo. Existem várias formas de usa-los, mas normalmente tem o "$" porque um parametro é uma variável (em bash)

```
teste=$parametro
echo $teste
```
Agora execute o script com a palavra teste (./script.sh teste)

em vez de receber "parametro", a saída deve ser "teste"

outro exemplo:
```
name=$1
surname=$2
```
Agora faça a mesma coisa da primeira vez, mas com 2 palavras diferentes
O resultado é o último parametro que você usou

Se você não quiser usar esse tipo de parametro, você pode permitir que o usuário digite seu nome de forma interativa, você pode fazer isso usando o comando `read`
```
echo "Digite seu nome: "
read name
echo "Olá, $name"
```

Quando executado, você deve ver algo como: 
<br>
![saída](../../../content/bash-input.png)

Para se adaptar com comandos básicos, você pode tentar criar algo, como um gerador de biografia, onde você usa nome idade e ocupação como parametros, armazena em variáveis exibe na tela dentro de uma frase

Lembra, a prática é o melhor jeito de estudar, já que você tem mais liberdade

### Arrays
Arrays são usados para armazenar mais de um dado em uma variável, esses dados são acessados por indices (index). Na programação, o **index começa em 0**

sintaxe:
`transporte=("carro" "trem" "bicicleta" "onibus")`

transporte = nome da array
cada frase entre aspas é um item de transporte
index:
carro = 0
trem = 1
bicicleta = 2
onibus = 3

para exibir todos os elementos da array:

`echo "${transporte[@]}"`
"@" Se refere a todos os elementos do array

Para exibir um elemento especifico você usa o indice dele
`echo "${transporte[1]}"`

Como trem é o index 1, trem é mostrado na saída

#### Modificando e removendo elementos da array

para remover um elemento de uma array, você pode usar unset

`unset transporte[1]`

Isso remove o item trem 

para definir um novo valor:
`transporte[1]="avião"`

tente expandir seu criador de biografia, incluindo arrays para armazenar mais nomes e mais fatos sobre a pessoa. 

### Condicionais

Estruturas condicionais na programação são muito comuns, elas são blocos de código que só são cumpridas caso uma condição seja atendida, normalmente isso é determinado com operadores relacionais

Vamos fazer uma declaração if simples para verificar se uma variável é igual a um valor, também é possível fazer um script que verifica se um arquivo existe e se ele é gravável, se for, escrevemos uma mensagem no arquivo, se não for ele é excluído e um novo é criado

Sintaxe básica:
if [condição]
then
Tudo entre then e fi é executado se a condição passar
fi

exemplo prático:
```
#!/bin/bash
count=10
if[$count -eq 10]
then 
    echo "True"
else
    echo "false"
fi
```
Essa condição testa se a variável count é igual a 10, e se for, imprime True, caso contrário imprime False


Você pode terminar o projeto do gerador de biografia adicionando uma condicional, você pode por exemplo adicionar uma condição para testar se a idade é maior ou igual a 18, se não for você exibe a mensagem "Você não pode trabalhar", e se for, você exibe "qual é seu trabalho" e um read logo depois


Boa sorte e tente não consultar as aulas para fazer o projeto, a prática é o caminho mais fácil para melhorar
#### Operadores relacionais


| Comando | Nome completo  |
|---------|----------------|
| -eq | Verifica se o valor de dois operandos é igual; se sim, a condição é verdadeira |
| -ne | Verifica se o valor de dois operandos é diferente; se sim, a condição é verdadeira. |
| -gt | Verifica se o valor do operando esquerdo é maior que o do direito; se sim, a condição é verdadeira. | 
| -lt | Verifica se o valor do operando esquerdo é menor que o do direito; se sim, a condição é verdadeira. |
| -ge |Verifica se o valor do operando esquerdo é maior ou igual ao do direito; se sim, a condição é verdadeira. |

você também pode usar operadores comuns:

```
#!/bin/bash

guess=$1

if [ "$guess" = "guessme" ]
then
    echo "They are equal"
else
    echo "They are not equal"
fi
```
#### Verificação de arquivos com condicional

```
#!/bin/bash

file=$1

if[-f "$file"] && [-w "$file"]
then
    echo "Hi" >> "$file"
else
    echo "Hi" > "$file"
fi
```

A flag -f verifica se é um arquivo e a flag -w verifica se é um arquivo gravável

### Debugando um arquivo

O Debug é uma parte muito importante na programação e pode te salvar na hora de resolver um problema o mais rápido possível. O bash tem algumas funções feitas para facilitar a sua vida

Agora que você sabe a sintaxe básica, você pode montar um script bash básico e talvez você faça algo errado, então você pode consertar isso com o debug mode para ver aonde você errou

O debug mode te mostra quais linhas funcionam e quais não funcionam, se você quiser debugar até um certo ponto do código, você pode usar `set x-` para iniciar o debug e `set x+` para finalizar
exemplo:
```
echo "hi"
set -x
# Essa parte do código seria debugada
set +x
```

