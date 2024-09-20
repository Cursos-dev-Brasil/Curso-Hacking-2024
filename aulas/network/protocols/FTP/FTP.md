# O que é FTP

O File Transfer Protocol (ou, para os íntimos, FTP) é como um carteiro da internet. Ele é responsável por transportar arquivos de um lado pro outro. Mas, ao contrário do carteiro real, que mantém suas correspondências lacradas, o FTP entrega tudo aberto.

## Como Funciona

Imagine que você é um cliente querendo enviar uma encomenda. Você se conecta ao servidor (o carteiro) através de uma porta específica, a 21. Quando o carteiro atende, vocês começam a conversar. Inicialmente, vocês trocam comandos: "Abra essa caixa!", "Feche aquela!" e coisas do tipo. Essa troca acontece através de um canal de comando, que é quase uma linha telefônica exclusiva para fofocas.

Mas, claro, o que interessa mesmo é a encomenda, né? Então, o FTP também tem um canal de dados, que é o caminho por onde os arquivos (a encomenda) são enviados. Assim, enquanto você continua dando ordens ao carteiro pelo canal de comando, a encomenda está viajando pelo canal de dados.

### Modos Ativo e Passivo
O FTP é tão bom (só que não) que oferece três formas de se conectar ao carteiro:

Ativa: Aqui, você (cliente) é quem espera a ligação. Abre uma porta e fica ali, escutando. O carteiro (servidor) é quem precisa ligar para você.

Passiva: Agora, é o carteiro quem espera. Ele abre uma porta e fica lá, pronto para receber sua ligação.

Ambas: Esse carteiro é tão flexível que pode tanto ligar quanto receber ligações – tudo depende do que você preferir.

Enumeração FTP
Para entrar no FTP, primeiro você precisa descobrir se tem um carteiro disponível. No Linux, a maioria das vezes ele já está lá, pronto para te atender. é só digitar ftp no terminal, e se um `ftp>` aparecer, parabéns, você encontrou o carteiro! Caso contrário, um `sudo apt install ftp` resolve o problema.

Agora, vamo brincar de detetive. No FTP, o comando cwd (Change Work Directory) é o equivalente a perguntar "O que tem aqui?". Se você pedir para ver o que tem em /home/user, e o carteiro responde "250 OK", bingo! Você encontrou um diretório. Mas, se ele disser "550 Not Found", parece que não tem nada lá.

Aqui vai um exemplo prático para você se sentir um verdadeiro Sherlock:

```
CWD /home
250 OK
```

```
CWD /home/user1
250 OK
```
```
CWD /home/user2
550 Not Found
```
Moral da história: O FTP pode ser útil, mas provavelmente seus dados vão acabar num 4chan de dados vazados. Então usa direito – e, se possível criptografado
