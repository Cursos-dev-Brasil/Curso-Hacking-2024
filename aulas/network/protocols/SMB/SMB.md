# SMB

O *SMB*, ou *Server Message Block Protocol* é um **protocolo de comunicação cliente-servidor** (client-server) usado para **compartilhar acesso** a **arquivos, impressoras, portas seriais** (serial ports) e outros recursos de rede. 

## Como funciona
Os **servidores disponibilizam sistemas de arquivos** e/ou recursos de rede (impressoras, named pipes, APIs) para o cliente. O **cliente pode ter seu próprio disco rígido**, mas **podem requisitar acesso** aos sistemas compartilhados **diretamente pelo servidor**.

O SMB é conhecido como um **protocolo de solicitação de resposta** (response-request), logo, ele **transmite várias mensagens entre cliente e servidor** até estabelecer uma conexão. O cliente **se conecta ao servidor usando TCP/IP** (Atualmente *NetBIOS* sobre TCP/IP, especificado em **RFC1001** e **RFC1002**), *NetNIEUI* ou *IPX/SPX*

Depois da conexão estabelecida, o **cliente envia comandos** (SMBs) para o servidor que **disponibiliza os dados** (leitura, gravação de arquivos e qualquer outro tipo de coisa), nesse caso, esse tipo de coisa é feita na rede

Os sistemas Windows desde Windows 95 incluem suporte ao protocolo SMB. O Samba é um servidor open source que suporta SMB e foi lançado para sistemas Unix-Like