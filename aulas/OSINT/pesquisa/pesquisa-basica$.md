# Pesquisas no hacking *
Hoje em dia, a capacidade de pesquisar é a qualidade mais importante de um hacker. Hacking requer conhecimento pelo menos base em várias áreas, já que entender como algo funciona é crucial para invadir. Mas ninguém sabe tudo, até hackers com 20 anos de experiência tem problemas e travam em algum lugar, é aí que a pesquisa entra, no mundo real, ninguém vai te dar respostas ou dicas

Com o tempo você vai perceber que dependendo da coisa que você pesquisa vai ser muito difícil encontrar algo, mas na SI, nunca vai ter um ponto em que você não precise procurar informações

alguns dos metódos de pesquisa principais são:
- Questão de pesquisa
- Ferramentas de busca de vulnerabilidades
- Páginas de manuais/documentações 

## Questão de pesquisa
Esse é o tipo de coisa que você provavelmente vai achar em um Capture the flag ou um pentesting

Vamos supor que você baixou uma imagem .JPEG de um servidor remoto e você suspeita que possa ter algo dentro dela

Primeiro procure no google: "Hiding things inside image"<br>
**nota: pesquisas em inglês na maioria das vezes vão ter mais resultados do que em português**

**aviso: O meu computador usa o navegador *Brave*, oque pode facilitar ou não a pesquisa, já que ele exibe a resposta diretamente por inteligência artificial, oque as vezes pode causar erros, então sempre é recomendável procurar em mais de uma fonte, independente do navegador**

![Técnica de Esteganografia](/content/steganography.png)

Nesse texto, steganography é mencionada como uma técnica para esconder arquivos ou textos dentro de uma imagem

Agora que você sabe disso, você pode pesquisar como extrair arquivos que usam esteganografia

Pesquise no google denovo: "extract file from steganography image"
![Extrair arquivos de esteganografia](/content/extract-steganography.png)<br>
[Clique para abrir o Link](https://0xrick.github.io/lists/stego/)<br>
O Link parece ser útil.

![StegHide](/content/steghide.png)

Essa ferramenta parece ser útil. Ela é usada para extrair arquivos embutidos em fotos **.JPEG, .BMP, .WAV, .AU**, também mostra que pode ser intalado usando `apt`, se você já viu as aulas de fundamentos, sabe oque é isso, senão viu, pode ou pesquisar, ou ler sobre o apt em: [fundamentos](../../linux/fundamentos/fundamentos%20pt4.md)

caso queira pesquisar:

Pesquise no google: "What is apt"

![apt install](/content/apt.png)

A IA apontou duas possibilidades para o significado de apt, a que nos interessa é a primeira. Agora sabemos oque significa apt

agora podemos baixar o steg hide usando apt, tente descobrir como fazer isso sozinho e instale-o na sua máquina

Voltando para o guia de ferramentas que estavamos antes, temos um passo a passo de como usar o steghide

acesse o link e descubra como usar a ferramenta<br>
[Clique para abrir o Link](https://0xrick.github.io/lists/stego/)<br>

A pesquisa que fizemos aqui foi simples, começamos com a necessidade de descobrir como extrair arquivos secretos de uma imagem, depois descobrimos uma técnica para fazer isso, depois descobrimos uma ferramenta, para depois descobrir como baixar e usar a ferramenta
