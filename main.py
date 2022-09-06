# William Caravello POGO
from PIL import Image, ImageGrab
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import math

mouse = MouseController()
keyboard = KeyboardController()
search_string = '3*&!costume&!shiny&!lucky&!legendary&!mythical'
# search_string = 'Skrelp'
# change  if pogo is in a diffent spot on screen X,Y on top left corner
x_start = 700
y_start = 493

# x_start = 570
# y_start = 40

num_star = 0


# temp = False
# apprase = True


def screenGrab(apprase):
    star = x, y = 383, 125
    attack = x, y = 172, 667
    defense = x, y = 172, 706
    hit_points = x, y = 172, 749
    loop_num = 5
    att, deff, hp = [0, 0, 0]
    # att_save, deff_save, hp_save = [0, 0, 0]
    st_save = [0, 0, 0]
    att_save = [0, 0, 0]
    deff_save = [0, 0, 0]
    hp_save = [0, 0, 0]
    time.sleep(1)
    if apprase == True:
        star_check()
        time.sleep(2)

    for i in range(loop_num):
        # im2 = ImageGrab.grab(bbox=(x_start + 1, y_start + 1, x_start + 426, y_start + 981))
        im2 = ImageGrab.grab(bbox=(x_start + 1, y_start + 1, x_start + 426, y_start + 981))
        # im2.show()
        # im2.save("M:\PoGo_python\prt_sc\\" + str(int(time.time())) + ".jpg")
        # exit()
        if (apprase == False):
            st = list(im2.getpixel(star))
        else:
            att = list(im2.getpixel(attack))
            deff = list(im2.getpixel(defense))
            hp = list(im2.getpixel(hit_points))
        print('screenshot ' + str(i))
        if (apprase == False):
            print(st)
        else:
            print(att)
            print(deff)
            print(hp)

        for a in range(3):
            # print(a)
            # print(att[a])
            if (apprase == False):
                st_save[a] += st[a]
            else:
                att_save[a] += att[a]
                deff_save[a] += deff[a]
                hp_save[a] += hp[a]

    # att = att / loop_num
    for b in range(3):
        # print(a)
        # print(att[a])
        if (apprase == False):
            st_save[b] /= loop_num
        else:
            att_save[b] /= loop_num
            deff_save[b] /= loop_num
            hp_save[b] /= loop_num

    print("Star: " + str(st_save))
    if (st_save[0] < 256 and st_save[1] < 195 and st_save[2] < 15 and
            st_save[0] > 245 and st_save[1] > 180 and st_save[2] > 0):
        print('will not appraise')
        save = False
    else:
        save = True
    if (apprase == True):
        print("attack: " + str(att_save))
        if (att_save[0] < 255 and att_save[1] < 155 and att_save[2] < 25 and
                att_save[0] > 245 and att_save[1] > 145 and att_save[2] > 15):
            print('attack > 13')
            a_save = True
        elif (att_save[0] < 240 and att_save[1] < 145 and att_save[2] < 125 and
              att_save[0] > 230 and att_save[1] > 135 and att_save[2] > 110):
            print('attack = 15')
            a_save = True
        else:
            print('attack < 13')
            a_save = False

        print("defense: " + str(deff_save))
        if (deff_save[0] < 255 and deff_save[1] < 155 and deff_save[2] < 25 and
                deff_save[0] > 245 and deff_save[1] > 145 and deff_save[2] > 15):
            print('defense > 13')
            d_save = True
        elif (deff_save[0] < 240 and deff_save[1] < 145 and deff_save[2] < 125 and
              deff_save[0] > 230 and deff_save[1] > 135 and deff_save[2] > 110):
            print('defense = 15')
            d_save = True
        else:
            print('defense < 13')
            d_save = False

        print("hp: " + str(hp_save))
        if (hp_save[0] < 255 and hp_save[1] < 155 and hp_save[2] < 25 and
                hp_save[0] > 245 and hp_save[1] > 145 and hp_save[2] > 15):
            print('HP > 13')
            h_save = True
        elif (hp_save[0] < 240 and hp_save[1] < 145 and hp_save[2] < 125 and
              hp_save[0] > 230 and hp_save[1] > 135 and hp_save[2] > 110):
            print('HP = 15')
            h_save = True
        else:
            print('hp < 13')
            h_save = False

        if a_save == True and d_save == True and h_save == True:
            save = True
        else:
            save = False

    return save


def get_cords():
    print(mouse.position)
    # pokeball click 737, 705
    # pokemon click 631, 662
    # serch type 724, 192


def start():
    mouse.position = (729, 714)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.move(-92, -70)
    mouse.click(Button.left, 1)
    mouse.move(+92, -460)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)

    for c in range(len(search_string)):
        keyboard.press(search_string[c])
        keyboard.release(search_string[c])
    time.sleep(1)
    mouse.move(-105, 115)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.click(Button.left, 1)

    # return move_on
    # end of start


def star_check():
    print('star check')
    mouse.position = (729, 714)
    time.sleep(1)
    mouse.move(120, 0)
    time.sleep(1)
    mouse.click(Button.left, 1)
    mouse.move(0, -120)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    # screenGrab(True)


def stat_check():
    print('stat check')


def save(num_star=None):
    print('save this pokemon')
    mouse.position = (729, 714)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.move(135, -580)
    mouse.click(Button.left, 1)


def delete():
    print('delete this pokemon')
    mouse.position = (729, 714)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.move(120, 0)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.move(0, -70)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.move(-120, -170)
    time.sleep(1)
    mouse.click(Button.left, 1)


def next():
    print('on to the next')
    mouse.position = (729, 714)
    # mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.move(120, -50)
    mouse.press(Button.left)
    for f in range(3):
        time.sleep(.1)
        mouse.move(-20, 0)
    mouse.release(Button.left)


def reselect(n_s):
    print('reselect the next pokemon')
    po_x = [614, 725, 834, 614, 725, 834, 614, 725, 834, 614, 725, 834]
    po_y = [294, 294, 294, 405, 405, 405, 546, 546, 546, 661, 661, 661]
    remader = math.remainder(n_s, 12)
    scroll = n_s / 12
    print(int(scroll))
    print(remader)

    for t in range(int(scroll)):
        mouse.position = (729, 670)
        mouse.press(Button.left)
        for p in range(25):
            time.sleep(.1)
            mouse.move(0, -20)
        mouse.release(Button.left)
        time.sleep(1)
        n_s -= 12
    mouse.position = (po_x[int(remader) - 1], po_y[int(remader) - 1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
    return n_s


#############################################

time.sleep(5)
get_cords()
exit()
#start()

for g in range(1000):
    time.sleep(2)
    move_on = screenGrab(False)
    if (move_on == True):
        keep = screenGrab(True)
        if keep == True:
            save()
            num_star += 1
            next()
            time.sleep(1)
        else:
            delete()
            time.sleep(2)
            num_star = reselect(num_star)
            time.sleep(1)
    else:
        num_star += 1
        next()