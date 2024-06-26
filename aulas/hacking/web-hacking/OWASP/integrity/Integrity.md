# Integridade

Quando falamos de integridade, Queremos dizer da capacidade de assegurar que um conjunto de dados fique inalterado. integridade é essencial, por que nos preocupamos em manter dados importantes livres de modificações maliciosas. Por exemplo, imagine que você esteja baixando o instalador mais recente de um aplicativo. Como você pode ter certeza de que, ao baixá-lo, ele não foi modificado durante o trânsito ou de alguma forma danificado por um erro de transmissão?

Para superar esse problema, você verá um hash junto com o arquivo para que você possa comprovar que o arquivo que baixou manteve sua integridade e não foi modificado. Um hash ou digest é um número da aplicação de um algoritmo sobre um conjunto de dados. Ao ler sobre algoritmos de hash, você encontrará sobre MD5, SHA1, SHA256 ou muitos outros disponíveis.

![Exemplo de um digest](/content/winSCP.png)

Esses hashes foram precalculados pelos criadores do WinSCP para que você possa verificar a integridade do arquivo. Se baixarmos o arquivo de setup, podemos recalcular os hashes e comparar com os publicados no SourceForge. Para calcular os tipos de hashes no Linux, você pode usar:

```bash
md5sum <arquivo com o hash md5>         
sha1sum <arquivo com o hash sha1> 
sha256sum <arquivo com o hash sha256> 
```

Se você tiver o mesmo hash do repositório, pode concluir que o arquivo que você baixou é uma cópia identica

# Falha na integridade de software e dados

Essa vulnerabilidade surge de código ou infraestrutura que utiliza software ou dados sem realizar qualquer tipo de verificação de integridade. Como nenhuma verificação está sendo feita, um atacante pode modificar o software ou dados enviados, resultando em consequências inesperadas. Existem principalmente dois tipos de vulnerabilidades nesta categoria:

- Falha na integridade de software
- Falha na integridade de Dados


