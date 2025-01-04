import subprocess

path = "Logic/board_UI.py"
sizeIn = input("Enter the size of the board as AxB, ex: 10x10 . ")

try:
    size = sizeIn.split("x")
    test = int(size[0]) - int(size[1])
except:
    print("Defaulting to 10x10")
    size = ["10", "10"]

subprocess.run(["python3", path] + size, text=True)


