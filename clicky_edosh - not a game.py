from tkinter import *
from random import *
import winsound
w = Tk()
w.configure(bg = 'black')
w.title('Edosh')
w.call('wm', 'iconphoto', w._w, PhotoImage(file='edoshes/edoshicon.gif'))
c = Canvas(w, width=1000, height=700)
c.pack()
bg = PhotoImage(file="edoshhouse.gif")
bgp = c.create_image(700,400,image = bg)
img = PhotoImage(file="edoshes/edoshhappy.gif")
mychar = c.create_image(500,350,image = img)
ef = None
def make_edosh(event):
    global img, mychar, ef
    k = event.keysym.lower()
    print(k)
    if k == 't':
        ef = "edoshes/edoshmono.gif"
    elif k == 'w':
        ef = "edoshes/edoshcry.gif"
    elif k == 'o':
        ef = "edoshes/edoshosh.gif"
    elif k == 'r':
        ef = "edoshes/edoshyell.gif"
    elif k == 'b':
        ef = "edoshes/edoshblush.gif"
    elif k == 'g':
        ef = "edoshes/edoshglass.gif"
    elif k == 'k':
        ef = "edoshes/edoshkiss.gif"
    elif k == 'z':
        ef = "edoshes/edoshsleep.gif"
    elif k == 'h':
        ef = "edoshes/edoshhsmoosh.gif"
    elif k == 'v':
        ef = "edoshes/edoshvsmoosh.gif"
    elif k == 'd':
        ef = "edoshes/edoshdsmoosh.gif"
    elif k == 'p':
        ef = "edoshes/edoshdevil.gif"
    elif k == 'f':
        ef = "edoshes/edoshangel.gif"
    elif k == 'l':
        ef = "edoshes/edoshlaugh.gif"
    elif k == 'a':
        ef = "edoshes/edoshhappy.gif"
    elif k == 'e':
        ef = "edoshes/edoshxplode.gif"
    elif k == 'x':
        ef = "edoshes/edoshx.gif"
    elif k == 's':
        ef = "edoshes/edoshstick.gif"
    elif k == 'c':
        ef = "edoshes/edoshicon.gif"
    elif k == 'u':
        ef = "edoshes/edoshusmoosh.gif"
    elif k == 'm':
        ef = "edoshes/edoshearless.gif"
    elif k == 'i':
        ef = "edoshes/edoshpixel.gif"
    elif k == 'n':
        ef = "edoshes/edosheye.gif"
    elif k == 'q':
        ef = "edoshes/edoshamongus.gif"
    elif k == 'j':
        ef = "edoshes/edoshwhistle.gif"
    elif k == 'y':
        ef = "edoshes/edoshoshold.gif"
    elif k == '0':
        ef = "edoshes/edoshjoy.gif"
    elif k == '9':
        ef = "edoshes/edoshsadness.gif"
    elif k == '8':
        ef = "edoshes/edoshanger.gif"
    elif k == '7':
        ef = "edoshes/edoshfear.gif"
    elif k == '6':
        ef = "edoshes/edoshdisgust.gif"
    elif k == '5':
        ef = "edoshes/edoshangrybird.gif"
    elif k == '4':
        ef = "edoshes/edoshcolorswap.gif"
    elif k == '3':
        ef = "edoshes/edoshmonkey.gif"
    elif k == '2':
        ef = "edoshes/edoshgirl.gif"
    elif k == '1':
        ef = "edoshes/edoshcat.gif"
    try:
        img = PhotoImage(file=ef)
    except:
        pass
    c.itemconfigure(mychar,image = img)
c.bind_all('<Key>', make_edosh)
def move_edosh(event):
    c.coords(mychar, event.x, event.y)
c.bind_all('<Button-1>', move_edosh)
w.mainloop()
