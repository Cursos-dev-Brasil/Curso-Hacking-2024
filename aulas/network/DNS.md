# DNS: O Guia de Navegação da Internet

O DNS (Domain Name System) é quase um GPS da internet, mas sem os anúncios chatos. Em vez de lembrar de números gigantes como 104.26.10.229, que são tão fáceis de esquecer quanto p número de telefone da sua avó, você só precisa lembrar de "site.com". O DNS traduz nomes em endereços IP, que são os números que os computadores usam para se encontrar.

## Domínio de Nível Superior (TLD): O Final da Linha
O TLD (Top-Level Domain) é a parte final de um domínio, tipo o sufixo que você coloca no final de um nome de arquivo para indicar o tipo. No "site.com", o TLD é ".com". Os TLDs podem ser genéricos (gTLDs) como ".com" (para negócios) ou ".org" (para organizações), ou códigos de país (ccTLDs) como ".ca" (para o Canadá) e ".co.uk" (para o Reino Unido). Só que conhecendo o mundo real, sabemos que nada é como deveria, então ninguém se importa com a utilidade de cada domínio e a única preocupação é conseguir um domínio .com (o resto sempre é suspeito aos olhos do público) 

## Domínio de Segundo Nível: A Parte que Você Escolhe
No exemplo "site.com", "site" é o Domínio de Segundo Nível. É como o nome da sua empresa ou o título da sua banda – é o que você escolhe. Esse nome pode ter até 63 caracteres e só pode usar letras, números e hífens (mas nada de hífens no começo ou no fim, e nada de hífens consecutivos, porque a vida já é complicada o suficiente).

## Subdomínio: O Extra
Os subdomínios são como quartos adicionais na casa do seu domínio. Em "youtu.be.com", "youtu" é um subdomínio. Você pode ter múltiplos subdomínios, como "jupiter.servers.tryhackme.com". É como adicionar "jupiter" e "servers" antes de "tryhackme.com", mas sem fazer uma reforma na casa

## Tipos de Registros DNS: Os Documentos de Identidade da Internet
O DNS não é só para sites, ele lida com vários tipos de registros. os principais são:

### Registro A
Este registro é quase um mapa que mostra onde encontrar um endereço IPv4. Tipo o endereço da sua casa, mas para servidores na internet.

### Registro AAAA
Aqui você encontra o endereço IPv6. É como o A, mas com mais dígitos, porque a internet está crescendo e precisa de mais espaço (mentira, é só uma desculpinha pra deixar as coisas mais difíceis e consequentemente mais caras)!

### Registro CNAME
O CNAME é como um "apelido" para um domínio. Se você tem "store.site.com" e ele aponta para "shops.shopify.com", o CNAME faz a mágica acontecer. É como quando você chama seu amigo de "Mano" em vez de "Carlos".

### Registro MX
Esses registros são responsáveis pelos e-mails. Se o e-mail não chega, é porque ele pode estar indo para o servidor errado – "alt1.aspmx.l.google.com" é um dos endereços onde seu e-mail pode tentar entregar a mensagem. É como se seu correio fosse entregue por uma equipe de entregadores em uma corrida!

### Registro TXT
Os registros TXT são como anotações que você pode colocar para qualquer finalidade, como verificar se você é o dono de um domínio ou listar servidores que podem enviar e-mails em seu nome. É como colocar post-its na sua mesa para lembrar de coisas importantes.

## O Que Acontece Quando Você Faz uma Solicitação DNS
Aqui está o que acontece quando você pede um site:

- Verificação no Cache Local: Seu computador verifica se já tem o endereço em memória, tipo quando você procura alguém no histórico de ligações do telefone. Se tiver, ele usa esse endereço e tudo é muito simples!

- Servidor DNS Recursivo: Como nada é simples, ele pode não encontrar no cache local. Se não encontrar, ele pergunta ao Servidor DNS Recursivo do seu ISP (tipo a claro), que pode ter o endereço na sua própria memória. É como perguntar ao seu amigo se ele sabe o endereço.

- Servidores DNS Raiz: Se o servidor recursivo não encontrar o endereço, ele começa uma busca muito chata pelos servidores DNS raiz da internet

- Servidor TLD: O servidor TLD é como o guia turístico que direciona você ao servidor que sabe tudo sobre o domínio .com, .org, etc.

- Servidor DNS Autoritativo: Este servidor é o verdadeiro "sabe-tudo" – ele tem os registros exatos para o domínio que você está procurando. Ele responde e diz: "Aqui está o endereço que você está procurando!"

- Valor TTL: Finalmente, o TTL (Time To Live) é como o tempo de validade de um cupom de desconto. Diz quanto tempo o endereço pode ser armazenado antes que seja necessário fazer outra consulta.

Se nada disso funcionar, eu sinto te informar, mas a sua internet da nasa (de 1940) acabou de traindo

Cliente -> Cache Local: Verifica se o endereço está armazenado localmente.
Cliente -> Servidor DNS Recursivo: Solicita ao servidor DNS recursivo se não encontrado localmente.
Servidor DNS Recursivo -> Cache Local: Verifica se o endereço está armazenado no cache local.
Servidor DNS Recursivo -> Servidor Raiz: Se não encontrado, solicita ao servidor raiz.
Servidor Raiz -> Servidor TLD: O servidor raiz redireciona para o servidor TLD apropriado.
Servidor TLD -> Servidor Autoritativo: O servidor TLD direciona para o servidor autoritativo.
Servidor Autoritativo -> Servidor DNS Recursivo: O servidor autoritativo responde com o registro DNS.
Servidor DNS Recursivo -> Cache Local: Armazena a resposta no cache local.
Servidor DNS Recursivo -> Cliente: Transmite a resposta de volta ao cliente original.

E assim, o DNS garante que, sempre que você digitar um nome de domínio, você será levado ao lugar certo, sem precisar se perder no caminho. É o GPS da web, sem precisar se preocupar com engarrafamentos! 🌐🚀