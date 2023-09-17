name = "Tyler"
hp = 100
hpmax = 100

def save():
    list = [
        name,
        str(hp),
        str(hpmax)
    ]
    file = open("loadex.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()

def load():
    try:
        f = open("loadex.txt", "r")
        load_list = f.readlines()
        if len(load_list) == 3:
            name = load_list[0][:-1]
            hp = int(load_list[1][:-1])
            hpmax = int(load_list[2][:-1])

            print("Welcome back, " + name + "!")

            input("> ")
        else:
            print("Corrupt save file!")
            input("> ")
    except OSError:
        print("No loadable save file!")
        input("> ")
save()
load()
