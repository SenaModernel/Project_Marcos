import pygame
from tkinter import simpledialog
import pickle 

pygame.init()

# Janela, icone, titulo do jogo
janela_game = (800,450)
ponto_branco = (255,255,255)
game_tela = pygame.display.set_mode(( janela_game))
icone_game = pygame.image.load("space.png")
pygame.display.set_caption("Um dia eu vi, uma estrela cadente e fiz um pedido!! Creio fui atendido")
pygame.display.set_icon(icone_game) 
fundo_game = pygame.image.load("bg.jpg")
font = pygame.font.Font('freesansbold.ttf', 15)

#Linhas do texto
linha1 = font.render("Pressione F10 para Salvar os Pontos", True, ponto_branco)
linha2 = font.render("Pressione F11 para Carregar os Pontos", True, ponto_branco)
linha3 = font.render("Pressione F12 para Deletar os Pontos", True, ponto_branco)
linha4 = font.render("Pressione ESC para Fechar o Jogo", True, ponto_branco)
#Linhas de posição 
linha1_pos = (0, 1)              
linha2_pos = (0, linha1.get_height())   
linha3_pos = (0, linha1.get_height() + linha2.get_height())   
linha4_pos = (0, linha1.get_height() + linha2.get_height() + linha4.get_height())   

# Músicas do game
pygame.mixer.init()
pygame.mixer.music.load("umPedido.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.020)
pygame.mixer.music.play(loops=-1)


# Funções do game
estrelas = {}
linha = []
nomes_estrelas = []


# "FPS" do game
clock = pygame.time.Clock()

running = True

# Definir background
game_tela.blit(fundo_game, (0, 0),)
game_tela.blit(linha1, linha1_pos)
game_tela.blit(linha2, linha2_pos)
game_tela.blit(linha3, linha3_pos) 
game_tela.blit(linha4, linha4_pos) 

primeiro_ponto = True
linha_estrelas = False
posicao_linha = None
posicao_linha_final = None
#Ideia das teclas f10,11,12
running = True
salvar_pontos = True
Carregar_pontos = True
apagar_pontos = True

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F10:
                if salvar_pontos:
                    with open('save', 'wb') as arquivo:
                        pickle.dump(estrelas, arquivo)
                   
            elif event.key == pygame.K_F11:
               try:
                    with open('save', 'rb') as arquivo:
                        estrelas = pickle.load(arquivo)
               except FileNotFoundError:
                    pass
            elif event.key == pygame.K_F12:
                if apagar_pontos:
                    estrelas = {}
                    game_tela.fill((0, 0, 0))  
                    game_tela.blit(fundo_game, (0, 0))  
                    game_tela.blit(linha1, linha1_pos)  
                    game_tela.blit(linha2, linha2_pos)
                    game_tela.blit(linha3, linha3_pos)
                    game_tela.blit(linha4, linha4_pos) 
                    pygame.display.update()
                    with open('save', 'wb') as arquivo:
                        pickle.dump(estrelas, arquivo)
                 

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
        
            if not item:
                item = "desconhecido" + str(pos)
            else: 
                item = item + str(pos)
            
            estrelas[item] = pos
            pygame.draw.circle(game_tela, ponto_branco, pos, 3)
            
            if primeiro_ponto:
                if not linha_estrelas:
                    posicao_linha = pos
                    linha_estrelas = True
                    primeiro_ponto = False
            
            elif linha_estrelas:
                posicao_linha_final = pos
                pygame.draw.line(game_tela, ponto_branco, posicao_linha, posicao_linha_final, 1)
                linha_estrelas = False
                    
            if posicao_linha_final is not None:
                pygame.draw.line(game_tela, ponto_branco, posicao_linha_final, pos, 1)
                posicao_linha_final = pos

        ponto_anterior = None

        for key, value in estrelas.items():
            pygame.draw.circle(game_tela, ponto_branco, value, 3)

            if ponto_anterior is not None:
                pygame.draw.line(game_tela, ponto_branco, ponto_anterior, value, 1)

            ponto_anterior = value

            fonte = pygame.font.Font(None, 30)
            texto = fonte.render(key, True, ponto_branco)
            game_tela.blit(texto, (value[0] - 10, value[1] + 10))


    pygame.display.update()
    
    clock.tick(60)

pygame.quit()