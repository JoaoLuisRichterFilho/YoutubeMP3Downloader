from turtle import color, width
from typing_extensions import Self
from pytube import YouTube
import os
from tkinter import *

def download():
    watch = str(inputWatch.get())
    print(watch)
    # watch = input("Input the video watch: ") 
    # YouTube('https://youtu.be/'+watch).streams.first().download()
    yt = YouTube('https://youtu.be/'+watch)
    out_file = yt.streams.filter( mime_type="audio/mp4", abr="128kbps",  progressive=False, type="audio").first().download()
    os.rename(out_file, 'new.mp3')

janela = Tk()
janela.title("Download Youtube Music")
janela.geometry("500x200")

texto = Label(janela, text="Input youtube watch and click in Download:")
texto.grid(column=0, row=0, padx=10, pady=10)

inputWatch = Entry(janela, font="Calibri 12")
inputWatch.grid(column=0, row=1, ipadx=90, ipady=2, padx=10, pady=10)

botao = Button(janela, text="Download", font="Calibri 10", command=download, foreground="#fafafa", background='#149825')
botao.grid(column=1, row=1, padx=10, pady=1, ipady=1)


# texto_resposta = Label(janela, text="")
# texto_resposta.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()

