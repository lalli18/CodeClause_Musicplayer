from tkinter import filedialog
from tkinter import *
import pygame
import os
window=Tk()
window.title('MUSIC PLAYER')
window.geometry("600x400")
pygame.mixer.init()
menubar=Menu(window)
window.config(menu=menubar)
songs=[]
current_song=""
paused=False
def load_music():
    global current_song
    window.directory=filedialog.askdirectory()
    for song in os.listdir(window.directory):
        name,ext=os.path.splitext(song)
        if ext=='.mp3':
            songs.append(song)
    for song in songs:
        songlist.insert("end",song)

    songlist.selection_set(0)
    current_song=songs[songlist.curselection()[0]]
def play_music():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory,current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False
def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused=True
def next_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu=Menu(menubar,tearoff=False)
organise_menu.add_command(label='Select the folder',command=load_music)
menubar.add_cascade(label='Organise',menu=organise_menu)

songlist=Listbox(window,bg="purple",fg="beige",width=120,height=20)
songlist.pack()
play_btn_image=PhotoImage(file='play.png')
pause_btn_image=PhotoImage(file='pause.png')
next_btn_image=PhotoImage(file='next.png')
prev_btn_image=PhotoImage(file='previous.png')
control_frame=Frame(window)
control_frame.pack()
play_btn=Button(control_frame,image=play_btn_image,borderwidth=0,command=play_music)
pause_btn=Button(control_frame,image=pause_btn_image,borderwidth=0,command=pause_music)
next_btn=Button(control_frame,image=next_btn_image,borderwidth=0,command=next_music)
prev_btn=Button(control_frame,image=prev_btn_image,borderwidth=0,command=prev_music)
play_btn.grid(row=0,column=1,padx=7,pady=12)
pause_btn.grid(row=0,column=2,padx=7,pady=12)
next_btn.grid(row=0,column=3,padx=7,pady=12)
prev_btn.grid(row=0,column=0,padx=7,pady=12)
window.mainloop()