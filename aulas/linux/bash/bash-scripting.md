# O que é Bash?

Imagina o Bash como o super-herói dos scripts de terminal. Ele é a linguagem que te ajuda a realizar tarefas, automatizar backups e salvar alguns segundos do seu dia, tudo com alguns comandos. Ele faz isso rodando no terminal do Linux e do macOS (novamente o windows sendo humilhado), e é o rei dos scripts que deixam o seu trabalho mais fácil.

## Começando no bash
Cada script Bash começa com a mesma linha de código, como uma introdução padrão de youtuber infantil:


`#!/bin/bash`

Essa linha é tipo a "Abertura" de um filme: diz ao sistema qual arsenal ele deve usar para rodar o script.

## Execute seu Primeiro Script
Vamos criar um script de boas-vindas, como um convite para uma festa:

```bash
#!/bin/bash
echo "HELLO WORLD"
ls
whoami
id
```
Salve isso como hello.sh, adicione privilégios:


`chmod +x hello.sh`
E execute a festa:


`./hello.sh`
## Variáveis: O começo da programação
Definir variáveis em Bash é como escolher o nome do seu personagem em um jogo:

`name="phantom"`
Para usar a variável, você só precisa colocar um $ antes do nome dela:


`echo $name`

A saída será phantom – o nome do seu personagem.

Para uma festa mais divertida:

```bash
name="Billy"
age=21
echo "$name tem $age anos de idade"
```

### Parâmetros: Os Convites para a Festa
Você pode passar parâmetros nos seus scripts como convites. Aqui está um exemplo

```bash
#!/bin/bash
name=$1
surname=$2
echo "$name $surname"
Execute seu script com parâmetros:
```

`./script.sh João Silva`

E assista a mágica!

Se preferir uma entrada interativa, use o comando read:

```bash
echo "Digite seu nome: "
read name
echo "Olá, $name"
```

### Arrays: Um grupo em uma linha
Arrays podem ser traduzidas como uma lista de amigos que você pode acessar usando índices (começam em 0). Aqui está um exemplo de um array de transporte:


`transporte=("carro" "trem" "bicicleta" "onibus")`

Para exibir todos os transportes do grupo:

`echo "${transporte[@]}"`

Para um item especifico específico:

`echo "${transporte[1]}"` (exibe trem)

Se quiser remover um amigo:

`unset transporte[1]`

adicionar um novo:

`transporte[1]="avião"`

## Condicionais
As condicionais são quase um pilar em qualquer algoritmo. elas servem para verificar se uma coisa é igual (ou diferente, existem vários tipos) a outra coisa:

```bash
#!/bin/bash
count=10
if [ $count -eq 10 ]; then
    echo "True"
else
    echo "False"
fi

```
Você pode usar essas condições para verificar se arquivos existem ou são graváveis, e até mesmo criar um novo arquivo se necessário.

### Operadores Relacionais
Aqui temos a tabela de operadores relacionais – é quase uma tabela de comparação:

| Comando | Descrição         |
|---------|-------------------|
| -eq     | Igualdade         |
| -ne     | Diferença         |
| -gt     | Maior que         |
| -lt     | Menor que         |
| -ge     | Maior ou igual    |
| -le     | Menor ou igual    |

Exemplo de comparação:

```bash
#!/bin/bash
guess=$1
if [ "$guess" = "guessme" ]; then
    echo "Eles são iguais"
else
    echo "Eles não são iguais"
fi
```

### Verificação de Arquivos com Condicionais
O seguinte script verifica se um arquivo existe e é gravável, e então decide o que fazer:

```bash
#!/bin/bash
file=$1
if [ -f "$file" ] && [ -w "$file" ]; then
    echo "Olá" >> "$file"
else
    echo "Olá" > "$file"
fi
```

### Debugando: O Paracetamol da programação
Às vezes, você precisa de uma mãozinha com o código. O modo debug no Bash é tipo um superpoder que revela o que está acontecendo com seu script. Para ativar o modo debug:


```bash
set -x
# Código que será depurado
set +x
```

## O Desafio Final

Crie um aplicativo de contatos, que tenha funções como adicionar contatos, excluir contatos, ver contatos e qualquer outra função, use condicionais e arrays

