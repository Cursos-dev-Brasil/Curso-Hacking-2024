# Command injection

A injeção de comandos acontece quando o código do lado do servidor em uma aplicação web faz uma chamada para uma função que interage diretamente com o console do servidor. Uma vulnerabilidade de injeção na web permite que um atacante aproveite essa chamada para executar comandos do sistema operacional no servidor. As possibilidades para o atacante a partir daqui são infinitas:

- listar arquivos
- ler arquivos
- executar alguns comandos básicos para fazer reconhecimento do servidor ou o que quiserem como se estivessem sentados em frente ao servidor e emitindo comandos no terminal.

## Exemplo de código

Vamos pensar em um cenário: uma empresa começou a desenvolver um aplicativo web para arte ASCII de vacas com texto personalizável. buscando maneiras de implementar o aplicativo, encontraram o comando cowsay no Linux, que faz exatamente isso. Em vez de codificar todo um aplicativo e a lógica necessária para fazer vacas "falarem" em ASCII, decidem escrever um código simples que chama o comando do console do sistema e envia seu conteúdo ao site.

Analise o código a seguir e tente entender por que ele é tão perigoso e o por que dele ser considerado uma vulnerabilidade OWASP

```
<?php
    if (isset($_GET["mooing"])) {
        $mooing = $_GET["mooing"];
        $cow = 'default';

        if(isset($_GET["cow"]))
            $cow = $_GET["cow"];
        
        passthru("perl /usr/bin/cowsay -f $cow $mooing");
    }
?>
```

esse código:

- Verifica se o parâmetro "mooing" está definido. Se estiver, a variável $mooing recebe o valor passado no campo de entrada.

- Verifica se o parâmetro "cow" está definido. Se estiver, a variável $cow recebe o valor passado pelo parâmetro.

- O programa então executa a função passthru("perl /usr/bin/cowsay -f $cow $mooing");.

- A função passthru simplesmente executa um comando no console do sistema operacional e envia a saída de volta para o navegador do usuário. Você pode ver que nosso comando é formado concatenando as variáveis $cow e $mooing no final. Como podemos manipular essas variáveis, podemos tentar injetar comandos adicionais usando truques simples. Se desejar, você pode ler a documentação sobre passthru() no site do PHP para mais informações sobre a própria função.

Agora que sabemos como funciona nos bastidores, aproveitamos um recurso do bash chamado "comandos in-line" Para abusar do servidor cowsay. O Bash permite que você execute comandos dentro de comandos

para executar comando in-line, você pode usar simplesmente "$comando", se o comando in-line for detectado, ele primeiro executa o comando in-line e usa o resultado como parâmetro para o próximo comando

um exemplo prático:

`echo $(whoami)`


Se executarmos esse comando, o comando no php fica assim: 

```php
passthru("perl /usr/bin/cowsay -f default $(whoami)"); 
```

Já que isso funciona, podemos executar qualquer comando como argumento para o comando cowsay, no nosso exemplo, isso faz a vaca falar o retorno do comando
