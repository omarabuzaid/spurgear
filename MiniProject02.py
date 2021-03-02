from tkinter import *
from functools import partial
from tkinter import filedialog
import pandas as pd
import xlrd
import matplotlib.pyplot as plt
from tkinter.ttk import Combobox
from math import *
from PIL import Image, ImageTk


    
def Gear(Speed,Power,Np,Ng,Av,Jp,Jg,I,Pd,Sat,Sac,Ep,Eg):    
    try:
         temp=""
         i=0
    
    #Pd 
    ################################
         if diap.get() == 1:
             if list.current() == 0:
                 PD=1.25
                 
             if list.current() == 1:
                 PD=2.0
                 
             if list.current() == 2:
                 PD=3.0
                 
             if list.current() == 3:
                 PD=4.0
                                    
         if diap.get() == 2:
             PD=float(Pd.get())
               
    #Ko 
    ################################
    
         if cb1.current() == 0:
             
              if cb2.current() == 0:
                 Ko=1.0
              if cb2.current() == 1:
                 Ko=1.25
              if cb2.current() == 2:
                 Ko=1.5
              if cb2.current() == 3:
                 Ko=1.75
              i=1
              
         if cb1.current() == 1:
             
              if cb2.current() == 0:
                 Ko=1.2
              if cb2.current() == 1:
                 Ko=1.4
              if cb2.current() == 2:
                 Ko=1.75
              if cb2.current() == 3:
                 Ko=2.25
              i=1
              
         if cb1.current() == 2:
             
              if cb2.current() == 0:
                 Ko=1.3
              if cb2.current() == 1:
                 Ko=1.7
              if cb2.current() == 2:
                 Ko=2.0
              if cb2.current() == 3:
                 Ko=2.75
              i=1
             
    #Ks
    #################################
         if PD < 5:
             if PD == 1.25:
                Ks = 1.4   
             if PD == 2:
                Ks = 1.25
             if PD == 3:
                Ks = 1.15
             if PD == 4:
                Ks = 1.05
     
         if PD>=5:
             Ks=1.0
              
    #Km 
    ####################################
         Dp = float(Np.get())/PD
         Dg = float(Ng.get())/PD
         Vt = pi*Dp*float(Speed.get())/12
         F=12/PD
         Speedg = float(Speed.get())*float(Np.get())/float(Ng.get())
          
          
         if F <= 1:
             Cpf = F/(10*Dp)-0.025
         else:
             Cpf = F/(10*Dp)-0.0375+0.0125*F   
            
            
         if Cma1.get() == 1:
             Cma = 0.247+0.0167*F-0.0000765*F**2
             i=1
         if Cma1.get() == 2:
             Cma = 0.127+0.0158*F-0.0001093*F**2
             i=1
         if Cma1.get() == 3:
             Cma = 0.0675+0.0128*F-0.0000926*F**2
             i=1  
         if Cma1.get() == 4:
             Cma = 0.038+0.0102*F-0.0000822*F**2
             i=1
         
         Km = 1+Cpf+Cma
         
    #KB
    #####################################
         
         if rim.get() == 1:
             ht = 2.2/PD+0.002
             mB = float(tR.get())/ht
             KB = 1.6*log(2.242/mB) 
             
         if rim.get() == 2:
             tR = 0
             KB = 1.0
             
    #Kv
    ######################################
             
         B=0.25*(float(Av.get())-5.0)**0.667
         C=50+56*(1.0-B)
         
         Kv=(C/(C+Vt**0.5))**(-B)
         
    #Force Analysis
    ######################################
         
         Wt=126000*float(Power.get())/(float(Speed.get())*Dp)
    
    #Bending Stress
    #####################################
    
         Stp=Ko*Ks*Km*KB*Kv*((Wt*PD)/(F*float(Jp.get())))
         Stg=Ko*Ks*Km*KB*Kv*((Wt*PD)/(F*float(Jg.get())))
         
         
    
    #Contact Stress
    #####################################
         Cp=sqrt((10**6)/(pi*((0.91/float(Ep.get()))+(0.91/float(Eg.get())))))                           
         Sc=Cp*sqrt((Wt*Ko*Ks*Km*Kv)/(F*Dp*(float(I.get()))))
         
    
    #Yn && Zn
    ####################################     
         if Life.current() == 0:
            L=1500
         if Life.current() == 1:
            L=2500
         if Life.current() == 2:
            L=3250
         if Life.current() == 3:
            L=4500
         if Life.current() == 4:
            L=11500
         if Life.current() == 5:
            L=25000
         if Life.current() == 6:
            L=25000
         if Life.current() == 7:
            L=50000
         if Life.current() == 8:
            L=150000
            
         Ncp=60*L*float(Speed.get())*1
         Ncg=60*L*Speedg*1
         if Ncp >= 7*(10**6):             
             YNp = 1.3558*Ncp**(-0.0178)
         if Ncg >= 7*(10**6):
             YNg = 1.3558*Ncg**(-0.0178)
         if Ncp < 7*(10**6) or Ncg < 7*(10**6):
             def YNcalc(Ncp,Ncg):
                 nonlocal YNp
                 nonlocal YNg
                 if Ncp < 7*(10**6):                     
                     if HBfinder.get() == 1:
                         YNp = 9.4518*Ncp**(-0.148)
                     if HBfinder.get() == 2:
                         YNp = 6.1514*Ncp**(-0.1192)
                     if HBfinder.get() == 3:
                         YNp = 4.9404*Ncp**(-0.1045)
                     if HBfinder.get() == 4:
                         YNp = 3.517*Ncp**(-0.0817)
                     if HBfinder.get() == 5:
                         YNp = 2.319*Ncp**(-0.0538)
                         
                 if Ncg < 7*(10**6): 
                     if HBfinder.get() == 1:
                         YNg = 9.4518*Ncg**(-0.148)
                     if HBfinder.get() == 2:
                         YNg = 6.1514*Ncg**(-0.1192)                     
                     if HBfinder.get() == 3:
                         YNg = 4.9404*Ncg**(-0.1045)                     
                     if HBfinder.get() == 4:
                         YNg = 3.517*Ncg**(-0.0817)                     
                     if HBfinder.get() == 5:
                         YNg = 2.319*Ncg**(-0.0538)
                                     
                 top2.destroy()
                 
             top2 = Toplevel(top)   
             Label(top2, text="Select Material Type").place(x=40, y=10)
             HBfinder=IntVar()
             HBfinder.set(False)
             n1=Radiobutton(top2, text="400 HB", variable=HBfinder , value=1)
             n2=Radiobutton(top2, text="Case-carb", variable=HBfinder , value=2)
             n3=Radiobutton(top2, text="250 HB", variable=HBfinder , value=3)
             n4=Radiobutton(top2, text="Nitrited", variable=HBfinder , value=4)
             n5=Radiobutton(top2, text="160 HB", variable=HBfinder , value=5)
             n1.place(x=40, y=30)
             n2.place(x=40, y=50)
             n3.place(x=40, y=70)
             n4.place(x=40, y=90)
             n5.place(x=40, y=110)            
             n = Button(top2, text='Calculate', command = partial(YNcalc,Ncp,Ncg))
             n.place(x=40 , y=140)    
             top2.wait_window()
             
                 
         
    ############################################  
                 
         if Ncp >= 10**7:
             ZNp = 1.4488*Ncp**(-0.023)
         elif HBfinder.get() == 4:
             ZNp = 1.249*Ncp**(-0.0138)
         else:
             ZNp = 2.466*Ncp**(-0.056)

              
         if Ncg >= 10**7:
             ZNg = 1.4488*Ncg**(-0.023)
         elif HBfinder.get() == 4:
             ZNg = 1.249*Ncg**(-0.0138)
         else:
             ZNg = 2.466*Ncg**(-0.056)    

                 
   #KR
    ###################################
    
         if Rlist.current() == 0:
             KR = 1.50
         if Rlist.current() == 1:
             KR = 1.25
         if Rlist.current() == 2:
             KR = 1.00
         if Rlist.current() == 3:
             KR = 0.85
            
    #SF
    ######################################
         
         SFtp = float(Sat.get())*(10**3)*YNp/(Stp*KR)
         SFtg = float(Sat.get())*(10**3)*YNg/(Stg*KR) 
         
         SFcp = float(Sac.get())*(10**3)*ZNp/(Sc*KR)
         SFcg = float(Sac.get())*(10**3)*ZNg/(Sc*KR) 
         
         temp += "Pinion Bending Stress Number = " + str(round(Stp, 3)) + "\n" 
         temp += "Gear Bending Stress Number = "  + str(round(Stg, 3)) + "\n"
         temp += "Contact Stress Number = " +  str(round(Sc, 3)) + "\n"
         temp += "Pinion Bending Factor of Safety = "  + str(round(SFtp, 3)) + "\n"
         temp += "Gear Bending Factor of Safety = " +  str(round(SFtg, 3)) +  "\n"
         temp += "Pinion Contact Factor of Safety = " +  str(round(SFcp, 3)) + "\n"
         temp += "gear Contact Factor of Safety = " +  str(round(SFcg, 3)) +  "\n"
         
         
         # if i==0:
         #     temp="no operation selected"
         result.configure(text=temp)
         return
    except:        
        xx.configure(text="Wrong or Missing Input Detected")
         
    
    

#Window
##################################################################### 
top = Tk()
top.geometry("1100x630")
top.title("Bending and Contact Stresses Calculator")

#Layout
##################################################################### 


x = Label(top, text="")
x.place(x=500, y=500)



canvas_width = 1020
canvas_height =630
w = Canvas(top,width=canvas_width,height=canvas_height)
w.place(x=10 ,y=0)
#title_font = font.Font(size=8, weight='bold')

# background = Image.open(r"gear.png")
# filenameb = ImageTk.PhotoImage(background,master=w)
# w.image = filenameb 
# w.create_image(0,0,anchor='nw',image=filenameb)


w.create_line(15, 20, 700, 20, fill="grey")
w.create_line(15, 20, 15, 255, fill="grey")
w.create_line(15, 255, 700, 255, fill="grey")
w.create_line(700, 255, 700, 20, fill="grey")
title1=Label(top,text="Input Data")
title1.place(x=40, y=10)

y0=293
y1=528
w.create_line(15, y0, 700, y0, fill="grey")
w.create_line(15, y1, 700, y1, fill="grey")
w.create_line(15, y0, 15, y1, fill="grey")
w.create_line(700, y0, 700, y1, fill="grey")
title2=Label(top,text="Application")
title2.place(x=40, y=280)
#title1['font'] = title_font

xx=Label(top,text="",bg="white")
xx.place(x=790,y=190)

title3=Label(top,text="Results",bg="white")
title3.place(x=835, y=160)
w.create_rectangle(750, 150, 1000, 400, fill="white")


#Widgets
##################################################################### 

#Text Entry Boxes
Speed=Entry(top)
Power=Entry(top)
Np=Entry(top)
Ng=Entry(top)
Av=Entry(top)
Ep=Entry(top)
Jp=Entry(top)
Jg=Entry(top)
Sat=Entry(top)
Sac=Entry(top)
I=Entry(top)
Eg=Entry(top)

#--------------------------------------------------------------------

#Diamterial_Pitch
def Diap_check():
    if diap.get() == 1:
        list.config(state=NORMAL)
        Pd.config(state=DISABLED)
    if diap.get() == 2:
        list.config(state=DISABLED)
        Pd.config(state=NORMAL)

diap = IntVar() 
diap.set(False)
Diap1 = Radiobutton(top, text="Pd < 5 (in)", variable=diap,value=1, command = Diap_check)
Diap1.place(x=30, y=40)
Diap2 = Radiobutton(top, text="Pd ≥ 5 (in)", variable=diap,value=2, command = Diap_check)
Diap2.place(x=260, y=40)

var = StringVar()
var.set("1.25")
data=('1.25','2','3','4')
list=Combobox(top, values=data,state=DISABLED)
list.place(x=110, y=40)
Pd=Entry(top, state=DISABLED)
Pd.place(x=350, y=40)
list.bind("<<ComboboxSelected>>",lambda e: Speed.focus())
#--------------------------------------------------------------------

#Applications for Ko
Label(top, text="Driver Gear Work Conditions").place(x=30, y=363)
var = StringVar()
var.set("Uniform")
data=('Uniform','Light Shock','Moderate Shock')
cb1=Combobox(top, values=data)
cb1.place(x=200, y=363)
cb1.bind("<<ComboboxSelected>>",lambda e: Speed.focus())


Label(top, text="Driven Gear Work Conditions").place(x=360, y=363)
var = StringVar()
var.set("Uniform")
data=('Uniform','Light Shock','Moderate Shock','Heavy Shock')
cb2=Combobox(top, values=data)
cb2.place(x=530, y=363)
cb2.bind("<<ComboboxSelected>>",lambda e: Speed.focus())

#--------------------------------------------------------------------

#Radiobuttons for Cma for Ks/Applications 
Label(top, text="Choose a Gear Type").place(x=60, y=403)
Cma1=IntVar()
Cma1.set(False)
r1=Radiobutton(top, text="Open Gearing", variable=Cma1 , value=1)
r2=Radiobutton(top, text="Commercial Enclosed", variable=Cma1 , value=2)
r3=Radiobutton(top, text="Precision Enclosed", variable=Cma1 , value=3)
r4=Radiobutton(top, text="Extra-Precsion Enclosed", variable=Cma1 , value=4)
r1.place(x=60, y=423)
r2.place(x=60, y=443)
r3.place(x=60, y=463)
r4.place(x=60, y=483)
#--------------------------------------------------------------------

#Rim state for KB
def Rim_check():
    if rim.get() == 1:
        tR.config(state=NORMAL)
    if rim.get() == 2:
        tR.config(state=DISABLED)
        
rim = IntVar() 
rim.set(False)
rim1 = Radiobutton(top, text="Rim ", variable=rim,value=1, command = Rim_check)
rim1.place(x=400, y=463)
rim2 = Radiobutton(top, text="Solid Blanks", variable=rim,value=2, command = Rim_check)
rim2.place(x=400, y=433)

tR=Entry(top, state=DISABLED)
Label(top, text="Choose Rim Type").place(x=400, y=403)
tR.place(x=405, y=493)
#--------------------------------------------------------------------

#Application/for design life L
Label(top, text="Choose Application").place(x=30, y=323)
life = StringVar()
life.set("Domestic Appliances")
data=('Domestic Appliances','Aircraft engines','Automotive','Agricutral Equipment','Elevators, indutrial fans, multipurpose gearing','Electric motors, industrial blowers', 'general industrial machines','Pumps and compressors','Critical Equipment in continuous 24-h operation')
Life=Combobox(top, values=data,width=70)
Life.place(x=160, y=323)
Life.bind("<<ComboboxSelected>>",lambda e: Speed.focus())

#--------------------------------------------------------------------

#Reliability 
R= StringVar()
R.set("99.99%")
data=('99.99%','99.9%','99%','90%')
Rlist=Combobox(top, values=data)
Rlist.place(x=525, y=70)
Rlist.bind("<<ComboboxSelected>>",lambda e: Speed.focus())


#Function Calling & Buttons
##################################################################### 
button1 = Button(top, text='Calculate Bending and Contact Stresses',bg="red",fg="white", command =partial(Gear,Speed,Power,Np,Ng,Av,Jp,Jg,I,Pd,Sat,Sac,Ep,Eg))     

quit = Button(top, text="Done, Exit",bg="black",fg="white", command=top.destroy)


#Widget Labels
##################################################################### 
label1 = Label(top,text="Pinion Speed (RPM)")
label1.place(x=30, y=120)
Speed.place(x=170, y=120)

label2 = Label(top,text="Power (HP)")
label2.place(x=30, y=140)
Power.place(x=170, y=140)

label3 = Label(top,text="Pinion teeth No.")
label4 = Label(top,text="Gear teeth No.")
label3.place(x=30, y=160)
label4.place(x=30, y=180)
Np.place(x=170, y=160)
Ng.place(x=170, y=180)

label6 = Label(top,text="Quality Number")
label6.place(x=30, y=200)
Av.place(x=170, y=200)

label8 = Label(top,text="Bending Geometry Factor(P)")
label9 = Label(top,text="Bending Geometry Factor(G)")
label8.place(x=320, y=120)
label9.place(x=320, y=140)
Jp.place(x=485, y=120)
Jg.place(x=485, y=140)

label12 = Label(top,text="Allowable Bending Stress (ksi)")
label13 = Label(top,text="Allowable Contact Stress (ksi)")
label12.place(x=320, y=160)
label13.place(x=320, y=180)
Sat.place(x=485, y=160)
Sac.place(x=485, y=180)

label14 = Label(top,text="Pitting Geometry Factor ")
label14.place(x=320, y=200)
I.place(x=485, y=200)

label7 = Label(top,text="Elastic modulue(P)(msi)")
label9 = Label(top,text="Elastic modulue(G)(msi)")
label7.place(x=30, y=220)
label9.place(x=320, y=220)
Ep.place(x=170, y=220)
Eg.place(x=485, y=220)

label15 = Label(top,text="Reliablity")
label15.place(x=525, y=40) 

result =Label(top,bg="white")
result2 = Label(top, fg="red",bg="white")

button1.place(x=750, y=40)
quit.place(x=825, y=70)
result.place(x=770, y=190)



##################################################################### 


def loadImage1():
    new_window1 = Toplevel()
    new_window1.title("Bending Geometry Factor Graph 20")
    img = Image.open(r"J20.png")
    filename = ImageTk.PhotoImage(img)
    canvas = Canvas(new_window1,height=700,width=1000)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    canvas.grid()
    
    
k = Button(top, text="J 20°", bg="#939d9e",fg="black", command=loadImage1)
k.place(x=620, y=130)


################

def loadImage2():
    new_window2 = Toplevel()
    new_window2.title("Bending Geometry Factor Graph 25")
    img = Image.open(r"J25.png")
    filename = ImageTk.PhotoImage(img)
    canvas = Canvas(new_window2,height=750,width=1000)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    canvas.grid()
    
    
k = Button(top, text="J 25°",bg="#939d9e",fg="black", command=loadImage2)
k.place(x=660, y=130)

################

def loadImage3():
    new_window3 = Toplevel()
    new_window3.title("Pitting Geometry Factor Graph 20")
    img = Image.open(r"I20.png")
    filename = ImageTk.PhotoImage(img)
    canvas = Canvas(new_window3,height=700,width=1100)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    canvas.grid()
    
    
k = Button(top, text="I 20°",bg="#939d9e",fg="black", command=loadImage3)
k.place(x=620, y=195)

################

def loadImage4():
    new_window4 = Toplevel()
    new_window4.title("Pitting Geometry Factor Graph 25")
    img = Image.open(r"I25.png")
    filename = ImageTk.PhotoImage(img)
    canvas = Canvas(new_window4,height=700,width=1100)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    canvas.grid()
    
    
k = Button(top, text="I 25°",bg="#939d9e",fg="black", command=loadImage4)
k.place(x=660, y=195)

################

def loadImage5():
    new_window5 = Toplevel()
    new_window5.title("Diametral Pitch Graph")
    img = Image.open(r"Pd.png")
    filename = ImageTk.PhotoImage(img)
    canvas = Canvas(new_window5,height=750,width=600)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    canvas.grid()
      
k = Button(top, text="Diametral Pitch Graph for steels",bg="#939d9e",fg="black", command=loadImage5)
k.place(x=200, y=70)
################

#Finally, draw the window + start the application
top.mainloop()
    
    
