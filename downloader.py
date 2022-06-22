import youtube_dl
import tkinter
from tkinter import *


def get_mp3():
    #la variable stringg récupère l'url qui est entré sur l'application
    stringg = entry.get()
    #on récupère toutes les infos sur la vidéo et on gère les paramètres pour télécharger la vidéo youtube comme par exemple le titre, le format ou autres
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=stringg, download=False
    )
    #gère les options qu'on veux pour notre vidéo
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        #grâce au info qu'on a récupèrer au dessus on met le titre puis le format (mp3) pour le fichier qui va être download
        'outtmpl': f"{video_info['title']}.mp3",

    }
    #dowload la vidéo sous le options qu'on lui a imposé
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

#même code que celui au dessus mais sous un autre format
def get_mp4():
    stringg = entry1.get()
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=stringg, download=False
    )

    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'keepvideo': True,
        'outtmpl': f"{video_info['title']}.mp4",
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

#petite fenêtre tkinter toute simple 
root = Tk()
root.title("Downloader")
root.geometry("1150x250")
root.iconbitmap('asset/iconn.ico')

label = Label(root,text="Download mp3",font='Helvetica 14')
label.grid(row=0, column=0,padx=25,pady=5)

entry = Entry(root,width=40,font='Helvetica 14')
entry.grid(row=1, column=0,padx=25,pady=5)

button = Button(root, text="Download MP3 Format !",font='Helvetica 14', command=get_mp3)
button.grid(row=2,column=0,padx=25,pady=5)



label1 = Label(root,text="Download mp4",font='Helvetica 14')
label1.grid(row=0, column=2,padx=25,pady=5)

entry1 = Entry(root,width=40,font='Helvetica 14')
entry1.grid(row=1, column=2,padx=25,pady=5)

button1 = Button(root, text="Download MP4 Format !",font='Helvetica 14', command=get_mp4)
button1.grid(row=2,column=2,padx=25,pady=5)

credit = Label(root,text="Created by Exarven",font='Helvetica 14')
credit.grid(row=3, column=1, pady=30)

root.mainloop()