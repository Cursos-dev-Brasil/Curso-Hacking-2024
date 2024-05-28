# Fundamentos Linux Parte 2

*obs: devido ao tamanho do arquivo anterior, criamos um novo*

## Comandos para interagir com sistema de arquivos
Outros comandos são muito importantes para: 
- criar diretórios
- apagar diretórios
- mover diretórios
- criar arquivos
- apagar arquivos
- mover arquivos

| Comando | Nome completo  | Função                         |
|---------|----------------|--------------------------------|
| mkdir   | make directory | cria um diretório              |
| rm      | remove         | remove um arquivo ou diretório |
| mv      | move           | mover um arquivo ou diretório  |
| cp      | copy           | cópia um arquivo ou diretório  |
| touch   | touch          | criar um arquivo               |
| file    | file           | determina um tipo de arquivo   |

- touch: **Criar um arquivo é muito simples, o comando touch aceita apenas um argumento, que é o nome do arquivo que vai ser criado, ao executar o comando: `touch note` o arquivo note é criado em branco, para adicionar texto, você pode usar o comando echo e os comandos ">" e ">>"**


## Parâmetros

A maioria dos comandos tem parâmetros. Parâmetros são formas de especificar algo para o comando. Se nenhum parâmetro for atribuído, o comando executará a forma padrão. Parâmetros são identificados com um hífen (-) seguido por uma letra ou palavra. Ex: `ls -a`

## Conexão usando *SSH*
Uma conexão SSH (Secure Shell) é um tipo de protocolo usado na transferência de dados entre máquinas. É um protocolo que criptografa seus dados ao serem enviados e só os descriptografa quando a mensagem alcança o destino.

### Sintaxe SSH
A sintaxe SSH é simples e fácil de lembrar. Para se conectar a uma máquina usando SSH, a sintaxe básica é:
`ssh nome_de_usuario@ip_alvo`

Se tudo der certo, o SSH vai pedir a confirmação de que você confia no Host. Caso você confirme, ele pedirá a senha.

*Nota: o campo da senha não vai ter feedback visual, ou seja, a senha não será mostrada. Apenas digite a senha e aperte enter.*