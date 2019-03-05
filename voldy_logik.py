#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:09:12 2019

@author: vol35098
"""

import tkinter as tk



class Application(tk.Tk):
    name = 'Logik'
    
    def __init__(self):
        super().__init__(className = self.name)
        self.title(self.name)
        self.barvy = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 #dd9900 #ffffff".split()
        self.sirka = 30
        self.vyska = 20
        #skrytá pole#
        self.skryteBarvy = []
        for sloupec in range(5):
            c = tk.Canvas(self, background='black', width=self.sirka, 
                          height=self.vyska)
            c.grid(column=sloupec, row=0)
            self.skryteBarvy.append(c)
        
        #titulek#
        tk.Label(self, text="Logik").grid(columnspan=5) #roztahnutí přez více sloupců
        
        #pole s hádanou barvou#
        self.hadaneBarvy = []
        for radek in range(10):
            radekBarev = []
            for sloupec in range(5):
                c = tk.Canvas(self, background='darkgray', width=self.sirka, 
                              height=self.vyska)
                c.grid(column=sloupec, row=radek + 2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)
        self.hadaneBarvy[1][4].config(background='magenta')
        
        #oddelovaci cara
        c = tk.Canvas(self, background='#777', width=6*self.sirka, height=8)
        c.grid(column=0, row=12, columnspan=5)
        
        #oodpoved programu   (-/-)
        odpovedProgramu = []
        for radek in range(10):
            lbl = tk.Label(self,text='-/-')
            lbl.grid(column=6, row=radek+2)
            odpovedProgramu.append(lbl)
            
        #tlacitka
        for radek, barvy in enumerate(self.barvy):
            for sloupec in range(5):
                def akce(r=radek, s=sloupec):
                    self.click(r, s)
                b = tk.Button(width=self.sirka, height=self.vyska, 
                              bg=barvy, fg= barvy, bitmap='gray12',
                              command=akce)     #bitmap - velikosti tlacitek v pismu ne v pixlech
                b.grid(row=radek+12, column=sloupec)
                
    def click(self, r, s):
        print(r, s)
                              
       
        
app = Application()
app.mainloop()