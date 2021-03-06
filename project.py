import tkinter as tk
from tkinter import *
from functools import partial

buttonWidth = 1

line = ''
lineAnswer = ''


def resultManager(m, *arg):    # mode, value
    global line
    global lineAnswer
    value = arg[0]

    if m == 'i':                # insert mode
        line += value
        result.config(text=line)
    if m == 'd':                # delete mode
        line = line[:-value]
        result.config(text=line)
    if m == 'a':                # answer mode
        lineAnswer = eval(line)
        edit = str(line) + '=' + str(lineAnswer)
        result.config(text=edit)


app = tk.Tk()
mainFrame = Frame(app)
mainFrame.pack()

left = Frame(mainFrame)
left.pack(side=LEFT)

right = Frame(mainFrame)
right.pack(side=RIGHT)

righter = Frame(right)
righter.pack(side=RIGHT)

numFrame4 = Frame(left)
numFrame4.pack(side=BOTTOM)

numFrame1 = Frame(left)
numFrame1.pack(side=BOTTOM)

numFrame2 = Frame(left)
numFrame2.pack(side=BOTTOM)

numFrame3 = Frame(left)
numFrame3.pack(side=BOTTOM)


commandFrame = Frame(right)
commandFrame.pack()

promptBox = tk.Label(commandFrame, text="")


# result = tk.Entry(left, width=20, justify='right')
result = tk.Label(left, width=16, bg="grey", wraplength=100)
result.pack()


print(line)
print(lineAnswer)


###
### Command Frame
###

buttonAnswer = tk.Button(righter, text="=", width=buttonWidth, height=5,
                          command=partial(resultManager, 'a', None))


buttonBackspace = tk.Button(righter, text="X", width=buttonWidth,
                          command=partial(resultManager, 'd', 1))

###
### Number Frame 4
###

buttonZero = tk.Button(numFrame4, text="0", width=7,
                          command=partial(resultManager, 'i', '0'))

buttonDot = tk.Button(numFrame4, text=".")

###
### Number Frame 1
###


buttonOne = tk.Button(numFrame1, text="1", width=buttonWidth,
                          command=partial(resultManager, 'i', '1'))


buttonTwo = tk.Button(numFrame1, text="2", width=buttonWidth,
                          command=partial(resultManager, 'i', '2'))


buttonThree = tk.Button(numFrame1, text="3", width=buttonWidth,
                          command=partial(resultManager, 'i', '3'))

###
### Number Frame 2
###

buttonFour = tk.Button(numFrame2, text="4", width=buttonWidth,
                          command=partial(resultManager, 'i', '4'))


buttonFive = tk.Button(numFrame2, text="5", width=buttonWidth,
                          command=partial(resultManager, 'i', '5'))


buttonSix = tk.Button(numFrame2, text="6", width=buttonWidth,
                          command=partial(resultManager, 'i', '6'))


###
### Number Frame 3
###


buttonSeven = tk.Button(numFrame3, text="7", width=buttonWidth,
                          command=partial(resultManager, 'i', '7'))


buttonEight = tk.Button(numFrame3, text="8", width=buttonWidth,
                          command=partial(resultManager, 'i', '8'))


buttonNine = tk.Button(numFrame3, text="9", width=buttonWidth,
                          command=partial(resultManager, 'i', '9'))



###
### Command Frame
###

buttonPlus = tk.Button(commandFrame, text="+", width=buttonWidth,
                          command=partial(resultManager, 'i', '+'))


buttonMin = tk.Button(commandFrame, text="-", width=buttonWidth,
                          command=partial(resultManager, 'i', '-'))


buttonMul = tk.Button(commandFrame, text="*", width=buttonWidth,
                          command=partial(resultManager, 'i', '*'))


buttonDiv = tk.Button(commandFrame, text="/", width=buttonWidth,
                          command=partial(resultManager, 'i', '/'))


###
### Packing
###

promptBox.pack()

buttonBackspace.pack(side=TOP)
buttonAnswer.pack(side=BOTTOM)

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

buttonZero.pack(side=LEFT)
buttonDot.pack(side=LEFT)

app.mainloop()
