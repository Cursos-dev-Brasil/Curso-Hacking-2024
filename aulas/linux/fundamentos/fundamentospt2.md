# Fundamentos Linux Parte 2

*obs: O arquivo anterior é muito grande, então criamos a parte 2 (mentira, é só pra somar mais conteúdo mesmo)*

## Comandos para interagir com sistema de arquivos
Outros comandos são importantes para: 
- criar diretórios
- apagar diretórios
- mover diretórios
- criar arquivos
- apagar arquivos
- mover arquivos

| Comando | Nome completo  | Função                         |
|---------|----------------|--------------------------------|
| touch   | touch          | criar um arquivo               |
| mkdir   | make directory | cria um diretório              |
| rmdir   | remove directory | Remove um diretório |
| rm      | remove         | remove um arquivo |
| mv      | move           | mover um arquivo ou diretório  |
| cp      | copy           | copia um arquivo ou diretório  |
| file    | file           | determina um tipo de arquivo   |

- touch e mkdir: **Criar arquivos ou pastas é muito simples, o comando touch aceita apenas um argumento, que é o nome do arquivo que vai ser criado, ao executar o comando: `touch note` o arquivo note é criado em branco, para adicionar texto, você pode usar o comando echo e os comandos ">" e ">>". O mkdir também aceita apenas um parametro, que é o diretório `mkdir new_dir`**

- rm, rmdir: **rm é um pouco diferente dos outros comandos que cobrimos até agora. Você pode simplesmente remover arquivos usando rm. No entanto, você precisa fornecer a flag -R do lado do nome do diretório que deseja remover**

- cp: **O comando de copy aceita 2 argumentos: arg1(o nome do arquivo existente) e o arg2(nome do novo arquivo copiado), por exemplo: `cp clientes.txt clientes_backup.txt`**

- mv: **cp copia todo o conteúdo do arquivo existente para o novo arquivo. No caso de mover um arquivo, o mv também aceita dois argumentos, mas, em vez de copiar e/ou criar um novo arquivo, mv junta ou modifica o segundo arquivo que fornecemos como argumento. Além de mover um arquivo para uma nova pasta, você também pode usar mv para renomear um arquivo ou pasta.**

- file: **Oque pode enganar as pessoas e causar confusão é a suposição do que tem dentro do arquivo. Na maioria das vezes um arquivo tem uma extensão, oque ajuda a saber oque tem dentro, mas pode acontecer da extensão não ter sido colocada. O comando *file* serve para descobrir exatamente o tipo de arquivo, e descobrir oque podemos fazer a partir disso**

## Parâmetros

A maioria dos comandos tem parâmetros. Parâmetros são jeitos de especificar algo comando. Se nenhum parâmetro for atribuído, o comando executa o comando padrão, aí você pergunta "e se a ferramenta não tiver uma forma padrão?" e eu te respondo, isso não é opção. Parâmetros são identificados com um hífen (um traço pra quem pulou a aula de português) depois uma letra ou palavra. Ex: `ls -a`

## Conexão usando *SSH*
Uma conexão SSH (Secure Shell) é um protocolo para transferir dados sem um idiota tentando roubar seus dados (um dia você vai ser esse idiota). Ele criptografa seus dados enviados e descriptografa quando a mensagem alcança o destino.

### Sintaxe SSH
A sintaxe é simples e não precisa de um bloco de notas pra lembrar dela. Para se conectar a uma máquina usando SSH, a sintaxe é:
`ssh nome_de_usuario@ip_alvo`

Se tudo funcionar, o SSH vai pedir a confirmação de que você confia no Host. Caso você confirme, ele pedirá a senha.

*Nota: o campo da senha não tem feedback visual, a senha não é mostrada, então não, seu teclado não desconectou.*

## Permissões
Alguns usuários tem controle sobre alguns arquivos e outros não, para saber oque um usuário pode ou não fazer em um arquivo, podemos usar o comando ls com a flag -lh

```
root@linux2:~$ ls -lh
-rw-r--r-- 1 cmnatic cmnatic 0 Feb 19 10:37 file1
-rw-r--r-- 8 cmnatic cmnatic 0 Feb 19 10:37 file2
```
Essa parte é importante para determinar caracteristicas de um arquivo ou pasta e se podemos acessar, alterar ou move-la. Alguns arquivos funcionam só pra um usuário especifico

as permissões que um usuário pode ter são:

- leitura
- Escrita
- Execução

## Mudando de usuário

trocar de usuário é tranquilo graças ao `su`, se você não for o root (ou esteja usando permissões de root com sudo) você precisa de 2 coisas

- O nome do usuário de destino você vai mudar
- a senha do usuário

su tem flags importantes. Por exemplo a flag -l ou --login para iniciar um shell semelhante ao usuário fazendo login no sistema, com váriaveis de ambiente e coisas do tipo

## Diretórios padrão

### /etc
Esse é um diretório essencial do linux. A pasta etc é um diretório padrão para arquivos de sistema do sistema operacional, para os queridos usuários Windows, a System32

alguns conteúdos importantes do diretório /etc são: 

O arquivo sudoers, por exemplo, tem uma lista de usuários que podem executar comandos como root usando sudo

Outro arquivo comum é o passwd e o shadow. Os dois são do linux, por que mostram como o sistema armazena as senhas usando criptografia sha512


### /var
O */var* (abreviação de variable data) é uma pasta com dados acessados ou escritos por serviços ou aplicações, tipo um arquivo de log, que é escrito em */var/log* ou outros dados que não precisam  ser relacionados a um usuário (como um banco de dados)

alguns conteúdos importantes do diretório /var são:

backups 
log 
opt 
tmp

### /root
a pasta root é a pasta home do administrador do sistema (vulgo root). Não tem muito oque dizer sobre essa, ninguém além do root pode abrir os arquivos de dentro dela, os arquivos desse diretório só dependem do usuário root

### /tmp
esse é um diretório raiz encontrado no linux, é abreviação de temporário e é usado para armazenar dados que só vão ser usados uma ou duas vezes, quando você reinicia o computador, esses dados são deletados

A parte útil dessa pasta para um pentester é que qualquer usuário pode editar o conteúdo dessa pasta por padrão. ou seja, tendo acesso a máquina, esse é um bom lugar para nossos dados, como scripts de enumeração