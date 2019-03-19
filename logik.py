#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:56:18 2019

@author: spu35165
"""

import tkinter as tk
from tkinter import Canvas, LabelFrame, Label, Button
################     OKNA    #################
hlavni=tk.Tk()
hlavni.title("Logik")

SkryteBarvy=LabelFrame(hlavni)
SkryteBarvy.grid(row=0)

Barvy=LabelFrame(hlavni)
Barvy.grid(row=1, column=0)

BarvaPozice=LabelFrame(hlavni)
BarvaPozice.grid(row=1, column=1)

VyberBarvy = LabelFrame(hlavni)
VyberBarvy.grid(row=2)


###########Šířka a výška tlačítek   ##########
sirka=30
vyska=20
barvy="#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 #dd9900 #ffffff".split()
################   SKRYTE BARVY   #################
skryteBarvy=[]
for sloupec in range(5):
    skryteBarvy.append( Canvas(SkryteBarvy, background='grey', width=sirka, height=vyska) )
    skryteBarvy[-1].grid(column=sloupec,row=0)

skryteBarvy[0].config(background='#c90000')



###############    BARVY   ######################

barvyhadat=[]
for radek in range (10):
    for sloupec in range(5):
        barvyhadat.append(Canvas(Barvy, background="grey", width=sirka, height=vyska))
        barvyhadat[-1].grid(column=sloupec+1, row=radek+1)
Label(Barvy,text="LOGIK").grid(column=0, columnspan=6, row=0)





Label(BarvaPozice, text="Barva / Pozice").grid(column=0) 
stats=[]    
for radek in range(10):
    stats.append(Label(BarvaPozice, text="-/-", padx=3, pady=3))
    stats[-1].grid()


############   BARVY VYBER   ######################
x=44
def odeslat():
    global x
    x=x-10


OdeslatButton=Button(VyberBarvy,command=odeslat, text="Potvrdit")
OdeslatButton.grid(row=radek+1)
    

    
for radek in range(1):
    for sloupec, barva in enumerate(barvy):
        def fce(s=sloupec, b=barva):
            barvaClick(s,b)
        b=tk.Button(VyberBarvy, width=sirka-4, height=vyska-1, bitmap="gray12", activebackground=barva, activeforeground=barva, bg=barva, fg=barva, command=fce)
        b.grid(row=radek, column=sloupec)    


def barvaClick(sloupec, barva):
    global x
    if x<=49:
        x=x+1
        barvyhadat[x].config(background=barva)
        

    
   

    

    
        
#skryteBarvy[0].config(background='green')

#barvyhadat[0].config(background="green")








hlavni.mainloop()