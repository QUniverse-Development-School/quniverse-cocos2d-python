import cocos
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite

from cocos.actions import *

director.init()

class MainLayer(Layer):

    def __init__(self):

        super(MainLayer, self).__init__()

        player = Sprite('sprites/Idle__000.png')
        player.scale = 0.2
        player.position = 120, 250

        caminarDerecha = MoveBy((450, 0), 5)
        caminarIzquierda = Reverse(caminarDerecha)

        patrullar = Repeat(Accelerate(caminarDerecha, 2) + Speed(caminarIzquierda, 5))

        player.do(patrullar)

        self.add(player)

scene = Scene(MainLayer())

director.run(scene)