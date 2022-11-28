import pygame
from pygame.locals import *
from sys import exit
import math

pygame.init()

length = 950
height = 540

background = pygame.image.load('fotoDoTrabalhoDeMEcanica.png')

fonte = pygame.font.SysFont('comic sans', 48)

tela = pygame.display.set_mode((length, height))
pygame.display.set_caption('Trabalho de Tatiana')
relogio = pygame.time.Clock()

def achar_m1(m2, mi):
    return m2 / (math.cos(math.radians(30))*mi - math.sin(math.radians(30)))

def achar_m2(m1, mi):
    return (m1*math.cos(math.radians(30))*mi) - m1*math.sin(math.radians(30))

def achar_mi(m1, m2):
    return (m2 + m1*math.sin(math.radians(30))) / (m1*math.cos(math.radians(30)))

def alterar_variavel(variavel, variacao, enable_up, enable_down, count):

    if event.type == KEYDOWN:
        count += 1

        if count >= 30:
            enable_up = True
            enable_down = True
            if count >= 100 and variacao == 0.0001:
                variacao *= 10
            if count >= 200 and variacao == 0.001:
                variacao *= 10

        if event.key == K_UP and enable_up:
            variavel += variacao
            enable_up = False
        elif event.key == K_DOWN and enable_down:
            variavel -= variacao
            enable_down = False

    if event.type == KEYUP:
        count = 0

        if event.key == K_UP:
            enable_up = True
        elif event.key == K_DOWN:
            enable_down = True

    return variavel, enable_up, enable_down, count

def mudar_caso(caso, enable_left, enable_right):
    if event.type == KEYDOWN:
        if event.key == K_LEFT and enable_left:
            caso -= 1
            enable_left = False
        elif event.key == K_RIGHT and enable_right:
            caso += 1
            enable_right = False

    if event.type == KEYUP:
        if event.key == K_LEFT:
            enable_left = True
        elif event.key == K_RIGHT:
            enable_right = True

    if caso < 0:
        caso = 0
    elif caso > 5:
        caso = 5

    return caso, enable_left, enable_right

m1 = 60.00
m2 = 30.00
mi = achar_mi(60, 30)

variacao = 1

caso = 0

posicao_bolinha_m1 = (675, 28)
posicao_bolinha_m2 = (675, 120)
posicao_bolinha_mi = (675, 215)

enable_up = True
enable_down = True

enable_left = True
enable_right = True

count = 0

while True:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(background, (0, 0))

    if pygame.key.get_pressed()[K_r]:
        m1 = 60.00
        m2 = 30.00
        mi = achar_mi(60, 30)

    caso, enable_left, enable_right = mudar_caso(caso, enable_left, enable_right)

    if caso == 0:
        pygame.draw.circle(tela, (0, 255, 0), posicao_bolinha_m1, 16)
        pygame.draw.circle(tela, (255, 0, 0), posicao_bolinha_m2, 16)

        m1, enable_up, enable_down, count = alterar_variavel(m1, 1, enable_up, enable_down, count)

        m2 = achar_m2(m1, mi)
    elif caso == 1:
        pygame.draw.circle(tela, (0, 255, 0), posicao_bolinha_m1, 16)
        pygame.draw.circle(tela, (255, 0, 0), posicao_bolinha_mi, 16)

        m1, enable_up, enable_down, count = alterar_variavel(m1, 1, enable_up, enable_down, count)

        mi = achar_mi(m1, m2)
    elif caso == 2:
        pygame.draw.circle(tela, (0, 255, 0), posicao_bolinha_m2, 16)
        pygame.draw.circle(tela, (255, 0, 0), posicao_bolinha_m1, 16)

        m2, enable_up, enable_down, count = alterar_variavel(m2, 1, enable_up, enable_down, count)

        m1 = achar_m1(m2, mi)
    elif caso == 3:
        pygame.draw.circle(tela, (0, 255, 0), posicao_bolinha_m2, 16)
        pygame.draw.circle(tela, (255, 0, 0), posicao_bolinha_mi, 16)

        m2, enable_up, enable_down, count = alterar_variavel(m2, 1, enable_up, enable_down, count)

        mi = achar_mi(m1, m2)
    elif caso == 4:
        pygame.draw.circle(tela, (0, 255, 0), posicao_bolinha_mi, 16)
        pygame.draw.circle(tela, (255, 0, 0), posicao_bolinha_m1, 16)

        mi, enable_up, enable_down, count = alterar_variavel(mi, 0.0001, enable_up, enable_down, count)

        m1 = achar_m1(m2, mi)
    elif caso == 5:
        pygame.draw.circle(tela, (0, 255, 0), posicao_bolinha_mi, 16)
        pygame.draw.circle(tela, (255, 0, 0), posicao_bolinha_m2, 16)

        mi, enable_up, enable_down, count = alterar_variavel(mi, 0.0001, enable_up, enable_down, count)

        m2 = achar_m2(m1, mi)

    texto_m1 = fonte.render(str(float(round(m1, 2))), True, (0, 0, 0))
    texto_m2 = fonte.render(str(float(round(m2, 2))), True, (0, 0, 0))
    texto_mi = fonte.render(str(float(round(mi, 4))), True, (0, 0, 0))
    texto_alerta = fonte.render("Situação", True, (255, 0, 0))
    texto_alerta2 = fonte.render("impossível!", True, (255, 0, 0))

    tela.blit(texto_m1, (785, -6))
    tela.blit(texto_m2, (788, 83))
    tela.blit(texto_mi, (752, 173))

    if m1 < 0 or m2 < 0 or mi < 0:
        tela.blit(texto_alerta, (700, 260))
        tela.blit(texto_alerta2, (700, 330))
    
    pygame.display.update()