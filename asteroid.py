import pygame
import random
from logger import log_state, log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_velocity_1 = self.velocity.rotate(angle)
            new_velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(*self.position, new_radius)
            asteroid2 = Asteroid(*self.position, new_radius)
            asteroid1.velocity = new_velocity_1 * 1.2
            asteroid2.velocity = new_velocity_2 * 1.2

            
