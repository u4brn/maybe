import os, random, sys, time

def aprint(text, delay=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def ainput(text, delay=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    return input()
def line(x):
    aprint("=" * x)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
aprint("uk3run3l apresenta:\n")
line(10)
aprint("Maybe")
line(10)
time.sleep(1)

clear()

options = ["Sim.", "Não.", "Talvez..."]

stop = False
while not stop:
    user = ainput("Faça a pergunta digitando ou oralmente e aperte Enter ou digite /s para sair:\n> ")
    if user.lower() == "/s" or user.lower() == "/sair":
        exit()
    else:
        clear()
        randomization = random.choice(options)
        aprint(randomization)
        time.sleep(2)
        clear()