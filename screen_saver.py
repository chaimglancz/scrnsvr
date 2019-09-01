from tkinter import *
from random import randint
root=Tk()
root.geometry('700x600')
root.configure(bg='#000000')
xx=35
yy=300
aa=1
cc=1
lst=['2','4','6','8','a','c','e','f']
def af():
    global xx
    global yy
    global cc
    global aa
    global bb
    global dd
    #xx=kk
    #yy=ll
    if xx > 700 or xx < 0 :
        
    #if (xx >= 700 and xx <= 706) or (xx >= 0 and xx <= 6):
        
    #if xx==700 or xx==701 or xx==702 or xx==703 or xx==704 or\
        #xx==705 or xx==706 or xx==0 or xx==1 or xx==2 or xx==3\
        #or xx==4 or xx==5 or xx==6 :
        aa+=1
    bb=aa%2
    if yy > 600 or yy < 0 :
    #if yy==600 or yy==601 or yy==602 or yy==603 or yy==604 or\
        #yy==605 or yy==606 or yy==0 or yy==1 or yy==2 or yy==3\
        #or yy==4 or yy==5 or yy==6 or yy==7 or yy==607:    
        cc+=1
    dd=cc%2
    if bb==0:
         xx-=6.7
    elif bb==1 :
         xx+=6.7  
    if dd==0:
        yy-=3.7
    elif dd==1:
        yy+=3.7
    #ee=randint(0,7)
    #ff=randint(0,7)
    #gg=randint(0,7)
    #hh=randint(0,7)
    #ii=randint(0,7)
    #jj=randint(0,7)
    colour_pieces = [ lst[randint(0, 7)] for n in range(6) ]    
    root1=Frame(root)
    #root1.configure(bg='#'+lst[ee]+lst[ff]+lst[gg]+lst[hh]+lst[ii]+lst[jj])
    root1.configure(bg='#'+ ''.join(colour_pieces))
    root1.place(width=7,height=7,x=xx,y=yy)
    root.after(30,af)
af()   

root.mainloop()
