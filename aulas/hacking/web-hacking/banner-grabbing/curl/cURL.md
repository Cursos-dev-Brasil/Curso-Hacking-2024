# Dicas de exploração de diretórios

As vezes, banner-grabbing pode contribuir na enumeração, por exemplo, alguns cabeçalhos http te deixam saber exatamente o que tá sendo hospedado no servidor. Podem revelar o framework de aplicação, opções de autenticação e se o servidor tem alguma configuração de segurança mal configurada. Você pode usar o cURL para recuperar cabeçalhos usando a CLI

`Klython@root[/~]$ curl -IL https://www.inlanefreight.com`

saída:

```
HTTP/1.1 200 OK
Date: Fri, 18 Dec 2020 22:24:05 GMT
Server: Apache/2.4.29 (Ubuntu)
Link: <https://www.inlanefreight.com/index.php/wp-json/>; rel="https://api.w.org/"
Link: <https://www.inlanefreight.com/>; rel=shortlink
Content-Type: text/html; charset=UTF-8
```

As flags do comando curl são:
