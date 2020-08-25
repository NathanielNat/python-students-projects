from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window = Tk()
from tkinter import messagebox

# the size of the window in width(700) and height(400) using the 'geometry' method
window.geometry("950x500")

# In order to prevent the window from getting resized i call 'resizable' method on the window
window.resizable(0, 0)




class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        dishList.append(self)
        dishNames.append(name)


class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        juiceList.append(self)
        juiceNames.append(name)


def getPrice1():
    for d in dishList:
        if d.name == selectedDish.get():
            foodPrice.set(d.price)


def getPrice2():
    for j in juiceList:
        if j.name == selectedJuice.get():
            drinkPrice.set(j.price)

def getTotal():
    price.set(foodPrice.get()+ drinkPrice.get())
    # getTotal = StringVar()
    # return foodPrice+ drinkPrice






dishList = []
dishNames = []
Dish("Red Red and Plantain", 15)
Dish("Akple and Okro Stew", 20)
Dish("Omotuo and Palmnut Soup", 25)
Dish("Ampesi and Kontomire Stew", 30)
Dish("Banku and Tilapia", 45)
Dish("Kokonte and Groundnut Soup", 35)

selectedDish = StringVar()
selectedDish.set(dishNames[0])


juiceList = []
juiceNames = []
Juice("Asaana", 7)
Juice("Lamugini", 8)
Juice("Solom", 5)
Juice("Palmwine", 10)
Juice("Brukutu", 12)
Juice("Sobolo", 15)

selectedJuice = StringVar()
selectedJuice.set(juiceNames[0])


#dish menu
dishMenu = OptionMenu(window, selectedDish, *dishNames)
dishMenu.pack()

#juice menu
juiceMenu = OptionMenu(window,selectedJuice, *juiceNames)
juiceMenu.pack()

#Frames
top_frame = Frame(window).pack()
lower_frame = Frame(window).pack(side="bottom")


#buttons
#button 1 should display cost of dish
#button2 should display cost of juice
#button3 TOTAL to display total cost of order placed (dish and juice)
btn1 = Button(top_frame, text="Select1", bg='white', fg='black', command=getPrice1).pack()
btn2 = Button(top_frame, text="Select2", bg='white', fg='black', command=getPrice2).pack()
btn3 = Button(lower_frame,text='Bill', bg='grey', fg='black', command=getTotal).pack()


#Labels
Label(window, text='Seys Local Bar!, Good Food Is Good Mood',fg='white',bg='green').pack(side='bottom',fill='x')



price = IntVar()
foodPrice = IntVar()
drinkPrice = IntVar()
#label
#textvariable used since its easy to update its content
priceLbl1 = Label(window, textvariable=price)
priceLbl2 = Label(window, textvariable=foodPrice)
priceLbl3 = Label(window, textvariable=drinkPrice)
priceLbl1.pack()
priceLbl2.pack()
priceLbl3.pack()

# priceLbl2 = Label(window, textvariable=price)
# priceLbl2.pack()



window.mainloop()
