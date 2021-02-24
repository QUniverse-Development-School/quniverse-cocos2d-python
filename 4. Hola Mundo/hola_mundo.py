import cocos
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite

director.init()

class MainLayer(Layer):

    def __init__(self):

        super(MainLayer, self).__init__()

        player = Sprite('sprites/Idle__000.png')
        player.scale = 0.2
        player.position = 120, 250

        self.add(player)

scene = Scene(MainLayer())

director.run(scene)