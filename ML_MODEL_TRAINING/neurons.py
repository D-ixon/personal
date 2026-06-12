from ursina import *
import random

app = Ursina()

window.color = color.black
camera.position = (0, 0, -20)

layers = [4, 6, 5, 3]
nodes = []
connections = []


class Neuron(Entity):
    def __init__(self, position):
        super().__init__(
            model='sphere',
            color=color.gray,
            scale=0.6,
            position=position
        )

        self.active = False
        self.timer = 0

    def activate(self):
        self.active = True
        self.timer = 0.3
        self.color = color.azure
        self.scale = 0.8

    def update(self):
        if self.active:
            self.timer -= time.dt

            pulse = 0.8 + 0.2 * abs(sin(time.time() * 10))
            self.scale = pulse

            if self.timer <= 0:
                self.active = False
                self.color = color.gray
                self.scale = 0.6


class Connection(Entity):
    def __init__(self, start, end):
        super().__init__(
            model=Mesh(
                vertices=[start.position, end.position],
                mode='line'
            ),
            color=color.dark_gray
        )

        self.start = start
        self.end = end
        self.timer = 0

    def activate(self):
        self.color = color.lime
        self.timer = 0.25

    def update(self):
        if self.timer > 0:
            self.timer -= time.dt
        else:
            self.color = color.dark_gray


# Create layers
x_spacing = 4
y_spacing = 2

for layer_index, count in enumerate(layers):

    layer = []

    x = layer_index * x_spacing

    for i in range(count):

        y = (count - 1) * y_spacing / 2 - i * y_spacing

        n = Neuron((x, y, 0))

        layer.append(n)

    nodes.append(layer)


# Connect layers
for i in range(len(nodes) - 1):

    for n1 in nodes[i]:

        for n2 in nodes[i + 1]:

            c = Connection(n1, n2)

            connections.append((c, n1, n2))


signal_timer = 0
current_layer = 0


def update():
    global signal_timer
    global current_layer

    signal_timer -= time.dt

    if signal_timer <= 0:

        if current_layer < len(nodes):

            for neuron in nodes[current_layer]:
                neuron.activate()

            for conn, start, end in connections:

                if start in nodes[current_layer]:
                    conn.activate()

            current_layer += 1

        else:
            current_layer = 0

        signal_timer = 0.5


Text(
    text="Neural Network Lighting Simulation",
    scale=1.5,
    y=.45
)

app.run()