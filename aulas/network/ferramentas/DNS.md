# DNS
O DNS (Domain Name System) fornece uma maneira para que você se comunique com dispositivos na internet sem precisar lembrar de números gigantes. Assim como cada casa tem um endereço único, cada computador na internet tem seu endereço único para comunicação, chamado de endereço IP. Um endereço IP se parece com: 104.26.10.229, composto por 4 conjuntos de dígitos que variam de 0 a 255, separados por um ponto. Quando você quer visitar um site, não é muito prático lembrar desse conjunto, e é aí que o DNS pode ajudar. Em vez de lembrar 104.26.10.229, você pode lembrar de discord.com.

## Domínio de Nível Superior (TLD)

Um TLD (Top-Level Domain) é a parte mais à direita de um domínio, em discord.com, o TLD é .com. Existem dois tipos de TLD: gTLD (Generic Top Level Domain) e ccTLD (Country Code Top Level Domain). Historicamente, um gTLD tinha o objetivo de indicar propósito do domínio; por exemplo, .com seria para fins comerciais, .org para organizações, .edu para educação e .gov para governo. Já um ccTLD era usado para propósitos geográficos, como .ca para sites baseados no Canadá, .co.uk para sites baseados no Reino Unido e assim por diante. Devido à alta demanda, há uma grande variedade de novos gTLDs, como .online, .club, .website, .biz e muitos outros. Para uma lista completa de mais de 2000 TLDs, clique [aqui](https://www.iana.org/domains/root/db).

## Domínio de Segundo Nível

Usando o exemplo discord.com, a parte .com é o TLD, e discord é o Domínio de Segundo Nível. Quando você registra um nome de domínio, o domínio de segundo nível é limitado a 63 caracteres, além do TLD, e pode usar apenas a-z, 0-9 e hífens (não pode começar ou terminar com hífens, nem ter hífens consecutivos).

### Subdomínio

Um subdomínio fica à esquerda do Domínio de Segundo Nível, separado por um ponto; por exemplo, no nome youtu.be.com, a parte youtu é o subdomínio. Um subdomínio tem as mesmas restrições de criação que um Domínio de Segundo Nível, sendo limitado a 63 caracteres e podendo usar apenas a-z, 0-9 e hífens (não pode começar ou terminar com hífens, nem ter hífens consecutivos). Você pode usar mais de um subdomínio separado por pontos para criar nomes longos, como jupiter.servers.tryhackme.com. No entanto, o comprimento total deve ser mantido em 253 caracteres ou menos. Não há limite para o número de subdomínios que você pode criar para o seu nome de domínio.

# Tipos de registros DNS

DNS não é usado só para sites, existem vários tipos de REGISTROS DNS, os principais são: 

## Registro A

Registram endereços IPv4

## Registro AAAA

Registram endereços IPv6

## Registro CNAME

Esses registros resolvem para outro nome de domínio. Por exemplo, a loja online do TryHackMe tem o nome de subdomínio store.tryhackme.com, que retorna um registro CNAME shops.shopify.com. Outra solicitação DNS seria feita para shops.shopify.com para descobrir o endereço IP.

## Registro MX 
Esses registros resolvem o endereço dos servidores que lidam com o e-mail para o domínio consultado. Por exemplo, uma resposta de registro MX para tryhackme.com poderia ser alt1.aspmx.l.google.com. Esses registros também vêm com uma flag de prioridade, indicando em qual ordem tentar os servidores, útil caso o servidor principal falhe e o e-mail precise ser enviado para um servidor de backup.
## Registro TXT

Os registros TXT são campos de texto livre onde qualquer dado baseado em texto pode ser armazenado. Eles têm múltiplos usos, mas alguns comuns incluem listar servidores autorizados a enviar e-mails em nome do domínio (ajudando a combater spam e e-mails falsificados) e verificar a propriedade do nome de domínio ao se inscrever em serviços de terceiros.

### O que acontece quando você faz uma solicitação DNS

1. **Verificação no cache local:** Quando você solicita um nome de domínio, seu computador verifica primeiro seu cache local para ver se você já consultou o endereço recentemente. Se encontrado, o endereço é usado e a solicitação termina aqui.

2. **Servidor DNS Recursivo:** Se o endereço não for encontrado localmente, uma solicitação é feita ao Servidor DNS Recursivo, geralmente fornecido pelo seu ISP, mas você pode escolher seu próprio servidor DNS. Este servidor também tem um cache local de nomes de domínio recentemente consultados. Se um resultado for encontrado localmente, ele é enviado de volta ao seu computador e a solicitação termina aqui.

3. **Servidores DNS Raiz:** Se o Servidor DNS Recursivo não encontrar o endereço, ele começa uma jornada para encontrar a resposta correta, começando pelos servidores DNS raiz da internet. Esses servidores redirecionam você para o Servidor de Domínio de Nível Superior (TLD) correto, dependendo do seu pedido. Por exemplo, ao solicitar www.tryhackme.com, o servidor raiz reconhece o TLD .com e encaminha você para o servidor TLD apropriado que lida com endereços .com.

4. **Servidor TLD:** O servidor TLD mantém registros sobre onde encontrar o servidor autoritativo que pode responder à solicitação DNS. O servidor autoritativo, ou servidor de nomes, é responsável por armazenar os registros DNS de um domínio específico. Por exemplo, os servidores de nomes para tryhackme.com são kip.ns.cloudflare.com e uma.ns.cloudflare.com.

5. **Servidor DNS Autoritativo:** Este servidor responde à solicitação DNS com os registros apropriados. Dependendo do tipo de registro solicitado, a resposta é enviada de volta ao Servidor DNS Recursivo, onde uma cópia local será armazenada em cache para futuras solicitações e depois retransmitida ao cliente original que fez a solicitação.

6. **Valor TTL:** Todos os registros DNS vêm com um valor TTL (Time To Live). Este valor, representado em segundos, indica quanto tempo a resposta deve ser armazenada em cache localmente até que você precise consultá-la novamente. O cache economiza a necessidade de fazer uma solicitação DNS toda vez que você se comunica com um servidor.

### Diagrama de Fluxo (Visualização):

1. **Cliente -> Cache Local:** Verifica se o endereço está armazenado localmente.
2. **Cliente -> Servidor DNS Recursivo:** Solicita ao servidor DNS recursivo se não encontrado localmente.
3. **Servidor DNS Recursivo -> Cache Local:** Verifica se o endereço está armazenado no cache local.
4. **Servidor DNS Recursivo -> Servidor Raiz:** Se não encontrado, solicita ao servidor raiz.
5. **Servidor Raiz -> Servidor TLD:** O servidor raiz redireciona para o servidor TLD apropriado.
6. **Servidor TLD -> Servidor Autoritativo:** O servidor TLD direciona para o servidor autoritativo.
7. **Servidor Autoritativo -> Servidor DNS Recursivo:** O servidor autoritativo responde com o registro DNS.
8. **Servidor DNS Recursivo -> Cache Local:** Armazena a resposta no cache local.
9. **Servidor DNS Recursivo -> Cliente:** Transmite a resposta de volta ao cliente original.