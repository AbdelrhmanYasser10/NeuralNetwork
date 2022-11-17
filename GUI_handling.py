from tkinter import *
from tkinter import messagebox

# variables
features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'gender', 'body_mass_g']
classes = ["Adelie", "Gentoo", "Chinstrap"]
firstFeature = ""
secondFeature = ""
class1 = ""
class2 = ""
eta = 0
m = 0
mse = 0
bias = False

master = Tk()

# functions
# validate functions
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

# button functions
def handlingIfWeWantBiasOrNot():
    if biasOrNot.get() != 0:
        if biasOrNot.get() == 1:
            label = "Congratulations You Fill The Data !!"
            messageVar.config(text=label, anchor=CENTER)
            my_Button.pack_forget()
            firstFinalChoice.pack_forget()
            secondFinalChoice.pack_forget()
            global bias
            bias = True
            master.destroy()
        elif biasOrNot.get() == 2:
            label = "Congratulations You Fill The Data !!"
            messageVar.config(text=label, anchor=CENTER)
            my_Button.pack_forget()
            firstFinalChoice.pack_forget()
            secondFinalChoice.pack_forget()
            master.destroy()

    else:
        messagebox.showerror("Error", "Make Sure to choose an option")

def validateEpochs():
    if epochsEntry.get() == "":
        messagebox.showerror("Error", "You Enter an empty text")
    else:
        global m
        flag = isInteger(epochsEntry.get())
        if flag:
            m = int(epochsEntry.get())
            label = "Enter MSE"
            messageVar.config(text=label)
            epochsEntry.pack_forget()
            mseEntry.focus_set()
            mseEntry.pack(anchor= CENTER,expand=YES)
            my_Button.config(command=validateMSE)
        else:
            messagebox.showerror("Error", "Enter a Integer number")

def validateMSE():
    if mseEntry.get() == "":
        messagebox.showerror("Error", "You Enter an empty text")
    else:
        global mse
        flag1 = isfloat(mseEntry.get())
        flag2 = isInteger(mseEntry.get())
        if flag1 or flag2:
            label = "Do you want bias?"
            messageVar.config(text=label)
            mseEntry.pack_forget()
            firstFinalChoice.pack(anchor=CENTER, expand=YES)
            secondFinalChoice.pack(anchor=CENTER, expand=YES)
            my_Button.config(command=handlingIfWeWantBiasOrNot)
            if flag2:
                mse = int(mseEntry.get())
            else:
                mse = float(mseEntry.get())
        else:
            messagebox.showerror("Error", "Enter a float number")

def validateLearningRate():
    if learningRateEntry.get() == "":
        messagebox.showerror("Error", "You Enter an empty text")
    else:
        global eta
        flag1 = isfloat(learningRateEntry.get())
        flag2 = isInteger(learningRateEntry.get())
        if flag1 or flag2:
            label = "Enter number of epochs"
            messageVar.config(text=label)
            epochsEntry.focus_set()
            epochsEntry.pack(anchor= CENTER,expand=YES)
            learningRateEntry.pack_forget()
            my_Button.config(command=validateEpochs)
            if flag1:
                eta = float(learningRateEntry.get())
            else:
                eta = int(learningRateEntry.get())
        else:
            messagebox.showerror("Error", "Enter a float number")

def selectSecondClass():
    global class2
    class2 = classVar.get()
    label = "Enter learning rate"
    messageVar.config(text=label)
    global allClasses
    allClasses.pack_forget()
    learningRateEntry.focus_set()
    learningRateEntry.pack(anchor= CENTER,expand=YES)
    my_Button.config(command=validateLearningRate)

def selectFirstClass():
    global class1
    label = "Choose The Second Class Classes You Need"
    messageVar.config(text=label)
    messageVar.pack(anchor=W)
    class1 = classVar.get()
    global allClasses
    r_index = allClasses['menu'].index(classVar.get())  # index of selected option.
    allClasses['menu'].delete(r_index)  # deleted the option
    classVar.set(allClasses['menu'].entrycget(0, "label"))
    allClasses.config(menu=allClasses['menu'])
    allClasses.pack(anchor=CENTER, expand=YES)
    my_Button.config(command=selectSecondClass)


def secondFeatureSelected():
    global secondFeature
    secondFeature = variable.get()
    feature.pack_forget()
    label = "Choose The First Class Classes You Need"
    messageVar.config(text=label)
    messageVar.pack(anchor=W)
    global allClasses
    allClasses.pack(anchor=CENTER, expand=YES)
    my_Button.config(command=selectFirstClass)


def firstFeatureSelected():
    global firstFeature
    firstFeature = variable.get()
    r_index = feature['menu'].index(variable.get())  # index of selected option.
    feature['menu'].delete(r_index)  # deleted the option
    variable.set(feature['menu'].entrycget(0, "label"))
    feature.config(menu=feature['menu'])
    global f_label
    f_label = "Choose The 2nd Feature You Need"
    messageVar.config(text=f_label)
    my_Button.config(command=secondFeatureSelected)


# The next code is to handle the GUI ::
master.title("Task 1")
master.geometry('200x200')

# label and button
f_label = "Choose The 1st Feature You Need"
messageVar = Message(master, text=f_label, width=190, bg='lightgreen')
messageVar.pack(anchor=W)


# drop box for the features
variable = StringVar(master)
variable.set(features[0])
feature = OptionMenu(master, variable, *features)
feature.pack(anchor=CENTER,expand=YES)

# that button function editable when we go far with GUI
my_Button = Button(master, text="Next", command=firstFeatureSelected, width=100,bg="lightblue")
my_Button.pack(anchor=CENTER,side=BOTTOM)

# class values
classVar = StringVar(master)
classVar.set(classes[0])
allClasses = OptionMenu(master, classVar, *classes)


# Entries
learningRateEntry = Entry(master)
epochsEntry = Entry(master)
biasEntry = Entry(master)
mseEntry = Entry(master)

# bias handling variables
biasOrNot = IntVar()
firstFinalChoice = Radiobutton(master, text='YES', variable=biasOrNot, value=1)
secondFinalChoice = Radiobutton(master, text='NO', variable=biasOrNot, value=2)

# Add mse

master.mainloop()