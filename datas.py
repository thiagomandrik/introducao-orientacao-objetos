class Data():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print("Data formatada: {:02d}/{:02d}/{}".format(self.dia, self.mes, self.ano))

# d = Data(14,1,2001)
# d.formatada()