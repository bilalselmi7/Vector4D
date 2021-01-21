# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:42:52 2020

@author: SELMI Bilal
"""

import math
import tkinter as tk

class Vect4D:
    
    def __init__(self,x,y,z,t):
        self.x=x
        self.y=y
        self.z=z
        self.t=t
        
    def __str__(self):
        return "\nx="+str(self.x)+"\ny="+str(self.y)+"\nz="+str(self.z)+"\nt="+str(self.t)
    
    def __abs__(self):
        return math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2 + (self.t)**2)
    
    def __add__(self,vecteur):
        return Vect4D (self.x+vecteur.x , self.y+vecteur.y , self.z+vecteur.z , self.t+vecteur.t)
    
    def __sub__(self,vecteur):
        return Vect4D (self.x-vecteur.x , self.y-vecteur.y , self.z-vecteur.z , self.t-vecteur.t)
    
    def __eq__(self,vecteur):
        return (self.x==vecteur.x) and (self.y==vecteur.y) and (self.z==vecteur.z) and (self.t==vecteur.t)
    
    def __mul__(self,other):
        result = None
        if isinstance(other,Vect4D):
            result = self.x*other.x + self.y*other.y + self.z*other.z + self.t*other.t
        elif isinstance(other,int) or isinstance(other,float):
            result = Vect4D (self.x*other , self.y*other , self.z*other , self.t*other)
        return result
    
    def __getitem__(self,indice):
        if indice == 0:
            return self.x
        elif indice == 1:
            return self.y
        elif indice == 2:
            return self.z
        elif indice == 3:
            return self.t
        else:
            return None
        
    def __setitem__(self,indice,value):
        if indice == 0:
            self.x = value
        elif indice == 1:
            self.y = value
        elif indice == 2:
            self.z = value
        elif indice == 3:
            self.t = value
        else:
            return None
        
class Mat4D:
    
        def __init__(self,v1=Vect4D,v2=Vect4D,v3=Vect4D,v4=Vect4D):
            self.v1 = v1
            self.v2 = v2
            self.v3 = v3
            self.v4 = v4
            
        def __str__(self):
            return "[" + "[" + str(self.v1) + "]\n" + "[" + str(self.v2) + "]\n" + "[" + str(self.v3) + "]\n" + "[" + str(self.v4) + "]"+"]"
        
        def __add__(self,matrice):
            a = self.v1 + matrice.v1
            b = self.v2 + matrice.v2
            c = self.v3 + matrice.v3
            d = self.v4 + matrice.v4
            return Mat4D(a,b,c,d)
        
        def __sub__(self,matrice):
            a = self.v1- matrice.v1
            b = self.v2 - matrice.v2
            c = self.v3 - matrice.v3
            d = self.v4 - matrice.v4
            return Mat4D(a,b,c,d)
        
        def __eq__(self, matrice):
            return (self.v1 == matrice.v1) and (self.v2 == matrice.v2) and (self.v3 == matrice.v3) and (self.v4 == matrice.v4)
    
        def __mul__(self,other):
            reponse = None
            if isinstance(other,Vect4D): 
                
               a = self.v1.x*other.x + self.v1.y*other.y + self.v1.z*other.z + self.v1.t*other.t
               b = self.v2.x*other.x + self.v2.y*other.y + self.v2.z*other.z + self.v2.t*other.t
               c = self.v3.x*other.x + self.v3.y*other.y + self.v3.z*other.z + self.v3.t*other.t
               d = self.v4.x*other.x + self.v4.y*other.y + self.v4.z*other.z + self.v4.t*other.t
               reponse = Vect4D(a,b,c,d)
               
            elif isinstance(other, int) or isinstance(other,float): 
               a = Vect4D(self.v1.x*other , self.v1.y*other , self.v1.z*other , self.v1.t*other)
               b = Vect4D(self.v2.x*other , self.v2.y*other , self.v2.z*other , self.v2.t*other)
               c = Vect4D(self.v3.x*other , self.v3.y*other , self.v3.z*other , self.v3.t*other)
               d = Vect4D(self.v4.x*other , self.v4.y*other , self.v4.z*other , self.v4.t*other)
               reponse = Mat4D(a,b,c,d)
                              
            elif isinstance(other,Mat4D):
              a=Vect4D(self.v1.x*other.v1.x+self.v1.y*other.v2.x+self.v1.z*other.v3.x+self.v1.t*other.v4.x,self.v1.x*other.v1.y+self.v1.y*other.v2.y+self.v1.z*other.v3.y+self.v1.t*other.v4.y,self.v1.x*other.v1.z+self.v1.y*other.v2.z+self.v1.z*other.v3.z+self.v1.t*other.v4.z,self.v1.x*other.v1.t+self.v1.y*other.v2.t+self.v1.z*other.v3.t+self.v1.t*other.v4.t)
              b=Vect4D(self.v2.x*other.v1.x+self.v2.y*other.v2.x+self.v2.z*other.v3.x+self.v2.t*other.v4.x,self.v2.x*other.v1.y+self.v2.y*other.v2.y+self.v2.z*other.v3.y+self.v2.t*other.v4.y,self.v2.x*other.v1.z+self.v2.y*other.v2.z+self.v2.z*other.v3.z+self.v2.t*other.v4.z,self.v2.x*other.v1.t+self.v2.y*other.v2.t+self.v2.z*other.v3.t+self.v2.t*other.v4.t)  
              c=Vect4D(self.v3.x*other.v1.x+self.v3.y*other.v2.x+self.v3.z*other.v3.x+self.v3.t*other.v4.x,self.v3.x*other.v1.y+self.v3.y*other.v2.y+self.v3.z*other.v3.y+self.v3.t*other.v4.y,self.v3.x*other.v1.z+self.v3.y*other.v2.z+self.v3.z*other.v3.z+self.v3.t*other.v4.z,self.v3.x*other.v1.t+self.v3.y*other.v2.t+self.v3.z*other.v3.t+self.v3.t*other.v4.t)  
              d=Vect4D(self.v4.x*other.v1.x+self.v4.y*other.v2.x+self.v4.z*other.v3.x+self.v4.t*other.v4.x,self.v4.x*other.v1.y+self.v4.y*other.v2.y+self.v4.z*other.v3.y+self.v4.t*other.v4.y,self.v4.x*other.v1.z+self.v4.y*other.v2.z+self.v4.z*other.v3.z+self.v4.t*other.v4.z,self.v4.x*other.v1.t+self.v4.y*other.v2.t+self.v4.z*other.v3.t+self.v4.t*other.v4.t)
              reponse = Mat4D(a,b,c,d)
    
            return reponse
        
        def __getitem__(self,indice):
            if indice == 0:
                return self.x
            elif indice == 1:
                return self.y
            elif indice == 2:
                return self.z
            elif indice == 3:
                return self.t
            else:
                return None
        
        def __setitem__(self,indice,value):
            if indice == 0:
                self.v1 = value
            elif indice == 1:
                self.v2 = value
            elif indice == 2:
                self.v3 = value
            elif indice == 3:
                self.v4 = value
            else:
                return None
            

def Id4D():
    return Mat4D(Vect4D(1,0,0,0) , Vect4D(0,1,0,0) , Vect4D(0,0,1,0) , Vect4D(0,0,0,1))

def SymX():
    return Mat4D(Vect4D(-1,0,0,0),Vect4D(0,1,0,0),Vect4D(0,0,1,0),Vect4D(0,0,0,1))

def SymY():
    return Mat4D(Vect4D(1,0,0,0),Vect4D(0,-1,0,0),Vect4D(0,0,1,0),Vect4D(0,0,0,1))

def SymZ():
    return Mat4D(Vect4D(1,0,0,0),Vect4D(0,1,0,0),Vect4D(0,0,-1,0),Vect4D(0,0,0,1))

def TransX(a):
    return Mat4D(Vect4D(1,0,0,a),Vect4D(0,1,0,0),Vect4D(0,0,1,0),Vect4D(0,0,0,1))

def TransY(a):
    return Mat4D(Vect4D(1,0,0,0),Vect4D(0,1,0,a),Vect4D(0,0,1,0),Vect4D(0,0,0,1))

def TransZ(a):
    return Mat4D(Vect4D(1,0,0,0),Vect4D(0,1,0,0),Vect4D(0,0,-1,a),Vect4D(0,0,0,1))

def RotX(Θ):
    return Mat4D(Vect4D(1,0,0,0),Vect4D(0,math.cos(Θ),math.sin(Θ),0),Vect4D(0,-math.sin(Θ),math.cos(Θ),0),Vect4D(0,0,0,1))

def RotY(Θ):
    return Mat4D(Vect4D(math.cos(Θ),0,math.sin(Θ),0),Vect4D(0,1,0,0),Vect4D(-math.sin(Θ),0,math.cos(Θ),0),Vect4D(0,0,0,1))

def RotZ(Θ):
    return Mat4D(Vect4D(math.cos(Θ),math.sin(Θ),0,0),Vect4D(-math.sin(Θ),math.cos(Θ),0,0),Vect4D(0,0,1,0),Vect4D(0,0,0,1))
        
def Tkinter():

    window = tk.Tk()
    window.config(background = '#FA8072')
    label_titre = tk.Label(window,text="Mat4D",font = ("Arial", 14), bg ='#FA8072', fg = 'White') #font donne la police d'écriture
    label_titre.grid(row=0,column=35)
    #frame.grid(row = 0, column = 3600)
    
    teta1 = tk.Label(window, text = "θ1",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    teta2 = tk.Label(window, text = "θ2",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    teta3 = tk.Label(window, text = "θ3",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    teta4 = tk.Label(window, text = "θ4",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
    e4 = tk.Entry(window)
    
    xentry = tk.Entry(window)
    yentry=tk.Entry(window)
    zentry=tk.Entry(window)
    
    teta1.grid(row = 2, column = 25,  pady = 2)
    teta2.grid(row = 4, column = 25,  pady = 2)
    
    e1.grid(row=2,column = 30, pady =2)
    e2.grid(row=4,column = 30, pady =2)
    
    teta3.grid(row = 2, column = 40,  pady = 2)
    teta4.grid(row = 4, column = 40,  pady = 2)
    
    e3.grid(row=2,column = 41, pady =2)
    e4.grid(row=4,column = 41, pady =2)
    
    l = tk.Label(window, text = "L",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    lentry = tk.Entry(window)
    l.grid(row=9,column=34)
    lentry.grid(row=9, column=35)
    
    x = tk.Label(window, text = "X",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    y = tk.Label(window, text = "Y",font = ("Arial", 14), bg ='#F08080', fg = 'White')
    z = tk.Label(window, text = "Z",font = ("Arial", 14), bg ='#F08080', fg = 'White')
                 
    x.grid(row = 11, column = 0,  pady = 2)
    xentry.grid(row=11,column = 20,sticky = "W", pady =2)
    
    
    y.grid(row = 11, column = 34)
    yentry.grid(row=11,column = 35)
    
    z.grid(row = 11, column = 55)
    zentry.grid(row=11,column = 60, sticky = "E")
    
    nom_matrice = tk.Label(window, text = "matrice = ",font = ("Arial", 14), bg ='#FA8072', fg = 'White')
    nom_matrice.grid(row = 20, column = 30)
    
    phrase_vecteur = tk.Label(window, text = "Le vecteur en coordonnées absolu est : = ",font = ("Arial", 14), bg ='#FA8072', fg = 'White')
    phrase_vecteur.grid(row =60,column = 35)
    
    
    def EnregistrerValeur():
        
       a=e1.get()
       b=e2.get()
       c=e3.get()
       d=e4.get()
       l=lentry.get()
       x = xentry.get()
       y=yentry.get()
       z=zentry.get()
       
       matrice1 = RotX(float(a))
       matrice2 = RotX(float(b))
       matrice3 = RotX(float(c))
       matrice4 = RotX(float(d))
       matriceL = TransX(float(l))
       
       matricefinal=matrice1*matrice2*matrice3*matrice4*matriceL
       
       affichage_matrice=tk.Label(window, text = matricefinal ,font = ("Arial", 14), bg ='#CD5C5C', fg = 'White')
       affichage_matrice.grid(row = 20, column = 35)
       
       
       vecteur = Vect4D(float(x),float(y),float(z),1)
       matricetransformation = matricefinal*vecteur
       
       affichage_vecteur =tk.Label(window, text = matricetransformation.__str__() ,font = ("Arial", 14), bg ='#CD5C5C', fg = 'White')
       affichage_vecteur.grid(row = 60, column = 36)
    
       
    
    bouton1 = tk.Button(window, text = "Afficher", command = EnregistrerValeur,font = ("Arial", 14), bg ='#CD5C5C', fg = 'White' )
    bouton1.grid(row=80, column =35)
    
    btn1 = tk.Button(window, text ="Quitter", command = window.destroy,font = ("Arial", 14), bg ='#CD5C5C', fg = 'White' ) 
    btn1.grid(row=120, column = 100, sticky="E") 
    
    
    
    #afficher l'application
    window.mainloop()
    
Tkinter()
          
        
        
        
        
        
        
        
    