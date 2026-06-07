from ursina import *
import numpy as np

app = Ursina()

# Set background to black
window.color = color.black
Sky(color=color.black)

# 1. Define the 3D surface function
def get_height(x, z):
    # This creates the complex landscape
    return 3 * np.exp(-((x - 1)**2 + (z - 1)**2)) + \
           2 * np.exp(-((x + 1)**2 + (z + 1)**2)) - \
           3 * np.exp(-(x**2 + z**2))

# Generate the grid mesh
size = 40
x = np.linspace(-3, 3, size)
z = np.linspace(-3, 3, size)
X, Z = np.meshgrid(x, z)
Y = get_height(X, Z)

verts = [Vec3(X[i, j], Y[i, j], Z[i, j]) for i in range(size) for j in range(size)]
cols = [color.rgb(255*(Y[i,j]+3)/6, 0, 255*(1-(Y[i,j]+3)/6)) for i in range(size) for j in range(size)]

landscape = Entity(model=Mesh(vertices=verts, colors=cols, mode='line'), scale=2)

# 2. The Optimizer "Ball" 
# Starting from a high peak to traverse more zones
learner = Entity(model='sphere', color=color.yellow, scale=0.2, position=(2, 2, 2))
trail = Entity(model=Mesh(mode='line', thickness=2), color=color.white)
path = []

def update():
    h = 0.01
    curr_x, curr_z = learner.x / 2, learner.z / 2
    
    dx = (get_height(curr_x + h, curr_z) - get_height(curr_x - h, curr_z)) / (2 * h)
    dz = (get_height(curr_x, curr_z + h) - get_height(curr_x, curr_z - h)) / (2 * h)
    
    # REDUCED LEARNING RATE: 0.02 instead of 0.1 makes it significantly slower
    lr = 0.02 
    
    learner.x -= dx * lr
    learner.z -= dz * lr
    learner.y = get_height(learner.x/2, learner.z/2) + 0.1
    
    path.append(learner.position)
    
    if len(path) > 1:
        trail.model.vertices = path
        trail.model.generate()

# 3. Setup Orbital Camera
ec = EditorCamera()
ec.rotation_speed = 100

app.run()