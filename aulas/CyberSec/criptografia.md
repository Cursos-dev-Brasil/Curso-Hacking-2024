# Criptografia

Caso você não proteja seus dados, eles podem ser interceptados por qualquer idiota usando Wireshark, a criptografia garante que caso qualquer engraçadinho tente roubar seus dados, receba um monte de letras e números sem o menor padrão e sem nenhuma possibilidade de descriptografia

A criptografia tem como objetivo garantir os princípios de confidenciabilidade, integridade e autenticidade do seu login no pornhub

## Como funciona

A criptografia funciona como um cano que carrega seus dados de um sistema pra outro(esse foi o pior exemplo possível), pros seus dados entrarem nesse cano, 2 alternativas são muito usadas

### Criptografia assimetrica X simétrica

Existem 2 tipos famosos de criptografia

#### Criptografia Simétrica

Nesse estilo de criptografia uma única chave é gerada para criptografar e descriptografar os dados, obviamente isso não é seguro, imagina enviar seus dados criptografados junto com a chave pra descriptografar, não é a decisão Mais inteligente que você pode tomar, normalmente a criptografia simétrica e usada nos dados e a criptografia assimétrica é usada na chave simétrica 

os principais 

#### Criptografia Assimétrica

o tipo mais seguro de criptografia, ela funciona no servidor-cliente, o servidor envia uma chave, conhecida como chave pública, para o cliente, essa chave é usada para criptografar os dados e enviar de volta pro servidor, quando os dados chegam no servidor, o servidor usa uma chave privada pra descriptografar os dados, as duas chaves se completam e a privada não funciona sem a pública 