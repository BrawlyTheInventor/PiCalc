try:
    from turtle import *
    from time import sleep
except:
    print("While handeling Launcher, A error occered: Could not load module. use pip3 list and if time, turtle, or guizero is not on the list, do pip3 install <modulename>")
    raise ModuleNotFoundError("Fatal: App crashed")
print("Initlizing PICalc...")
def program():
    sleep(0.5)

    x = input("Enter X to map")
    y = input("Enter Y to map")
    action = input("Enter action(mapline, etc)")
    if action == "mapline":
        goto(int(x), int(y))

speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
            try:
                sleep(5)
                clear()
                sleep(0.5)
                write("PiCalc", font=('Arial', 30, 'normal'))
                sleep(2)
                bye()
            except:
                break
                program()
            finally:
                break
                program()

try:
    end_fill()
    done()
    reset()
except:
    program()
