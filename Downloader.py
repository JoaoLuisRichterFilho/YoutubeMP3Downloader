import mimetypes
from tkinter import filedialog
import tkinter
from turtle import color, width
from typing_extensions import Self
from pytube import YouTube
import os
from tkinter import *
import shutil
import clipboard
import base64

def file_save(out_file):
    file_name, file_extension = os.path.splitext(out_file)
    arrayName = file_name.split("\\")
    file_path = filedialog.asksaveasfilename(confirmoverwrite=False, filetypes=[("MP3 File", ".mp3")], defaultextension=".mp3", initialfile=arrayName.pop())
    if(file_path):
        os.rename(out_file, 'file.mp3')
        shutil.move('file.mp3', file_path)
        clear()
        tkinter.messagebox.showinfo(title="Sucesso!", message="MP3 Baixado com sucesso!")
    
    try:
        cdir = os.getcwd()
        test = os.listdir(cdir)
        for item in test:
            if item.endswith(".mp4"):
                os.remove(os.path.join(cdir, item))
    except:
        print("Fail to delete files .mp4")
        

def download():
    print("Quality: " + str(v.get()))
    YoutubeLink = str(inputYoutubeLink.get())
    # print(YoutubeLink)
    if(YoutubeLink):
        try:
            quality = str(v.get())
            mime_type = ''
            if quality == "128":
                mime_type = 'audio/mp4'
            else:
                mime_type = 'audio/webm'

            print("Mime Type: " + mime_type)
            yt = YouTube(YoutubeLink)
            out_file = yt.streams.filter( mime_type=mime_type, abr=quality+"kbps",  progressive=False, type="audio").first().download()
            file_save(out_file)
        except:
            tkinter.messagebox.showerror(title="Falha!", message="Por favor, tente uma qualidade de áudio diferente!")


def clear():
    inputYoutubeLink.delete(0,END)

def paste():
    clip = clipboard.paste()
    inputYoutubeLink.delete(0,END)
    inputYoutubeLink.insert(0,clip.strip())

janela = Tk()
janela.title("Download Youtube Music")
janela.geometry("800x300")

iconDelB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAA7EAAAOxAGVKw4bAAATUklEQVR42gFHE7jsAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAIB/fwB9fn4AhICACu7l5dT//////v7+/v///////////////////////////v7+/v/////u5OTUhICACn1+fgCAf38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAIB/fwB5enoAmZOTK/38/Pr+/f38/fz8/P79/fz+/f38/v39/P79/fz+/f38/fz8/P79/fz9/Pz6mZOTK3l6egCAf38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAF4eXkAn5eXNP//////////////////////////////////////////////////////////n5eXNHh5eQCAgIABgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAH+AgAB/f38AgYGBAoGBgQOBgYECgYGBA4GBgQN8fX0DmJGRJ+Td3cLk3d3C5N3dwuTd3cLk3d3C5N3dwuTd3cLk3d3C5N3dwuTd3cLk3d3CmJGRJ3x9fQOBgYEDgYGBA4GBgQKBgYEDgYGBAn9/fwB/gIAAgICAAICAgACAgIAAAICAgACAgIAAf39/AICAgAB/gIAAeHl5AHd3dwB3eHcAd3d3AHd3dwB3eHgAdnZ2AHNxcQBzcXEAc3FxAHNxcQBzcXEAc3FxAHNxcQBzcXEAc3FxAHNxcQBzcXEAdnZ2AHd4eAB3d3cAd3d3AHd4dwB3d3cAeHl5AH+AgACAgIAAf39/AICAgACAgIAAAICAgACAgIAAgICAAH5+fgB+fHwAop2dQKuoqFerp6hWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVqunqFarqKhXop2dQH58fAB+fn4AgICAAICAgACAgIAAAICAgACAgIAAf39/AXt5egDRyMiZ/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9HHx5l7eXkAf39/AYCAgACAgIAAAICAgACAgIAAent7AJGNjR////////////7+/v3+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v79//////////+RjY0fent7AICAgACAgIAAAICAgACAgIAAeXp6AJWTkyv///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+Vk5MreXp6AICAgACAgIAAAICAgACAgIAAent7AJSRkSf++fn4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P75+fiUkZEnent7AICAgACAgIAAAICAgACAgIAAf39/AIOBgQSSjIwdkoyMHY+KihePiYoXj4qKF4+JihePiYoXj4mKF4+JihePiYoXj4mKF4+JihePiooXj4mKF4+JihePiYoXj4qKF4+JihePiYoXj4mKF4+JihePiYoXj4qKF4+JihePiooXkoyMHZKMjB2DgYEEf39/AICAgACAgIAAAICAgACAgIAAgICAAH9/fwB7fHwAe3x8AISEhAqFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyEhIQKfHx8AHt8fAB/f38AgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB+fn4AgX9/Aurk5ND49/fx9/X18Pj29vH49vbx+Pb28fj29vH49vbx+Pb28fj29vH49vbx+Pb28fj39/H49vbx+Pb28fj29vH49vbx+Pb28fj29vH49vbx9/X18Pj39/Ho4+POgX5+AX5+fgCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38Afnt7AOvm5tP////////////////////////////////////////////////////////////////////////////////////////////////////////////////p5OTPfXt7AH9/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38Aenl5AOHc3L///////v39/P/+/v///////v7+/v/+/v/////////////////+/v7+//7+//7+/v7//////////////////////v7+/v///////v7//f39/P/////f2dm6eXh4AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIABeHd3ANnU1K///////v7++////////v7//v7+/f/+/v6zrKxfpZ6eQ/z6+vj+/v7+//7+//7+/v78+vr4o52dQbWtrWL//v7//v7+/f/+/v///////v7++//////W0NCod3d3AICAgAGAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECdnZ2ANHLzJ7//////v7+/P///////v7////////9/f2PiYkVfnx8APfy8un///////39///////z8PDnent6AJCKihn//f3////////9/f///v7//v7+/P/////Nx8eWdnZ2AIGBgQKAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIADdXV1AMnDw43//////v7+/P/+/v///v7//v7+/v/8/PyVj48ghYKCBfjz8+r+/v7+//7+//7+/v7y8PDogIGAApaQkCT//Pz//v7+/v/+/v///////v7++//////Evr6DdXV1AICBgQOAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECdnV1AMC6unv//////v7++////////v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogIGAApaQkCT//f3////////+/v///v7//v7+/P////+6tLRxdXZ2AIGBgQKAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECdXZ2ALexsWr//////v39/P/+/v///f3////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogIGAApaQkCT//f3////////+/v///f3//f39/f////+yq6tednd3AICAgAOAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIADdnd3AK6pqVj//////f7+/f/9/f///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v///v7//v7+/v/+/v+ooqNMd3h4AIGBgQKAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECd3h4AKagoUj//v7//v7+/v/+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogIGAApaQkCT//f3////////+/v///f3///////7///+fmpo7eHl5AICAgAGAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIABeHl5AJ6ZmTj+///////////9/f///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v///v7//v7+/v/+/v+Yk5MreXp6AIB/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAf38AeXp6AJeSkin//v7//v///v/+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogH+AApaQkCT//f3////////+/v///v7///////36+vqQjIwdent7AH+AgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/gIAAent7AJCMjBz9+vr5///////+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v/+/f3///////j19e+JhoYRe3x8AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAe3x8AImGhhH49PXv//////79/f7//v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v///v7///////Pu7uOEgYEGfX19AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAfX19AISBgQbz7+/k///////+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v/+/v7+/////+zn59V/fX0Afn9/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAfn5+AIB9fQDt6OjY//////7+/v7//v7//v///v/9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3//v7+/v/+/v/+/v79/////+Xf38Z8enoAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AHx6egDm4eHJ//////7+/v3//v7////////8/PyUjo4ehIGBBPfy8uj///////39///////y8PDmf39/AZWPjyL//Pz////////+/v/9/v78/////9zW17V4eHgAgICAAYCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAHl4eADe2dm5//////3+/vz//f3//v7+/v/9/f2Si4wcgXx8APn19e7+/v7+//7+//7+/v728/Ptfnt7AJSNjR///f3//v7+/v/9/f/+/v79/////9TOzqN2dnYAgYGBAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAXd3dwDW0dGp//////7+/v3//v7//v7+/f/////j3d3C3NXWs//+/v/+/v7+//7+//7+/v7//v7/3NXVsuTe3sP//////v39/f/+/v/+/v79/////8rFxZF1dXUAgYGBA4CAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBAnZ2dgDOyMiY//////7+/v3///////7+///+/v7//////////////////v7////////+/v/+/////////////////v7///7+///////+/v79//7+/8G7u352dXUAgICAAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBA3V1dQDIwcGK//////39/fz//////v///v/////+/v79/f39/P/////+///+//7+//7///7//////f39/P7+/v3//////v///v/+/v/9/f38/////7qzs291dnYAgYGBA4CAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAnZ3dwCyrK1g/v7+/v7+/v3//v7+//////////////////////////////////////////////////////////////////////7+/v7+/v79/v39/aagoEd3eHgAgICAAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgH9/AH5+fgCAfX0F5tzcxf7////+/v79//////////////////////////////////////////////////////////////////7+//7+/v3/////3tLSsX16egB/f38Bf39/AICAgACAgIAAgICAAICAgACAgIAAPsPVMoHn1bMAAAAASUVORK5CYII=
'''
iconDel0 = base64.b64decode(iconDelB64)
iconDel  = PhotoImage(data=iconDel0)

iconDownloadB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAIGNIUk0AAHolAACAgwAA+f8AAIDoAABSCAABFVgAADqXAAAXb9daH5AAAAEOSURBVHja7FZdSsYwENyJ+OoBBB989JYew8vom/fwACUUEvoQmxkfbKSK9vezn2AWAs1Cdic76e5Akm0xSRmAG74J4GJLHGdntgqgAqgATgUAlYIK4F8CUKXgEADe+6t3zaG8NCjJZGby3t8tUTZz68NI5uIn2Y/8LP6ccxqfaZrmeio+5iTZILcw2guAk9QXGVZ8JJNz7nJNm56lYEim0R6S+F3Z1yY3M0MJXm6xtBJ7BtQ4FvSZA6yhY8d01Kbf8CsdpxjNq/vATyAGHw5pRABcCOGe5CvJPsb4MPV+Fj3Cvcpm6xz5W63Ye3/z2wnbtr2douD4CqSUXs6VPMb4ZJKs67pnHWwhhEdJ9jYATSdxC6Kfg2EAAAAASUVORK5CYII=
'''
iconDownload0 = base64.b64decode(iconDownloadB64)
iconDownload  = PhotoImage(data=iconDownload0)

iconPasteB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFwSURBVFiF7dfNShxBFAXgL0MkgoSMBHyFIIMhm4A7XfoEcaHJKmvBhaCBBAZExFfIA4T4CCELcREIbpxRx5eQoAiiJCRZVDU2Mz0/sXtmEftAU123761z6nZDn+K+40Gf51W8xxwmc3Jd4xBbOBmkYBzH+FPwdYVaQvKwh4BXMfEIb3E2iOo+G1rHa2xguV/BjqB4LSdxGs/jmo0k0N6BcSziGeZjbAFP70B2jW/4kor9jONYVkHVcN75xxTHdIy1kkC6Ax/cvvNP+P0v283ABFaE7+czvvYr+B7VzeYkTqMe16zHeUcHKqnkx3G8KFDAedvaHah0ezAqlAJKAaWAUkApYNQCqnG8TAK9LFmReCnYsKU4389Kagm/yukCiVd1GpQmniQJo+rAgWBITrGLmywBv4YgKvF+e3iXlZAmO8KM4IK3BVOZB1N4E++bgxTUhEND0aa0gUfdSNuPZjWhVS8Ei54HP4TWbyrW5v1n+AuAlXpNOiJQbAAAAABJRU5ErkJggg==
'''
iconPaste0 = base64.b64decode(iconPasteB64)
iconPaste  = PhotoImage(data=iconPaste0)

texto = Label(janela, font="Calibri 12", width=40, text='Input the "Youtube Link" and click in Download:')
texto.grid(column=0, columnspan=4, row=0, padx=2, pady=10, sticky=W,)

inputYoutubeLink = Entry(janela, font="Calibri 12")
inputYoutubeLink.grid(column=0, row=1, ipadx=185, ipady=2, padx=10, pady=0)

btnPaste = Button(janela, image=iconPaste, command=paste, foreground="#fafafa", background='#FBBC05')
btnPaste.grid(column=1, row=1, padx=10, pady=1, ipady=2, ipadx=2)

btnDownload = Button(janela, image=iconDownload, command=download, foreground="#fafafa", background='#149825')
btnDownload.grid(column=2, row=1, padx=10, pady=1, ipady=2, ipadx=2)

btnClear = Button(janela, image=iconDel, command=clear, foreground="#fafafa", background='#EA3E3E')
btnClear.grid(column=3, row=1, padx=10, pady=1, ipadx=1, ipady=1)

texto2 = Label(janela, font="Calibri 12", text='Quality:')
texto2.grid(column=0, columnspan=4, row=2, padx=5, pady=0, sticky=W,)

def setQuality():
    print(v.get())

v = tkinter.IntVar()
v.set(1)

qualities = [("50kbps", 50),
   	         ("70kbps", 70),
   	         ("128kbps", 128),
   	         ("160kbps", 160)]

row = 3
for quality, val in qualities:
    tkinter.Radiobutton(janela, 
                   text=quality,
                   padx = 20, 
                   variable=v, 
                   command=setQuality,
                   value=val).grid(column=0, row=row, padx=1, pady=0, sticky=W,)
    row+=1

# texto_resposta = Label(janela, text="")
# texto_resposta.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()

