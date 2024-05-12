import pygame
from numpy import pi, sqrt, arccos
pygame.init()

#cores
cores = {'azul_escuro': (230, 57, 70),
         'azul': (69, 123, 157),
         'azul_claro':(168, 218, 220),
         'branco':(241, 250, 238),
         'vermelho':(230, 57, 70)}
fonte = pygame.font.SysFont('Arial', 20)

#janela
largura_janela = 800
altura_janela = 800
janela = pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE)
pygame.display.set_caption('Trigonometria')
janela.fill(cores['branco'])


def angulo(index_ponto):
    angles = []
    for i in range(len(pontos)):
        x1 = pontos[index_ponto][0]
        x2 = pontos[i][0]
        y1 = pontos[index_ponto][1]
        y2 = pontos[i][1]
        if index_ponto != i:
            if x2 > x1:
                if y2 < y1:
                    quadrante = int(1)
                else: quadrante = int(4)
            if x2 < x1:
                if y2 > x1:
                    quadrante = int(2)
                else: quadrante = int(3)
            distancia = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            ca = x1 - x2
            if distancia == 0:
                angles.append(0)  # ou outro valor que faça sentido no seu contexto
            else:
                angles.append(arccos(ca / distancia))
    start_angle = min(angles) + (quadrante-2) * ((1/2) * pi)
    stop_angle = max(angles) + (quadrante-2) * ((1/2) * pi)
    return start_angle, stop_angle

pontos = []
def add_bolinha(x, y):
    distância = []
    if len(pontos) == 3:
        janela.fill(cores['branco'])
        for i in range(len(pontos)):
            distância.append(sqrt((pontos[i][0] - x) ** 2 + (pontos[i][1] - y)**2))
        del pontos[distância.index(min(distância))]
    pontos.append((x, y))

def desenhar_bolinhas(x, y):
    for i in range(len(pontos)):
        pygame.draw.circle(janela, cores['vermelho'], pontos[i], 10)

def desenhar_triângulo():
    for i in range(len(pontos)):
        if i<2:end_pos = i+1 
        else: end_pos = 0
        pygame.draw.line(janela, cores['azul_claro'], pontos[i], pontos[end_pos], width=3)

def desenhar_dados(x, y):
    if len(pontos) == 3:
        for i in range(len(pontos)):
            if pontos[i][0]-10 < x < pontos[i][0]+10 and pontos[i][1]-10 < y < pontos[i][1]+10:
                texto1 = fonte.render(f"Ponto {i+1}", True, cores['azul_escuro'])
                texto1_rect = texto1.get_rect()
                texto1_rect.center = (100, 100)
                janela.blit(texto1, texto1_rect)
                start_angle = angulo(i)[0]
                stop_angle = angulo(i)[1]
                pygame.draw.arc(janela, cores['azul'], (pontos[i][0]-20, pontos[i][1]-20, 40, 40), start_angle, stop_angle, width=2)

# loop principal
run = True
while run:
    pygame.time.delay(60)
#    x_indice = janela.get_width()/ 6
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            add_bolinha(mouse_x, mouse_y)
    janela.fill(cores['branco'])
    if len(pontos) == 3: desenhar_triângulo()
    desenhar_bolinhas(mouse_x, mouse_y)
    desenhar_dados(mouse_x, mouse_y)
    pygame.display.update()
pygame.quit()
