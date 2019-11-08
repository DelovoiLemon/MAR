import time

DAYS = 100

hero = {'power': 100, 'money': 10, 'charisma': 0, 'busy': 0}

delta = {'power': 0, 'money': 0, 'charisma': 0}

power = {("rest", "tv"): 1, ("rest", "mount"): 2, ("rest", "yacht"): 3,
         ("work", "employee"): -5, ("work", "freelance"): -3,
         ("work", "corporation"): -7, ("work", "mafia"): -10,
         ("clean", "room"): -2, ("clean", "outdoor"): -5,
         ("clean", "bank"): -6 }

money = {("rest", "tv"): 0, ("rest", "mount"): -2, ("rest", "yacht"): -5,
         ("work", "employee"): 7, ("work", "freelance"): 8,
         ("work", "corporation"): 10, ("work", "mafia"): 20,
         ("clean", "room"): 0, ("clean", "outdoor"): 5,
         ("clean", "bank"): 10}

charisma = {("rest", "tv"): 0, ("rest", "mount"): 2, ("rest", "yacht"): -5,
            ("work", "employee"): -7, ("work", "freelance"): -8,
            ("work", "corporation"): -10, ("work", "mafia"): -20,
            ("clean", "room"): 3, ("clean", "outdoor"): 5, ("clean", "bank"): 10}


def work():
    print('На кого будем работать?')
    print('1. На EPAM')
    print('2. Дома')
    print('3. На корпораци')
    print('4. На мафию ')

    Input = input("Сделай выбор: ")

    while True:
        if Input == '1':
            delta['power'] = power[("work", "employee")]
            delta['money'] = money[("work", "employee")]
            delta['charisma'] = charisma[("work", "employee")]
            break
        elif Input == '2':
            delta['power'] = power[("work", "freelance")]
            delta['money'] = money[("work", "freelance")]
            delta['charisma'] = charisma[("work", "freelance")]
            break
        elif Input == '3':
            delta['power'] = power[("work", "corporation")]
            delta['money'] = money[("work", "corporation")]
            delta['charisma'] = charisma[("work", "corporation")]
            break
        elif Input == '4':
            delta['power'] = power[("work", "mafia")]
            delta['money'] = money[("work", "mafia")]
            delta['charisma'] = charisma[("work", "mafia")]
            break
        else:
            Input = input("Попробуйте ещё раз: ")

    while True:
        try:
            days = int(input("Сколько дней будешь отдыхать? "))
            if days < DAYS:
                break
        except:
            pass

    hero['busy'] = days
    return


def clean():
    print('Что будем убирать?')
    print('1. Комнату')
    print('2. Улицу')
    print('3. Банк')

    Input = input("Сделай выбор : ")

    while True:
        if Input == '1':
            delta['power'] = power[("clean", "room")]
            delta['money'] = money[("clean", "room")]
            delta['charisma'] = charisma[("clean", "room")]
            break
        elif Input == '2':
            delta['power'] = power[("clean", "outdoor")]
            delta['money'] = money[("clean", "outdoor")]
            delta['charisma'] = charisma[("clean", "outdoor")]
            break
        elif Input == '3':

            delta['power'] = power[("clean", "bank")]
            delta['money'] = money[("clean", "bank")]
            delta['charisma'] = charisma[("clean", "bank")]
            break
        else:
            print("")

    while True:
        try:
            days = int(input("Сколько дней будешь отдыхать? "))
            break
        except:
            pass

    hero['busy'] = days
    return


def rest():
    print('Где будем отдыхать?')
    print('1. Дома на диване.')
    print('2. В горах.')
    print('3. На яхте.')

    Input = input("Сделай выбор: ")
    while True:
        if Input == '1':
            delta['power'] = power[("rest", "tv")]
            delta['money'] = money[("rest", "tv")]
            delta['charisma'] = charisma[("rest", "tv")]
            break
        elif Input == '2':
            delta['power'] = power[("rest", "mount")]
            delta['money'] = money[("rest", "mount")]
            delta['charisma'] = charisma[("rest", "mount")]
            break
        elif Input == '3':
            if hero['money'] < 5:
                print("Не хватает денег!")
                break
            delta['power'] = power[("rest", "yacht")]
            delta['money'] = money[("rest", "yacht")]
            delta['charisma'] = charisma[("rest", "yacht")]
            break
        else:
            Input = input("Попробуйте ещё раз: ")

    while True:
        try:
            days = int(input("Сколько дней будешь отдыхать? "))
            if days < DAYS:
                break
        except:
            pass

    hero['busy'] = days
    return


def menu(days):
    while days > 0 and hero['charisma'] < 100:
        if hero['power'] <= 0:
            print("You DIE!!!\n")
            break

        if hero['busy'] > 0:
            print("Буду занят еще ", hero['busy'], " дней\день\n\n")
            hero['busy'] -= 1
            hero['power'] += delta['power']
            hero['money'] += delta['money']
            hero['charisma'] += delta['charisma']
            time.sleep(0.2)
            days -= 1
        else:
            print("---- Статистика ---- ")
            print("Дни:       ", days)
            print("Сила:      ", hero['power'])
            print("Деньги:    ", hero['money'])
            print("Репупация: ", hero['charisma'], "\n")

            print("Чем займёмся?")
            print("1. Будем отдыхать.")
            print("2. Будем работать.")
            print("3. Будем убирать.")
            Input = input("Сделай выбор: ")
            while True:

                if Input == '1':
                    rest()
                    break
                elif Input == '2':
                    work()
                    break
                elif Input == '3':
                    clean()
                    break
                else:
                    Input = input("Попробуйте ещё раз: ")

    if hero['charisma'] >= 100 and hero['power'] > 1:
        print("You WIN!!!")
    else:
        print("You LOSE!!!")


menu(DAYS)
