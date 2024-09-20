# Autenticação
A autenticação é um processo de verificação da identidade, normalmente com credenciais (como nome de usuário, ID de usuário ou senha), a autenticação envolve verificar se alguém é quem diz ser. A autorização (que é diferente da autenticação) determina o que um usuário pode ou não fazer; a autorização.

## Credenciais padrão
Você provavelmente já comprou (ou baixou um serviço/programa) com credenciais no início, esses programas costumam exigir que você altere a senha após a configuração (geralmente essas credenciais no início são as mesmas para cada dispositivo/cada cópia do software). O problema é que, se não for alterado, um invasor pode procurar (ou até adivinhar) as credenciais.

O que é ainda pior é que esses dispositivos são expostos à Internet, permitindo que qualquer pessoa os acesse. Em 2018, foi relatado que uma botnet (dispositivos conectados à Internet controlados por um invasor para realizar ataques DDoS) chamada Mirai se aproveitou de dispositivos da Internet Of Things (IoT) registrando e configurando o dispositivo para realizar ataques em controle do atacante; o botnet infectou mais de 600.000 dispositivos IoT por meio de varredura na Internet e uso de credenciais padrão.

Na verdade, empresas como a Starbucks e o Departamento de Defesa dos EUA foram vítimas de serviços funcionando com credenciais padrão, e os bug hunters foram recompensados ​​por relatar esses problemas  simples de forma responsável (a Starbucks pagou US$ 250 pelo problema relatado)

https://hackerone.com/reports/195163 - Starbucks, recompensa de bugs para credenciais padrão.
https://hackerone.com/reports/804548 - Departamento de Defesa dos EUA, acesso de administrador por meio de credenciais padrão.
Em 2017, foi relatado que 15% de todos os dispositivos IoT ainda usam senhas padrão.

A SecLists é uma coleção de listas, incluindo nomes de usuário, senhas, URLs e mais. Uma lista de senhas conhecida como *“rockyou.txt”* é usada em desafios de segurança e  deve fazer parte do seu kit de ferramentas.


## Ataques de dicionário usando BurpSuite
Um ataque de dicionário é um jeito de invadir um sistema autenticado iterando uma lista de credenciais. Se você tiver uma lista de nomes e senhas padrão (ou comuns), pode passar por cada um deles na esperança de que uma das combinações funcione.

Você pode usar várias ferramentas para um ataque de dicionário, sendo uma delas o Hydra (um cracker de login de rede rápido) e o BurpSuite, uma ferramenta padrão usada para testes de penetração de aplicativos web.

Para baixar o BurpSuite [clique aqui](https://portswigger.net/burp/communitydownload)


### Inicie o Burp

Depois de carregado, você deseja "Interceptar" seu tráfego com proxy através do Burp, que encaminha a solicitação para o destino (no nosso caso um site).

Com o proxy ativado, navegue até o site alvo, ao interceptar o tráfego, você vai ver que o Burp não enviou a solicitação até você mandar ele fazer isso. Vamos ao burp enviar os dados em um formulário, no nosso caso é um formulário de login genérico. Esta solicitação aparece na aba Proxy. Clique com o botão direito e clique em "Enviar para o Intruder", o Burp tem muitas funcionalidades para repetir, modificar e manipular solicitações, o Intruder é uma ferramenta para automatizar ataques. Usamos o intruder para fazer um loop e enviar uma solicitação usando uma lista de credenciais, na esperança de que um dos nomes e senhas da lista funcionem.

![Intruder](/content/intruder.png)

Vá para a aba Intruder, você deve ver a solicitação lá. Aqui vamos inserir “posições” (informando ao Burp quais campos atualizar na automação da solicitação), selecionar uma lista por posição e atacar.
Clique na aba "Posições" e limpe as posições pré-selecionadas.
Adicione os valores de nome de usuário e senha como posições (selecione o texto e clique em "Adicionar")
Selecione "Cluster Bomb" no menu Tipo de Ataque, esse ataque itera por meio de cada conjunto de payloads, então cada combinação é testada.

![definição de payloads](/content/payload.png)
##  Posições do Burp
Vamos informar a cada "Posição" qual Payload usar. Nesse caso, selecionamos uma lista de nomes para o campo user e uma lista de senhas para o campo de senha.

Clique em "Payloads", selecione seu conjunto de Payload (o conjunto 1 é o campo de username, o conjunto 2 é o campo de senha) e selecione sua lista na seção "Opções de Payload" (ou adicione manualmente).
Para o conjunto 1 (nome de usuário), vamos usar credenciais comuns de username, como "admin", "root" e "user"
![payload User](/content/payload1.png)
### Listas de Posições do Burp
Para o conjunto 2 (senha), adicionamos senhas comuns, como "password", "admin" e "12345"

![Payload password](/content/payload2.png)

Clique no botão "Iniciar Ataque", isso executa cada linha da lista em todas as combinações. Você pode ordenar por "Comprimento" ou "Status" para identificar um login bem-sucedido (todos os logins incorretos tem o mesmo status ou comprimento, se uma combinação estiver correta, ele).

