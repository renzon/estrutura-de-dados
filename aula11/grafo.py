class Arco():
    def __init__(self, origem, destino, valor):
        self.valor = valor
        self.vertices = (origem, destino)

    def __hash__(self):
        return hash(self.vertices + (self.valor,))

    def __eq__(self, arco):
        return (self.valor,) + self.vertices == (arco.valor,) + arco.vertices


import unittest


class ArcoTestes(unittest.TestCase):
    def teste_init(self):
        arco = Arco('origem', 'destino', 1)
        self.assertTupleEqual(('origem', 'destino'), arco.vertices)
        self.assertEqual(1, arco.valor)

    def teste_oposto(self):
        arco = Arco('origem', 'destino', 1)
        self.assertEqual('origem', arco.oposto('destino'))
        self.assertEqual('destino', arco.oposto('origem'))


# Dados a serem usados nos testes

# Dados de vérticos
bertioga = 'Bertioga'
caragua = 'Caragua'
jacarei = 'Jacareí'
mogi = 'Mogi da Cruzes'
santos = 'Santos'
sjc = 'São José dos Campos'
sao_paulo = 'São Paulo'
taubate = 'Taubaté'

vertices_cidades = (bertioga,
                    caragua,
                    jacarei,
                    mogi,
                    santos,
                    sjc,
                    sao_paulo,
                    taubate)
# Dados de arcos
arco_tauba_sjc = Arco(taubate, sjc, 43900)
arco_scj_jaca = Arco(sjc, jacarei, 13200)
arco_scj_caragua = Arco(sjc, caragua, 86900)
arco_caragua_bertioga = Arco(caragua, bertioga, 114000)
arco_bertioga_mogi = Arco(bertioga, mogi, 48700)
arco_mogi_jaca = Arco(mogi, jacarei, 54300)
arco_mogi_sp = Arco(mogi, sao_paulo, 61900)
arco_jaca_sp = Arco(jacarei, sao_paulo, 81800)
arco_santos_sp = Arco(santos, sao_paulo, 72800)
arco_santos_bertioga = Arco(santos, bertioga, 74400)

arcos_distancias = (arco_tauba_sjc,
                    arco_scj_jaca,
                    arco_scj_caragua,
                    arco_caragua_bertioga,
                    arco_bertioga_mogi,
                    arco_mogi_jaca,
                    arco_mogi_sp,
                    arco_jaca_sp,
                    arco_santos_sp,
                    arco_santos_bertioga)


class GrafoTestes(unittest.TestCase):
    def teste_adicionar_vertice(self):
        grafo = Grafo()
        self.assert_mesmo_elementos(tuple(), grafo.vertices())
        grafo.adicionar_vertice(santos)
        self.assert_mesmo_elementos((santos,), grafo.vertices())
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos((santos, jacarei), grafo.vertices())
        grafo.adicionar_vertice(mogi)
        self.assert_mesmo_elementos((santos, jacarei, mogi), grafo.vertices())
        grafo.adicionar_vertice(caragua)
        self.assert_mesmo_elementos((santos, jacarei, mogi, caragua), grafo.vertices())

    def teste_adicionar_arco(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(sjc))
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(jacarei))
        grafo.adicionar_arco(arco_scj_jaca)
        self.assert_mesmo_elementos((arco_scj_jaca,), grafo.arcos(jacarei))
        self.assert_mesmo_elementos((arco_scj_jaca,), grafo.arcos(sjc))
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_tauba_sjc)
        self.assert_mesmo_elementos((arco_scj_jaca, arco_tauba_sjc), grafo.arcos(sjc))
        self.assert_mesmo_elementos((arco_tauba_sjc,), grafo.arcos(taubate))

    def teste_caminho(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(sjc))
        grafo.adicionar_vertice(jacarei)
        self.assertListEqual([], grafo.caminho(sjc, jacarei))
        grafo.adicionar_arco(arco_scj_jaca)
        self.assertListEqual([sjc, jacarei], grafo.caminho(sjc, jacarei))
        grafo.adicionar_vertice(taubate)
        self.assertListEqual([], grafo.caminho(taubate, jacarei))

        grafo.adicionar_arco(arco_scj_jaca)
        self.assertListEqual([taubate, sjc, jacarei], grafo.caminho(taubate, jacarei))
        grafo.adicionar_vertice(sao_paulo)
        grafo.adicionar_arco(arco_jaca_sp)
        self.assertListEqual([taubate, sjc, jacarei, sao_paulo], grafo.caminho(taubate, jacarei))

    def assert_mesmo_elementos(self, iteravel, outro_iteravel):
        "Método auxiliar para asserção de elementos"
        self.assertSetEqual(set(iteravel), set(outro_iteravel))
