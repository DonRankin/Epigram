import random
import math
WIDTH = 800
Download
the code
HEIGHT = 600 # the size of the screen
from GitHub:
wfmag.cc/
DRAG = 0.8 # how much a particle slows down by each second
wfmag1
# the colour of each particle in R, G, B values
PARTICLE_COLOR = 255, 230, 128
MAX_AGE = 3 # the time in seconds for which a particle is displayed
particles = [] # an array to hold the details of the explosion particles

def explode(x, y, speed=300): # Creates a new explosion at co-ordinates
age = 0
# these are new particles, so set their age to zero
for _ in range(100):
# generate 100 particles per explosion
# for each particle, generate a random angle and distance
angle = random.uniform (0, 2 * math.pi)
radius = random.uniform(0, 1) ** 0.5
# convert angle and distance from the explosion point into x and y velocity:
vx = speed * radius * math.sin(angle)
vy = speed * radius * math.cos(angle)
# add the particle’s position, velocity and age to the array
particles.append((x, y, vx, vy, age))

def draw():
# This function redraws the screen by plotting each particle in the array
screen.clear() # clear the screen
for x, y, *_ in particles: # loop through all the particles in the array
# for each particle in the array, plot its position on the screen:
screen.surface.set_at((int(x), int(y)), PARTICLE_COLOR)

def update(dt): # This function updates the array of particles
new_particles = [] # to update the particle array, create a new empty array
# loop through the existing particle array:
for (x, y, vx, vy, age) in particles:
# if a particle was created more than a certain time ago, it can be removed:
if age + dt > MAX_AGE:
continue
drag = DRAG ** dt # update particle’s velocity - they slow down over time
vx *= drag
vy *= drag
x += vx * dt
y += vy * dt # update the particle’s position according to its velocity
age += dt
# update the particle’s age
# add the particle’s new position, velocity and age to the new array:
new_particles.append((x, y, vx, vy, age))
particles[:] = new_particles # replace current array with the new one

def explode_random(): # creates an explosion at random location
x = random.randrange(WIDTH)
y = random.randrange(HEIGHT) # select a random position on the screen

explode(x, y) # call the explosion function for that position
# call the random explosion function every 1.5 seconds:
clock.schedule_interval(explode_random, 1.5)
