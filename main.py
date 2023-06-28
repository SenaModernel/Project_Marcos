import pygame
from tkinter import simpledialog
import pickle
import math

pygame.init()

# Janela, icone, titulo do jogo
janela_game = (1705, 960)
ponto_branco = (255, 255, 255)
game_tela = pygame.display.set_mode(janela_game)
icone_game = pygame.image.load("space.png")
pygame.display.set_caption("Um dia eu vi, uma estrela cadente e fiz um pedido!! Creio fui atendido")
pygame.display.set_icon(icone_game)
fundo_game = pygame.image.load("bg.png")
font = pygame.font.SysFont('Verdana', 20)

# Linhas do texto
linha1 = font.render("Pressione F10 para Salvar os Pontos", True, ponto_branco)
linha2 = font.render("Pressione F11 para Carregar os Pontos", True, ponto_branco)
linha3 = font.render("Pressione F12 para Deletar os Pontos", True, ponto_branco)
linha4 = font.render("Pressione ESC para Fechar o Jogo", True, ponto_branco)
# Posições das linhas

linha1_pos = (85, 50)
linha2_pos = (85, linha1_pos[1] + linha1.get_height() + 20)
linha3_pos = (85, linha2_pos[1] + linha2.get_height() + 20)
linha4_pos = (85, linha3_pos[1] + linha3.get_height() + 20)

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

# Definir Background
game_tela.blit(fundo_game, (0, 0))
game_tela.blit(linha1, linha1_pos)
game_tela.blit(linha2, linha2_pos)
game_tela.blit(linha3, linha3_pos)
game_tela.blit(linha4, linha4_pos)

# Funcionamento das Linhas
primeiro_ponto = True
linha_estrelas = False
posicao_linha = None
posicao_linha_final = None

running = True

#Funções do Menu
salvar_pontos = True
Carregar_pontos = True
apagar_pontos = True


def calcular_distancia(ponto1, ponto2):
    return int(math.sqrt((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2))


def ajustar_texto(texto, pos):
    if pos[0] <= 50:
        texto = "Desconhecido X " + str(pos)
    elif pos[0] >= janela_game[0] - 50:
        texto = "Desconhecido X " + str(pos[::-1])
    elif pos[1] <= 50:
        texto = "Desconhecido Y " + str(pos)
    elif pos[1] >= janela_game[1] - 50:
        texto = "Desconhecido Y " + str(pos[::-1])

    return texto

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
                item = "Desconhecido " + str(pos)
            else:
                item = item + " " + str(pos)
            
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

                # 
                distancia = calcular_distancia(ponto_anterior, value)
                texto_distancia = font.render(str(distancia), True, ponto_branco)
                texto_distancia_rect = texto_distancia.get_rect(center=((ponto_anterior[0] + value[0]) // 2,(ponto_anterior[1] + value[1]) // 2))
                game_tela.blit(texto_distancia, texto_distancia_rect)

            ponto_anterior = value

            texto = ajustar_texto(key, value)
            texto_renderizado = font.render(texto, True, ponto_branco)
            texto_renderizado_rect = texto_renderizado.get_rect(center=(value[0], value[1] + 15))
            game_tela.blit(texto_renderizado, texto_renderizado_rect)

    pygame.display.update()

    clock.tick(60)