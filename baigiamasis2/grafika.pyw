import random
import os
from tkinter import *
from PIL import ImageTk, Image
from db_kurimas import *


# programos kurimas
kurti_db()
langas = Tk()
langas.geometry('600x365')
langas.iconbitmap("icon.ico")
langas.title("Žaidimas 'Kartuvės'")
paveiksleliai = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"]
meniu = Menu(langas)
langas.config(menu=meniu)


# paveikslelis
img = ImageTk.PhotoImage(Image.open(paveiksleliai[0]))
paveikslelis = Label(langas, image=img)


# funkcijos
def restart():
    langas.destroy()
    trinti_db()
    os.startfile("grafika.pyw")


def zodzio_generavimas():
    rows = session.query(Zodynas).count()
    random_zodzio_nr = int(random.randrange(rows))
    random_eilute_zodyne = str(session.query(Zodynas).get(random_zodzio_nr))
    random_zodis = random_eilute_zodyne.split()[1]
    random_zodis_listas = list(random_zodis)
    naujas_zodis = []
    for raide in random_zodis_listas:
        bruksnys = raide.replace(raide, "—")
        naujas_zodis.append(bruksnys + " ")
    naujas_zodis_v2 = "".join(naujas_zodis)
    return random_zodis, naujas_zodis_v2, random_zodis_listas

# kintamieji ir listai
random_zodis, naujas_zodis_v2, random_zodis_listas = zodzio_generavimas()
spejimai = 0
atspetos_raides = []
neatspetos_raides = []
zodis_su_bruksn = []
print(random_zodis)


def spejimas(event):
    global spejimai
    spej_raide = iv_laukas.get()
    iv_laukas.delete(0, END)
    if spej_raide == "" or len(spej_raide) > 1 or spej_raide in neatspetos_raides or spej_raide.isupper():
        status["text"] = "Netinkamai įvesta raidė"
        return
    if spej_raide in random_zodis_listas:
        atspetos_raides.append(spej_raide)
        status["text"] = "Atspėjote"
        for x in random_zodis_listas:
            if x in atspetos_raides:
                zodis_su_bruksn.append(x)
            else:
                zodis_su_bruksn.append("—" + " ")
            zodis_su_bruksn_v2 = "".join(zodis_su_bruksn)
            uzrasas2["text"] = zodis_su_bruksn_v2
        zodis_su_bruksn.clear()
        if len(set(random_zodis_listas)) == len(set(atspetos_raides)):
            status["text"] = "Laimėjote"
            uzrasas["text"] = "Laimėjote!!!"
            uzrasas5["text"] = "Norėdami žaisti dar kartą, spauskite 'Naujas žodis'!"
            iv_laukas.configure(state="disabled")
            return
    elif len(set(random_zodis_listas)) != len(set(atspetos_raides)):
        spejimai += 1
        status["text"] = "Neatspejote"
        uzrasas["text"] = f"Jums liko {6-spejimai} spėjimai."
        neatspetos_raides.append(spej_raide)
        uzrasas4["text"] = neatspetos_raides
        if spejimai > 5:
            status["text"] = "Pralaimejote"
            img7 = ImageTk.PhotoImage(Image.open(paveiksleliai[6]))
            paveikslelis.configure(image=img7)
            paveikslelis.image = img7
            uzrasas["text"] = f"Pralaimėjote, žodis buvo - {random_zodis} \n norėdami žaisti dar kartą, " \
                              f"spauskite 'Naujas žodis' "
            uzrasas5["text"] = "Norėdami žaisti dar kartą, spauskite 'Naujas žodis'!"
            iv_laukas.configure(state="disabled")
        if spejimai == 1:
            img2 = ImageTk.PhotoImage(Image.open(paveiksleliai[1]))
            paveikslelis.configure(image=img2)
            paveikslelis.image = img2
        if spejimai == 2:
            img3 = ImageTk.PhotoImage(Image.open(paveiksleliai[2]))
            paveikslelis.configure(image=img3)
            paveikslelis.image = img3
        if spejimai == 3:
            img4 = ImageTk.PhotoImage(Image.open(paveiksleliai[3]))
            paveikslelis.configure(image=img4)
            paveikslelis.image = img4
        if spejimai == 4:
            img5 = ImageTk.PhotoImage(Image.open(paveiksleliai[4]))
            paveikslelis.configure(image=img5)
            paveikslelis.image = img5
        if spejimai == 5:
            img6 = ImageTk.PhotoImage(Image.open(paveiksleliai[5]))
            paveikslelis.configure(image=img6)
            paveikslelis.image = img6


def isjungimas():
    langas.destroy()
    trinti_db()


# Meniu
meniu.add_cascade(label="Naujas žodis", command=restart)
meniu.add_cascade(label="Išeiti", command=isjungimas)
iv_laukas = Entry(langas)

# Status juosta
status = Label(langas, text='....', bd=1, relief=SUNKEN, anchor=W)

# tekstas appse
uzrasas = Label(langas, text="Spėdami raides galite suklysti 6 kartus.")
uzrasas2 = Label(langas, text=naujas_zodis_v2, fg="#f00")
uzrasas3 = Label(langas, text="Neatspėtos raidės:")
uzrasas4 = Label(langas, text="")
uzrasas5 = Label(langas, text="Įveskite mažąsias raides (a - ž) ir spauskite 'ENTER'")
uzrasas6 = Label(langas, text="Tema")

# grid
paveikslelis.grid(rowspan=5, columnspan=5, sticky=W+N)
uzrasas.grid(row=0, column=6)
uzrasas2.grid(row=1, column=6)
iv_laukas.grid(row=2, column=6, sticky=S)
uzrasas3.grid(row=4, column=6)
uzrasas4.grid(row=5, column=6)
uzrasas5.grid(row=3, column=6, sticky=N)
uzrasas6.grid(row=1, column=7)
status.grid(row=7, columnspan=5, sticky=W+E)
langas.bind("<Return>", spejimas)

langas.mainloop()

