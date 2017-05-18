from tkinter import *

root = Tk()

displayFrame = Frame(root, width=400, height=400)
optionsFrame = Frame(root, width=400, height=100)

typeLabel = Label(optionsFrame, text='Type:')
typeTextbox = Text(optionsFrame, width=20, height=1)
zoomLabel = Label(optionsFrame, text='Zoom:')
zoomTextbox = Text(optionsFrame, width=20, height=1)

typeLabel.grid(row=0, column=0)
typeTextbox.grid(row=0, column=1)
zoomLabel.grid(row=0, column=2)
zoomTextbox.grid(row=0, column=3)

displayFrame.pack()
optionsFrame.pack(side=BOTTOM)


root.mainloop()