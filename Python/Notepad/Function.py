

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