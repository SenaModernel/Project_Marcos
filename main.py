import pygame
from tkinter import simpledialog
from funcoes import menu

pygame.init()

# Janela, icone, titulo do jogo
janela_game = (800,450)
ponto_branco = (255,255,255)
game_tela = pygame.display.set_mode(( janela_game))
icone_game = pygame.image.load("space.png")
pygame.display.set_caption("Um dia eu vi, uma estrela cadente e fiz um pedido!! Creio fui atendido")
pygame.display.set_icon(icone_game)
fundo_game = pygame.image.load("bg.jpg")

# Músicas do game
pygame.mixer.init()
pygame.mixer.music.load("umPedido.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.007)

# Funções do game
estrelas = {}
linha = []
nomes_estrelas = []

# "FPS" do game
clock = pygame.time.Clock()

running = True

# Definir background
game_tela.blit(fundo_game, (0, 0))

primeiro_ponto = True
linha_estrelas = False
posicao_linha_final = None

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
        
            if not item:
                item = "desconhecido" + str(pos)
            else: 
                item = item + str(pos)
            
            estrelas[item] = pos
            pygame.draw.circle(game_tela, ponto_branco, pos, 5)


            for key, value in estrelas.items():
                
                fonte = pygame.font.Font(None, 30)
                texto = fonte.render(key, True, ponto_branco)
                game_tela.blit(texto, (value[0] - 10, value[1] + 10))

            if primeiro_ponto:
                if not linha_estrelas:
                    posicao_linha = pos
                    linha_estrelas = True
                    primeiro_ponto = False
            
            elif linha_estrelas:
                posicao_linha_final = pos
                pygame.draw.line(game_tela, ponto_branco, posicao_linha, posicao_linha_final, 2)
                linha_estrelas = False
                    
            if posicao_linha_final is not None:
                pygame.draw.line(game_tela, ponto_branco, posicao_linha_final, pos, 2)
                posicao_linha_final = pos


    pygame.display.update()
    clock.tick(60)

pygame.quit()