from tkinter import *

BaseWindow  = Tk()
BaseWindow.title("Input Form")
BaseWindow.geometry("600x470")

###  Entries Labels ###
Label(BaseWindow,text="Please fill the required input for training the model",font="arial 16").pack(pady=50)

Label(text="No. Hidden Layers",font=23).place(x=100,y=100)

Label(text="No. Neurons",font=23).place(x=100,y=150)

Label(text="Learning rate",font=23).place(x=100,y=200)

Label(text="epochs",font=23).place(x=100,y=250)

#Label(text="Bias",font=23).place(x=100,y=350)

Label(text="Activation Function",font=23).place(x=100,y=350)

### Entries ###
hiddenLayers = IntVar()
neurons = IntVar()
Lr = DoubleVar()
epochs = IntVar()
Biased = BooleanVar()
activation = IntVar()

HLEntry  = Entry(BaseWindow,textvariable=hiddenLayers,width=10,bd=2,font=20)
HLEntry.place(x=300,y=100)

NeuronsEntry  = Entry(BaseWindow,textvariable=neurons,width=10,bd=2,font=20)
NeuronsEntry.place(x=300,y=150)

LrEntry  = Entry(BaseWindow,textvariable=Lr,width=10,bd=2,font=20)
LrEntry.place(x=300,y=200)

EpochsEntry  = Entry(BaseWindow,textvariable=epochs,width=10,bd=2,font=20)
EpochsEntry.place(x=300,y=250)


BiasBox  = Checkbutton(text="Bias ?",variable=Biased,font=20)
BiasBox.place(x=100,y=300)


sigBtn = Radiobutton(BaseWindow,text="Sigmoid",variable=activation,value=1)
sigBtn.place(x=320,y=350)
tanhBtn = Radiobutton(BaseWindow,text="Tanh",variable=activation,value=2)
tanhBtn.place(x=400,y=350)

def getInputs():
    return hiddenLayers.get(),neurons.get(),Lr.get(),epochs.get(),Biased.get(),activation.get()


Button(text="Submit",font=20,width=11,height=2,command=getInputs).place(x=250,y=400)

BaseWindow.mainloop()
