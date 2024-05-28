# fundamentos Linux parte 2

*obs: devido ao tamanho do arquivo anterior, criamos um novo*

## Comandos para interagir com sistema de arquivos 
outros comandos são muito importantes para: 
- criar diretórios
- apagar diretórios
- mover diretórios
- criar arquivos
- apagar arquivos
- mover arquivos

| Comando | Nome completo | função |
| mkdir | make directory |cria um diretório |
| rm | remove | remove um arquivo ou diretório |
| mv | move | mover um arquivo ou diretório |
| cp | copy | cópia um arquivo ou diretório |
| touch | touch | criar um arquivo |
| file | file | determina um tipo de arquivo |
## parâmetros

A maioria dos comandos tem parâmetros, parâmetros são formas de especificar algo para o comando, se nenhum parâmetro for atribuído o comando executará a forma padrão, parâmetros são identificados com um hífen(-) seguido por uma letra ou palavra. Ex: ls -a

## conexão usando *SSH*
uma conexão Ssh (secure shell) é um tipo de protocolo usado na transferência de dados entre máquinas, é um protocolo que criptografa seus dados ao ser enviados e só os descriptografa quando a mensagem alcança o destino

### Sintaxe ssh
A sintaxe ssh é simples e fácil de lembrar. para se conectar a uma máquina usando ssh a sintaxe básica é:
`ssh nome_de_usuario@ip_alvo`

se tudo der certo, o ssh vai pedir a confirmação de que você confia no Host, caso você confirme ele pedirá a senha

*nota: o campo da senha a não vai ter feedback visual, ou seja, a senha não será mostrada, só digite a senha e aperte enter

