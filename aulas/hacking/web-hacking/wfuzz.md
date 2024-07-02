# Fuzzing

Fuzzing pode ser considerado uma *"força bruta sofisticada"*. Mas, você pode Fuzzar, oque não pode forçar. Fuzzing é usar ferramentas de segurança para automatizar entrada de dados. Fuzzing é eficaz, já que os computadores realizam ações trabalhosas, como encontrar arquivos/pastas ocultas e testar nomes de usuário e senha muito mais rápido do que um ser humano pode (e quer fazer)

Aplicações mal construidas não conseguem lidar com dados como deveriam em situações de carga intensa. Além disso, os dados que enviamos podem ser intepretados e executados (ou seja, comandos). Podemos usar fuzzing para que a aplicação acione uma condição de erro, o que pode ser explorado por um pentester ou bug bounter

## Wfuzz

O conceito de Wfuzz é simples, as vezes você precisa de um pouco mais de informações sobre dados dentro de um aplicativo web. Isso pode ser desde um arquivo, um código de Status (por exemplo 404 not found) ou parametros usados em formulários

Vamos supor que você está realizando um pentest em um app de notas e quer ver se consegue visualizar outras notas de outras pessoas. Uma maneira de fazer isso é FUZZar usuários (sabendo que cada usuário tem um note.txt como padrão), o comando do wfuzz seria:
`wfuzz -c -z file,/path/da/wordlist.txt www.example.com/FUZZ`
Dessa forma, a palavra FUZZ é substituida pelas palavras da wordlist

Consulta 1: https://www.example.com/admin/note.txt
Consulta 2: https://www.example.com/administrator/note.txt
Consulta 3: https://www.example.com/system/note.txt   

É importante lembrar que você pode fuzzar qualquer parte da URL, então você pode usar qualquer parâmetro mesmo não conhecendo ele

O Wfuzz também possui uma [página de manual](https://manpages.debian.org/buster/wfuzz/wfuzz.1.en.html), ela detalha algumas opções avançadas do wfuzz

Algumas das principais opções do wfuzz são: 

| Opção | Descrição |
|-------|------------|
| -c | Mostra a saída colorida |
| -d | Especifica os parâmetros que você deseja fuzzar, onde os dados são codificados para um formulário HTML |
| -z | Especifica o que substituirá "FUZZ" na solicitação. Por exemplo, -z file,big.txt. Estamos dizendo ao wfuzz para procurar arquivos substituindo "FUZZ" pelas palavras dentro de "big.txt" |
| --hc | Não mostrar determinados códigos de resposta HTTP. Por exemplo, não mostrar respostas 404 que indicam que o arquivo não existe, ou "200" para indicar que o arquivo existe |
| --hl | Não mostrar uma determinada quantidade de linhas na resposta |
| --hh | Não mostrar uma determinada quantidade de caracteres |


