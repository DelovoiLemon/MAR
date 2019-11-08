import time

DAYS = 100
hero = {'power':100, 'money':10, 'charisma':0, 'busy':0}
delta = {'power':0, 'money':0, 'charisma':0}

power = {("rest", "tv"):1,("rest", "mount"):2,("rest", "yacht"):3,
         ("work", "employee"):-5,("work", "freelance"):-3,("work", "corporation"):-7,("work", "mafia"):-10,
         ("clean", "komnata"):-2,("clean", "ylitsa"):-5,("clean", "bank"):-6}         
money = {("rest", "tv"):0,("rest", "mount"):-2,("rest", "yacht"):-5,
         ("work", "employee"):7,("work", "freelance"):8,("work", "corporation"):10,("work", "mafia"):20,
         ("clean", "komnata"):0,("clean", "ylitsa"):5,("clean", "bank"):10} 
charisma ={("rest", "tv"):0,("rest", "mount"):2,("rest", "yacht"):-5,
         ("work", "employee"):-7,("work", "freelance"):-8,("work", "corporation"):-10,("work", "mafia"):-20,
         ("clean", "komnata"):3,("clean", "ylitsa"):5,("clean", "bank"):10} 

def work():
    print('На кого будем работать?')
    print('1. На EPAM')
    print('2. Дома')
    print('3. На корпораци')
    print('4. На мафию ')
    while True :
        choice = int(input("Сделай выбор: "))
        if choice == 1:
            delta['power'] = power[("work", "employee")]
            delta['money'] = money[("work", "employee")]
            delta['charisma'] = charisma[("work", "employee")]
            break
        elif choice == 2:
            delta['power'] = power[("work", "freelance")]
            delta['money'] = money[("work", "freelance")]
            delta['charisma'] = charisma[("work", "freelance")]
            break
        elif choice == 3:
            delta['power'] = power[("work", "corporation")]
            delta['money'] = money[("work", "corporation")]
            delta['charisma'] = charisma[("work", "corporation")]
            break
        elif choice == 4:
            delta['power'] = power[("work", "mafia")]
            delta['money'] = money[("work", "mafia")]
            delta['charisma'] = charisma[("work", "mafia")]
            break
        else:
             print("Правильно давай выбирай!")
    days = int(input("Сколько дней будешь работать? "))
    hero['busy'] = days
    return;

def clean():
    print('Что будем убирать?')
    print('1. Комнату')
    print('2. Улицу')
    print('3. Банк')
    while True :
        choice = int(input("Сделай выбор : "))
        if choice == 1:
            delta['power'] = power[("clean", "komnata")]
            delta['money'] = money[("clean", "komnata")]
            delta['charisma'] = charisma[("clean", "komnata")]
            break
        elif choice == 2:
            delta['power'] = power[("clean", "ylitsa")]
            delta['money'] = money[("clean", "ylitsa")]
            delta['charisma'] = charisma[("clean", "ylitsa")]
            break
        elif choice == 3:
            
            delta['power'] = power[("clean", "bank")]
            delta['money'] = money[("clean", "bank")]
            delta['charisma'] = charisma[("clean", "bank")]
            break
        else:
             print("Правильно давай выбирай!")
    days = int(input("Сколько дней будешь убирать? "))
    hero['busy'] = days 
    return;

def rest ():
    print('Где будем отдыхать?')
    print('1. Дома на диване.')
    print('2. В горах.')
    print('3. На яхте.')
    while True :
        choice = int(input("Сделай выбор : "))
        if choice == 1:
            delta['power'] = power[("rest", "tv")]
            delta['money'] = money[("rest", "tv")]
            delta['charisma'] = charisma[("rest", "tv")]
            break
        elif choice == 2:
            delta['power'] = power[("rest", "mount")]
            delta['money'] = money[("rest", "mount")]
            delta['charisma'] = charisma[("rest", "mount")]
            break
        elif choice == 3:
            if hero['money'] < 5:
                print("Не хватает дениг!!!!!!")
                break
            delta['power'] = power[("rest", "yacht")]
            delta['money'] = money[("rest", "yacht")]
            delta['charisma'] = charisma[("rest", "yacht")]
            break
        else:
            print("Правильно давай выбирай!")
    days = int(input("Сколько дней будешь отдыхать? "))
    hero['busy'] = days
    return;

while DAYS > 0 and hero['charisma'] < 100:
    if hero['power'] <= 0:
        print("You Die!!!")
        break
    print ("---------------Осталось дней: ", DAYS)
    print ("Осталось силы: ", hero['power'])
    print ("Осталось денег: ", hero['money'])
    print ("Осталось репупации: ", hero['charisma'])

    if hero['busy'] > 0:
        print ("Буду занят еще ", hero['busy'], " дней")
        hero['busy'] -= 1
        hero['power'] += delta['power']
        hero['money'] += delta['money']
        hero['charisma'] += delta['charisma']
        time.sleep(0.1)
        DAYS -= 1
    else:
        print ("Чем займёмся?")
        print ("1. Будем отдыхать.")
        print ("2. Будем работать.")
        print ("3. Будем убирать.")
        while True :
            choice = input ("Сделай выбор: ")

            if choice == '1':
                rest()
                break
            elif choice == '2':
                work()
                break
            elif choice == '3':
                clean()
                break
            else:
                print("Правильно давай выбирай!")
if (hero['charisma'] >= 100 and hero['power'] > 1):
    print("YOU WIN!!!")
else:
    print("GAME OVER!!!")

