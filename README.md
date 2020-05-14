# temnet

Script simples em Python que utiliza a stdlib do Python para registrar as faltas de internet do meu provedor.

O script funciona atraves das requisicoes em algum site para teste de rede e no ipify para registro do IP de saida, dado uma execucao, o script tenta bater no google (por padrao) e depois no ipify, caso de certo ele registra no banco (sqlite) a data e hora, o status de sucesso, o URL testado, o status code e o IP de saida, no caso de falha ele segue a mesma linha exceto que o status fica de FALHA, o status code de 0 e o IP de saida de 0.0.0.0.

## TODO

- Daemon
- Notificacoes
- Flask WebUI para reportings
