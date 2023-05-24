class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linha:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def __gt__(self, other):
        return self.comprimento() > other.comprimento()

    def __lt__(self, other):
        return self.comprimento() < other.comprimento()

    def __ge__(self, other):
        return self.comprimento() >= other.comprimento()

    def __le__(self, other):
        return self.comprimento() <= other.comprimento()

    def __eq__(self, other):
        return self.comprimento() == other.comprimento()

    def comprimento(self):
        dx = self.ponto2.x - self.ponto1.x
        dy = self.ponto2.y - self.ponto1.y
        return (dx ** 2 + dy ** 2) ** 0.5

ponto1 = Ponto(1, 2)
ponto2 = Ponto(4, 6)
ponto3 = Ponto(2, 3)

linha1 = Linha(ponto1, ponto2)
linha2 = Linha(ponto2, ponto3)

print(linha1 > linha2)  
print(linha1 < linha2)  
print(linha1 >= linha2)  
print(linha1 <= linha2)  
print(linha1 == linha2) 
