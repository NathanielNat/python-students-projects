from tkinter import *
# ttk is needed for combobox
from tkinter import ttk
# Tkinter window
window = Tk()
from tkinter import messagebox
# the size of the window in width(1090) and height(400) using the 'geometry' method
window.geometry("1090x400")
# In order to prevent the window from getting resized i call 'resizable' method on the window
window.resizable(0, 0)
# the title of the window is Annan_BMI_Calculator
window.title("Annan_BMI_Calculator")


# there 3 titles on this app:

# t1 = 1st title is to welcome to the app 
t1=Label(window, text='You, Welcome to Annan_BMI_Calculator',fg='green',font=('arial',15,'bold'))
t1.grid(row=0, column=2)

# t2 =2nd title is t insruct you input your details 
t2=Label(window, text='Please Enter Your Details',fg='blue',font=('arial',12,'bold'))
t2.grid(row=1, column=2)

#t3 =  3rd title is given the standard bmi range that everyone have
t3=Label(window, text='Standard BMI Range is 18.5 – 24.9',fg='black',font=('arial',12,'bold'))
t3.grid(row=2, column=2)


# there 3 labels on this app:

# l1 = 1st label promting you to enter your First Name
l1=Label(window, text='First Name:',font=('arial',12,'bold'))
l1.grid(row=1, column=0)
fname = StringVar()

# Entry1 = Entryfield to enter your first name
fname = Entry(window,font=('arial',12,'bold'), highlightcolor = "green", highlightthickness = 3,bg='powder blue', fg='black',width=12)
fname.grid(row=1, column=1, )

# l2 = 2nd label promting you to enter your Height cm
l2=Label(window, text='Height cm:',font=('arial',12,'bold'))
l2.grid(row=1, column=3)
height = IntVar()
# Entry2 = Entryfield to enter your Height cm
height = Entry(window,font=('arial',12,'bold'), highlightcolor = "green", highlightthickness = 3,bg='powder blue', fg='black',width=8)
height.grid(row=1, column=4)

# l3 = 3nd label promting you to select your gender type
l3=Label(window, text='Gender:',font=('arial',12,'bold'))
l3.grid(row=3, column=0)

# Entry3 = selectionfield to select your gender type with combobox
gender = ttk.Combobox(window, 
                            values=[
                              "Male", 
                              "Female",
                              "Other",
                            ],width=15, font=('arial',10,'bold'))

gender.grid(column=1, row=3)
gender.current(0)

# l4 = 4th label promting you to enter your Age
l4=Label(window, text='Age:',font=('arial',12,'bold'))
l4.grid(row=2, column=0)
age =  DoubleVar()
# Entry4 = Entryfield to enter your Age
age = Entry(window,font=('arial',12,'bold'), highlightcolor = "green", highlightthickness = 3,width=12,bg='powder blue', fg='black')
age.grid(row=2, column=1)

# l5 = 5th label promting you to enter your Weight kg
l5=Label(window, text='Weight kg:',font=('arial',12,'bold'))
l5.grid(row=2, column=3)
weight = DoubleVar()
# Entry5 = Entryfield to enter your Weight kg
weight = Entry(window,font=('arial',12,'bold'), highlightcolor = "green", highlightthickness = 3,width=8,bg='powder blue', fg='black')
weight.grid(row=2, column=4)

# there are 3 functions on this app:

def calcBMI():
# 1. convert cm to metre and calculate bmi in float with the formula
    Metre_Unit = 0.01
    Height_Metre = float(height.get()) * Metre_Unit
    bmi = float(weight.get()) / (Height_Metre**2)
    Under_BMI(bmi)
    

def Under_BMI(BMI):
# 2. Display wherethere BMI is Under Weight/Normal Weight/Over Weight/Obesity in if statement.#
    if BMI < 18.5:
        output_text.set(str(BMI)  + ' ' +  fname.get() +   'You are  --Under Weight')
    elif(BMI >= 18.5) and (BMI <= 24.9):
        output_text.set(str(BMI) +   '--Normal Weight')
    elif(BMI >=25) and (BMI <= 29.9):
        output_text.set(str(BMI) +   '--Over Weight')
    else: 
        output_text.set(str(BMI)  + ' ' +  fname.get() +   'You have Obesity')


def button_clear():
# 3. function clears the input field or previous calculations using the button "CLEAR"
    global expression
    expression = ""
    output_text.set("")



# there are 2 buttums on this app

# bt1 is the clear button that clears the input field or previous calculations using the button "CLEAR"
clear = Button(window, text = 'CLEAR', bg='powder blue',command=button_clear, fg='black',font=('arial',13,'bold'))
clear.grid(row=3, column=3)


# bt2 is the BMI button to calculate bmi in float
bmi = Button(window, text = 'BMI',font=('arial',15,'bold'), bg='powder blue', fg='green',command=calcBMI)
bmi.grid(row=3, column=2)

# output area is wherethere bmi is Under Weight/Normal Weight/Over Weight/Obesity and the BMI Display
output_text = StringVar()

# output area frame 
output_frame = Frame(window, width = 500, height = 350, bd = 0, highlightbackground = "green", highlightcolor = "black", highlightthickness = 5)
output_frame.grid(row=5, column=2)

# output field 
output = Label(output_frame,textvariable=output_text,width=32,height=2,fg='blue',font=('arial',15,'bold')).pack()


# there are 7 interpretation on this app:

# t1 is the  the title to interpretate your BMI status 
t1=Label(window, text=' BMI Chart Reader',fg='black',font=('arial',15,'bold'))
t1.grid(row=7, column=2)

# t2 is, if your BMI status is Under Weight what you should do
t2=Label(window, text=' Under Weight ( < 18.5) --- Eat balance diet always, to gain more body fat ok!! ',fg='green',font=('arial',10,'bold'))
t2.grid(row=8, column=2)

# t3 is, if your BMI status is Normal Weight what you should do
t3=Label(window, text=' Normal Weight (18.5 - 24.9) --- You are taken good care of yourself, Please keep it up ok!',fg='black',font=('arial',10,'bold'))
t3.grid(row=9, column=2)

# t4 is, if your BMI status is Over Weight what you should do
t4=Label(window, text=' Over Weight (25.0 - 29.9) --- Exercise a lot, to loss more body fat ok!',fg='green',font=('arial',10,'bold'))
t4.grid(row=10, column=2)

# t5 is, if your BMI status is Obesity what you should do
t5=Label(window, text=' Obesity ( 30.0 >) --- You Stand a High Risk of Testing Positive for C0VD-19 and Cardiovascular Diseases ',fg='black',font=('arial',10,'bold'))
t5.grid(row=11, column=2)

# t6 is, if your BMI status is Under Weight/Over Weight/Obesity, it priscribe a Doctor for you
t4=Label(window, text=' Speak to Dr.Annan form V-Clinic for help +233 (0) 244 656 694. ',fg='green',font=('arial',10,'bold'))
t4.grid(row=12, column=2)

# t7 is,  telling you to always check and know your BMI status to stay save 
t4=Label(window, text=' Its good to check and know your Body Mass Index (BMI) always for a healty life Ok! ',fg='black',font=('arial',10,'bold'))
t4.grid(row=13, column=2)

# window mainloop() to keep the app running 
window.mainloop()




