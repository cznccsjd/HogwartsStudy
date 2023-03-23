from python_studuy_230319.Hero import Hero
import random

"""
定义一个新类，后裔，后裔继承于 Hero，并多了护甲属性。
重新定义另外一个 defense 属性：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个 hp 进行对比，血量先为零的人输掉比赛
"""

class Houyi(Hero):
    def __init__(self, name, hp, power, defense=0):
        super().__init__(name, hp, power)
        self.defense = defense
        print('初始化。。。。')
        print(f'{self.name}的hp是：{self.hp}')
        print(f'{self.name}的power是：{self.power}')
        print(f'{self.name}的defense是：{self.defense}\n')

    def fight(self, enemy):
        n = 1
        while (self.hp > 0 and enemy.hp > 0):
            num = random.randint(0, 1)
            if num < 1:
                print(f'第{n}回合，{self.name}被{enemy.name}打了')
                self.hp = self.hp + self.defense - enemy.power
            else:
                print(f'第{n}回合，{enemy.name}被{self.name}打了')
                enemy.hp = enemy.hp - self.power

            print(f'now, {self.name} is {self.hp}, {enemy.hp} is {enemy.hp}\n')
            n += 1

        if self.hp <= 0:
            result = f'最终, {enemy.name} WIN.. hp is:{enemy.hp}'
        elif enemy.hp <= 0:
            result = f'最终, {self.name} WIN.. hp is: {self.hp}'
        print(result)
        return result

if __name__ == '__main__':
    houyi = Houyi(name='houyi', hp=random.randint(1000,1200), power=random.randint(100,150), defense=random.randint(100,150))
    EZ = Houyi('EZ', random.randint(1000,1200), random.randint(100,150))
    houyi.fight(EZ)