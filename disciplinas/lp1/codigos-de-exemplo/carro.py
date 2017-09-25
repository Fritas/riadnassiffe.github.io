class Carro:

    velocidade = 0
    direcao = {'esquerda':1, 'direita':1,'frente':-1,'tras':-1 }
    direcao_atual = 0

    def __init__(self, cor, velocidade_maxima, aceleracao, freagem, combustivel):
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.aceleracao = -1*aceleracao
        self.freagem = freagem
        self.combustivel = combustivel

    def acelerar(self):
        if abs(self.velocidade + self.aceleracao) <= self.velocidade_maxima and self.combustivel >= 1:
            self.velocidade += self.aceleracao
            self.combustivel -= 1

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -=self.freagem

    def mover(self, direcao):
        self.direcao_atual = self.direcao[direcao]
        self.aceleracao = self.aceleracao*self.direcao_atual
        if self.direcao_atual == 1:
            self.desacelerar()

    def desacelerar(self):
        self.velocidade -=1
