import tkinter as tk
from tkinter import *
from functools import partial

prompt = ''


def promptAppend(letter):
    global prompt
    prompt += str(letter)
    promptBox.config(text=str(prompt))
    print(prompt)


def promptRemove(num):
    global prompt
    prompt = prompt[:-num]
    promptBox.config(text=str(prompt))
    print(prompt)


def promptSolve():
    global prompt
    answer = eval(prompt)
    buttonAnswer.config(text=str(answer))
    print(answer)

line = ''
lineAnswer = ''

def resultManager(m, *arg):    # mode, value
    global line
    global lineAnswer
    mode = arg[0]

    if m == 'i':                # insert mode
        line += mode
        result.delete(0,END)
        result.insert(0,line)
    if m == 'd':                # delete mode
        line = line[:-mode]
        result.delete(0,END)
        result.insert(0,line)
    if m == 'a':                # answer mode
        lineAnswer = eval(line)
        edit = str(line) + '=' + str(lineAnswer)
        result.delete(0,END)
        result.insert(0,edit)




app = tk.Tk()
mainFrame = Frame(app)
mainFrame.pack()

left = Frame(mainFrame)
left.pack(side=LEFT)

right = Frame(mainFrame)
right.pack(side=RIGHT)

numFrame1 = Frame(left)
numFrame1.pack(side=BOTTOM)

numFrame2 = Frame(left)
numFrame2.pack(side=BOTTOM)

numFrame3 = Frame(left)
numFrame3.pack(side=BOTTOM)

commandFrame = Frame(right)
commandFrame.pack()

promptBox = tk.Label(commandFrame, text="")


result = tk.Entry(left)
result.pack()



print(line)
print(lineAnswer)


###
### Command Frame
###

buttonAnswer = tk.Button(commandFrame, text="=", width=1,
                          command=partial(resultManager, 'a', None))


buttonBackspace = tk.Button(commandFrame, text="X", width=1,
                          command=partial(resultManager, 'd', 1))


buttonZero = tk.Button(mainFrame, text="0",
                          command=partial(resultManager, 'i', '0'))

###
### Number Frame 1
###

buttonOne = tk.Button(numFrame1, text="1",
                          command=partial(resultManager, 'i', '1'))


buttonTwo = tk.Button(numFrame1, text="2",
                          command=partial(resultManager, 'i', '2'))


buttonThree = tk.Button(numFrame1, text="3",
                          command=partial(resultManager, 'i', '3'))

###
### Number Frame 2
###

buttonFour = tk.Button(numFrame2, text="4",
                          command=partial(resultManager, 'i', '4'))


buttonFive = tk.Button(numFrame2, text="5",
                          command=partial(resultManager, 'i', '5'))


buttonSix = tk.Button(numFrame2, text="6",
                          command=partial(resultManager, 'i', '6'))


###
### Number Frame 3
###


buttonSeven = tk.Button(numFrame3, text="7",
                          command=partial(resultManager, 'i', '7'))


buttonEight = tk.Button(numFrame3, text="8",
                          command=partial(resultManager, 'i', '8'))


buttonNine = tk.Button(numFrame3, text="9",
                          command=partial(resultManager, 'i', '9'))

###
### Command Frame
###

buttonPlus = tk.Button(commandFrame, text="+", width=1,
                          command=partial(resultManager, 'i', '+'))


buttonMin = tk.Button(commandFrame, text="-", width=1,
                          command=partial(resultManager, 'i', '-'))


buttonMul = tk.Button(commandFrame, text="*", width=1,
                          command=partial(resultManager, 'i', '*'))


buttonDiv = tk.Button(commandFrame, text="/", width=1,
                          command=partial(resultManager, 'i', '/'))


###
### Packing
###

promptBox.pack()
buttonAnswer.pack()
buttonBackspace.pack()

buttonDiv.pack()
buttonMul.pack()
buttonPlus.pack()
buttonMin.pack()

buttonOne.pack(side=LEFT)
buttonTwo.pack(side=LEFT)
buttonThree.pack(side=LEFT)

buttonFour.pack(side=LEFT)
buttonFive.pack(side=LEFT)
buttonSix.pack(side=LEFT)

buttonSeven.pack(side=LEFT)
buttonEight.pack(side=LEFT)
buttonNine.pack(side=LEFT)

buttonZero.pack(side=BOTTOM)

app.mainloop()
