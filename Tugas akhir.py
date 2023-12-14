import json 
import os 
import time
import random

file = 'data.json'

def clear():
    os.system('cls')

def load():
    try:
        with open(file, 'r') as output:
            data = json.load(output)
        return data
    except FileNotFoundError:
        data_kosong = []
        with open(file, 'w') as output:
            json.dump(data_kosong, output, indent=4)
        return data_kosong

def nambah(data):
    with open(file, 'w') as output:
        json.dump(data, output, indent=4)

def register():
    clear()
    print('Silahkan Masukkan data diri anda untuk diregisterkan')
    user = load()
    for i in range(1):
        username = input('Masukkan Username: ')
        password = input('Masukkan password: ')
        data_user ={
            'Username' : username,
            'Password' : password
        }
        user.append(data_user)
        nambah(user)
        print(5*('='),'Registrasi selesai',5*('='))
        tm()
        main()

def login():
    clear()
    username = input('Masukkan username anda: ')
    password = input('Masukkan password anda: ')
    user = load()

    status_login = False
    if len(user) != 0:
        for i in user:
            if i['Username'] == username and i['Password'] == password:
                status_login = True
    else:
        print('silahkan daftar dulu karena database masih belum ada akun')
        tt()
        main()    
    if status_login:
        clear()
    else:
        print('login gagal')
        tt()
        main()
    
def main():
    clear()
    print('Pilih 1 atau 2')
    pilih = int(input('1.Register\n2.Login\nPilih: '))
    if pilih == 1:
        register()
    if pilih == 2:
        login()

def tm():
    time.sleep(1)

def tt():
    time.sleep(2)

def atk(attacker, defender):
    dmg = attacker['atk']
    defender ['hp'] = defender ['hp'] - dmg
    if defender ['hp'] <= 0:
        tm()
        print ('{} took {} damage!'.format(defender['name'], dmg))        
        tm()
        print ('{} have been slain'.format(defender['name']))
    else:
        tm()
        print ('{} took {} damage!'.format(defender['name'], dmg))
        tm()
        print('{} have {} hp left'.format(defender['name'], defender ['hp']))
        time.sleep(1/2)

def heal(attacker, defender):
    attacker ['hp'] = attacker ['hp'] + 20
    tm()
    print ('{} healed for 20!'.format(attacker['name']))
    tm()
    print('{} have {} hp left'.format(attacker['name'], attacker ['hp']))
    time.sleep(1/2)

def buff(attacker, defender):
    attacker ['atk'] = attacker ['atk'] + 10
    tm()
    print ('{} buffed its atk for 10!'.format(attacker['name']))
    tm()
    print('{} now have {} atk'.format(attacker['name'], attacker ['atk']))
    time.sleep(1/2)

def rng(attacker, defender):
    dmg = random.randint(1,100)
    defender ['hp'] = defender ['hp'] - dmg
    if defender ['hp'] <= 0:
        tm()
        print ('{} took {} damage!'.format(defender['name'], dmg))
        tm()
        print ('{} have been slain'.format(defender['name']))
    else:
        tm()
        print ('{} took {} damage!'.format(defender['name'], dmg))
        tm()
        print('{} have {} hp left'.format(defender['name'], defender ['hp']))
        time.sleep(1/2)    

def commands(player, enemy):   
    while player ['hp'] >0 and enemy ['hp'] >0:
        cmd= int(input('1| Attack\n2| Heal\n3| Buff\n4| RNG move\n\nChoose your move: '))
        
        if cmd==1:
            tm()
            print('You attacked!')
            atk(player, enemy)
            if enemy ['hp'] >0:
                tm()
                print("{} attacked!".format(enemy['name']))
                atk(enemy, player)
                tm()
                clear()
                print(char, '=', player ['hp'],'    |',enemy ['name'], '=', enemy ['hp'])
        elif cmd==2:
            tm()
            print('You healed yourself!')
            heal(player, enemy)
            if enemy ['hp'] >0:
                tm()
                print("{} attacked!".format(enemy['name']))
                atk(enemy, player)
                tm()
                clear()
                print(char, '=', player ['hp'],'    |',enemy ['name'], '=', enemy ['hp'])                
        elif cmd==3:
            tm()
            print('You buffed your own atk')
            buff(player,enemy)
            if enemy ['hp'] >0:
                tm()
                print("{} attacked!".format(enemy['name']))
                atk(enemy, player)
                tm()
                clear()
                print(char, '=', player ['hp'],'|    |',enemy ['name'], '=', enemy ['hp'])                
        elif cmd==4:
            tm()
            print('You use your secret move! The damage will be random from 1 to 100')
            rng(player, enemy)
            if enemy ['hp'] >0:
                tm()
                print("{} attacked!".format(enemy['name']))
                atk(enemy, player)
                tm()
                clear()
                print(char, '=', player ['hp'],'    |',enemy ['name'], '=', enemy ['hp'])                
        else:
            print("Invalid move\n")

#cabang story
def end():
    tm()
    print('You finally arrived on the demon island,')
    tt()
    print('after you step your feet into the ground of the island,')
    tt()
    print('youre welcomed by the demon lord Udondondodon.')
    tt()
    print('So the final battle begins!\n')
    tt()
    commands(mc, boss)
    time.sleep(3)
    clear()
    if mc ['hp']>0:
        tt()
        print('After a long fight, you finally slayed the demon lord.')
        tt()
        print('You saved the world.\n')
        tt()
        print('The end        |GOOD ENDING|')
        time.sleep(4)
    else:
        tt()
        print('it seems like you didnt prepared much for the outcome')
        tt()
        print('you failed to saved the world, and the demon race wins the war')
        tt()
        print('and rule it for a thousand year later')
        tt()
        print('waiting for the new hero to rise.\n')
        tt()
        print('The end        |BAD ENDING|')
        time.sleep(4)

#Code mulai
main()

clear()
print('Welcome to RNG RPG before you enter the game\n')
tm()
char = input('insert your character name here: ')
print(char, 'it is then')
tt()
clear()

#Daftar dict
mc={'name' : char, 'hp':80, 'atk':15}
imp={'name' :'Imp', 'hp':25, 'atk':4}
dragon={'name' :'Blue Eyes White Dragon', 'hp':90, 'atk':12}
leviathan={'name' :'Leviathan', 'hp':40, 'atk':45}
boss={'name' :'Udondondodon', 'hp':100, 'atk':50}

print('Once upon a time the human and demon race were living together peacefully,')
tt()
print('until they did not. Then a war between them erupted.')
tt()
print('This war have been going on for about a thousand year,')
tt()
print('its time for our hero to rise and stop this disaster')
tt()
print('for good and that will be your job',char)
tt()
print('So! The journey of',char,'begins!')
time.sleep(3)

clear()
print('The time has come,', char, 'have been preparing for this moment.')
tt()
print('So he grabbed all of his gear and set himself on an adventure.')
tt()
print('Before that', char,'have to choose his own path!\n')
tt()
while True:
    print('1| Forest\n2| Cliff\n3| Exit Program')
    choose= int(input('Choose your path: '))
    if choose==1:
        tm()
        clear()
        print('You meet an imp, it seems like it wants to kill you\n')
        tm()
        commands(mc, imp)
        time.sleep(3)
        if mc ['hp']>0:
            tm()
            clear()
            print('after you killed the imp, you want to continue your journey\n')    
            print('1| Mountain\n2| Sea\n3| Exit Program')
            choose= int(input('Choose your path: '))
            clear()
            if choose==1:
                tm()
                clear()
                print('You decided to go through the Mountains, according to the rumor,')
                tt()
                print('there is a legendary dragon sleeping on top of it.')
                tt()
                print('You planned to ask the dragon to take you to the\nDemon Island')
                tt()
                print('After you climbed the mountain you finally meet the dragon,')
                tt()
                print('he wants to test you before he obeys your command!')
                commands(mc, dragon)
                time.sleep(3)
                clear()
                if mc ['hp']>0:
                    end()
                    break
                else:
                    print('Better luck next time!\n')
                    break
            elif choose==2:
                tm()
                clear()
                print('You decided to go through the Sea, according to the rumor,')
                tt()
                print('there is a divine beast sleeping inside of it.')
                tt()
                print('You planned to ask the beast to take you to the\nDemon Island')
                tt()
                print('After you swam through the ocean you finally meet the beast,')
                tt()
                print('she wants to test you before she obeys your command!')
                commands(mc, leviathan)
                time.sleep(3)
                clear()
                if mc ['hp']>0:
                    end()
                    break
                else:
                    print('Better luck next time!\n')     
                    break
            elif choose==3:
                break               
            else:
                print('Just follow the script pls\n')
                tt()
                clear()
    elif choose==2:
        print('You fell into the abyss and died!\n')
        break
    elif choose==3:
        break
    else:
        print('Just follow the script pls\n')
        tt()
        clear()