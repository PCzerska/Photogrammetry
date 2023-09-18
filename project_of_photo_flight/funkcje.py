from tkinter import *
from tkinter import ttk
from baza import samoloty,kamery
from math import ceil, pi


def rysowanie(window):
    frame = LabelFrame(window)
    frame.grid(row=1, column=1)
    frame1 = LabelFrame(window)
    frame1.grid(row=1, column=0)

    lbl1 = Label(frame1, text="Wybierz samolot: ")
    lbl1.grid(column=0, row=0)
    lbl2 = Label(frame1, text="Wybierz kamerę: ")
    lbl2.grid(column=0, row=1)
    lbl3 = Label(frame1, text="Podaj terenowy rozmiar pixela GSD w cm: ")
    lbl3.grid(column=0, row=2)
    lbl4 = Label(frame1, text="Podaj średnią wysokość terenu w m: ")
    lbl4.grid(column=0, row=3)
    lbl5 = Label(frame1, text="Podaj pokrycie poprzeczne w %: ")
    lbl5.grid(column=0, row=4)
    lbl5 = Label(frame1, text="Podaj pokrycie podłużne w %: ")
    lbl5.grid(column=0, row=5)
    lbl6 = Label(frame1, text="Podaj zasięg obszaru opracowania w poprzek kierunku lotu: ")
    lbl6.grid(column=0, row=6)
    lbl7 = Label(frame1, text="Podaj zasięg obszaru opracowania wzdłuż kierunku lotu: ")
    lbl7.grid(column=0, row=7)
    lbl8 = Label(frame1, text="Podaj współrzędną X lewego dolnego narożnika: ")
    lbl8.grid(column=0, row=8)
    lbl9 = Label(frame1, text="Podaj współrzędną Y lewego dolnego narożnika: ")
    lbl9.grid(column=0, row=9)

    var1 = StringVar()
    wart1 = ["1." + samoloty[0].nazwa, "2." + samoloty[1].nazwa, "3." + samoloty[2].nazwa, "4." + samoloty[3].nazwa]
    cb1 = ttk.Combobox(frame, textvariable=var1)
    cb1['values'] = wart1
    cb1['state'] = 'readonly'

    cb1.grid(column=1, row=0)

    var2 = StringVar()
    wart2 = ["1." + kamery[0].nazwa, "2." + kamery[1].nazwa, "3." + kamery[2].nazwa, "4." + kamery[3].nazwa]
    cb2 = ttk.Combobox(frame, textvariable=var2)
    cb2['values'] = wart2
    cb2['state'] = 'readonly'

    cb2.grid(column=1, row=1)

    txt3 = Entry(frame, width=20)
    txt3.grid(row=2, column=1, padx=15, pady=1)

    txt4 = Entry(frame, width=20)
    txt4.grid(row=3, column=1, padx=15, pady=1)

    txt5 = Entry(frame, width=20)
    txt5.grid(row=4, column=1, padx=15, pady=1)

    txt6 = Entry(frame, width=20)
    txt6.grid(row=5, column=1, padx=15, pady=1)

    txt7 = Entry(frame, width=20)
    txt7.grid(row=6, column=1, padx=15, pady=1)

    txt8 = Entry(frame, width=20)
    txt8.grid(row=7, column=1, padx=15, pady=1)

    txt9 = Entry(frame, width=20)
    txt9.grid(row=8, column=1, padx=15, pady=1)

    txt10 = Entry(frame, width=20)
    txt10.grid(row=9, column=1, padx=15, pady=1)

    text_area = Text(window)
    text_area.grid(row=3, column=0, columnspan=2, rowspan=2, pady=3)


    return cb1,cb2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10,text_area

def obliczenia(f, GSD, px, hsr, pulap, wym1, wym2, v1, v2, cykl, p, q, Dx, Dy):
    W = (f * (GSD*10)) / (px/1000)
    W = W / 1000
    Wabs= W + hsr


    if(wym1 > wym2):
        lx = wym2
        ly = wym1
    else:
        lx = wym1
        ly = wym2

    Lx = lx * (GSD/100)
    Ly = ly * (GSD/100)

    Bx = Lx * (100-p)/100
    By = Ly * (100-q)/100

    Ny= ceil(Dy/By)
    Nx= ceil(Dx/Bx + 4)

    By= Dy/Ny
    Bx= Dx/(Nx-4)

    v1= v1/3.6
    v2= v2/3.6
    V= v1+v2/2
    delt = Bx/V

    N= Nx * Ny
    Pn = Bx * By
    Pob = Dx * Dy
    K = N * Pn / Pob


    return Wabs, Nx, Ny, Bx, By, N, Pob, Pn,Lx,Ly,K,delt
