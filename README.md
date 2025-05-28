# Trabalho Final de Mininet

### Criando Topologia ###

Topologia de profundidade 4 e ramificação 3 com largura de banda de 35Mbps

```bash
 sudo mn --topo=tree,depth=4,fanout=3 --mac --link=tc,bw=35
```

# Informações de interface

Verifique a topologia criada com
```bash
    nodes
```

Verificar os enlaces
```bash
    net
```

Verificando os enderecos logicos dos dispositivos da rede.

```bash
    dump
```

# Pings
Pingando todos os nós

```bash
    pingall
```


Pingando nós específicos
```bash
    h1 ping -c 5 h2
```

```bash
    h1 ping -c 5 h81
```


```bash
    h1 ping -c 5 h50
```


```bash
    h1 ping -c 5 h25
```


# Abrindo as interfaces para monitoramento

```bash
    xterm h1 h81
```

Executar os pings para teste

```bash
    ping 10.0.0.81
```

Escutando os pings na porta 81

```bash
    tcpdump -1 h81-eth0
```


# Testes de iperf nas diferentes larguras de banda (BW)

Para trocar as larguras de banda, basta trocar o valor de BW para 5, 10 ,25 ou 35

Exemplo com largura de BW=25
```bash
 sudo mn --topo=tree,depth=4,fanout=3 --mac --link=tc,bw=25
```

Porta do servidor (h1)
```bash
    iperf -s -p 5555 -i 1
```

Porta do cliente (h2) -> 20 seg de teste
```bash
    iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
```


# Comandos para executar um código python no PuTTy

Comando para adicionar um código no terminal do PuTTy baste digitar nano + nome do arquivo e colar as linhas de codigo no terminal
```bash
nano custom_topo.py
```

Executando o código
```bash
    sudo mn --custom custom_topo.py --topo customimagetopo --m  
```

Apagando a conexão com o Switch 1

Para apagar uma conexão basta executar o seguinte comando:
```bash
    sh sudo ovs-ofctl del-flows s1
```


Verificar se a conexão foi removida
```bash
    sh sudo ovs-ofctl dump-flows s1
```


Comandos para adicionar uma nova regra de conexão

Switch 1
```bash
sudo ovs-ofctl add-flow s1 in_port=1,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:2

sudo ovs-ofctl add-flow s1 in_port=2,dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1
```

Switch 1
```bash
sudo ovs-ofctl add-flow s2 in_port=1,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:3

sudo ovs-ofctl add-flow s2 in_port=3,dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1
```

Switch 3
```bash
sudo ovs-ofctl add-flow s3 in_port=1,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:2

sudo ovs-ofctl add-flow s3 in_port=2,dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1
```




