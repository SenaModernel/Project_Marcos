import pygame
from tkinter import simpledialog

pygame.init()

janela_game = (800,450)
ponto_branco = (255,255,255)
game_tela = pygame.display.set_mode(( janela_game))
icone_game = pygame.image.load("space.png")
pygame.display.set_caption("Um dia eu vi, uma estrela cadente e fiz um pedido!! Creio fui atendido")
pygame.display.set_icon(icone_game)
fundo_game = pygame.image.load("bg.jpg")
marca_ponto = []
pygame.mixer.init()
pygame.mixer.music.load("umPedido.mp3")
pygame.mixer.music.play(-1)
Desenvolvimento = pygame.time.Clock()
estrelas = []
item = []
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
        
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            if item == None:
                item = "desconhecido"+str(pos)
            estrelas[item] = pos 
            
            for key,value in estrelas.item():
                
                game_tela.fill((0, 0, 0)) 
                

        for i in range(len(marca_ponto) - 1):
            point1, _ = marca_ponto[i]
            point2, _ = marca_ponto[i + 1]
            pygame.draw.line(game_tela, (255, 255, 255), point1, point2, 2)
            
              
    game_tela.blit(fundo_game,(0,0))
    
    pygame.draw.circle(game_tela, ponto_branco, (255,130), 3)

    pygame.time.Clock().tick(60)

    pygame.display.update()

pygame.quit()