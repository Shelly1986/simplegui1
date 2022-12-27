import PySimpleGUI as sg
import sqlite3
import sqlfunctions

layout = [
    
[sg.Text("Theme Cake Order Form")],
[sg.Text('Your Name: ',size=(20,1)),sg.InputText(key="-TEXT1-")],
[sg.Text('Address: ',size=(20,1)),sg.InputText(key="-TEXT2-")],
[sg.Text('Ph Number: ',size=(20,1)),sg.InputText(key="-TEXT3-")],
[sg.Text('Serving Size: ',size=(20,1)),
 sg.Radio('Desert Size(2x1)', "RADIO1",key='-RADIO1-'),
 sg.Radio('Coffee Size(1x1)', "RADIO1",key='-RADIO2-')],
[sg.Text("Flavour:  "),
 sg.Combo(['Mud Cake Chocolate','Mud Cake Caramel','Vanilla', 'Mud Cake Toblerone'],default_value='Vanilla',key='-flavour-')],
[sg.Text("Extra Toppings: ")],
[sg.Checkbox('Chocolates and Candies', key = '-CHOCO-')],
[sg.Checkbox('Coconut Enveloping', key = '-COCO-')],
[sg.Checkbox('Fruit Toppings', key = '-FRUIT-')],
[sg.Checkbox('Crunchy Nuts', key = '-NUTS-')],
[sg.Button('Click to Order', key = '-BUTTON-')],
[sg.Button('Past orders', key = '-BUTTON2-')]

]

window = sg.Window('Cake Order', layout)
while True:
    price = 0
    
    event, values = window.read()
    name = values['-TEXT1-']
    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON-':
        if values['-RADIO1-']== True:
            price = price + 30
        else:
            price = price + 20

        flavor = values['-flavour-']
        if flavor == 'Mud Cake Chocolate':
            price = price + 10
        elif flavor == 'Mud Cake Caramel':
            price = price + 12
        elif flavor == 'Mud Cake Toblerone':
            price = price + 15
        else:
            price = price + 10

        if values['-CHOCO-'] == True:
            price = price + 5
        if values['-COCO-'] == True:
            price = price + 6
        if values['-FRUIT-'] == True:
            price = price + 7
        if values['-NUTS-'] == True:
            price = price + 8
        
        output = f'Thank You for your order {name}.The total cost of your order is {price} zlots'
        sg.Popup('Confirmation',output)
        
    if event == '-BUTTON2-':
        sqlfunctions.show_all()
        
        
window.close()
