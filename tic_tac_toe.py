import re

name_user1 = input("Имя играющего х: ")
name_user2 = input("Имя играющего 0: ")

field = {" ": [0, 1, 2], 0: ["-", "-", "-"], 1: ["-", "-", "-"], 2: ["-", "-", "-"]}


def print_f():
    for k, v in field.items():
        v = str(v)
        v = re.sub("[]|'|,|[]", "", v)
        print(k, v)


def change(x_or_0):
    if motion_user == "00":
        field[0][0] = x_or_0
        print_f()

    elif motion_user == "01":
        field[0][1] = x_or_0
        print_f()

    elif motion_user == "02":
        field[0][2] = x_or_0
        print_f()

    elif motion_user == "10":
        field[1][0] = x_or_0
        print_f()

    elif motion_user == "11":
        field[1][1] = x_or_0
        print_f()

    elif motion_user == "12":
        field[1][2] = x_or_0
        print_f()

    elif motion_user == "20":
        field[2][0] = x_or_0
        print_f()

    elif motion_user == "21":
        field[2][1] = x_or_0
        print_f()

    elif motion_user == "22":
        field[2][2] = x_or_0
        print_f()
    else:
        print("что-то не получилось")


def win(field):
    if (
        (field[0][0] == "x" and field[0][1] == "x" and field[0][2] == "x")
        or (field[1][0] == "x" and field[1][1] == "x" and field[1][2] == "x")
        or (field[2][0] == "x" and field[2][1] == "x" and field[2][2] == "x")
        or (field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x")
        or (field[0][2] == "x" and field[1][1] == "x" and field[2][0] == "x")
        or (field[0][0] == "x" and field[1][0] == "x" and field[2][0] == "x")
        or (field[0][1] == "x" and field[1][1] == "x" and field[2][1] == "x")
        or (field[0][2] == "x" and field[1][2] == "x" and field[2][2] == "x")
    ):
        print("========================")
        print(f"Победитель {name_user1}")
        print("========================")
        exit()
    elif (
        (field[0][0] == "0" and field[0][1] == "0" and field[0][2] == "0")
        or (field[1][0] == "0" and field[1][1] == "0" and field[1][2] == "0")
        or (field[2][0] == "0" and field[2][1] == "0" and field[2][2] == "0")
        or (field[0][0] == "0" and field[1][1] == "0" and field[2][2] == "0")
        or (field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0")
        or (field[0][0] == "0" and field[1][0] == "0" and field[2][0] == "0")
        or (field[0][1] == "0" and field[1][1] == "0" and field[2][1] == "0")
        or (field[0][2] == "0" and field[1][2] == "0" and field[2][2] == "0")
    ):
        print("========================")
        print(f"Победитель {name_user2}")
        print("========================")
        exit()


def motion(text):
    motion_user = input(text)
    if re.fullmatch(r"[0-2][0-2]", motion_user):
        return str(motion_user)
    else:
        print("Вы ввели что-то не то, попробуйте ещё")
        motion(text)


print("===========================================================")
print_f()
print(f"Первый ходит {name_user1}!")
motion_user = motion(
    "Выберите место куда будете ходить и напишите координаты в формате '01': "
)
while True:
    change("x")
    win(field)
    motion_user = motion(f"Теперь ходит {name_user2}: ")
    change("0")
    win(field)
    motion_user = motion(f"Теперь ходит {name_user1}: ")
