import pygame
pygame.init()
from pygame.locals import *
from sys import exit
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Latin-Squares-Activity")
clock = pygame.time.Clock()


def render_text(text,font,color):
    text_rendered = font.render(text,True,color)
    return text_rendered,text_rendered.get_rect()

def main():
    running = True
    fps = 30
    screen_width = 800
    screen_height = 600
    button_width = 200
    button_height = 50
    button1_x = (screen_width-button_width)//2
    button1_y = (screen_height-button_height)//2
    button1 = pygame.Rect(button1_x,button1_y,button_width,button_height)
    button2 = pygame.Rect(button1_x,button1_y+button_height+10,button_width,button_height)
    button3 = pygame.Rect(button1_x,button1_y-button_height-10,button_width,button_height)
    font = pygame.font.SysFont(None,25)
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN :
                if event.button == 1:
                    if button1.collidepoint(event.pos):
                        game_loop()
                    elif button2.collidepoint(event.pos):
                        print("Green")
                    elif button3.collidepoint(event.pos):
                        print("Blue")
            
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(255,0,0),button1)
        pygame.draw.rect(screen,(0,255,0),button2)
        pygame.draw.rect(screen,(0,0,255),button3)
        button1_text,button1_text_rect = render_text("Moderate",font,(255,255,255))
        button1_text_rect.center = button1.center
        screen.blit(button1_text,button1_text_rect)
        button2_text,button2_text_rect = render_text("Hard",font,(255,255,255))
        button2_text_rect.center = button2.center
        screen.blit(button2_text,button2_text_rect)        
        button3_text,button3_text_rect = render_text("Easy",font,(255,255,255))
        button3_text_rect.center = button3.center
        screen.blit(button3_text,button3_text_rect)
        pygame.display.update()
        clock.tick(fps)

def game_loop():
    exit_game = False
    game_over = False
    while not exit_game:
        if  game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
        else :
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()            
        pygame.display.update()
        clock.tick(30)
    exit()

main()


