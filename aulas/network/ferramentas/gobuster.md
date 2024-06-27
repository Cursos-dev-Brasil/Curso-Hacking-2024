# Introdução ao gobuster
Logicamente, muitas partes de um site tem erros que um usuário médio não pode ver. Esses erros podem ser qualquer coisa, de um sitemap até um diretório oculto com arquivos que não deveriam ser vistos por qualquer um. Infelizmente, isso faz com que os desenvolvedores com preguiça de proteger esses diretórios (experiência própria), permitindo que qualquer um descubra esses diretórios, e consequentemente, acesse ele para roubar informações. O Gobuster é uma ferramenta importante para descobrir esses diretórios. A ideia por trás da ferramenta é simples: forçar paths (diretórios) comuns para verificar se são válidos. Parecido como você faria no navegador, mas muito, muito e muito mais rápido. o Gobuster tem 3 modos: dir, vhost e dns, o modo mais provável de ser usado é o dir, então vamos usar ele, a sintaxe para esse comando é: 

`gobuster dir <resto do comando>`

## Como funcionam wordlists

Vamos usar a tabela abaixo para demonstrar como uma wordlist funciona:

| URL Original              | Item na Wordlist | URL Final                        |
|---------------------------|------------------|----------------------------------|
| http://example.com        | backups          | http://example.com/backups       |
| http://example.com        | shepards         | http://example.com/shepards      |

O gobuster tem alguns truques, ele suporta extensões, então você pode forçar arquivos. Podemos usar outra tabela para mostrar isso: 

| URL Original         | Item na Wordlist | Extensão Especificada | URL Final                       |
|----------------------|------------------|-----------------------|---------------------------------|
| http://example.com   | backup           | php                   | http://example.com/backup.php   |
| http://example.com   | backup           | txt                   | http://example.com/backup.txt   |
| http://example.com   | icecream         | html                  | http://example.com/icecream.html |

Para encontrar os dados usamos o seguinte comando (supondo que sua wordlist tenha as palavras backup e icecream)

`gobuster dir -u example.com -w wordlist.txt -x php,txt,html`

Embora seja mais rápido do que suas alternativas (como dirbuster) no kali, é limitado a worldists e opções fornecidas, quanto melhor a wordlist para o alvo, mais resultados você terá. Wordlists como a SecLists têm listas para aplicações e plataformas, você pode usar as informações na enumeração para determinar qual wordlist se encaixa melhor no seu caso

Gobuster funciona como qualquer ferramenta linux, então tem um [manual online](https://manpages.ubuntu.com/manpages/noble/en/man1/gobuster.1.html), você pode usar ela como referência para aprender outros parametros e opções, aqui, vamos entrar em telhas da principais

### Opções Comuns
| Opção    | Descrição
|----------|------------------------------------------------------|
| -u       | Usado para especificar a URL enumerada                                |
| -w       | Usado para especificar qual Wordlist será anexada ao caminho         |
| -x       | Usado para especificar extensões de arquivos                          |
