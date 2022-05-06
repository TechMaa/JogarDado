import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.layout = [
        [sg.Text("JOGAR O DADO? ")],
        [sg.Button("SIM"),sg.Button("NÃO")]
        ]

    def Iniciar(self):

        self.janela = sg.Window("SIMULADOR DE DADO",layout = self.layout)
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'SIM':
                self.GerarValorDoDado()
            elif self.eventos == 'NÃO':
                print("AGRADECEMOS SUA PARTICIPAÇÃO")
            else:
                print("FAVOR DIGITAR APENAS SIM OU NÃO!!")
        except:
            print("OCORREU UM ERRO AO RECEBER SUA RESPOSTA")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
