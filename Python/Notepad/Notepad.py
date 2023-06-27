import sys
sys.path.append('/users/maria/Documents')

from typing import LiteralString
import tkinter 
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import *
self.__thisTextArea.grid(sticky = N + E + S + W)
self.__thisFileMenu.add_command(label = "New",
                               command = self._newFile)
self.__thisFileMenu.add_command(label = "Open",
                              command = self.openFile)
self.__thisFileMenu.add_command(label = "Save",
                               command = self.savefile)
self.thisFileMenu.add_seperator()
self.__thisFileMenu.add_command(label = "Exit",
                                command = self.__quitApplication)
self.__thisMenuBar.add_cascade(label = "File",
                               menu = self.__thisFileMenu)
self.__thisEditMenu.add_command(label = "Cut",
                                command = self.__cut)
self.__thisEditMenu.add_command(label = "Copy",
                                command = self.__copy)
self.__thisEditMenu.add_command(label = "Paste",
                                command = self.__paste)
self.__thisMenuBar.add_cascade(label = "Edit",
                               menu = self.__thisEditmenu)

# Create a feature of description
self.__thisHelpMenu.add_command(label = "About Notepad",
                                command = self.__showAbout)
self.thisMenuBar.add_cascade(label = "Help",
                             menu = self.__thisHelpmenu)
self.__root.config(menu = self.__thisMenuBar)
self.__thisScrollBar.pac(side= RIGHT, fill = Y)

# Scrollbar adjust according to content
self.__thisScrollBar.config(command = self.__thisTextArea.yview)
self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)



import os
from tkinter import END
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


def __quitApplication(self):
    self.__root.destroy()
    # exit()
def __showAbout(self):
    showinfo("Notepad", "Mrinal Verma")
def __openFile(self):
    self.__file = askopenfilename(defaultextension=".txt",
                                  filetypes=[("All Files","*.*"),
                                         ("Text Documents","*.txt")])    
    if self.__file == "":

      # no file to open
      self.__file = None
    else:
        # try to open the file // set the window title
        self.__root.title(os.path.basename(self.__file) + " - Notepad")
        self.__thisTextArea.delete(1.0,END)
        file = open(self.__file, "r")
        self.__thisTextArea.insert(1.0,file.read())
        file.close()
def __newFile(self):
    self._root.title("Untitled - Notepad")
    self.__file = None
    self.__thisTextArea.delete(1.0,END)
def __saveFile(self):
    if self.__file == None:
        self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                        defaulttextension=".txt",
                                        filetypes=[("All Files","*.*"),
                                                   ("Text Documents","*.txt")])
        if self.__file == "":
            self.__file = None
        else: # save file
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
            self.__root.title(os.path.basename(self.__file) + " - Notepad") # change window title
    else:
        file = open(self.__file,"w")
        file.write(self.__thisTextArea.get(1,0,END))
        file.close()
def __cut(self):
    self.__thisTextArea.event_generate("<<Cut>>")
def __copy(self):
    self.__thisTextArea.event_generate("<<Copy>>")
def __paste(self):
    self.__thisTextArea.event_generate("<<Paste>>")
def __bold(self):
    self.__thisTextArea.event_generate("<<Bold>>")
def __italic(self):
    self.__thisTextArea.event_generate("<<Italic>>")
def __underline(self):
    self.__thisTextArea.event_generate("<<Underline>>")
def __color(self):
    self.__thisTextArea.event_generate("<<Color>>")

from ast import Pass
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    __root = Tk()
    #default window w & h
    __thisWidth = 300
    __thisheight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff = 0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff = 0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff = 0)
    # add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        # Set Icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        # Window Size
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
          pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
          pass
        self.__root.title("Untitled - Notepad")
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        left = (screenWidth /2) - (self.__thisWidth /2)
        top = (screenHeight / 2) - (self.__thisHeight /2)
        self.__root.geomety('%dx%d+%d+%d' % (self.__thisWidth,
                                             self.__thisHeight,
                                             left, top))
        # auto resize
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky = N + E + S + W)
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)
        self.__thisFileMenu.add_seperator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self._quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)
        self.__thisEditMenu.add_command("Cut",
                                        command=self.__cut)
        self.__thisEditMenu.add_command("Paste",
                                        command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__ThisEditMenu)
        self.__thisEditMenu.add_command(label="Bold",
                                        command=self.__bold)
        self.__thisEditMenu.add_command(label="Italic",
                                        command=self.__italic)
        self.__thisEditMenu.add_command(label="Underline",
                                        command=self.__underline)
        self.__thisEditMenu.add_command(label="Color",
                                        command=self.__color)
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    def __quitApplication(self):
        self.__root.destroy() 
    def __showAbout(self):
         showinfo("Notepad", "Mrinal Verma")
    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                                 ("Text Documents","*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()
    def __newFile(self):
        self.__root.title("Untitle - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                ("Text Documents","*.txt")])
            if self.__file == "":
                self.__file = None
            else: 
                file = open(self.__file,"w")
                file.write(self._thisTextArea.get(1.0,END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()
notepad = Notepad(width=600,height=400)
notepad.run()