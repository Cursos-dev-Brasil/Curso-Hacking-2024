# whois

Você já parou pra pensar como seria difícil lembrar de todos os IPs dos sites que você visita? Pensa num um mundo onde, para acessar o Google, você tivesse que se lembrar do IP dele. Pois é, a vida seria bem mais chata do que já é. Felizmente, a solução para esse problema são os sistemas de dominios!

## O que é um Domínio?
Um domínio é um nome legalzinho que traduz um IP, permitindo que você acesse sites sem decorar números complicados. Por exemplo, ao invés de lembrar o IP do Google, você só precisa digitar google.com (se você não sabia disso parabéns, você viveu numa caverna por 30 anos). Esse negócio só é possível graças a  registradoras de domínios, que alugam e gerenciam domínios por períodos determinados

## O que é o whois?
O comando whois é como um detetive de domínios na internet. Ele permite que você descubra informações sobre o registro de um domínio, como quem registrou e quais os detalhes de contato. Embora na Europa alguns detalhes pessoais sejam ocultos, em muitas partes do mundo você pode obter informações valiosas sobre o proprietário do domínio.

### Como Usar o whois
Para usar o whois, você pode simplesmente digitar:

`whois google.com`

Esse comando retorna uma série de informações, como o registrador, as datas de criação e expiração, e os detalhes de contato do proprietário (se disponíveis).

#### Instalando o whois
Em alguns sistemas, o whois pode não estar instalado. Se for o seu caso, você pode instalar usando o apt. Por exemplo, no Ubuntu

`sudo apt install whois`

##### Exemplos de Uso

`whois example.com`

Isso mostra quem está registrando o domínio example.com e outras informações úteis.

###### Verificar a Disponibilidade de um Domínio

Você também pode usar o whois para verificar se um domínio está disponível para registro. Se o domínio estiver registrado, você verá informações sobre o registro. Se não estiver, o whois informará que o domínio está disponível.

#### Por Que o whois é Importante?
O whois é uma ferramenta poderosa para várias situações, incluindo:

- Verificação de Propriedade: Descubra quem é o proprietário de um site.
- Verificação de Registro: Verifique a validade e a data de expiração de um domínio.
- Contato: Encontre informações de contato para registrar um domínio ou resolver problemas relacionados ao domínio.

Para mais detalhes e opções, consulte a documentação ou o manual:

`man whois`