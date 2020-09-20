import tkinter
import random
root = tkinter.Tk()
root.geometry("600x300")
root.maxsize(600, 300)
root.minsize(600, 300)
dicelabel = tkinter.Label(root, text='', font=('Roboto', 260))


def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dicelabel.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    dicelabel.pack()


btn1 = tkinter.Button(root, text='Roll Dice', foreground='black', command=roll_dice)
btn1.grid(row=0, column=3, padx=100)
btn1.pack()
root.mainloop()
