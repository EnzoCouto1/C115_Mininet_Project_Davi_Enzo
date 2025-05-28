from mininet.topo import Topo

class CustomImageTopo(Topo):
    "Topologia customizada conforme a imagem fornecida"

    def __init__(self):
        # Inicializa a topologia
        Topo.__init__(self)

        # Adicionando switches com failMode='standalone'
        # Isso faz com que os switches atuem como learning switches L2 sem um controlador externo.
        s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')
        s3 = self.addSwitch('s3', failMode='standalone')
        s5 = self.addSwitch('s5', failMode='standalone')

        # Adicionando hosts com IPs na mesma sub-rede (para comunicação L2)
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        h5 = self.addHost('h5', ip='10.0.0.5/24')
        h6 = self.addHost('h6', ip='10.0.0.6/24')
        h7 = self.addHost('h7', ip='10.0.0.7/24')
        h8 = self.addHost('h8', ip='10.0.0.8/24')

        # Criando links conforme a topologia da imagem
        # Conexões entre hosts e switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s5)
        self.addLink(h4, s5)
        self.addLink(h5, s2)
        self.addLink(h6, s3)
        self.addLink(h7, s3)
        self.addLink(h8, s3)

        # Conexões entre switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s5)

# O Mininet CLI precisa saber como instanciar sua topologia.
# Isso permite que você a chame com `sudo mn --custom <seu_arquivo>.py --topo customimagetopo`
topos = {'customimagetopo': (lambda: CustomImageTopo())}