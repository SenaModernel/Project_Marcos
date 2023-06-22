import pygame
from tkinter import simpledialog

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

# Funções do game
estrelas = {}
linha = []

# "FPS" do game
clock = pygame.time.Clock()

running = True

# Definir background
game_tela.blit(fundo_game, (0, 0))

linha_estrelas = 0
primeiro_ponto = 0
posicao_linha_final = None

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            pygame.draw.circle(game_tela, ponto_branco, pos, 5)
            estrelas[item] = pos

            if primeiro_ponto == 0:
                if linha_estrelas == 0:
                    posicao_linha = pos
                    linha_estrelas += 1
                    primeiro_ponto += 1

            elif primeiro_ponto > 1 and linha_estrelas == 0:     
                    posicao_linha = posicao_linha_final
                    linha_estrelas += 1
                    
            elif linha_estrelas == 1:
                posicao_linha_final = pos
                pygame.draw.line(game_tela, ponto_branco, posicao_linha, posicao_linha_final, 2)
                linha_estrelas -= 1

            if posicao_linha_final is not None:
                pygame.draw.line(game_tela, ponto_branco, posicao_linha_final, pos, 2)
                posicao_linha_final = pos
                

            for key, value in estrelas.items():
                
                fonte = pygame.font.Font(None, 30)
                texto = fonte.render(item, True, ponto_branco)
                game_tela.blit(texto, (pos[0] - 10, pos[1] + 10))

            if item == None:
                item = "desconhecido"+str(pos)
            


    pygame.display.update()
    clock.tick(60)

pygame.quit()