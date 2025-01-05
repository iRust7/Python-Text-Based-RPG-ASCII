import os, sys, time, random

from map import Map
from tile import player
from colors import *
from ascii import *


run = True
menu = True
play = False
tutorial = False
key = False
fight = False
tempshield = True
buy = False
talk = False
boss = False
name = None

HP = 100
HPMAX = 500
ATK = 10
pot = 10
rune = 10
gold = 500
x_loc = 0
y_loc = 0

            # x = 0             # x = 1           # x = 2            # x = 3            # x = 4           # x = 5
map_data = [["Hampara Luas",  "Rawa Berlumpur",      "Wali Kota",      "Old Knight",    "Padang Rumput",  "Gunung Berbatu"],  # y = 0
           ["Padang Rumput",     "Hutan Rimba",    "Kepala Desa",      "Old Knight",   "Gunung Berbatu",   "Jembatan Kayu"],  # y = 1
           ["Toko Misterius","Bandit Perampok",  "Padang Rumput",     "Kepala Desa",    "Padang Rumput", "Tentara Bayaran"],  # y = 2
           ["Jembatan Batu",     "Kepala Desa",          "Bukit",    "Penyihir Tua",              "Gua",  "Toko Misterius"],  # y = 3
           ["Padang Rumput",    "Penyihir Tua","Tentara Bayaran",          "Sungai",   "Toko Misterius", "Bandit Perampok"]]  # y = 4

y_loc_len = len(map_data)-1
x_loc_len = len(map_data[0])-1


sisahp_symbol = "▓"
losthp_symbol = "_"

hp_bars = 20

biom = {
    "Padang Rumput": {
        "t": "Hamparan luas, tidak ada yang menarik disini",
        "e": True,
        "a": ascii_field},
    "Hutan Rimba": {
        "t": "Hutan yang lebat, Hati - Hati monster disini",
        "e": True,
        "a": ascii_forest},
    "Gunung Berbatu": {
        "t": "Gunung yang tinggi, Sepertinya banyak batu dan mineral",
        "e": False,
        "a": ascii_mtrock},
    "Jembatan Kayu": {
        "t": "Jembatan yang terbuat dari kayu, akan runtuh kapan saja",
        "e": False,
        "a": ascii_wood},
    "Jembatan Batu": {
        "t": "Jembatan yang terbuat dari batu, kokoh dan aman",
        "e": False,
        "a": ascii_stone},
    "Sungai": {
        "t": "Sungai yang deras, mungkin ada ikan disini",
        "e": False,
        "a": ascii_river},
    "Rawa Berlumpur": {
        "t": "Rawa yang berlumpur, mungkin ada monster disini",
        "e": True,
        "a": ascii_swamp},
    "Bukit": {
        "t": "Bukit yang tinggi, Aku harus berhati-hati disini",
        "e": True,
        "a": ascii_hill},
    "Toko Misterius": {
        "t": "Toko yang menjual barang-barang misterius",
        "e": False,
        "a": ascii_shop},
    "Kepala Desa": {
        "t": "Desa yang ramai",
        "e": False,
        "a": ascii_village},
    "Wali Kota": {
        "t": "Pusat Kota",
        "e": False,
        "a": ascii_city},
    "Gua": {
        "t": "Gua yang gelap, Mungkin Ada boss disini",
        "e": True,
        "a": ascii_cave,},
    "Hampara Luas": {
        "t": "Hamparan luas yang indah, namum entah kenapa terasa sepi",
        "e": False,
        "a": ascii_field},
    "Old Knight": {
        "t": "Knight Tua yang sedang bersandar di batu besar",
        "e": False,
        "a": ascii_reknight},
    "Bandit Perampok": {
        "t": "Sekelompok Bandit yang sedang beristirahat",
        "e": True,
        "a": ascii_pbandit},
    "Penyihir Tua": {
        "t": "Penyihir Tua yang sedang bermeditasi di depan gubuk",
        "e": True,
        "a": ascii_gubuk},
    "Tentara Bayaran": {
        "t": "Seorang Tentara Bayaran yang sedang berlatih",
        "e": False,
        "a": ascii_latsoldier
    }
}

e_list = ["Ghoul", "Goblin", "Orc", "Troll", "Slime", "Vampire", "Werewolf", "Banshee"]

mobs = {
    "Ghoul": {
        "hp": 18,
        "at": 3,
        "go": 12,
        "a": ascii_ghoul
    }
    ,
    "Goblin": {
        "hp": 20,
        "at": 7,
        "go": 18,
        "a": ascii_goblin
    },
    "Orc": {
        "hp": 37,
        "at": 12,
        "go": 22,
        "a": ascii_orc
    },
    "Troll": {
        "hp": 50,
        "at": 16,
        "go": 28,
        "a": ascii_troll
    },
    "Slime": {
        "hp": 5,
        "at": 1,
        "go": 1,
        "a": ascii_slime
    },
    "Vampire": {
        "hp": 43,
        "at": 14,
        "go": 28,
        "a": ascii_vampire
    },
    "Werewolf": {
        "hp": 60,
        "at": 27,
        "go": 35,
        "a": ascii_warewolf
    },
    "Banshee": {
        "hp": 80,
        "at": 33,
        "go": 47,
        "a": ascii_banshe
    }
}

espc_list = ["Old Knight", "Bandit Perampok", "Penyihir Tua", "Tentara Bayaran", "Morthos the Shadow Weaver"]

smobs = {
    "Old Knight": {
        "hp": 100,
        "at": 20,
        "go": 100
    },
    "Bandit Perampok": {
        "hp": 80,
        "at": 15,
        "go": 60
    },
    "Penyihir Tua": {
        "hp": 120,
        "at": 25,
        "go": 120
    },
    "Tentara Bayaran": {
        "hp": 80,
        "at": 10,
        "go": 150
    },
    "Morthos the Shadow Weaver": {
        "hp": 670,
        "at": 50,
        "go": 500
    }
}

def clear():
    os.system("cls")

def gris():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def artprint(artlist, delay):
    for row in artlist:
        print(row)
        time.sleep(delay)


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(rune),
        str(gold),
        str(x_loc),
        str(y_loc),
        str(key)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def heal(jumlah):
    global HP
    if HP + jumlah <= HPMAX:
        HP += jumlah
    else:
        HP = HPMAX
    print("Hero", name + " HP regenerasi ke : " + str(HP) + "!")

def hpcolor(hp, hpmax):
    if hp > 0.66 * hpmax:
        HP_color = color_green1
    elif hp > 0.33 * hpmax:
        HP_color = color_yellow
    else:
        HP_color = color_red
    return HP_color

def finalcave():
    global boss, key, fight

    while boss:
        clear()
        gris()
        sprint("Goa Penyihir Hitam, Morthos the Shadow Weaver, Akhir perjalananmu telah tiba, Hero " + name + "!")
        gris()
        if key == True :
            print("1 - Masuki Goa")
        else:
            print("Anda membutuhkan kunci untuk masuk. Dapatkan dari Kepala Desa, Old Knight, atau Wali Kota.")
        print("2 - Kembali")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            if key == True:
                fight = True
                battle_boss()
            else:
                print("Anda membutuhkan kunci untuk masuk. Dapatkan dari Kepala Desa, Old Knight, atau Wali Kota.")
                input("> ")
        elif choice == "2":
            boss = False

def shop():
    global buy, gold, ATK, pot, rune

    while buy:
        clear()
        gris()
        print("Selamat Datang di Toko Misterius, Hero ")
        gris()
        print("Hero", name + " Gold : " + str(gold))
        print("Ramuan : " + str(pot))
        print("Rune : " + str(rune))
        print("Attack : " + str(ATK))
        gris()
        print("1 - Upgrade Attack (55 Gold)")
        print("2 - Beli Ramuan (15 Gold)")
        print("3 - Beli Rune (25 Gold)")
        print("0 - Kembali")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            if gold >= 55:
                gold -= 55
                ATK += 5
                print("Attack Hero " + name + " meningkat!")
            else:
                print("Gold tidak cukup")
            input("> ")
        elif choice == "2":
            if gold >= 15:
                gold -= 15
                pot += 1
                print("Kamu mendapatkan ramuan!")
            else:
                print("Gold tidak cukup")
            input("> ")
        elif choice == "3":
            if gold >= 25:
                gold -= 25
                rune += 1
                print("Kamu mendapatkan rune!")
            else:
                print("Gold tidak cukup")
            input("> ")
        elif choice == "0":
            buy = False

def battle_boss():
    global fight, play, run, HP, pot, rune, gold, boss

    enemy = "Morthos the Shadow Weaver"
    hp = smobs[enemy]["hp"]
    hpmax = hp
    atk = smobs[enemy]["at"]
    g = smobs[enemy]["go"]

    while fight:
        clear()
        HP_color_player = hpcolor(HP, HPMAX)
        HP_color_enemy = hpcolor(hp, hpmax)
        sisahp_bars_player = round(HP / HPMAX * hp_bars)
        losthp_bars_player = hp_bars - sisahp_bars_player
        sisahp_bars_enemy = round(hp / hpmax * hp_bars)
        losthp_bars_enemy = hp_bars - sisahp_bars_enemy
        gris()
        artprint(ascii_mortos, 0.01)
        print("Kalahkan : " + enemy + "!")
        print("Boss : Morthos the Shadow Weaver", ", Level 99")
        gris()
        print(enemy + " HP : " + HP_color_enemy + str(hp) + "/" + str(hpmax) + color_default)
        print(f"|{HP_color_enemy}{sisahp_bars_enemy * sisahp_symbol}{losthp_bars_enemy * losthp_symbol}{color_default}|")
        print("Hero :", name + ", HP : " + HP_color_player + str(HP) + "/" + str(HPMAX) + color_default)
        print(f"|{HP_color_player}{sisahp_bars_player * sisahp_symbol}{losthp_bars_player * losthp_symbol}{color_default}|")
        print("Ramuan : " + str(pot))
        print("Rune : " + str(rune))
        gris()
        print("1 - Attack")
        if pot > 0:
            print("2 - Pakai Buffed Ramuan (150HP)")
        if rune > 0:
            print("3 - Pakai Buffed Rune (250HP)")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            hp -= ATK
            print("Kamu menyerang " + enemy + " dengan " + str(ATK) + " damage")
            if hp > 0:
                HP -= atk
                print("Kamu diserang " + enemy + " dengan " + str(atk) + " damage")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(150)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki ramuan")
            input("> ")
        elif choice == "3":
            if rune > 0:
                rune -= 1
                heal(250)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki rune")
            input("> ")

        if HP <= 0:
            print(enemy + " mengalahkanmu, Hero " + name + "!")
            gris()
            fight = False
            play = False
            run = False
            print("Game Over")
            input("> ")
            quit()

        if hp <= 0:
            print("Kamu mengalahkan " + enemy + "!")
            gris()
            fight = False
            gold += g
            print("Kamu mendapatkan " + str(g) + " gold")
            if random.randint(0, 100) <= 10:
                print("Kamu mendapatkan rune!")
                rune += 1
            if random.randint(0, 100) <= 30:
                print("Kamu mendapatkan ramuan!")
                pot += 1
            if enemy == "Morthos the Shadow Weaver":
                gris()
                print("Kamu menyelesaikan misi dan menyelamatkan desa dari kutukan!")
                print("Inilah akhir dari petualanganmu, Hero " + name + "!")
                print("Terima kasih telah bermain!")
                boss = False
                play = False
                run = False
                quit()
            input("> ")
            clear()

def sprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def battle_wizard():
    global fight, play, run, HP, pot, rune, gold

    enemy = "Penyihir Tua"
    hp = smobs[enemy]["hp"]
    hpmax = hp
    atk = smobs[enemy]["at"]
    g = smobs[enemy]["go"]

    while fight:
        clear()
        HP_color_player = hpcolor(HP, HPMAX)
        HP_color_enemy = hpcolor(hp, hpmax)
        sisahp_bars_player = round(HP / HPMAX * hp_bars)
        losthp_bars_player = hp_bars - sisahp_bars_player
        sisahp_bars_enemy = round(hp / hpmax * hp_bars)
        losthp_bars_enemy = hp_bars - sisahp_bars_enemy
        gris()
        artprint(ascii_wizard, 0.01)
        print("Kalahkan : " + enemy + "!")
        print("Penyihir : " + wizard.name + ", Level " + str(wizard.level))
        gris()
        print(enemy + " HP : " + HP_color_enemy + str(hp) + "/" + str(hpmax) + color_default)
        print(f"|{HP_color_enemy}{sisahp_bars_enemy * sisahp_symbol}{losthp_bars_enemy * losthp_symbol}{color_default}|")
        print("Hero :", name + ", HP : " + HP_color_player + str(HP) + "/" + str(HPMAX) + color_default)
        print(f"|{HP_color_player}{sisahp_bars_player * sisahp_symbol}{losthp_bars_player * losthp_symbol}{color_default}|")
        print("Ramuan : " + str(pot))
        print("Rune : " + str(rune))
        gris()
        print("1 - Attack")
        if pot > 0:
            print("2 - Pakai Ramuan (40HP)")
        if rune > 0:
            print("3 - Pakai Rune (80HP)")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            hp -= ATK
            print("Kamu menyerang " + enemy + " dengan " + str(ATK) + " damage")
            if hp > 0:
                HP -= atk
                print("Kamu diserang " + enemy + " dengan " + str(atk) + " damage")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(40)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki ramuan")
            input("> ")
        elif choice == "3":
            if rune > 0:
                rune -= 1
                heal(80)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki rune")
            input("> ")

        if HP <= 0:
            print(enemy + " mengalahkanmu, Hero " + name + "!")
            gris()
            fight = False
            play = False
            run = False
            print("Game Over")
            input("> ")
            quit()

        if hp <= 0:
            print("Kamu mengalahkan " + enemy + "!")
            gris()
            fight = False
            gold += g
            print("Kamu mendapatkan " + str(g) + " gold")
            if random.randint(0, 100) <= 10:
                print("Kamu mendapatkan rune!")
                rune += 1
            if random.randint(0, 100) <= 30:
                print("Kamu mendapatkan ramuan!")
                pot += 1
            input("> ")
            clear()

def battle_soldier():
    global fight, play, run, HP, pot, rune, gold

    enemy = "Tentara Bayaran"
    hp = smobs[enemy]["hp"]
    hpmax = hp
    atk = smobs[enemy]["at"]
    g = smobs[enemy]["go"]

    while fight:
        clear()
        HP_color_player = hpcolor(HP, HPMAX)
        HP_color_enemy = hpcolor(hp, hpmax)
        sisahp_bars_player = round(HP / HPMAX * hp_bars)
        losthp_bars_player = hp_bars - sisahp_bars_player
        sisahp_bars_enemy = round(hp / hpmax * hp_bars)
        losthp_bars_enemy = hp_bars - sisahp_bars_enemy
        gris()
        artprint(ascii_soldier, 0.01)
        print("Kalahkan : " + enemy + "!")
        print("Mercenary : " + soldier.name + ", Level " + str(soldier.level))
        gris()
        print(enemy + " HP : " + HP_color_enemy + str(hp) + "/" + str(hpmax) + color_default)
        print(f"|{HP_color_enemy}{sisahp_bars_enemy * sisahp_symbol}{losthp_bars_enemy * losthp_symbol}{color_default}|")
        print("Hero :", name + ", HP : " + HP_color_player + str(HP) + "/" + str(HPMAX) + color_default)
        print(f"|{HP_color_player}{sisahp_bars_player * sisahp_symbol}{losthp_bars_player * losthp_symbol}{color_default}|")
        print("Ramuan : " + str(pot))
        print("Rune : " + str(rune))
        gris()
        print("1 - Attack")
        if pot > 0:
            print("2 - Pakai Ramuan (40HP)")
        if rune > 0:
            print("3 - Pakai Rune (80HP)")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            hp -= ATK
            print("Kamu menyerang " + enemy + " dengan " + str(ATK) + " damage")
            if hp > 0:
                HP -= atk
                print("Kamu diserang " + enemy + " dengan " + str(atk) + " damage")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(40)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki ramuan")
            input("> ")
        elif choice == "3":
            if rune > 0:
                rune -= 1
                heal(80)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki rune")
            input("> ")

        if HP <= 0:
            print(enemy + " mengalahkanmu, Hero " + name + "!")
            gris()
            fight = False
            play = False
            run = False
            print("Game Over")
            quit()

        if hp <= 0:
            print("Kamu mengalahkan " + enemy + "!")
            gris()
            fight = False
            gold += g
            print("Kamu mendapatkan " + str(g) + " gold")
            if random.randint(0, 100) <= 10:
                print("Kamu mendapatkan rune!")
                rune += 1
            if random.randint(0, 100) <= 30:
                print("Kamu mendapatkan ramuan!")
                pot += 1
            input("> ")
            clear()

def battle_bandit():
    global fight, play, run, HP, pot, rune, gold

    enemy = "Bandit Perampok"
    hp = smobs[enemy]["hp"]
    hpmax = hp
    atk = smobs[enemy]["at"]
    g = smobs[enemy]["go"]

    while fight:
        clear()
        HP_color_player = hpcolor(HP, HPMAX)
        HP_color_enemy = hpcolor(hp, hpmax)
        sisahp_bars_player = round(HP / HPMAX * hp_bars)
        losthp_bars_player = hp_bars - sisahp_bars_player
        sisahp_bars_enemy = round(hp / hpmax * hp_bars)
        losthp_bars_enemy = hp_bars - sisahp_bars_enemy
        gris()
        artprint(ascii_bandit, 0.01)
        print("Kalahkan : " + enemy + "!")
        print("Bandit : " + bandit.name + ", Level " + str(bandit.level))
        gris()
        print(enemy + " HP : " + HP_color_enemy + str(hp) + "/" + str(hpmax) + color_default)
        print(f"|{HP_color_enemy}{sisahp_bars_enemy * sisahp_symbol}{losthp_bars_enemy * losthp_symbol}{color_default}|")
        print("Hero :", name + ", HP : " + HP_color_player + str(HP) + "/" + str(HPMAX) + color_default)
        print(f"|{HP_color_player}{sisahp_bars_player * sisahp_symbol}{losthp_bars_player * losthp_symbol}{color_default}|")
        print("Ramuan : " + str(pot))
        print("Rune : " + str(rune))
        gris()
        print("1 - Attack")
        if pot > 0:
            print("2 - Pakai Ramuan (40HP)")
        if rune > 0:
            print("3 - Pakai Rune (80HP)")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            hp -= ATK
            print("Kamu menyerang " + enemy + " dengan " + str(ATK) + " damage")
            if hp > 0:
                HP -= atk
                print("Kamu diserang " + enemy + " dengan " + str(atk) + " damage")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(40)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki ramuan")
            input("> ")
        elif choice == "3":
            if rune > 0:
                rune -= 1
                heal(80)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki rune")
            input("> ")

        if HP <= 0:
            print(enemy + " mengalahkanmu, Hero " + name + "!")
            gris()
            fight = False
            play = False
            run = False
            print("Game Over")
            quit()

        if hp <= 0:
            print("Kamu mengalahkan " + enemy + "!")
            gris()
            fight = False
            gold += g
            print("Kamu mendapatkan " + str(g) + " gold")
            if random.randint(0, 100) <= 10:
                print("Kamu mendapatkan rune!")
                rune += 1
            if random.randint(0, 100) <= 30:
                print("Kamu mendapatkan ramuan!")
                pot += 1
            input("> ")
            clear()
def battle():
    global fight, play, run, HP, pot, rune, gold

    enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        HP_color_player = hpcolor(HP, HPMAX)
        HP_color_enemy = hpcolor(hp, hpmax)
        sisahp_bars_player = round(HP / HPMAX * hp_bars)
        losthp_bars_player = hp_bars - sisahp_bars_player
        sisahp_bars_enemy = round(hp / hpmax * hp_bars)
        losthp_bars_enemy = hp_bars - sisahp_bars_enemy
        gris()
        artprint(mobs[enemy]["a"],0.01)
        print("Kalahkan : " + enemy + "!")
        gris()
        print(enemy + " HP : " + HP_color_enemy + str(hp) + "/" + str(hpmax) + color_default)
        print(f"|{HP_color_enemy}{sisahp_bars_enemy * sisahp_symbol}{losthp_bars_enemy * losthp_symbol}{color_default}|")
        print("Hero :", name + ", HP : " + HP_color_player + str(HP) + "/" + str(HPMAX) + color_default)
        print(f"|{HP_color_player}{sisahp_bars_player * sisahp_symbol}{losthp_bars_player * losthp_symbol}{color_default}|")
        print("Ramuan : " + str(pot))
        print("Rune : " + str(rune))
        gris()
        print("1 - Attack")
        if pot > 0:
            print("2 - Pakai Ramuan (40HP)")
        if rune > 0:
            print("3 - Pakai Rune (80HP)")
        gris()

        choice = input("#Apa Keputusanmu? : ")

        if choice == "1":
            hp -= ATK
            print("Kamu menyerang " + enemy + " dengan " + str(ATK) + " damage")
            if hp > 0:
                HP -= atk
                print("Kamu diserang " + enemy + " dengan " + str(atk) + " damage")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(40)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki ramuan")
            input("> ")
        elif choice == "3":
            if rune > 0:
                rune -= 1
                heal(80)
                HP -= atk
                print(enemy + " menyerangmu dengan " + str(atk) + " damage")
            else:
                print("Kamu tidak memiliki rune")
            input("> ")

        if HP <= 0:
            print(enemy + " mengalahkanmu, Hero " + name + "!")
            gris()
            fight = False
            play = False
            run = False
            input("> ")
            print("Game Over")

        if hp <= 0:
            print("Kamu mengalahkan " + enemy + "!")
            gris()
            fight = False
            gold += g
            print("Kamu mendapatkan " + str(g) + " gold")
            if random.randint(0, 100) <= 10:
                print("Kamu mendapatkan rune!")
                rune += 1
            if random.randint(0, 100) <= 30:
                print("Kamu mendapatkan ramuan!")
                pot += 1
            input("> ")
            clear()

class NPC:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def talk(self):
        pass

    def prints(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.01)
        print("\n")

class npc_kdesa(NPC):
    def __init__(self, name, level):
        super().__init__(name, level)

    def kdesa(self):
        clear()
        global talk, key
        while talk:
            gris()
            artprint(ascii_kdesa, 0.01)
            self.prints("Kepala Desa : Selamat datang di desa kami, petualang. " + name + " Kami sudah lama menantikan kedatanganmu.")
            gris()
            self.prints("Maaf?, tapi apa maksud Anda? Aku belum pernah datang ke desa ini sebelumnya.")
            input("> ")
            self.prints("Kepala Desa : Ah, kami sudah mendengar cerita tentangmu. kisah - kisah heroik tentang petualanganmu telah menyebar ke seluruh negeri.")
            self.prints("Kepala Desa : Seorang petualang pemberani yang telah menyelesaikan banyak tugas berbahaya. Kami sangat membutuhkan bantuanmu.")
            self.prints("Kepala Desa : Kami memiliki masalah besar yang harus diselesaikan, dan kami tidak tahu harus berbuat apa.")
            gris()
            self.prints("Bantuan? Masalah apa yang sedang desa ini hadapi?")
            input("> ")
            clear()
            artprint(ascii_kdesa, 0.005)
            gris()
            self.prints("Kepala Desa : Sebuah kutukan kuno telah menghantui desa kami. Para penduduk menderita penyakit misterius, tanaman layu, dan hewan ternak mati secara tiba-tiba.")
            print("Kepala Desa : Kami percaya kutukan ini berasal dari gua penyihir hitam ditimur gunung.")
            gris()
            self.prints("Gua penyihir hitam? Apa yang membuat Anda yakin kutukan itu berasal dari sana?")
            input("> ")
            self.prints("Kepala Desa : Beberapa penduduk desa yang berani mencoba menyelidiki gua itu, tapi tidak ada yang kembali.")
            self.prints("Kepala Desa : Hanya ada satu orang yang berhasil lolos, dan dia menceritakan tentang kekuatan jahat yang bersemayam di sana.")
            self.prints("Aku mengerti. Aku akan pergi ke gua itu dan mencari tahu apa yang sebenarnya terjadi. Tapi saya butuh informasi lebih lanjut tentang penyihir hitam itu.")
            while True:
                gris()
                self.prints("1 - Tanyakan Lokasi Goa Penyihir Hitam")
                self.prints("2 - Tanyakan Tentang Desa Ini")
                self.prints("3 - Pergi menyelidiki")
                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    gris()
                    if ATK < 30:
                        self.prints("Kepala Desa : Namanya Morthos the Shadow Weaver. Dia adalah penyihir yang sangat kuat dan jahat, Kamu Perlu Meningkatkan Kekuatan (30)")
                        key = False
                    else :
                        gris()
                        clear()
                        self.prints("Kepala Desa : Namanya Morthos the Shadow Weaver. Dia adalah penyihir yang sangat kuat dan jahat.")
                        self.prints("Kepala Desa : Dia membenci manusia dan ingin menghancurkan desa kami. Hati-hati, Hero. Morthos tidak akan mudah dikalahkan.")
                        self.prints("Kepala Desa : Goa Penyihir Hitam berada di timur desa ini, di balik gunung.")
                        key = True
                        save()
                        input("> ")
                        talk= False
                        break
                elif choice == "2":
                    gris()
                    self.prints("Kepala Desa : Desa ini adalah tempat yang damai, kami hidup berdampingan dengan alam")
                    self.prints("Kepala Desa : Kami juga memiliki toko yang menjual barang-barang yang mungkin kamu butuhkan")
                    self.prints("Kepala Desa : Jika kamu membutuhkan bantuan, jangan ragu untuk bertanya")
                    input("> ")
                    talk = False
                    clear()
                    break
                elif choice == "3":
                    self.prints("Kepala Desa : Baiklah, jangan ragu untuk datang kembali jika kau membutuhkan sesuatu")
                    input("> ")
                    talk = False
                    clear()
                    break

class npc_mayor(NPC):
    def __init__(self, name, level):
        super().__init__(name, level)

    def mayor(self):
        clear()
        global talk, key
        while talk:
            artprint(ascii_mayor, 0.01)
            gris()
            self.prints("Wali Kota : Selamat datang di kota kami, petualang. " + name + " Kami sudah lama menantikan kedatanganmu.")
            gris()
            self.prints("Maaf?, tapi apa maksud Anda? Aku belum pernah datang ke kota ini sebelumnya.")
            input("> ")
            self.prints("Wali Kota : Ah, kami sudah mendengar cerita tentangmu. kisah - kisah heroik tentang petualanganmu telah menyebar ke seluruh negeri.")
            self.prints("Wali Kota : Seorang petualang pemberani yang telah menyelesaikan banyak tugas berbahaya. Kami sangat membutuhkan bantuanmu.")
            self.prints("Wali Kota : Kami memiliki masalah besar yang harus diselesaikan, dan kami tidak tahu harus berbuat apa.")
            gris()
            self.prints("Bantuan? Masalah apa yang sedang kota ini hadapi?")
            input("> ")
            clear()
            gris()
            artprint(ascii_mayor, 0.005)
            self.prints("Wali Kota : Sebuah kutukan kuno telah menghantui kota kami. Para penduduk menderita penyakit misterius, tanaman layu, dan hewan ternak mati secara tiba-tiba.")
            self.prints("Wali Kota : Kami percaya kutukan ini berasal dari gua penyihir hitam ditimur gunung.")
            gris()
            self.prints("Gua penyihir hitam? Apa yang membuat Anda yakin kutukan itu berasal dari sana?")
            input("> ")
            self.prints("Wali Kota : Beberapa penduduk kota yang berani mencoba menyelidiki gua itu, tapi tidak ada yang kembali.")
            self.prints("Wali Kota : Hanya ada satu orang yang berhasil lolos, dan dia menceritakan tentang kekuatan jahat yang bersemayam di sana.")
            self.prints("Aku mengerti. Aku akan pergi ke gua itu dan mencari tahu apa yang sebenarnya terjadi. Tapi saya butuh informasi lebih lanjut tentang penyihir hitam itu.")
            while True:
                gris()
                self.prints("1 - Tanyakan Lokasi Goa Penyihir Hitam")
                self.prints("2 - Tanyakan Tentang Kota Ini")
                self.prints("3 - Pergi menyelidiki")
                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    gris()
                    if ATK < 30:
                        self.prints("Wali Kota : Namanya Morthos the Shadow Weaver. Dia adalah penyihir yang sangat kuat dan jahat, Kamu Perlu Meningkatkan Kekuatan (30)")
                        key = False
                    else :
                        gris()
                        clear()
                        self.prints("Wali Kota : Namanya Morthos the Shadow Weaver. Dia adalah penyihir yang sangat kuat dan jahat.")
                        self.prints("Wali Kota : Dia membenci manusia dan ingin menghancurkan kota kami. Hati-hati, Hero. Morthos tidak akan mudah dikalahkan.")
                        self.prints("Wali Kota : Goa Penyihir Hitam berada di timur kota ini, di balik gunung.")
                        key = True
                        save()
                        input("> ")
                        talk= False
                        break
                elif choice == "2":
                    gris()
                    self.prints("Wali Kota : Kota ini adalah tempat yang damai, kami hidup berdampingan dengan alam")
                    self.prints("Wali Kota : Kami juga memiliki toko yang menjual barang-barang yang mungkin kamu butuhkan")
                    self.prints("Wali Kota : Jika kamu membutuhkan bantuan, jangan ragu untuk bertanya")
                    input("> ")
                    talk = False
                    clear()
                    break
                elif choice == "3":
                    self.prints("Wali Kota : Baiklah, jangan ragu untuk datang kembali jika kau membutuhkan sesuatu")
                    input("> ")
                    talk = False
                    clear()
                    break

class npc_wizard(NPC):
    def __init__(self, name, level):
        super().__init__(name, level)
    def wizard(self):
        clear()
        global talk, fight, gold, pot, rune
        while talk:
            artprint(ascii_wizard, 0.01)
            gris()
            self.prints("(Mendekati sebuah gubuk tua di tengah hutan) Permisi! Ada orang di dalam?")
            self.prints("(Muncul dari balik pintu, mengenakan jubah lusuh dan memegang tongkat kayu)")
            self.prints("Penyihir Misterius : Siapa yang berani mengganggu ketenanganku? Ah, seorang petualang rupanya. Apa yang membawamu kemari?")
            input("> ")
            gris()
            self.prints("Aku "+ name + " dalam perjalanan dan tersesat di hutan ini. Apakah Anda bisa membantu menunjukkan jalan keluar?")
            self.prints("Penyihir Misterius : Hmm, mungkin saja. Tapi tidak ada yang gratis di dunia ini, anak muda.")
            self.prints("Aku seorang penyihir, dan aku punya barang-barang yang mungkin kamu butuhkan. Tapi tentu saja, dengan harga yang pantas.")
            input("> ")
            gris()
            self.prints("Penyihir Misterius : Ramuan penyembuh, mantra pelindung, jimat keberuntungan... Apa pun yang kamu inginkan, aku punya. Tentu saja, dengan harga yang pantas.")
            self.prints("Oberion Wise Wizard : Orang-orang menyebutku Oberoin Thistlewood, tapi kamu bisa memanggilku Oberion. Jadi, katakan padaku, petualang muda, apa yang hatimu inginkan?")
            input("> ")
            gris()
            self.prints("Oberion Wise Wizard : Selamat datang, Petualang "+ name + " Apakah kau ingin membeli ramuan atau rune?")
            gris()
            print("1 - Beli Ramuan (15 Gold)")
            print("2 - Beli Rune (25 Gold)")
            print("3 - Tanyakan tentang masa lalunya")
            print("4 - Tidak, Terima kasih")
            choice = input("#Apa Keputusanmu? : ")
            if choice == "1":
                if gold >= 15:
                    gold -= 15
                    pot += 1
                    print("Kamu mendapatkan ramuan!")
                    input("> ")
                    talk = False
                else:
                    print("Gold tidak cukup")
                    input("> ")
            elif choice == "2":
                if gold >= 25:
                    gold -= 25
                    rune += 1
                    print("Kamu mendapatkan rune!")
                    input("> ")
                    talk = False
                else:
                    print("Gold tidak cukup")
                    input("> ")
            elif choice == "3":
                clear()
                artprint(ascii_wizard, 0.005)
                self.prints("Hmmm....Oberion Thistlewood, Aku pernah mendengar nama itu... (Mencoba Mengingat) Bukankah Twistlewood dulu penyihir kerajaan yang membelot, Apa itu kau Sir Oberion?")
                self.prints("Oberion Wise Wizard : (Tatapannya menajam) Kenangan masa lalu lebih baik dikubur dalam-dalam, anak muda. Apa yang sudah berlalu biarlah berlalu.")
                self.prints("1 - Maaf, aku tidak bermaksud mengganggu")
                self.prints("2 - Aku hanya ingin tahu lebih banyak tentang Anda (Memicu Konflik), Kenapa anda meninggalkan istana kerajaan?")
                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    self.prints("Oberion Wise Wizard : Baiklah, jangan ragu untuk datang kembali jika kau membutuhkan sesuatu")
                    input("> ")
                    clear()
                    talk = False
                elif choice == "2":
                    clear()
                    artprint(ascii_wizard, 0.005)
                    self.prints("Oberion Wise Wizard :(Mulai kesal) Hahaha, kau berani sekali anak muda, Apa kau disewa oleh anjing - anjing istana itu?. Tapi kau tidak akan mendapatkan apa pun dari ku!")
                    self.prints("Rasa ingin tahumu terlalu besar, anak muda. Beberapa hal lebih baik tidak diungkit kembali. Sekarang pergilah!")
                    self.prints("1 - Maafkan Aku, Sir Oberion. aku tidak bermaksud menyinggung perasaan Anda....  hanya penasara")
                    self.prints("2 - Kenapa Anda begitu marah? Apakah Anda menyembunyikan yang mengancam kerajaan?")
                    choice = input("#Apa Keputusanmu? : ")
                    if choice == "1":
                        self.prints("Oberion Wise Wizard : Baiklah, percakapan kita berhenti disini, sekarangg pergilah !!!")
                        input("> ")
                        clear()
                        talk = False
                    elif choice == "2":
                        self.prints("Oberion Wise Wizard : (Mengamuk, Membanting tongkatnya ke lantai, membuat gubuk bergetar) CUKUP! Kau sudah melewati batas, anak muda! Masa laluku bukan urusanmu! (Pertempuran dimulai)")
                        fight = True
                        battle_wizard()
                        talk = False
            elif choice == "4":
                self.prints("Oberion : Baiklah, jangan ragu untuk datang kembali jika kau membutuhkan sesuatu")
                input("> ")
                talk = False

class npc_bandit(NPC):
    def __init__(self, name, level):
        super().__init__(name, level)
    def bandit(self):
        clear()
        global talk, fight, gold
        while talk:
            gris()
            artprint(ascii_bandit, 0.01)
            self.prints("(Seseorang berteriak), Bandit : Siapa kau?!! Apa yang kau lakukan di wilayah kami?")
            self.prints("Bandit : Wah, wah, lihat siapa yang kita temui di sini. malang nasibmu bertemu denganku Ronan Razoe, petualang!")
            self.prints("Razoe The Bandit : Seorang petualang kaya raya, ya? Bagaimana kalau kita buat kesepakatan? Serahkan hartamu, dan aku jamin perjalananmu akan aman.")
            gris()
            self.prints("1 - Tidak semudah itu! Aku tidak akan menyerahkan hartaku tanpa perlawanan! (Memicu pertempuran)")
            self.prints("2 - Berapa yang kau inginkan? Mungkin kita bisa mencapai kesepakatan. (Mencoba bernegosiasi)")
            self.prints("3 - Aku tidak punya harta yang berharga. Pergilah! (Mencoba menggertak)")
            choice = input("#Apa Keputusanmu? : ")
            if choice == "1":
                gris()
                self.prints("Razoe The Bandit : Oh, jadi mau main kasar? Baiklah, kalau itu maumu! (Pertempuran dimulai)")
                input("> ")
                fight = True
                battle_bandit()
                talk = False
            elif choice == "2":
                clear()
                artprint(ascii_bandit, 0.005)
                gris()
                self.prints("Razoe The Bandit : Hmm, menarik. Aku suka orang yang bisa diajak berbisnis. Bagaimana kalau setengah dari hartamu? Itu harga yang murah untuk nyawamu, bukan?")
                gris()
                self.prints("1 - Setengah terlalu banyak! Bagaimana kalau seperempat saja? (Negosiasi lebih lanjut)")
                self.prints("2 - Baiklah, ini setengah dari hartaku. Tapi jangan coba-coba macam-macam lagi! (Menyetujui kesepakatan)")
                self.prints("3 - Tidak, aku tidak akan memberikan apapun! (Menolak dan bersiap untuk pertempuran)")
                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    clear()
                    artprint(ascii_bandit, 0.005)
                    gris()
                    self.prints("Razoe The Bandit : Seperempat? Kau ini lucu juga. Tapi baiklah, aku menghargai usahamu. Bagaimana kalau sepertiga? Itu sudah sangat murah, mengingat reputasi kami di daerah ini")
                    gris()
                    self.prints("1 - Seperempat atau tidak sama sekali! (Bersikeras pada tawaran sebelumnya)")
                    self.prints("2 - Baiklah, sepertiga. Tapi ini terakhir kalinya aku berurusan denganmu. (Menyetujui tawaran bandit)")
                    choice = input("#Apa Keputusanmu? : ")
                    if choice == "1":
                        self.prints("Razoe The Bandit : Hmm... Kau keras kepala juga, ya. Tapi aku suka semangatmu. Baiklah, seperempat. Tapi ingat, lain kali jangan coba-coba menawar lagi! (Bandit mengambil seperempat harta pemain)")
                        gold = gold // 4
                        input("> ")
                        talk = False
                    elif choice == "2":
                        self.prints("Razoe The Bandit : Hahaha! Keputusan yang bijak. Percayalah, kau tidak akan menyesalinya. Selamat jalan, petualang! (Bandit mengambil sepertiga harta pemain)")
                        gold = gold // 3
                        input("> ")
                        talk = False
                elif choice == "2":
                    self.prints("Razoe The Bandit : Hahaha! Keputusan yang bijak. Percayalah, kau tidak akan menyesalinya. Selamat jalan, petualang! (Bandit mengambil setengah harta pemain)")
                    gold = gold // 2
                    input("> ")
                    talk = False
                elif choice == "3":
                    self.prints("Razoe The Bandit : Oh, jadi mau main kasar? Baiklah, kalau itu maumu! (Pertempuran dimulai)")
                    input("> ")
                    fight = True
                    battle_bandit()
                    talk = False
            elif choice == "3":
                clear()
                artprint(ascii_bandit, 0.005)
                gris()
                self.prints("Razoe The Bandit : Oh ya? Kita lihat saja nanti. Anak buahku akan menggeledahmu sampai ketemu! (Bandit memanggil anak buahnya untuk menggeledah pemain)")
                gris()
                self.prints("1 - Baiklah, baiklah, ini sedikit koin. Jangan ambil semuanya! (Menyerahkan sepertiga harta gold)")
                self.prints("2 - Aku tidak punya apa-apa! Pergilah! (Menolak dan bersiap untuk pertempuran)")
                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    self.prints("Razoe The Bandit : Hahaha! Kau ini lucu juga, ya. Tapi baiklah, aku menghargai usahamu. Bagaimana kalau setengah? Itu sudah sangat murah, mengingat reputasi kami di daerah ini")
                    self.prints("1 - Sepertiga atau tidak sama sekali! (Bersikeras pada tawaran sebelumnya)")
                    self.prints("2 - Baiklah, setengah. Tapi ini terakhir kalinya aku bertemu denganmu. (Menyetujui tawaran bandit)")
                    choice = input("#Apa Keputusanmu? : ")
                    if choice == "1":
                        self.prints("Razoe The Bandit : Hmm... Kau keras kepala juga, ya. Tapi aku suka semangatmu. Baiklah, setengah. Tapi ingat, lain kali jangan coba-coba menawar lagi! (Bandit mengambil setengah harta pemain)")
                        gold = gold // 3
                        input("> ")
                        talk = False
                    elif choice == "2":
                        self.prints("Razoe The Bandit : Hahaha! Keputusan yang bijak. Percayalah, kau tidak akan menyesalinya. Selamat jalan, petualang! (Bandit mengambil setengah harta pemain)")
                        gold = gold // 2
                        input("> ")
                        talk = False
                elif choice == "2":
                    self.prints("Razoe The Bandit: Oh, jadi mau main kasar? Baiklah, kalau itu maumu! (Pertempuran dimulai)")
                    input("> ")
                    fight = True
                    battle_bandit()
                    talk = False

class npc_soldier(NPC):
    def __init__(self, name, level):
        super().__init__(name, level)
    def soldier(self):
        clear()
        global talk, fight
        while talk:
            gris()
            artprint(ascii_soldier, 0.01)
            self.prints("(Seseorang Muncul Dari Belakang) Tangan di atas kepala! Jangan macam-macam atau kalian akan menyesal!")
            self.prints("1 - Tenang Kawan, kami tidak mencari masalah, (Mencoba meredakan situasi)")
            self.prints("2 - Pergi (Mencoba kabur)")

            choice = input("#Apa Keputusanmu? : ")
            if choice == "1":
                gris()
                self.prints("Mercenary : Oh ya?, Aku bukan Kawanmu, Lalu apa yang kau lakukan di tempat terpencil seperti ini? Jangan coba-coba membodohiku!")
                self.prints("1 - Tanyakan tentang gua yang ada di sebelah timur")
                self.prints("2 - Tanyakan Tentang dirinya, Apa yang sedang dia lakukan di hutan penuh monster ini, (Mencoba mencari informasi)")
                self.prints("3 - Pergi, aku tidak ingin masalah")
                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    gris()
                    self.prints("Mercenary : Goa? Aku tidak tahu apa yang ada di sana, tapi aku mendengar cerita tentang monster yang mengerikan di dalamnya")
                    self.prints("Mercenary : Kau tidak akan bisa melewatinya, tidak dengan kekuatanmu yang sekarang")
                    self.prints("1 - Monster ?! Apa yang kau maksud? dan siapa dirimu? (Mencoba mendapatkan informasi lebih lanjut)")
                    self.prints("2 - Terima kasih atas informasinya")
                    choice = input("#Apa Keputusanmu? : ")
                    if choice == "1":
                        self.prints("Mercenary : Aku Corvus Raveneye Tentara Bayaran Kerajaan Alfheim, saat aku menjalani misi, aku mendengar rumor tentang penyihir hitam yang memancing monster ke dalam gua itu")
                        input("> ")
                        self.prints("Sir Corvus : Jadi, apa yang kau lakukan di sini? (Mencoba mengintimidasi)")
                        self.prints("1 - Aku hanya seorang petualang yang tersesat, aku tidak mencari masalah")
                        self.prints("2 - Aku mencari petunjuk untuk melanjutkan perjalanan")
                        choice = input("#Apa Keputusanmu? : ")
                        if choice == "1":
                            self.prints("Sir Corvus : Baiklah, aku rasa perckapan kita berakhir disini.")
                            input("> ")
                            talk = False
                            clear()
                        elif choice == "2":
                            self.prints("Sir Corvus : Petunjuk? Tidak ada petunjuk dengan kekuatanmu saat ini!!?")
                            input("> ")
                            talk = False
                            clear()
                elif choice == "2":
                    self.prints("Mercenary : Corvus Raveneye, Tentara Bayaran Kerajaan Alfheim, Aku sedang dalam misi melacak penyihir pembelot Twistlewood")
                    self.prints("Sir Corvus : Tapi sepertinya aku malah menemukan petualang yang tersesat di hutan ini")
                    self.prints("1 - Penyihir pembelot Twistlewood? Apa yang dia lakukan?")
                    self.prints("2 - Terima kasih atas informasinya, selamat tinggal")
                    choice = input("#Apa Keputusanmu? : ")
                    if choice == "1":
                        self.prints("Sir Corvus : Twistlewood adalah penyihir yang dulu setia pada kerajaan, tapi dia membelot dan kabur ke hutan ini")
                        self.prints("Sir Corvus : Aku mendengar rumor bahwa dia yang membunuh pangeran Gareth, dan sekarang dia bersembunyi di hutan ini")
                        self.prints("Sir Corvus : Walaupun tidak ada yang menyukai pangeran Gareth, tetapi dia tetap seorang pangeran")
                        self.prints("Sir Corvus : Aku akan menangkapnya, dan membawanya ke pengadilan untuk dihukum")
                        input("> ")
                        self.prints("Sir Corvus : Baiklah kau sudah mendengar terlalu banyak informasi, kurasa percakapan kita berakhir disini!")
                        input("> ")
                        talk = False
                        clear()
                    elif choice == "2":
                        self.prints("Sir Corvus : Baiklah, jangan lupa untuk berhati-hati di hutan ini")
                        input("> ")
                        talk = False
                        clear()
                elif choice == "3":
                    self.prints("Mercenary : Baiklah, jangan coba-coba kembali ke tempat ini")
                    input("> ")
                    talk = False
                    clear()
            elif choice == "2":
                fight = True
                battle_soldier()
                talk = False

class npc_knight(NPC):
    def __init__(self, name, level):
        super().__init__(name, level)
    def knight(self):
        clear()
        global talk, key
        while talk:
            artprint(ascii_knight, 0.01)
            self.prints("(Seseorang sedang beristirahat diatas batu, Seorang knight yang cukup tua)")
            self.prints("(Kamu tidak sengaja membangunkannya)")
            self.prints("Knight Tua : Ah, seorang petualang muda. Apakah engkau mencari petunjuk, atau hanya tersesat di belantara ini?")
            input("> ")
            self.prints("Knight Tua : Aku Sir Ronal dari Kerajaan Alfheim, Boleh kutahu namamu, petualang?")
            self.prints("Knight Tua : Aku sudah lama tidak melihat wajah baru di sini. Apa yang membawamu ke tempat terpencil ini? Hero " + name)
            while True:
                gris()
                self.prints("1 - Tanya Petunjuk tentang goa d timur")
                self.prints("2 - Tanya Tujuannya di sini")
                self.prints("3 - Tanya Tentang Dunia")
                self.prints("4 - Pergi")

                choice = input("#Apa Keputusanmu? : ")
                if choice == "1":
                    gris()
                    if ATK < 30:
                        self.prints("Sir Ronal : Petualang muda, kau harus meningkatkan kekuatanmu (30) sebelum melanjutkan perjalananmu")
                        key = False
                    else:
                        clear()
                        artprint(ascii_knight, 0.005)
                        self.prints("Sir Ronal : Petunjuk? Di balik gunung itu, terdapat sebuah gua yang menyimpan rahasia kuno, namun ada penyihir hitam disana, Mungkin engkau tertarik untuk mencarinya?, Hero " + name)
                        self.prints("Sir Ronal : Dengan Kekuatanmu saat ini, kurasa kamu bisa mengalahkannya")
                        self.prints("Sir Ronal : Aku tidak bisa membantu lebih dari ini, semoga kau selamat di perjalananmu")
                        key = True
                        save()
                        talk = False
                        break
                if choice == "2":
                    clear()
                    artprint(ascii_knight, 0.005)
                    self.prints("Sir Ronal : Aku sedang dalam perjalanan ke desa terdekat, ada laporan tentang penyakit yang mematikan disana")
                    self.prints("Sir Ronal : Aku akan mencari tahu apa yang terjadi, dan mencoba menyelamatkan mereka")
                    input("> ")
                    self.prints("Sir Ronal : Baik jika tidak ada hal lain yang ingin kau tanyakan, aku akan melanjutkan perjalananku, farewell hero " + name)
                    input("> ")
                    talk = False
                    clear()
                    break
                elif choice == "3":
                    clear()
                    artprint(ascii_knight, 0.005)
                    self.prints("Sir Ronal : Dunia ini adalah tempat yang penuh dengan misteri dan bahaya. Hati-hati, Hero " + name)
                    self.prints("Sir Ronal : Semakin sedikit yang kau tau semakin baik, ingat kata kataku hero " + name)
                    input("> ")
                    self.prints("Sir Ronal : Baik jika tidak ada hal lain yang ingin kau tanyakan, aku akan melanjutkan perjalananku, farewell hero " + name)
                    input("> ")
                    talk = False
                    clear()
                    break
                elif choice == "4":
                    talk = False
                    clear()
                    break

game_map = Map(60, 20, player)
previous_x_loc = x_loc
previous_y_loc = y_loc
move = ''

def move_marker(move, marker_x, marker_y):
    if move == 'w' and marker_y > 0:
        marker_y -= 1
    elif move == 's' and marker_y < len(game_map.map_data) - 1:
        marker_y += 1
    elif move == 'a' and marker_x > 0:
        marker_x -= 1
    elif move == 'd' and marker_x < len(game_map.map_data[0]) - 1:
        marker_x += 1
    return marker_x, marker_y

while run:
    while menu:
        clear()
        gris()
        artprint(ascii_game, 0.05)
        print(ANSI_CYAN + "Selamat Datang Di" + ANSI_RESET + ANSI_YELLOW + " Fable" + ANSI_RESET + ANSI_GREEN + " tales !" + ANSI_RESET)
        print(ANSI_CYAN,"1. PLAY", ANSI_RESET)
        print(ANSI_GREEN,"2. LOAD GAME",ANSI_RESET)
        print(ANSI_YELLOW,"3. TUTORIAL",ANSI_RESET)
        print(ANSI_RED,"4. EXIT",ANSI_RESET)
        print(ANSI_YELLOW,"Bukalah Tutorial Game, Hero!", ANSI_RESET)
        print(ANSI_GREEN,"Simple Text game for Proyek Akhir PBO", ANSI_RESET)
        gris()


        if tutorial:
            print("Ingat semua pilihan anda akan berdampak pada cerita yang akan anda alami")
            print("Pilihlah dengan bijak")
            print("\n")
            print("Jika Terminal > maka input ENTER untuk melanjutkan")
            print("Jika Terminal # maka input keputusanmu untuk memilih")
            print("Tips : Kamu akan memperoleh HP tambahan jika heal di luar pertempuran")
            print("Kamu akan bertemu musuh saat menjelajadi peta game")
            print("Hati - hati saat bertemu bandit, setiap pilihanmu akan berdampak pada gold yang telah kamu kumpulkan")
            print("Apalagi ya? ~ Haq")
            tutorial = False
            choice = ""
            input("> ")
            clear()
        else:
            choice = input("# Apa Keputusanmu? : ")

        if choice == "1":
            clear()
            name = input("Nama Adalah Takdir, Hero , Pilihlah Dengan Bijak! : ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = (load_list[0][:-1])
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    rune = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x_loc = int(load_list[6][:-1])
                    y_loc = int(load_list[7][:-1])
                    key = load_list[8][:-1] == "True"
                    clear()
                    artprint(ascii_hero, 0.05)
                    print(ANSI_YELLOW,"Senang melihatmu kembali, Hero " + name, ANSI_RESET)
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("File save rusak/corrupt")
                    input("> ")
            except OSError:
                print("Tidak ada file save")
                input("> ")

        elif choice == "3":
            tutorial = True
        elif choice == "4":
            quit()

    while play:
        save()

        if not tempshield:
            if biom[map_data[y_loc][x_loc]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if play:
            gris()
            sisahp_bars = round(HP / HPMAX * hp_bars)
            losthp_bars = hp_bars - sisahp_bars
            artprint(biom[map_data[y_loc][x_loc]]["a"], 0.05)
            print(ANSI_GREEN,"Lokasi : " + biom[map_data[y_loc][x_loc]]["t"],ANSI_RESET)
            gris()
            print("Nama Hero : ", name )
            HP_color = hpcolor(HP, HPMAX)
            print("HP : " + HP_color + str(HP) + "/" + str(HPMAX) + color_default)
            print(f"|{HP_color}{sisahp_bars * sisahp_symbol}{losthp_bars * losthp_symbol}{color_default}|")
            print(ANSI_RED,"Attack : " + str(ATK), ANSI_RESET)
            print(color_blue3,"Potion : " + str(pot), color_default)
            print(ANSI_CYAN,"Rune : " + str(rune),ANSI_RESET)
            print(color_brown,"Gold : " + str(gold),color_default)
            print("Koordiant : x,y ", x_loc, y_loc)
            gris()
            print(ANSI_RED,"0 - SAVE GAME DAN KEMBALI KE MENU",ANSI_RESET)
            if y_loc > 0:
                print(" 1 - Berjalan Ke Utara")
            if x_loc < x_loc_len:
                print(" 2 - Berjalan Ke Timur")
            if y_loc < y_loc_len:
                print(" 3 - Berjalan Ke Selatan")
            if x_loc > 0:
                print(" 4 - Berjalan Ke Barat")
            if pot > 0:
                print(color_blue3,"5 - Pakai Ramuan (100HP)",color_default)
            if rune > 0:
                print(ANSI_CYAN,"6 - Pakai Rune (200HP)",ANSI_RESET)
            if map_data[y_loc][x_loc] == "Toko Misterius" or map_data[y_loc][x_loc] == "Kepala Desa" or map_data[y_loc][x_loc] == "Wali Kota" or map_data[y_loc][x_loc] == "Gua" or map_data[y_loc][x_loc] == "Old Knight" or map_data[y_loc][x_loc] == "Bandit Perampok" or map_data[y_loc][x_loc] == "Penyihir Tua" or map_data[y_loc][x_loc] == "Tentara Bayaran":
                print(ANSI_YELLOW,"7 - Interaksi", ANSI_RESET)
            print(ANSI_GREEN,"M - Untuk Menjelajahi Area Game Map", ANSI_RESET)
            if x_loc != previous_x_loc or y_loc != previous_y_loc:
                game_map = Map(60, 20, player)
                previous_x_loc = x_loc
                previous_y_loc = y_loc
            gris()

            dest = input("Apa Keputusanmu? : ")

            if dest == "0":
                menu = True
                play = False
                save()
            elif dest == "1":
                if y_loc > 0:
                    y_loc -= 1
                    tempshield = False
                    clear()
            elif dest == "2":
                if x_loc < x_loc_len:
                    x_loc += 1
                    tempshield = False
                    clear()
            elif dest == "3":
                if y_loc < y_loc_len:
                    y_loc += 1
                    tempshield = False
                    clear()
            elif dest == "4":
                if x_loc > 0:
                    x_loc -= 1
                    tempshield = False
                    clear()
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(100)
                else:
                    print("Kamu tidak memiliki ramuan")
                input("> ")
                tempshield = True
            elif dest == "6":
                if rune > 0:
                    rune -= 1
                    heal(200)
                else:
                    print("Kamu tidak memiliki rune")
                input("> ")
                tempshield = True
            elif dest == "7":
                if map_data[y_loc][x_loc] == "Toko Misterius":
                    buy = True
                    shop()
                elif map_data[y_loc][x_loc] == "Kepala Desa":
                    talk = True
                    kdesa = npc_kdesa('Kepala Desa', 7)
                    npc_kdesa.kdesa(self=kdesa)
                elif map_data[y_loc][x_loc] == "Wali Kota":
                    talk = True
                    mayor = npc_mayor('Walikota', 15)
                    npc_mayor.mayor(self=mayor)
                elif map_data[y_loc][x_loc] == "Gua":
                    boss = True
                    finalcave()
                elif map_data[y_loc][x_loc] == "Old Knight":
                    talk = True
                    knight = npc_knight('Sir Ronal', 65)
                    npc_knight.knight(self=knight)
                elif map_data[y_loc][x_loc] == "Bandit Perampok":
                    talk = True
                    bandit = npc_bandit('Ronan Razoe',27)
                    npc_bandit.bandit(self=bandit)
                elif map_data[y_loc][x_loc] == "Penyihir Tua":
                    talk = True
                    wizard = npc_wizard('Oberion Thistlewood', 97)
                    npc_wizard.wizard(self=wizard)
                elif map_data[y_loc][x_loc] == "Tentara Bayaran":
                    talk = True
                    soldier = npc_soldier('Corvus Raveneye',47)
                    npc_soldier.soldier(self=soldier)


            elif dest.upper() == "M":
                marker_x, marker_y = Map.load_player_position()
                while True:
                    clear()
                    game_map.display_map(marker_x, marker_y)
                    print(ANSI_YELLOW,"Simbol . adalah dataran", ANSI_RESET)
                    print(ANSI_RED, "Simbol X adalah Player", ANSI_RESET)
                    print(ANSI_GREEN, "Simbol 8 adalah Hutan", ANSI_RESET)
                    print(ANSI_GREEN, "Simbol Y adalah Pohon", ANSI_RESET)
                    print(ANSI_CYAN, "Simbol ~ adalah Perairan", ANSI_RESET)
                    print(ANSI_WHITE, "Simbol A adalah Bukit/Pegunungan", ANSI_RESET)
                    print(ANSI_MAGENTA,"Simbol T adalah Kota", ANSI_RESET)
                    print(ANSI_YELLOW,"Simbol D adalah Desa", ANSI_RESET)
                    print("\n")
                    print("Input key untuk menjelajahi area map")
                    print("[W] - ATAS")
                    print("[S] - BAWAH")
                    print("[A] - KIRI")
                    print("[D] - KANAN")
                    print("Input 'c' Untuk Menutup Map Dan melanjutkan pengembaraanmu.")
                    move = input("Input (w/a/s/d) : ")
                    if move in ['w', 's', 'a', 'd']:
                        if random.randint(0, 100) <= 30:
                            fight = True
                            battle()
                        marker_x, marker_y = move_marker(move, marker_x, marker_y)
                        game_map.update_player_pos(marker_x, marker_y)
                    elif move == 'c':
                        Map.save_player_position(marker_x, marker_y)
                        break
            else:
                tempshield = True


