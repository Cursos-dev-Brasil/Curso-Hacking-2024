# Fundamentos Linux Parte 2
*Obs: O arquivo anterior era tão grande que teve que ser cortado em dois. (Na verdade, só queríamos te dar mais trabalho, mas fica entre nós.)*

## Comandos para Interagir com Arquivos

Agora que você já está começando a dominar o Linux (mentira, você não sabe nem o que é um kernel), é hora de se preparar para os comandos de manipulação de arquivos e diretórios. Se você não decorar isso, provavelmente não vai saber nem mexer num terminal. Entre as funções de manipulação de arquivos mais importantes estão:

Criar diretórios
Apagar diretórios
Mover diretórios
Criar arquivos
Apagar arquivos
Mover arquivos

| Comando | Nome Completo     | Função                         |
|---------|-------------------|--------------------------------|
| touch   | touch             | Criar um arquivo               |
| mkdir   | make directory    | Criar um diretório             |
| rmdir   | remove directory  | Remover um diretório           |
| rm      | remove            | Remover um arquivo             |
| mv      | move              | Mover um arquivo ou diretório  |
| cp      | copy              | Copiar um arquivo ou diretório |
| file    | file              | Determinar o tipo de arquivo   |


### Criar Arquivos e Diretórios
Touch e mkdir: Com uma palavra, você cria um arquivo pra botar qualquer coisa (é sério, é qualquer coisa):

`touch [nome_do_arquivo]`

com mkdir, você cria um diretório (ou uma pasta pros nossos amigos da janela), do jeito que você quiser:

`mkdir [nome_da_pasta]`

### Remover Arquivos e Diretórios
rm e rmdir: O comando rm é um balde de água na fogueira (ele apaga tudo). Para remover um arquivo, é só colocar um:

`rm [arquivo]`

Agora, se você quiser eliminar uma pasta e tudo o que tem dentro deela, adicione a flag -R e se prepara pra ver a coitada sumir:

`rm -R [pasta]`

Mas, se você só quer se livrar de um diretório vazio, use rmdir:

`rmdir [pasta_vazia]`

Um golpe só e vala.

### Copiar e Mover Arquivos e Diretórios
cp e mv: Quer multiplicar arquivos? cp é o comando para isso:

cp: O comando de copy só copia os arquivos, é bem simples

`cp [arquivo] [copia_arquivo]`

Simples, né? É tipo tirar uma selfie com um amigo e depois tirar outra. Só que, em vez de se preocupar com a iluminação, você só tem que se preocupar em não perder a cópia!

mv: Serve pra duas coisas, mover e renomear, porque? não sei tbm, vai ver 1 comando a mais ia deixar o linux muito pesado:

`mv documento.txt novo_documento.txt`

pra mover o arquivo para outra pasta:

`mv documento.txt /novo_diretorio/`

file: Se você se deparou com um arquivo e não faz ideia do que ele é, file é seu Sherlock Holmes. Ele analisa e revela a identidade do arquivo, sem o drama

`file arquivo`

## Permissões e Segurança: O Mundo dos Direitos

Para saber quem pode fazer o quê com seus arquivos, use o comando ls com a flag -lh:

`ls -lh`

Isso mostra quem tem permissão para ler, escrever ou executar arquivos.

## Conexão usando SSH
Uma conexão SSH (Secure Shell) é um protocolo para transferir dados sem um idiota tentando roubar seus dados (um dia você pode ser esse idiota). Ele criptografa seus dados enviados e descriptografa quando a mensagem chega ao destino.

obs: esses dados só são descriptografados com uma chave de criptografia (RSA)

### Sintaxe SSH
A sintaxe é fácil e não precisa de um bloco de notas pra lembrar. Para se conectar a uma máquina usando SSH, a sintaxe é:

ssh [nome_de_usuario]@[ip_alvo]

Se tudo funcionar, o SSH vai pedir a confirmação de que você confia no Host. Caso você confirme, ele vai pedir a senha.

Nota: O campo da senha não tem feedback visual; a senha não é mostrada, então não, seu teclado não desconectou (eu já fiquei 40 minutos achando que era erro no teclado).

## Mudando de Usuário
Trocar de usuário é tranquilo graças ao su.

su tem flags importantes. Por exemplo, a flag -l ou --login inicia um shell fazendo login no sistema, com variáveis de ambiente e essas coisas.

## Diretórios Padrão

O linux é um sistema organizado e não tem um monte de pasta com nome sem sentido e sem nehuma utilidade, por isso ele tem alguns diretórios que você precisa conhecer pra trabalhar com essa maravilha de sistema

/etc: A central de comando do Linux. Aqui ficam os arquivos de configuração do sistema. É quase o coração do sistema, com arquivos que definem o que todos podem ou não fazer

/var: Onde tudo que é variável fica. Aqui ficam logs, backups e outros dados temporários.

/root: A área VIP para o superusuário. Só o root pode mexer aqui. É tipo a sala secreta do dono.

/tmp: O depósito de lixo descartável. Arquivos que você não precisa para sempre vão aqui. É tipo a lixeira, mas um pouco mais organizada.

## Parâmetros
A maioria dos comandos tem parâmetros. Um parâmetro é tipo uma forma de dizer "execute isso com isso". Se nenhum parâmetro for atribuído, o comando executa a função padrão. Se você se pergunta "e se a ferramenta não tiver uma função padrão?", eu te respondo: Não faz pergunta difícil amigo. Parâmetros são identificados com um hífen (ou um traço, pra quem pulou a aula de português) seguido de uma letra ou palavra. Exemplo: ls -a.
