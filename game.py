import random


# 定义英雄类
class Hero(object):
    money = random.randint(300,5000)
    def __init__(self, *name):
        self.name = name
        self.hp = random.randint(30000,50000)  # 血量
        self.attack = random.randint(2000, 7000)  # 随机产生攻击值
        self.defense = random.randint(1000, 1500)

    # 显示英雄信息
    def __str__(self):
        return "名字:%s 血量:%s 攻击:%d 防御:%d" % (self.name, self.hp, self.attack, self.defense)

    # 攻击函数
    def fight(self, monster):
        # 计算怪物掉血多少
        mhp = random.randint(1,7000) - monster.defense
        # 减少怪物血量
        monster.hp = monster.hp - mhp
        # 提示信息
        print("精灵%s对精灵%s造成了%d伤害!" % (self.name, monster.name, mhp))


#  定义怪物类
class Monster(object):
    def __init__(self, *name):
        self.name = name
        self.hp = random.randint(30000,50000)  # 血量
        self.attack = random.randint(2000, 7000)  # 随机产生攻击值
        self.defense = random.randint(1000, 1500)

    # 显示怪物信息
    def __str__(self):
        return "名字:%s 血量:%s 攻击:%d 防御:%d" % (self.name, self.hp, self.attack, self.defense)
    # 攻击函数
    def fight(self, hero):
        # 计算怪物掉血多少
        mhp = random.randint(1, 7000) - hero.defense
        # 减少怪物血量
        hero.hp = hero.hp - mhp
        # 提示信息
        print("精灵%s对精灵%s造成了%d伤害!" % (self.name, hero.name, mhp))


# 创建对象
hero = Hero(random.choice(("古拉顿", "皮卡丘", "雷精灵","雷公","炎帝","水君","洛奇亚","凤王","基拉祈","代欧奇希斯","帝牙卢卡","帕路奇亚","达克莱伊","阿尔宙斯","蜥蜴王","巨沼怪","火焰鸡","土台龟","烈焰猴","帝王拿波","君主蛇","炎武王","大剑鬼")))
# 创建怪物
monster = Monster(random.choice(("裂空座","盖欧卡","喷火龙","水箭龟","妙蛙花","大针蜂","尼多王","霸王花","哥达鸭","风速狗","化石翼龙","快龙","火暴兽","布里卡隆","妖火红狐","甲贺忍蛙"," 狙射树枭","炽焰咆哮虎","西狮海壬","大竺葵","飞天螳螂","巨金怪")))
# 回合数
my_round = 1
# 开始回合战斗
while True:
    input()
    print(hero)
    print(monster)
    print("-" * 50)
    print("当前第%d回合:" % my_round)
    hero.fight(monster)
    if monster.hp <= 0:
        print("精灵%s成功打败了%s,获得了%s元!" % (hero.name, monster.name, hero.money))
        break
    monster.fight(hero)
    if hero.hp <= 0:
        print("野生精灵%s打败了你，你的眼前一片黑暗!" % monster.name)
        break

    my_round += 1