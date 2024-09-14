# SMB

O SMB (Server Message Block Protocol) é tipo o carteiro da rede, mas em vez de entregar cartas, ele entrega acesso. É um protocolo de comunicação que funciona em um esquema de cliente-servidor, onde o servidor é o cara generoso que compartilha tudo, e o cliente é o curioso que quer dar uma olhada em (e usar) tudo o que está sendo compartilhado.

## Como Acontece
O servidor coloca na mesa tudo o que ele tem pra oferecer: sistemas de arquivos, impressoras, named pipes (nome chique para canais de comunicação), e até APIs. O cliente, mesmo tendo seu HDzinho em casa, pensa: "Por que não pegar um pouco disso? Ele tá oferecendo" E aí ele pede acesso diretamente ao servidor, e pronto

O SMB é conhecido por ser um protocolo de solicitação e resposta. Em outras palavras, é um pingue-pongue de mensagens entre cliente e servidor até que eles estejam bem alinhados e prontos para compartilhar o que precisam. O cliente se conecta no servidor usando TCP/IP, que é como a estrada que eles usam para se encontrar (atualmente eles usam NetBIOS sobre TCP/IP, e quem quiser saber mais pode dar uma olhada nas RFCs 1001 e 1002). Outras rotas, como NetNIEUI e IPX/SPX, também estão disponíveis para quem gosta de variar.

Depois que essa conexão está firme, o cliente manda comandos, tipo "me dá aquele arquivo", e o servidor responde "tá aqui, agora vaza". Essa troca de favores acontece em toda a rede, permitindo que o trabalho flua tranquilamente.

Desde o Windows 95, o sistema da Microsoft já dava um super apoio ao SMB. Mas, como o mundo não é só Windows, o Samba veio para dar uma força aos sistemas Unix-Like, obviamente em alguns anos o samba já era melhor que o smb (até o nome é melhor)


