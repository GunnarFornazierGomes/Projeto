import pygame

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Player")

# Classe para o jogador
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 50
        self.altura = 50
        self.cor = (255, 0, 0)  # Cor vermelha

    def desenhar(self):
        pygame.draw.rect(janela, self.cor, (self.x, self.y, self.largura, self.altura))

# Criando uma instância do jogador
jogador = Player(150, altura // 2)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        jogador.y += 15
    if key[pygame.K_DOWN]:
        jogador.y -= 15
    # Lógica do movimento do jogador (por exemplo, usando teclas)
    # jogador.x += velocidade_x
    # jogador.y += velocidade_y
    janela.fill((120,0,125))
    # Desenha o jogador na tela
    jogador.desenhar()
    
    # Atualiza a tela
    pygame.display.update()

    # Controla a taxa de quadros por segundo
    pygame.time.Clock().tick(60)
