# Criptografia

Caso você não proteja seus dados, eles podem ser interceptados por qualquer idiota usando Wireshark, a criptografia garante que caso qualquer engraçadinho tente roubar seus dados, a única coisa que ele vai ter é um monte de letras e números sem o menor padrão e sem nenhuma possibilidade de descriptografia

## Como funciona

A criptografia funciona como um cano que transporta seus dados (esse foi o pior exemplo possível), para seus dados entrarem nesse cano, 2 alternativas são muito usadas

### Criptografia assimetrica X simétrica

#### Criptografia Simétrica

o tipo mais seguro de criptografia, ela funciona no servidor-cliente, o servidor envia uma chave, conhecida como,chave pública para o cliente, essa chave é usada para criptografar os dados e enviar pro servidor, quando os dados chegam no servidor, o servidor usa uma chave privada pra descriptografar os dados, as duas chaves se completam e a privada não funciona sem a pública

#### Criptografia Assimétrica

É bem menos segura, esse tipo de criptografia gera só uma chave, essa chave é usada para criptografia e descriptografa 