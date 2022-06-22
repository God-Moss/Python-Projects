import turtle
import random
t = turtle.Pen()
t.ht()
t.color("orange", "black")
t.width(7)
t.speed(10)
t.begin_fill()
t.up()
t.right(90)
t.forward(300)
t.right(90)
t.down()
t.forward(350)
t.right(90)
t.forward(600)
t.right(90)
t.forward(700)
t.right(90)
t.forward(600)
t.right(90)
t.forward((700/3)*2)
t.right(90)
t.forward(600)
t.right(90)
t.forward(700/3)
t.right(90)
t.forward(600)
t.left(90)
t.forward(700/3)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.right(90)
t.forward(200)
t.right(90)
t.forward(700)
t.right(90)
t.forward(400)
t.right(90)
t.forward(250)
t.end_fill()

def middle_o():
    y = 48
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(180)
    x.forward(50)
    x.left(90)
    x.forward(10)
    x.down()
    while y > 0:
        x.left(8)
        x.forward(8)
        y = y - 1
def left_o():
    y = 48
    a = turtle.Pen()
    a.ht()
    a.color("orange")
    a.width(5)
    a.up()
    a.left(180)
    a.forward(290)
    a.left(90)
    a.forward(10)
    a.down()
    while y > 0:
        a.left(8)
        a.forward(8)
        y = y - 1
def right_o():
    y = 48
    b = turtle.Pen()
    b.ht()
    b.color("orange")
    b.width(5)
    b.up()
    b.left(360)
    b.forward(290)
    b.left(90)
    b.forward(10)
    b.down()
    while y > 0:
        b.left(8)
        b.forward(8)
        y = y - 1
def upper_left_o():
    y = 48
    a = turtle.Pen()
    a.ht()
    a.color("orange")
    a.width(5)
    a.up()
    a.left(180)
    a.forward(290)
    a.right(90)
    a.forward(200)
    a.left(180)
    a.forward(10)
    a.down()
    while y > 0:
        a.left(8)
        a.forward(8)
        y = y - 1
def upper_right_o():
    y = 48
    b = turtle.Pen()
    b.ht()
    b.color("orange")
    b.width(5)
    b.up()
    b.left(360)
    b.forward(290)
    b.left(90)
    b.forward(200)
    b.left(360)
    b.forward(10)
    b.down()
    while y > 0:
        b.left(8)
        b.forward(8)
        y = y - 1
def lower_left_o():
    y = 48
    a = turtle.Pen()
    a.ht()
    a.color("orange")
    a.width(5)
    a.up()
    a.left(180)
    a.forward(290)
    a.left(90)
    a.forward(200)
    a.left(360)
    a.forward(10)
    a.down()
    while y > 0:
        a.left(8)
        a.forward(8)
        y = y - 1
def lower_right_o():
    y = 48
    b = turtle.Pen()
    b.ht()
    b.color("orange")
    b.width(5)
    b.up()
    b.left(360)
    b.forward(290)
    b.right(90)
    b.forward(200)
    b.left(180)
    b.forward(10)
    b.down()
    while y > 0:
        b.left(8)
        b.forward(8)
        y = y - 1
def lower_o():
    y = 48
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.right(90)
    x.forward(200)
    x.left(270)
    x.forward(50)
    x.left(90)
    x.forward(10)
    x.down()
    while y > 0:
        x.left(8)
        x.forward(8)
        y = y - 1
def upper_o():
    y = 48
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(90)
    x.forward(200)
    x.left(90)
    x.forward(50)
    x.left(90)
    x.forward(10)
    x.down()
    while y > 0:
        x.left(8)
        x.forward(8)
        y = y - 1
def middle_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(180)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def left_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(180)
    x.forward(230)
    x.left(180)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def right_x():
    x = turtle.Pen()
    x.color("orange")
    x.ht()
    x.width(5)
    x.up()
    x.forward(230)
    x.left(180)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def upper_left_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(180)
    x.forward(230)
    x.right(90)
    x.forward(200)
    x.left(270)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def upper_right_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.forward(230)
    x.left(90)
    x.forward(200)
    x.left(270)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def lower_left_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(180)
    x.forward(230)
    x.left(90)
    x.forward(200)
    x.left(270)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def lower_right_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.forward(230)
    x.right(90)
    x.forward(200)
    x.left(270)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def upper_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.left(90)
    x.forward(200)
    x.left(270)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def lower_x():
    x = turtle.Pen()
    x.ht()
    x.color("orange")
    x.width(5)
    x.up()
    x.right(90)
    x.forward(200)
    x.left(270)
    x.forward(55)
    x.left(90)
    x.forward(55)
    x.down()
    x.left(135)
    x.forward(160)
    x.up()
    x.backward(80)
    x.down()
    x.right(90)
    x.forward(80)
    x.up()
    x.backward(80)
    x.down()
    x.backward(80)
def middle_line():
    x = turtle.Pen()
    x.ht()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.right(180)
    x.up()
    x.forward(300)
    x.down()
    x.right(180)
    x.forward(600)
def upper_line():
    x = turtle.Pen()
    x.ht()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.right(180)
    x.up()
    x.forward(300)
    x.right(90)
    x.forward(200)
    x.down()
    x.right(90)
    x.forward(600)
def lower_line():
    x = turtle.Pen()
    x.ht()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.right(180)
    x.up()
    x.forward(300)
    x.left(90)
    x.forward(200)
    x.down()
    x.left(90)
    x.forward(600)
def l_diagnol():
    x = turtle.Pen()
    x.ht()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.up()
    x.right(180)
    x.forward(300)
    x.right(90)
    x.forward(250)
    x.right(130)
    x.down()
    x.forward(800)
def r_diagnol():
    x = turtle.Pen()
    x.ht()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.up()
    x.forward(300)
    x.left(90)
    x.forward(250)
    x.left(130)
    x.down()
    x.forward(800)
def l_vertical():
    x = turtle.Pen()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.ht()
    x.right(180)
    x.up()
    x.forward(230)
    x.right(90)
    x.forward(270)
    x.right(180)
    x.down()
    x.forward(540)
def r_vertical():
    x = turtle.Pen()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.ht()
    x.up()
    x.forward(230)
    x.left(90)
    x.forward(270)
    x.left(180)
    x.down()
    x.forward(540)
def m_vertical():
    x = turtle.Pen()
    x.color("white")
    x.width(5)
    x.speed(10)
    x.ht()
    x.left(90)
    x.up()
    x.forward(270)
    x.down()
    x.left(180)
    x.forward(540)

print("Welcome to Spooky Tic-Tac-Toe!")
player_1 = input("Player 1 choose Name: ")
player_2 = input("Player 2 choose Name: ")
num = random.randint(0, 10)
while True:
    while True:
        try:
            player_1_choice = int(input(player_1 + " Chose number 1-10: "))
        except:
            print("Enter valid number")
        if player_1_choice >1 and player_1_choice <= 10:
            break
        else:
            print("Must be 1-10")
            continue
    while True:
        try:
            player_2_choice = int(input(player_2 + " Chose number 1-10: "))
        except:
            print("Enter valid number")
        if player_2_choice > 1 and player_2_choice <= 10:
            break
        else:
            print("Must be 1-10")
            continue
    while abs(num - player_1_choice) != abs(num - player_2_choice):
        if abs(num - player_1_choice) < abs(num - player_2_choice):
            print(player_1 + " goes first")
            first_move = player_1
            second_move = player_2
            break
        elif abs(num - player_2_choice) < abs(num - player_1_choice):
            print(player_2 + " goes first")
            first_move = player_2
            second_move = player_1
            break
    if abs(num - player_1_choice) != abs(num - player_2_choice):
        break
    while abs(num - player_1_choice) == abs(num - player_2_choice):
        print("Tie. Choose again.")
        break
    continue
print("Time to start!")
while True:
    fmc = input(first_move + " choose X or O: ")
    if fmc == "X" or fmc == "O":
        break
    else:
        print("Must choose X or O")
        continue
if fmc == "X":
    print(second_move + " is O")
elif fmc == "O":
    print(second_move + " is X")
count = 1
x_list = ["middle_x", "left_x", "right_x", "upper_left_x", "upper_right_x", "upper_x", "lower_x", "lower_left_x", "lower_right_x"]
o_list = ["middle_o", "left_o", "right_o", "upper_left_o", "upper_right_o", "upper_o", "lower_o", "lower_left_o", "lower_right_o"]
played = []
if fmc == "X":
    while True:
        if count % 2 != 0:
            express = first_move + ", here are your choices: "
            for x_choice in x_list:
                express = express + x_choice + ", "
            print(express)
            choice = input("Your Turn " + first_move + ": ")
            if choice in x_list:
                choice_pos = x_list.index(choice)
                played.append(x_list[choice_pos])
                x_list.remove(x_list[choice_pos])
                o_list.remove(o_list[choice_pos])

            else:
                print("Invalid. Must be an unused X")
                continue
        elif count % 2 == 0:
            express = second_move + ", here are your choices: "
            for o_choice in o_list:
                express = express + o_choice + ", "
            print(express)
            choice = input("Your Turn " + second_move + ": ")
            if choice in o_list:
                choice_pos = o_list.index(choice)
                played.append(o_list[choice_pos])
                o_list.remove(o_list[choice_pos])
                x_list.remove(x_list[choice_pos])

            else:
                print("Invalid. Must be an unused O")
                continue
        eval(choice + "()")
        if set(["middle_x", "left_x", "right_x"]).issubset(played) or set(["middle_o", "left_o", "right_o"]).issubset(played) :
            middle_line()
            print("Winner")
            break
        elif set(["upper_x", "upper_left_x", "upper_right_x"]).issubset(played) or set(["upper_o", "upper_left_o", "upper_right_o"]).issubset(played) :
            upper_line()
            print("Winner")
            break
        elif set(["lower_x", "lower_left_x", "lower_right_x"]).issubset(played) or set(["lower_o", "lower_left_o", "lower_right_o"]).issubset(played) :
            lower_line()
            print("Winner")
            break
        elif set(["left_x", "upper_left_x", "lower_left_x"]).issubset(played) or set(["left_o", "upper_left_o", "lower_left_o"]).issubset(played) :
            l_vertical()
            print("Winner")
            break
        elif set(["middle_x", "upper_x", "lower_x"]).issubset(played) or set(["middle_o", "upper_o", "lower_o"]).issubset(played) :
            m_vertical()
            print("Winner")
            break
        elif set(["right_x", "lower_right_x", "upper_right_x"]).issubset(played) or set(["right_o", "upper_right_o", "lower_right_o"]).issubset(played) :
            r_vertical()
            print("Winner")
            break
        elif set(["upper_left_x", "middle_x", "lower_right_x"]).issubset(played) or set(["upper_left_o", "middle_o", "lower_right_o"]).issubset(played) :
            l_diagnol()
            print("Winner")
            break
        elif set(["upper_right_x", "middle_x", "lower_left_x"]).issubset(played) or set(["upper_right_o", "middle_o", "lower_left_o"]).issubset(played) :
            r_diagnol()
            print("Winner")
            break
        elif x_list == [] and o_list == []:
            print("Tie")
            break
        count = count + 1
if fmc == "O":
    while True:
        if count % 2 != 0:
            express = first_move + ", here are your options: "
            for o_choice in o_list:
                express = express + o_choice + ", "
            print(express)
            choice = input("Your Turn " + first_move + ": ")
            if choice in o_list:
                choice_pos = o_list.index(choice)
                played.append(o_list[choice_pos])
                o_list.remove(o_list[choice_pos])
                x_list.remove(x_list[choice_pos])
            else:
                print("Invalid. Must be an unused O")
                continue
        elif count % 2 == 0:
            express = second_move + ", here are your options: "
            for x_choice in x_list:
                express = express + x_choice + ", "
            print(express)
            choice = input("Your Turn " + second_move + ": ")
            if choice in x_list:
                choice_pos = x_list.index(choice)
                played.append(x_list[choice_pos])
                o_list.remove(o_list[choice_pos])
                x_list.remove(x_list[choice_pos])
            else:
                print("Invalid. Must be an unused X")
                continue
        eval(choice + "()")
        if set(["middle_x", "left_x", "right_x"]).issubset(played) or set(["middle_o", "left_o", "right_o"]).issubset(played) :
            middle_line()
            print("Winner")
            break
        elif set(["upper_x", "upper_left_x", "upper_right_x"]).issubset(played) or set(["upper_o", "upper_left_o", "upper_right_o"]).issubset(played) :
            upper_line()
            print("Winner")
            break
        elif set(["lower_x", "lower_left_x", "lower_right_x"]).issubset(played) or set(["lower_o", "lower_left_o", "lower_right_o"]).issubset(played) :
            lower_line()
            print("Winner")
            break
        elif set(["left_x", "upper_left_x", "lower_left_x"]).issubset(played) or set(["left_o", "upper_left_o", "lower_left_o"]).issubset(played) :
            l_vertical()
            print("Winner")
            break
        elif set(["middle_x", "upper_x", "lower_x"]).issubset(played) or set(["middle_o", "upper_o", "lower_o"]).issubset(played) :
            m_vertical()
            print("Winner")
            break
        elif set(["right_x", "lower_right_x", "upper_right_x"]).issubset(played) or set(["right_o", "upper_right_o", "lower_right_o"]).issubset(played) :
            r_vertical()
            print("Winner")
            break
        elif set(["upper_left_x", "middle_x", "lower_right_x"]).issubset(played) or set(["upper_left_o", "middle_o", "lower_right_o"]).issubset(played) :
            l_diagnol()
            print("Winner")
            break
        elif set(["upper_right_x", "middle_x", "lower_left_x"]).issubset(played) or set(["upper_right_o", "middle_o", "lower_left_o"]).issubset(played) :
            r_diagnol()
            print("Winner")
            break
        elif x_list == [] and o_list == []:
            print("Tie")
            break
        count = count + 1
print("Game Over!")
turtle.done()
