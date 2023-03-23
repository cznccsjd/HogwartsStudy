#coding:utf-8

"""
实战练习 1 - 需求说明(面向对象)

一个回合制游戏，有两个英雄，分别是 EZ 和 JINX。
每个英雄都有 hp 属性和 power 属性，分别代表血量和攻击力
EZ 初始值： hp，1100； power，190
Jinx 初始值： hp，1000； power，210
每个英雄都有一个 fight 方法：
hero_final_hp = hero_hp - enemy_power
enemy_final_hp = enemy_hp - hero_power
对比 hero_final_hp 和 enemy_final_hp，血量先为零的人输掉比赛
"""
import random

class Hero:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def fight(self, enemy):
        '''
        1、判断本回合谁挨打
        2、挨打的人掉血
        :return:
        '''
        n = 1
        while (self.hp > 0 and enemy.hp > 0):
            num = random.randint(0, 1)
            if num < 1:
                print(f'第{n}回合，{self.name}被{enemy.name}打了')
                self.hp = self.hp - enemy.power
            else:
                print(f'第{n}回合，{enemy.name}被{self.name}打了')
                enemy.hp = enemy.hp - self.power

            print(f'now, EZ.hp is :{EZ.hp}, Jinx.hp is {Jinx.hp}\n')
            n += 1

        if self.hp <= 0:
            result = f'最终, {enemy.name} WIN.. hp is:{enemy.hp}'
        elif enemy.hp <= 0:
            result = f'最终, {self.name} WIN.. hp is: {self.hp}'
        print(result)
        return result

if __name__ == '__main__':
    EZ = Hero('EZ', 1100, 190)
    Jinx = Hero('Jinx', 1000, 210)
    EZ.fight(Jinx)
