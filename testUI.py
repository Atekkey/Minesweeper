import PySimpleGUI as sg

sg.theme('LightBlue1') 


layout = [
        [[sg.Button("", size = (4, 2), button_color = "Orange", key = (str(i) + str(j)) ) for j in range(10)] for i in range(10)],
        [sg.Button("exit")]
          ]

window = sg.Window('Minesweeper', layout, size = (570,570))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "exit":
        break
    window[event].update(event + "_", button_color = "green")

window.close()
