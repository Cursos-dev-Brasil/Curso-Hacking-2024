# **Man pages**

Uma das funcionalidades embutidas do Linux é o comando `man`, que oferece acesso ao manual da maioria das ferramentas diretamente no terminal. Em algum momento, você pode encontrar uma ferramenta sem a página de manual, mas isso é raro. Quando você não sabe usar uma ferramenta, `man` é a sua primeira opção.

Vamos supor que você quer logar em um computador usando SSH, mas você não sabe como fazer isso. Você pode tentar usar o comando `man ssh`.

**Você pode ver que a sintaxe padrão do SSH é `ssh user@host`.**

Você pode usar as páginas de manual para procurar por flags específicas. Um exemplo disso seria o `steghide`, que pode ser usado para extrair e embutir arquivos dentro de uma imagem.

**Por exemplo, você pode procurar na página do manual uma flag para mostrar a versão do SSH. Para isso, você pode descer na página do manual até encontrar a flag correta ou você pode usar `grep`:**

![Exemplo de uso de grep com man](/content/grep-man.png)
