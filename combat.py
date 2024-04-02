import random


class Character:
    def __init__(self, health=100, damage=10, defence=0.7):
        self.health = health
        self.damage = damage
        self.defence = defence

    def __repr__(self):
        return f'{self.name} health: {self.health}, damage: {self.damage}, defence: {self.defence}'

    def attack(self, enemy):
        enemy.health -= int(self.damage * enemy.defence)
        print(f'У противника осталось {enemy.health}')

    def _set_lucky_number(self):
        return random.randint(1, 100)

    def choose_weapon(self, item=None):
        if item == 'Щит':
            self.defence = round(self.defence - 0.3, 2)
        elif item == 'Меч':
            self.damage += 10
            self.defence = round(self.defence - 0.1, 2)
        elif item == 'Лук':
            self.damage += 15
            self.defence = round(self.defence + 0.1, 2)
        elif item is None:
            pass
        else:
            print('Оружия нет. Персонаж без оружия.')


class Human(Character):
    name = 'Human'

    def __init__(self, health=90, damage=9, defence=0.8, luck=20):
        super().__init__(health, damage, defence)
        self.luck = luck

    def attack(self, enemy):
        if self._set_lucky_number() <= self.luck:
            enemy.health -= int(self.damage * 2 * enemy.defence)
            print(f'{self.name} атакует. CуперАтака: У противника {enemy.name} осталось {enemy.health}')
        else:
            enemy.health -= int(self.damage * enemy.defence)
            print(f'{self.name} атакует. У противника {enemy.name} осталось {enemy.health}')


class Cyclop(Character):
    name = 'Cyclop'

    def __init__(self, health=150, damage=24, defence=0.7, unluck=10):
        super(Cyclop, self).__init__(health, damage, defence)
        self.unluck = unluck

    def attack(self, enemy):
        if self._set_lucky_number() <= self.unluck:
            print(f'{self.name} атакует. Неудача: промах')
        else:
            enemy.health -= int(self.damage * enemy.defence)
            print(f'{self.name} атакует. У противника {enemy.name} осталось {enemy.health}')


class Elf(Character):
    name = "Elf"

    def __init__(self,  health=70, damage=14, defence=0.9, recovery=30):
        super().__init__(health, damage, defence)
        self.recovery = recovery

    def attack(self, enemy):
        if self._set_lucky_number() <= self.recovery:
            self.health = int(self.health * 1.3)
            enemy.health -= int(self.damage * enemy.defence)
            print(f'{self.name} Регенерация {self.health}')
            print(f'{self.name} атакует. У противника {enemy.name} осталось {enemy.health}')
        else:
            enemy.health -= int(self.damage * enemy.defence)
            print(f'{self.name} атакует. У противника {enemy.name} осталось {enemy.health}')


class Mage(Character):
    name = "Mage"

    def __init__(self,  health=40, damage=6, defence=0.9, magic=35):
        super().__init__(health, damage, defence)
        self.magic = magic

    def attack(self, enemy):
        if self._set_lucky_number() <= self.magic:
            enemy.defence = round(enemy.defence + 0.2, 2)
            enemy.damage = int(enemy.damage * 0.75)
            enemy.health -= int(self.damage * enemy.defence)
            print(f'Магия Урон противника {enemy.damage} Защита противника {enemy.defence}')
            print(f'{self.name} атакует. У противника {enemy.name} осталось {enemy.health}')
        else:
            enemy.health -= int(self.damage * enemy.defence)
            print(f'{self.name} атакует. У противника {enemy.name} осталось {enemy.health}')


def player_choice():
    group = []
    while True:
        data = {"Эльф": Elf, "Человек": Human, "Циклоп": Cyclop, "Маг": Mage}
        choice = input('Выберите расу("Эльф, Человек, Циклоп, Маг"): ').capitalize().rstrip()
        if data.get(choice) is None:
            print('Такой расы нет')
        else:
            n = int(input('Введите количество персонажей: '))
            #weapon = input('Выберите оружие:(Меч, Лук, Щит): ').capitalize().rstrip()
            for i in range(n):
                group.append(data[choice]())
                weapon = input('Выберите оружие:(Меч, Лук, Щит): ').capitalize().rstrip()
                group[-1].choose_weapon(weapon)
            answer = input('Команда собрана? Да или Нет ').capitalize().rstrip()
            if answer == 'Нет':
                continue
            elif answer == 'Да':
                print(group)
                return group


class Battle:
    def __init__(self):
        self.player1 = player_choice()
        self.player2 = player_choice()

    def fight(self):
        while True:
            self.player1[0].attack(self.player2[0])
            if self.player2[0].health <= 0:
                print(f'{self.player2[0].name} умер')
                del self.player2[0]
                if len(self.player2) == 0:
                    print('Player1 выиграл')
                    print(self.player1)
                    print(f'В войске осталось {len(self.player1)} персонажей')
                    break
                print('Player2')
                answer1 = self.get_answer()
                if answer1 == 'Да':
                    continue
                elif answer1 == 'Нет':
                    print('Player2 сдался')
                    break
            self.player2[0].attack(self.player1[0])
            if self.player1[0].health <= 0:
                print(f'{self.player1[0].name} умер')
                del self.player1[0]
                if len(self.player1) == 0:
                    print('Player2 выиграл')
                    print(self.player2)
                    print(f'В войске осталось {len(self.player2)} персонажей')
                    break
                print('Player1')
                answer2 = self.get_answer()
                if answer2 == 'Да':
                    continue
                elif answer2 == 'Нет':
                    print('Player1 сдался')
                    break

    def get_answer(self):
        print(f'Армия Player1 {self.player1}')
        print(f'Армия Player2 {self.player2}')
        answer = input('Вы будете продолжать бой? (Да или Нет) ').capitalize().rstrip()
        return answer


# def main():
#     player1 = player_choice()
#     player2 = player_choice()
#     while True:
#         if len(player1) == 0:
#             print('Player2 выиграл')
#             print(player2)
#             print(f'В войске осталось {len(player2)} персонажей')
#             break
#         elif len(player2) == 0:
#             print('Player1 выиграл')
#             print(player1)
#             print(f'В войске осталось {len(player1)} персонажей')
#             break
#         player1[0].attack(player2[0])
#         if player2[0].health <= 0:
#             print(f'{player2[0].name} умер')
#             del player2[0]
#             continue
#         player2[0].attack(player1[0])
#         if player1[0].health <= 0:
#             print(f'{player1[0].name} умер')
#             del player1[0]
#             continue


if __name__ == '__main__':
    Battle().fight()
