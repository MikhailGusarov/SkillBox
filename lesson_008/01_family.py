# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100). +
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов +
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды. +
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода. +
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз. +
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.  +
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи. +
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов, +
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая) +
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии. +
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    def __init__(self):
        self.money = 100
        self.eat = 50
        self.mud = 0
        self.eat_for_cat = 30

    def __str__(self):
        return 'В доме {} денег, {} еды и {} грязи'.format(self.money, self.eat, self.mud)

    def get_mud(self):
        self.mud += 5


class Human:
    amount_money = 0
    eaten_food = 0
    bought_coat = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.die = False

    def __str__(self):
        if self.die:
            return '{} умер'.format(self.name)
        return 'У {} сытость {}, степень счастья {}'.format(self.name, self.fullness, self.happiness)

    def eat(self, max_eat=30):
        if self.house.eat == 0:
            cprint('{}: Еды нет!'.format(self.name), color='red')
            self.fullness -= 10
            if self.fullness <= 0:
                self.die = True
                return
        if self.house.eat > max_eat:
            eat = max_eat
        else:
            eat = self.house.eat
        self.fullness += eat
        self.house.eat -= eat
        Human.eaten_food += eat
        return '{} съел {} еды'.format(self.name, eat)

    def go_to_the_house(self, house):
        self.house = house
        print('{} заселился в доме'.format(self.name))

    def pick_up_cat(self, cat):
        cat.house = self.house
        return '{} подобрал кота.'.format(self.name)

    def pet_the_cat(self):
        self.happiness += 5
        return '{} гладит кота'.format(self.name)

    def act(self):
        if self.die:
            cprint('{} умер'.format(self.name), color='red')
            return False
        if self.happiness < 10:
            self.die = True
            cprint('{} умер от горя'.format(self.name), color='red')
            return False
        return True


class Husband(Human):

    def act(self):
        if super().act():
            if self.house.mud > 90:
                self.happiness -= 5
            if self.fullness <= 30:
                self.eat()
            elif self.house.money < 300:
                self.work()
            elif self.house.eat_for_cat < 30:
                self.go_to_pet_shop()
            else:
                dice = randint(1, 6)
                if dice == 1:
                    self.eat()
                elif dice == 2:
                    self.work()
                elif dice == 3:
                    self.pet_the_cat()
                elif dice == 4:
                    self.go_to_pet_shop()
                else:
                    self.gaming()

    def eat(self, max_eat=30):
        res = super().eat()
        if res:
            cprint(res, color='blue')

    def go_to_pet_shop(self):
        self.fullness -= 10
        if self.house.money < 10:
            cprint('{}: денег нет'.format(self.name), color='red')
            return
        if self.house.money > 50:
            self.house.eat_for_cat += 50
            self.house.money -= 50
        else:
            self.house.eat_for_cat += self.house.money
            self.house.money = 0
        cprint('{} сходил в зоомагазин'.format(self.name), color='blue')

    def pick_up_cat(self, cat):
        cprint(super().pick_up_cat(cat=cat), color='blue')

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        cprint('{} сходил на работу'.format(self.name), color='blue')
        Human.amount_money += 150

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint('{} играл в WoT'.format(self.name), color='blue')

    def pet_the_cat(self):
        cprint(super().pet_the_cat(), color='blue')


class Wife(Human):

    def act(self):
        if super().act():
            if self.house.mud > 90:
                self.happiness -= 5
            if self.fullness <= 30:
                self.eat()
            elif self.house.eat < 350:
                self.shopping()
            elif self.house.mud > 100:
                self.clean_house()
            else:
                dice = randint(1, 6)
                if dice == 1:
                    self.eat()
                elif dice == 2:
                    self.shopping()
                elif dice == 3:
                    self.clean_house()
                elif dice == 4:
                    self.pet_the_cat()
                else:
                    self.buy_fur_coat()

    def pick_up_cat(self, cat):
        cprint(super().pick_up_cat(cat=cat), color='magenta')

    def pet_the_cat(self):
        cprint(super().pet_the_cat(), color='magenta')

    def eat(self, max_eat=30):
        res = super().eat()
        if res:
            cprint(res, color='magenta')

    def shopping(self):
        self.fullness -= 10
        if self.house.money < 10:
            cprint('{}: денег нет'.format(self.name), color='red')
            return
        if self.house.money > 50:
            self.house.eat += 50
            self.house.money -= 50
        else:
            self.house.eat += self.house.money
            self.house.money = 0
        cprint('{} сходила в магазин'.format(self.name), color='magenta')

    def buy_fur_coat(self):
        if self.house.money < 350:
            cprint('На шубу нет денег', color='magenta')
            return
        self.fullness -= 10
        self.house.money -= 350
        self.happiness += 60
        cprint('{} купила шубу'.format(self.name), color='magenta')
        Human.bought_coat += 1

    def clean_house(self):
        self.fullness -= 10
        if self.house.mud > 100:
            self.house.mud -= 100
        else:
            self.house.mud = 0
        cprint('{} убралась дома'.format(self.name), color='magenta')


class Child(Human):
    def act(self):
        if super().act():
            if self.fullness < 30:
                self.eat()
            else:
                dice = randint(0, 3)
                if dice:
                    self.sleep()
                else:
                    self.eat()

    def eat(self, max_eat=10):
        res = super().eat(max_eat=max_eat)
        if res:
            cprint(res, color='white', attrs=['bold'])

    def sleep(self):
        self.fullness -= 10
        cprint('{} спит'.format(self.name), color='white', attrs=['bold'])


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None
        self.die = False

    def __str__(self):
        if self.die:
            return '{} умер'.format(self.name)
        return 'У {} сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.die:
            cprint('{} мертв'.format(self.name), color='red')
            return
        if self.fullness < 30:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.eat()
            elif dice == 2:
                self.soil()
            else:
                self.sleep()

    def eat(self):
        if self.house.eat_for_cat <= 0:
            cprint('Закончилась еда для кота!', color='red')
            self.fullness -= 10
            if self.fullness <= 0:
                self.die = True
                cprint('{} умер от голода'.format(self.name), color='red')
            return
        if self.house.eat_for_cat > 10:
            eat = 10
        else:
            eat = self.house.eat_for_cat
        self.fullness += 2 * eat
        self.house.eat_for_cat -= eat
        cprint('{} съел {} кошачьего корма'.format(self.name, eat), color='green')

    def sleep(self):
        self.fullness -= 10
        cprint('{} спал весь день'.format(self.name), color='green')

    def soil(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('{} подрал обои'.format(self.name), color='green')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
teftel = Cat(name='Тефтель')
lev = Child(name='Лев')
serge.go_to_the_house(home)
masha.go_to_the_house(home)
masha.pick_up_cat(teftel)
lev.go_to_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    teftel.act()
    lev.act()
    home.get_mud()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(teftel, color='cyan')
    cprint(lev, color='cyan')
    cprint(home, color='cyan')

cprint('================== Итого ==================', color='yellow')
cprint('Заработано денег {}'.format(Human.amount_money), color='yellow')
cprint('Съедено еды {}'.format(Human.eaten_food), color='yellow')
cprint('Куплено шуб {}'.format(Human.bought_coat), color='yellow')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо +
# отщепить ветку develop и в ней начать добавлять котов в модель семьи +
#
# Кот может: +
#   есть, +
#   спать, +
#   драть обои +
#
# Люди могут: +
#   гладить кота (растет степень счастья на 5 пунктов) +
#
# В доме добавляется: +
#   еда для кота (в начале - 30) +
#
# У кота есть имя и степень сытости (в начале - 30) +
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов +
# Еда для кота покупается за деньги: за 10 денег 10 еды. +
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды. +
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода. +
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов +


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка +
#
# Ребенок может: +
#   есть, +
#   спать, +
#
# отличия от взрослых - кушает максимум 10 единиц еды, +
# степень счастья  - не меняется, всегда ==100 ;) +



######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

