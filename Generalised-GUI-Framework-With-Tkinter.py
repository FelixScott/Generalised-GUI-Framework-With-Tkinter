import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import random


def fBoop():
    # This function just puts the word boop in the readout to check that something can call a function
    global gvReadoutText
    gvReadoutText.append("Boop")


def fUpdate():
    # This function executes all update code
    # Global variable references
    global gvReadoutText
    global gvReadoutWidget  # Global variable references
    # Readout Updater
    i = 0
    print(len(gvReadoutText))
    while i < len(gvReadoutText):
      gvReadoutWidget.insert("end", gvReadoutText[i])
      i += 1
    gvReadoutText = []  # Readout Updater
    # Re-calls the update function, change the number to change update speed
    root.after(100, fUpdate)


def fCreateButtonsMenu(fvButtonNames, fvButtonFunctions, fvContainerFrame):
   ButtonsMenuFrame = Frame(fvContainerFrame, bg=cElement1)
   i=0
   ButtonTitle = Label(ButtonsMenuFrame, text="Button Title", bg=cElement1, fg=cTextStandard)
   ButtonTitle.config(font=("Courier", 22))
   ButtonTitle.pack()
   ButtonFrame = Frame(ButtonsMenuFrame, bg=cElement1)
   while i < len(fvButtonNames):
      newButton = Button(ButtonFrame, text=fvButtonNames[i], command=fvButtonFunctions[i], height=2, width=20,
                         bg=cElement2, fg=cTextStandard)
      if i <= 9:
         newButton.grid(row=0, column=i)
      else:
         newButton.grid(row=1, column=i-10)
      i += 1
   ButtonFrame.pack(pady=5, padx=5)
   ButtonsMenuFrame.pack()


def fCreateReadout(fvBodyFrame):
   # global variable references
   global gvReadoutWidget  # global variable references
   # create the readout frame
   readoutFrame = Frame(fvBodyFrame, bg=cElement1, width=300, height=1160)  # create the readout frame
    # create the readout
   scrollbar = Scrollbar(readoutFrame, orient=VERTICAL)
   readoutTitle = Label(readoutFrame, text="Readout", fg=cTextStandard, bg=cElement1)
   readoutTitle.config(font=("Courier", 22))
   readoutTitle.pack(side=TOP)
   gvReadoutWidget = Listbox(readoutFrame, yscrollcommand=scrollbar.set, width=45, height=53, fg=cTextStandard, bg=cElement1)
   scrollbar.config(command=gvReadoutWidget.yview)
   scrollbar.pack(side=RIGHT, fill=Y)
   gvReadoutWidget.pack(side=TOP)  # create the readout
   # place the readout frame
   readoutFrame.place(x=0, y=0)  # place the readout frame


def fCreateSpace(fvBodyFrame):
    SpaceFrame = Frame(fvBodyFrame, bg=cBackground, width=1510, height=10)  # Create the space frame
    SpaceFrame.pack()


def fCreateTextbox(fvBodyFrame):
    # Create the textbox frame
    textboxFrame = Frame(fvBodyFrame, bg=cElement1)  # Create the textbox frame
    # Create the textbox frame
    TextBoxTitle = Label(textboxFrame, text="Textbox Title", bg=cElement1, fg=cTextStandard)
    TextBoxTitle.config(font=("Courier", 22))
    TextBoxTitle.pack()
    # Create the textbox
    textboxText = "Sample Text"
    textbox = Label(textboxFrame, text=textboxText, bg=cElement2, fg=cTextStandard, width=213, anchor='nw')
    textbox.pack(pady=5)  # Create the textbox
    # Place the textbox frame
    textboxFrame.pack(fill=X)  # Place the textbox frame


def fCreateGUI(fvRoot):
   fvRoot.state('zoomed')

   # create the background
   background = Frame(fvRoot, bg=cBackground, width=1980, height=1240)
   background.grid_propagate(False)
   background.pack_propagate(False)
   background.pack()

   # create the title
   titleFrame = Frame(background, bg=cBackground, width=1980, height=80)
   titleFrame.pack()

   title = Label(titleFrame, text="Title", bg=cBackground, fg=cTextBackContrast)
   title.config(font=("Courier", 44))

   # create the body
   bodyFrame = Frame(background, bg=cBackground, width=1880, height=900)
   bodyFrame.pack_propagate(False)
   bodyFrame.grid_propagate(False)
   bodyFrame.place(x=20, y=80)

   # create the readout
   fCreateReadout(bodyFrame)

   # create the widget frame
   widgetFrame = Frame(bodyFrame, bg=cBackground, width=1500, height=1160)

   # create the widgets
   buttonNameList = ["Button1", "Button2", "Button3 but it\n has a really long name", "Button4", "Button5", "Button6",
                     "Button7", "Button8", "Button9", "Button10", "Button1", "Button2",
                     "Button3 but it\n has a really long name", "Button4", "Button5"]
   buttonFunctionList = [fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop, fBoop,
                         fBoop, fBoop]
   fCreateButtonsMenu(buttonNameList, buttonFunctionList, widgetFrame)
   fCreateSpace(widgetFrame)
   fCreateTextbox(widgetFrame)
   widgetFrame.place(x=330, y=0)

   title.pack()


# GLOBAL VARIABLE DECLARATIONS

gvReadoutText = ["Start1", "Start2", "Start3"]
gvReadoutWidget = None

# colours
cBackground = "#263D42"
cElement1 = "#6D868B"
cElement2 = "#D8F3F9"
cTextStandard = "black"
cTextBackContrast = "white"    # GLOBAL VARIABLE DECLARATIONS
# GUI creation
root = Tk()
fCreateGUI(root)
fUpdate()
root.mainloop()  # GUI creation
