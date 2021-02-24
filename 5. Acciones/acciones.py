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

        # player.do(MoveBy((450, 0), 3))

        # player.do(Place((120, 400)))
        # player.do(RotateBy(120,0))
        # player.do(ScaleTo(1, 3))

        # player.do(Blink(10, 3))
        # player.do(Repeat(RotateBy(360, 1)))

        # caminarDerecha = MoveBy((450, 0), 2)
        # reiniciarPosicion = Place((120, 250))
        # player.do(caminarDerecha + reiniciarPosicion)

        # caminarDerecha = MoveBy((450, 0), 2)
        # rotar = RotateBy(360, 1) * 2
        # player.do(caminarDerecha | rotar)

        # player.do(Blink(10, 3) + Show())

        rotar = Repeat(RotateBy(360, 1))
        achicar = ScaleTo(0, 2.5)
        player.do(rotar | achicar)

        self.add(player)

scene = Scene(MainLayer())

director.run(scene)