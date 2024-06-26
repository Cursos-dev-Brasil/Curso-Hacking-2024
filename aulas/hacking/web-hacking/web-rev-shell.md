# Shell reverso
## ploads de arquivos
Existem inúmeros usos para uploads de arquivos na Internet. Embora uploads de arquivos sejam comuns,  também são fáceis de implementar de forma insegura. Por isso, é importante entender a gravidade do possível ataque.

Quando você pode upar arquivos para um servidor, você tem um caminho para um RCE (Remote Code Execution). Uma entrada de upload sem tratamento significa permitir o upload de um script que se conecta de volta à máquina atacante e te dá capacidade de executar qualquer comando. Seria incomum encontrar um upload de arquivo sem filtragem, mas é menos incomum encontrar um upload que tenha técnicas de filtragem falhas que podem ser contornadas. O script deve ser escrito em linguagem que o servidor pode executar. PHP geralmente é uma boa escolha, já que a maioria dos sites é escrita com back-end PHP.

Não temos texto (e paciência) para repassar todos os tipos de desvios de filtro (vamos nos detalhar em uma aula futura). Em vez disso, vamos abordar apenas um dos tipos mais comuns de filtro

### 1. Filtragem de extensão de arquivo:

como o nome diz, a filtragem de extensão verifica a extensão do arquivo. Isso é feito com uma lista de extensões permitidas e comparando o arquivo com a lista. Se a extensão não estiver na lista, o upload é rejeitado. Então... qual é o desvio? Bem, a resposta é que depende de como o filtro é implementado. Muitos filtros dividem um nome de arquivo no ponto (.) e verificam o que vem depois dele. Isso torna fácil contornar o upload com uma extensão dupla (por exemplo, .jpg.php). O filtro se divide nos pontos e verifica o que ele considera ser a extensão na lista. Se jpg for permitida, o upload é bem-sucedido e o script PHP é carregado no servidor.
adicionando um sistema de upload, é uma boa prática fazer upload dos arquivos para um diretório que não pode ser acessado remotamente. Infelizmente, isso geralmente não é o caso, e os scripts são carregados em um subdiretório no servidor web (tipo /uploads, /images, /media ou /resources), podemos encontrar o script em https://www.thebestfestivalcompany.xyz/images/shell.jpg.php.


## Web Reverse Shell
Vamos supor que você achou um lugar para carregar um script malicioso e contornar o filtro. Existem vários caminhos para fazer isso: o mais comum é o upload de um reverse shell. Este script cria uma conexão do servidor para nossa máquina. A maioria dos servidores são escritos em back-end PHP, o que significa que precisamos de um script shell reverso PHP. acontece que já tem um no Kali em /usr/share/webshells/php/php-reverse-shell.php

Copie o shell para o diretório atual (cp /usr/share/webshells/php/php-reverse-shell.php .) e abra com o nano. Role para baixo até onde tem $ip e $port (marcados com // CHANGE THIS). Defina o IP para o seu endereço e não esqueça de deixar as aspas duplas. Defina a porta como 443 (ou qualquer outra porta alta), salve e saia. Parabéns, agora você tem um script de shell reverso configurado.

Os shells de PHP podem ser ativados quando armazenamos em um lugar acessível: é só navegar até o arquivo no navegador para executar o script

![diagrama](/content/rev-shell-diagram.png)

No diagrama, primeiro carregamos o shell. Depois, navegamos até ele no navegador, fazendo com que o servidor envie um shell de volta ao listener em espera.

### Listener de reverse shell

Já falamos sobre ouvintes de shell, mas o que são eles? Resumindo, um listener de shell reverso é usado para abrir um soquete de rede para receber uma conexão, como uma criada por um shell executado. A forma mais simples de listener é criada usando o netcat. Podemos criar um ouvinte shell carregado usando o comando: `sudo nc -lvnp 443`. Isso cria um ouvinte na porta 443. Em um ambiente real, você precisa usar uma porta comum que não é filtrado por firewalls na maioria das vezes, aumentando as chances de nosso shell reverso se conectar de volta. Depois que o netcat for configurado, nosso shell reverso pode se conectar