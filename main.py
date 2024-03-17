from pygame import *

window = display.set_mode((700,500)) #fjvrvrfvvrf
display.set_caption("sprites run")
clock = time.Clock()
FPS = 60

bg_image = image.load("background.png")
bg_image = transform.scale( bg_image,(700,500))
player_1 = image.load("sprite1.png")
player_2 = image.load("sprite2.png")

class Player(sprite.Sprite):
    def __init__(self, sprite_image, x ,y) -> None:
        super().__init__()
        self.image = transform.scale(sprite_image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.hp = 10
        self.speed = 4

    def draw(self,window):
        window.blit(self.image,self.rect)

    def update(self, key_left, key_right,key_up,key_down):
        keyes = key.get_pressed()
        if keyes[key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keyes[key_down] and self.rect.bottom < 500:
            self.rect.y += self.speed
        if keyes[key_right] and self.rect.right < 700:
            self.rect.x += self.speed
        if keyes[key_left] and self.rect.x > 0:
            self.rect.x -= self.speed



player1 = Player(player_1,0,200)
player2 = Player(player_2,400,100)


game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  

    window.blit(bg_image,(0,0))
    player1.draw(window)
    player2.draw(window)
    player2.update(K_LEFT,K_RIGHT,K_UP,K_DOWN)
    player1.update(K_a,K_d,K_w,K_s)
    display.update()
    clock.tick(FPS)



