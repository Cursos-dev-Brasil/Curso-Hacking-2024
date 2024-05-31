# **Encapsulamento**

O processo de **encapsulamento** é fundamental no modelo OSI. Ele envolve adicionar informações da camada aos dados conforme descem pela camada do modelo. Por exemplo, a camada de rede adiciona os IPs de origem e destino no header, enquanto a camada de transporte inclui detalhes do protocolo. Já a camada de enlace adiciona um trailer para verificar a integridade dos dados, aumentando a segurança.

Esse processo varia a terminologia de cada camada. Nas camadas 7, 6 e 5, os dados são chamados de **dados**. Na camada de transporte, eles são denominados **segmentos** ou **datagramas**, dependendo do uso de TCP/UDP. A camada de rede transforma os dados em um **pacote**, e na camada de enlace, eles se tornam um **quadro** antes de serem transmitidos como bits.

![Representação do encapsulamento](/content/encapsulamento.png)

# **Desencapsulamento**

Ao receber a mensagem, o computador receptor reverte o processo com o **desencapsulamento**, começando da camada física e subindo até a de aplicação, removendo informações adicionais enquanto avança. Esse método garante uma transmissão consistente de dados entre dispositivos habilitados para rede, independentemente do fabricante, sistema operacional e outras configurações.
