import tkinter as tk
from tkinter import *
from pytube import Youtube
from tkinter import messagebox, filedialog

def CreateWidges():
    linkLabel = Label(root, text = "ENTER THE VIDEO LINK : ", bg = "skyblue")
    linkLabel.grid(row=1, column = 0, pady = 5, padx = 5)

    root.linkText = Entry(root, width = 60)
    root.linkText.grid(row = 1, column = 1, pady = 5, padx = 5, columnspan = 2)

    destinationLabel = Label(root, text = "SAVE DESTINATION : ", bg = "skyblue")
    destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5)

    root.destinationText = Entry(root, width = 38)
    root.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5)

    browseButton = Button(root, text = "Browse", command = Browse, width = 15)
    browseButton.grid(row = 2, column = 2, pady = 5, padx = 5)

    dwldButton = Button(root, text = "DOWNLOAD", command = Download, width = 30)
    dwldButton.grid(row = 3, column = 1, pady = 5, padx = 5)

def Browse():
    root.destinationDIR = filedialog.askdirectory(initialdir = "C:\Python\PyVideo")
    root.destinationText.insert('1', root.destinationDIR)

def Download():
    getVideo = YouTube(root.linkText.get())
    videoStream = getVideo.streams.first()
    videoStream.download(root.destinationDIR)
    massagebox.showinfo("SUCCESS!,", "VIDEO DOWNLOADED AND SAVED IN\n" + root.destinationDIR)   
root = tk.Tk()
root.geometry("530*110")
root.title("youtube-video-downloader by eliorcc")
root.resizable(False, False)
root.config(background = "skyblue")
CreateWidges()
root.mainloop() 