# Man pages

Uma das funcionalidades embutidas do linux é o comando man, que oferece acesso ao manual da maior parte das ferramentas direto no terminal. Em algum momento você vai encontrar uma ferramenta sem a página de manual, mas isso é raro
quando você não sabe usar uma ferramenta, man é a sua primeira opção

Vamos supor que você quer logar em um computador usando ssh, mas você não sabe fazer isso, você pode tentar usar o comando `man ssh`

você pode ver que a sintaxe padrão do ssh é `ssh user@host`

Você pode usar as páginas de manual para procurar por flags especificas. Um exemplo disso seria o steghide, que pode ser usado para extrair e embutir arquivos dentro de uma imagem

você pode por exemplo procurar na página do manual uma flag para mostrar a versão do ssh, para isso você pode descer na página do manual até encontrar a flag correta ou você pode usar grep 

![grep + man](/content/grep-man.png)
