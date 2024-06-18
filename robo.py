# fazer a classe
class robo:
    def __init__(self,nome,bateria):
        self.nome = nome
        self.bateria = bateria
        
    def apresentar (self):
      print("apresentar: ola sou breiniac")

    def falar (self):
      print("falar: todos os sistemas em ordem")

    #criando o objeto da classe. "instancia"
breiniac = robo("breiniac",100)
woule = robo("woule",85)

#chamando o objeto na tela

print("meu robo se chama {} e possui {} % de bateria".format(breiniac.nome,breiniac.bateria))
breiniac.apresentar()

print("meu robo se chama {} e possui {} % de bateria".format(woule.nome,woule.bateria))
woule.falar()
