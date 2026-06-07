from ursina import *
import numpy as np

app = Ursina()

# Camera
EditorCamera()

# Cost function
def cost(x, z):
    return 0.1 * (x**2 + z**2)

# Create bowl surface
surface = Entity(
    model=Mesh(
        vertices=[
            Vec3(x, cost(x, z), z)
            for x in np.arange(-10, 10, 0.5)
            for z in np.arange(-10, 10, 0.5)
        ],
        triangles=[
            (
                i,
                i + 1,
                i + 40,
                i + 1,
                i + 41,
                i + 40
            )
            for z in range(39)
            for i in range(z * 40, z * 40 + 39)
        ],
        mode='triangle'
    ),
    color=color.azure,
    double_sided=True
)

# Ball representing parameters
ball = Entity(
    model='sphere',
    color=color.red,
    scale=0.5
)

# Starting point
theta_x = 8
theta_z = 6

learning_rate = 0.05

trail = []

def update():
    global theta_x, theta_z

    # Gradients
    grad_x = 0.2 * theta_x
    grad_z = 0.2 * theta_z

    # Gradient Descent
    theta_x -= learning_rate * grad_x
    theta_z -= learning_rate * grad_z

    y = cost(theta_x, theta_z)

    ball.position = Vec3(theta_x, y + 0.3, theta_z)

    # Leave trail behind
    marker = Entity(
        model='sphere',
        color=color.yellow,
        scale=0.08,
        position=ball.position
    )

    trail.append(marker)

# Light
DirectionalLight()
AmbientLight(color=color.rgba(100,100,100,0.5))

# Ground
Entity(
    model='plane',
    scale=50,
    color=color.gray,
    y=-0.1
)

app.run()