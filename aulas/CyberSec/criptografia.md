# Criptografia

Imagina que você tem uma fofoca daquelas e ninguém pode descubrir. É isso que a criptografia faz: transforma suas informações valiosas em um código ininteligível, como se você tivesse jogado suas mensagens em um cofre com 7 camadas de segurança (No nosso caso é só uma mesmo). Se algum enxerido tentar ler com o Wireshark, vai encontrar letras e números extremamente sem sentido.

## Como Funciona

### Criptografia Simétrica
Aqui, a gente usa uma chave para criptografar e descriptografar tudo. A parte engraçada é que, se você enviar a chave junto com os dados, seria como se você deixasse a chave da sua casa na fechadura. A criptografia simétrica é rápida, mas não é a mais segura.

Algoritmos famoso incluem AES (o top 1, não me pergunte por que), RC4, DES, RC5 e RC6. É como ter vários tênis com diferentes modelos e tamanhos, mas todos com o mesmo objetivo: andar.

### Criptografia Assimétrica
Aqui a coisa fica mais legal. Usamos um par de chaves: uma pública e uma privada. A chave pública, que é quase um cofre com a combinação aberta, é compartilhada com todos. A chave privada, que é o segredo mais bem guardado, é usada para descriptografar. Então, qualquer um pode trancar o cofre com a chave pública, mas apenas você pode abrir com a chave privada.

Essa abordagem adiciona uma camada extra de segurança, mas é um pouco mais lenta, pois envolve mais trabalho criptográfico.

# Assinatura Digital
Vamo simplificar isso. A assinatura digital é tipo resumir aquele filme chato pra ninguém precisar perder tempo assistindo.

1. Criação do Hash: O servidor faz um resumo (hash) da mensagem original.
2. Criptografia do Hash: O servidor criptografa esse resumo com a chave privada, criando uma assinatura digital.
3. Envio: O servidor envia a mensagem original junto com a assinatura digital.

Verificação:

1. O cliente usa a chave pública para descriptografar a assinatura e obter o hash original.
2. O cliente faz o hash da mensagem recebida.
3. Compara os dois hashes: se eles forem iguais, a mensagem é autêntica e intacta.

# Hashing
Hashing é como transformar dados em um enigma de uma via. Uma vez que você aplica o hash, não tem volta. Ideal pra armazenar senhas sem sair mostrando ela pra geral.

Os hashes comuns incluem MD5, NTLM, SHA-2 e SHA-3.

# Sal e Pimenta

## Salt (Sal)
O salt é como um tempero que você adiciona na sua senha antes de aplicá-la ao hash (por isso chama sal, pelo menos eu acho). Isso garante que mesmo que dois usuários tenham a mesma senha, os resultados serão diferentes. Ninguém quer receber a mensagem "Senha já cadastrada"

1. um salt aleatório é gerado quando a senha é criada.
2. O salt é misturado com a senha antes de aplicar o hash.
3. O salt é armazenado com a senha no banco de dados.

Na hora do login, o salt é recuperado e o processo é repetido.
Mesmo se alguém invadir o banco de dados, precisaria de uma tabela nova pra cada senha, tornando o ataque  mais difícil e muito mais sem graça.

## Pepper

O pepper é parecido com o salt, mas não é armazenado. Em vez disso, é um valor adicionado à senha antes de hashear ela, aumentando a segurança..

