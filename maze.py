#создай игру "Лабиринт"!
from pygame import *
#создай окно игры
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_len - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right' 

        if self.rect.x >= win_len -85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_len, wall_height):
        super().__init__()     
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.x = wall_x
        self.y = wall_y
        self.len = wall_len
        self.height = wall_height
        self.image = Surface((self.len, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
win_len = 700
win_height = 500

window = display.set_mode((win_len, win_height))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"), (win_len, win_height))




player = Player('Star_Platinum_SO_Infobox_Anime.webp', 5, win_height -80, 4)
monster = Enemy('dio_sc_2.webp', win_len - 80, 280, 3)
final = GameSprite('treasure.png', win_len - 120, win_height - 80, 0)
w1 = Wall(154, 205, 100,  100, 20, 700, 10)
w2 = Wall(154, 205, 100,  100, 480, 350, 10)
w3 = Wall(154, 205, 100, 100, 20, 10, 380)
w4 = Wall(154, 205, 100, 430, 300, 60, 225)
w5 = Wall(154, 205, 100, 500, 20, 10, 200)
w6 = Wall(154, 205, 100, 300, 200, 70, 500)
w7 = Wall(154, 205, 100, 370, 350, 70, 500)
game = True


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('star-platinum-za-warudo.mp3')
kick = mixer.Sound('kick.ogg')
finish = False

font.init()
font = font.SysFont('Arial', 70)
win = font.render('You win', True, (255, 215, 0))
lose = font.render('You lose', True, (180, 0, 0))


clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        player.reset()
        monster.reset()
        final.reset()
        monster.update()



    
    

    
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
    
    
    display.update()
    clock.tick(FPS)

