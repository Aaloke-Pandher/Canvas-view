# Canvas view 
import pygame 

# Define colors 
Grey = [128, 128, 128] 
White = [255, 255, 255] 
Blue = [0, 0, 255]  
Red = [255, 0, 0] 
Green = [0, 255, 0]  
Black = [0, 0, 0] 
WorldWidth = 2000 
Screen_width = 800 
Screen_length = 600

# Player Class 
class Player():
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h  
        self.view = 0 
        self.dx = 5 
        self.dy = 0
        self.accel = 0.5

    def update(self):
        # Movement 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.dx
        if keys[pygame.K_RIGHT]: 
            self.x += self.dx  
        
        # Update view
        self.view = self.x - 400 

        # Move Vertically
        self.dy += self.accel
        self.y += self.dy

    def drawPlayer(self, screen): 
        pygame.draw.rect(screen, Blue, [self.x - self.view, self.y, self.w, self.h])  

    def limitView(self):
        if self.view < 0:
            self.view = 0 
        elif self.view > WorldWidth - Screen_width:
            self.view = WorldWidth - Screen_width 

    def limitPlayer(self):
        if self.x < 0:
            self.x = 0 
        elif self.x > WorldWidth - self.w:
            self.x = WorldWidth - self.w  
        elif self.y > 580 - self.h:
            self.y = 580 - self.h 
            self.dy = 10

# Circle Platform 
class Platform():
    def __init__(self, x, y, w, h):  
        self.h = h
        self.w = w 
        self.x = x 
        self.y = y 

    def drawPlatform(self, screen, player):
        pygame.draw.rect(screen, Grey, [self.x - player.view, self.y, self.w, self.h]) 

# platform list 
platforms = [] 
platforms.append(Platform(200, 500, 200, 20)) 
platforms.append(Platform(500, 400, 200, 20))
platforms.append(Platform(800, 300, 200, 20))
platforms.append(Platform(1100, 500, 200, 20))
platforms.append(Platform(1400, 400, 200, 20))
platforms.append(Platform(1700, 300, 200, 20))
platforms.append(Platform(2000, 200, 200, 20)) 

# Collision Function 
def rectCollision(rect1, rect2): 
   return rect1.x < rect2.x + rect2.w and rect1.y < rect2.y + rect2.h and rect1.x + rect1.w > rect2.x and rect1.y + rect1.h > rect2.y
   
#Player
player = Player(400, 560, 20, 20)
# Main function 
def main():
    pygame.init() 
    # Canvas 
    size = (Screen_width, Screen_length)
    screen = pygame.display.set_mode(size)  
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Main Program Loop 
    while not done:
        # Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.dy = -10

        # Logic 
        player.update() 
        player.limitView() 
        player.limitPlayer()
        # Draw 
        screen.fill(White) 
        pygame.draw.rect(screen, Grey, [0, 580, 2000, 20]) 
        player.drawPlayer(screen) 
        for i in range(len(platforms)):
            platforms[i].drawPlatform(screen, player) 
            if rectCollision(player, platforms[i]):
                player.y = platforms[i].y - platforms[i].h  
                player.dy = 0
        pygame.display.flip() 

        # --- Limit frames
        clock.tick(60)  

     # Close window
    pygame.quit()  

main()