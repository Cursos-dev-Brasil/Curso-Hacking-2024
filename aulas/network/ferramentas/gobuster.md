# Descobrindo Segredos com o Gobuster

Imagina que você está navegando por um site, navegando pelas páginas que todo mundo vê. Mas e se eu te disser que, escondido no meio daquele dominio, existem diretórios secretos, arquivos esquecidos e até mesmo sitemaps abandonados que os desenvolvedores deixaram de proteger? Sim, isso acontece mais do que você imagina! E é aqui que entra o Gobuster, uma ferramenta incrível para caçar esses segredos como um verdadeiro detetive digital.

## O que é o Gobuster?
O Gobuster é como aquele amigo impaciente que, ao invés de explorar um site clicando em cada link, decide testar todos os caminhos de uma vez só – e rápido! Ele é feito para descobrir diretórios e arquivos ocultos, forçando caminhos comuns que os desenvolvedores esquecem de esconder. E se você já tentou adivinhar URLs no navegador, sabe como é chato. Mas o Gobuster faz isso em uma fração de minutos!

## Os Modos do Gobuster

O Gobuster tem três modos principais, mas o que você vai usar na maior parte do tempo é o modo dir. Por quê? Porque é o modo que força a barra de diretórios num dominio, ou seja, ele procura diretórios tepois do https://site.com/<>. A sintaxe básica do comando é:

`gobuster dir <resto do comando>`

### Wordlists
Sem uma wordlist, o gobuster faz o mesmo trabalho que os presidentes do Brasil, ou seja, nenhum. Pensa nela como a "contribuição" que o presidente ganha pra trabalhar. Nesse caso é uma lista de palavras.

#### Como Funciona?

| URL Original            | Item na Wordlist  | URL Final                        |
|------------------------ |------------------ |----------------------------------|
| http://example.com      | backups           | http://example.com/backups       |
| http://example.com      | shepards          | http://example.com/shepards      |

Simples, né? Mas calma que tem mais! O Gobuster é mais esperto que você e consegue forçar arquivos específicos usando extensões

| URL Original           | Item na Wordlist | Extensão Especificada | URL Final                        |
|------------------------|------------------|-----------------------|----------------------------------|
| http://example.com      | backup           | php                   | http://example.com/backup.php    |
| http://example.com      | backup           | txt                   | http://example.com/backup.txt    |
| http://example.com      | icecream         | html                  | http://example.com/icecream.html |

Imagina que você tem uma wordlist com as palavras "backup" e "icecream". O comando para o Gobuster seria algo assim

`gobuster dir -u example.com -w wordlist.txt -x php,txt,html`

O Gobuster vai tentar “backup.php”, “backup.txt”, “icecream.html” e assim por diante. Rápido, eficiente e preparado pra descobrir qualquer coisa que os desenvolvedores idiotas tenham deixado para trás

##### Quanto Melhor a Wordlist, Melhor o Resultado

Na verdade, o poder do Gobuster tá nas wordlists que você usa. Quanto mais específica e bem construída a  wordlist, mais chances de encontrar algo. E, se você está se perguntando onde encontrar essas listas, a resposta é simples: [SecLists](https://github.com/danielmiessler/SecLists). Lá, você encontra wordlists para diferentes tipos de aplicações e plataforma.

### Opções Comuns do Gobuster
Aqui estão algumas das opções comuns que você vai usar no Gobuster

| Opção | Descrição                                          |
|-------|----------------------------------------------------|
| -u    | Especifica a URL que você quer explorar.          |
| -w    | Especifica a wordlist que você vai usar para tentar os caminhos. |
| -x    | Especifica as extensões de arquivos que você quer forçar. |

E se você quiser ir além do básico, o Gobuster funciona como qualquer ferramenta Linux. Tem um [manual online](https://manpages.ubuntu.com/manpages/focal/man1/gobuster.1.html) que você pode consultar para explorar todas as outras opções e parâmetros.





