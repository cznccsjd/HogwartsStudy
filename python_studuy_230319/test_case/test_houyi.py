from python_studuy_230319.houyi import Houyi
import random

def test_fight():
    houyi = Houyi(name='houyi', hp=random.randint(1000, 1200), power=random.randint(100, 150),
                  defense=random.randint(100, 150))
    EZ = Houyi('EZ', random.randint(1000, 1200), random.randint(100, 150))
    assert 'WIN' in houyi.fight(EZ)
