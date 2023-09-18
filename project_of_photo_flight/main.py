from baza import samoloty,kamery
from math import ceil, pi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as img
from tkinter import *
from funkcje import rysowanie, obliczenia
window = Tk()
window.title("Projekt nalotu fotogrametrycznego:")
window.geometry('1425x650')


cb1,cb2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10,text_area=rysowanie(window)
cb1.current(0)
cb2.current(0)

def pobierz_wartosci():

    global GSD,hsr,samolot,kamera,p,q,Dy,Dx,x,y
    nr1 = cb1.current()
    samolot = samoloty[nr1]

    nr2 = cb2.current()
    kamera = kamery[nr2]

    if float(txt3.get())<0:
        text_area.insert(END,"GSD nie może być ujemne!!\n")
    else:
        GSD = float(txt3.get())

    if float(txt4.get())<0:
        text_area.insert(END,"Średnia wysokość nie może być ujemna!!\n")
    else:
        hsr = float(txt4.get())

    if float(txt5.get())<30 or float(txt5.get())>100:
        text_area.insert(END,"Pokrycie poprzeczne powinno być w zakresie 30-100!!\n")
    else:
        q = float(txt5.get())

    if float(txt6.get())<60 or float(txt6.get())>100:
        text_area.insert(END,"Pokrycie podłużne powinno być w zakresie 60-100!!\n")
    else:
        p = float(txt6.get())

    if float(txt7.get())<0 or float(txt8.get())<0:
        text_area.insert(END,"Zasięg nie powinien być mniejszy 0!!\n")
    else:
        Dy = float(txt7.get())
        Dx = float(txt8.get())

    x = float(txt9.get())
    y = float(txt10.get())

    return samolot,kamera,GSD,hsr,q,p,Dy,Dx,x,y



def wyniki():
    H, Nx, Ny, Bx, By, N, Pob, Pn, Lx, Ly,K,delt = obliczenia(kamera.ogniskowa, GSD, kamera.wym_pix, hsr, samolot.pulap,
                                                       kamera.wym_matr1, kamera.wym_matr2, samolot.predkosc_min,
                                                       samolot.predkosc_max, kamera.cykl,p,q,Dx,Dy)
    if (H > samolot.pulap):
        text_area.insert(END, "Wysokość absolutna jest większa od maksymalnego pułapu!!!")
    if (delt < kamera.cykl):
        text_area.insert(END,"interwał czasu pomiędzy ekspozycjami (Δt) jest mniejszy od cyklu pracy kamery!!")
    text_area.insert(END,"H:"+str(round(H,2))+" m"+"\n")
    text_area.insert(END,"Nx:"+str(Nx)+"\n")
    text_area.insert(END,"Ny:" + str(Ny)+"\n")
    text_area.insert(END,"Bx:" + str(round(Bx,2))+"\n")
    text_area.insert(END,"By:" + str(round(By,2))+"\n")
    text_area.insert(END, "N:" + str(N)+"\n")
    text_area.insert(END,"Pob:" + str(round(Pob,2))+" m^2\n")
    text_area.insert(END, "Pn:" + str(round(Pn,2))+" m^2\n")
    text_area.insert(END, "Lx:" + str(Lx)+"\n")
    text_area.insert(END, "Ly:" + str(Ly)+"\n")
    text_area.insert(END, "K:" + str(K) + "\n")


    fig=plt.figure(figsize=(6,4))
    iksy = []
    igreki = []
    Ykolo = []

    #Rysowanie punktów
    for i in range(Ny):
        temp_x = []
        temp_y = []
        for j in range(Nx):
            X = x + j * Bx - 1.5 * Bx
            Y = By/2 + y + i * By
            iksy.append(X)
            igreki.append(Y)
            temp_x.append(X)
            temp_y.append(Y)
        Ykolo.append(Y)
        plt.plot(temp_x, temp_y, color='red', linewidth=2)
        plt.text(temp_x[0], temp_y[0], f"{i + 1}      ", fontsize=10, color='black', ha='right', va='center')
    minX = min(iksy)
    maxX = max(iksy)
    plt.scatter(iksy, igreki, color='red')

     #Zaznaczanie punktów początkowych i końcowych
    if Ny%2==0:
        rys_pocz_x = max(iksy)
        rys_pocz_y = max(igreki)
        plt.scatter(rys_pocz_x,rys_pocz_y,color='green')
        plt.annotate(u'\u2708', xy=(rys_pocz_x, rys_pocz_y), xytext=(rys_pocz_x + 10, rys_pocz_y + 10),
                     xycoords='data', textcoords='data',
                     fontsize=20, ha='center',rotation=180)
    else:
        rys_pocz_x = min(iksy)
        rys_pocz_y = max(igreki)
        plt.scatter(rys_pocz_x, rys_pocz_y, color='green')
        plt.annotate(u'\u2708', xy=(rys_pocz_x, rys_pocz_y), xytext=(rys_pocz_x + 10, rys_pocz_y + 10),
                     xycoords='data', textcoords='data',
                     fontsize=20, ha='center')

    rys_kon_x = max(iksy)
    rys_kon_y = min(igreki)
    plt.scatter(rys_kon_x, rys_kon_y, color='green')
    plt.annotate(u'\u2708', xy=(rys_kon_x, rys_kon_y), xytext=(rys_kon_x + 10, rys_kon_y + 10),
                 xycoords='data', textcoords='data',
                 fontsize=20, ha='center')

    # Rysowanie łuków
    for i in range(Ny):
        while i < Ny - 1:
            xstart, ystart = minX, Ykolo[i]
            xkoniec, ykoniec = minX, Ykolo[i + 1]
            promien = abs((ykoniec - ystart) / 2)
            srodek = (xstart, (ystart + ykoniec) / 2)
            kat = np.linspace(pi / 2, 3 / 2 * pi, 300)
            xl = srodek[0] + promien * np.cos(kat)
            yl = srodek[1] + promien * np.sin(kat)
            plt.plot(xl, yl, color='red', linewidth=2)
            i = i + 2
        else:
            break

    for i in range(Ny):
        while i < Ny - 2:
            xstart, ystart = maxX, Ykolo[i + 1]
            xkoniec, ykoniec = maxX, Ykolo[i + 2]

            promien = abs((ykoniec - ystart) / 2)
            srodek = (xstart, (ystart + ykoniec) / 2)

            kat = np.linspace(-pi / 2, pi / 2, 300)
            xl = srodek[0] + promien * np.cos(kat)
            yl = srodek[1] + promien * np.sin(kat)


            plt.plot(xl, yl, color='red', linewidth=2)
            i = i + 2

        else:
            break
    droga_kol = (Ny - 1) * np.pi * promien


    #Rysowanie siatki
    for i in range(Ny):
        for j in range(0, Nx - 4):
            xp = x + j * Bx - 3* Bx / 4
            yp = y + i * By - By / 4

            rect = ptch.Rectangle((xp, yp), Lx, Ly, linewidth=1, edgecolor='blue', facecolor='none')
            plt.gca().add_patch(rect)

    # Droga i Czas
    droga = ((Nx+3) * (Dx/Nx)) * Ny
    droga = droga + droga_kol
    droga_cal = round((droga + droga_kol)/1000,2)
    text_area.insert(END, "Droga: " + str(droga_cal)+"km\n")
    min_czas = droga / (samolot.predkosc_max/3.6)
    minczas_s= min_czas/60
    minczas_ost = int(minczas_s)  # w minutach
    sek = (minczas_s - int(minczas_s))*60
    text_area.insert(END, "Czas: " + str(minczas_ost)+"m" + str(int(sek))+"s")

    #Strzałka północy
    arrow_image = img.imread('polnoc.jpg')
    arrowbox = OffsetImage(arrow_image, zoom=0.2)
    arrowbox.image.axes = plt.gca()
    ab = AnnotationBbox(arrowbox, (1, 1), xycoords='axes fraction', xybox=(1, 1), frameon=False)
    plt.gca().add_artist(ab)
    plt.gca().set_aspect('equal', adjustable='box')

    #Obszar opracowania
    ramka_x = [x, Dx, Dx, x, x]
    ramka_y = [y, y, Dy, Dy, y]
    plt.plot(ramka_x, ramka_y, color='green', linewidth= 4)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=5, padx=15, pady=15)



guzik= Button(window, text='Potwierdź wartości',command=pobierz_wartosci)
guzik.grid(row=2, column=0)

guzik2= Button(window, text='Pokaż wyniki',command=wyniki)
guzik2.grid(row=2, column=1)


window.mainloop()


