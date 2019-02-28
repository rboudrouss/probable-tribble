from tkinter import *

nb = 0
multi = 1


def clic():
	global nb
	global multi
	nb +=1*multi
	var.config(text="Nombre de cookie : {0}".format(nb))

def ajout_multi():
	global nb
	global multi
	try:
		assert (nb - 20)>0
	except:
		print("pas assez d'argent")
	else:
		nb -=20
		multi += 1
		multiplicateur.config(text="Votre multuplicateur : {0}".format(multi))
		var.config(text="Nombre de cookie : {0}".format(nb))

def fill_multi():
	global nb
	global multi
	while nb>=20:
		nb -=20
		multi += 1
	multiplicateur.config(text="Votre multuplicateur : {0}".format(multi))
	var.config(text="Nombre de cookie : {0}".format(nb))




main = Tk()
main.geometry("950x620")
main.title("Cookie clicker")
main.minsize(950,620)
main.maxsize(1000,1000)
main.config(bg="#4065A4")


left_frame = Frame(main,bg="#4065A4",bd=1)

right_frame = Frame(main,bg="#4065A4",bd=1)

#ce qu'ill y a dans le title frame
title = Label(main,text="Cookie Clicker", font=("Helvetica",20),bg="#4065A4",fg="black")

#ce qu'ill y a dans le title frame
var = Label(main,text="Nombre de cookie : 0", font=("Helvetica",20),bg="#4065A4",fg="black")


#la right frame

	#creation d'image
width = 500
height = 500

#charge l'image
image = PhotoImage(file="MG.gif").zoom(50).subsample(37)

    #créé un canvas (espace dédié au composant graphique)
canvas = Canvas(right_frame,width=width,height=height,bg="#4065A4",bd=0,highlightthickness=0)

    #met l'image dans le cavas en spécifiant le centre de l'image
canvas.create_image(width/2,height/2,image=image)

    #on place le canvas à gauche du sous frame (1ligne,1colomn)
canvas.pack()

#bouton
clic_bouton_cookie = Button(right_frame,text="Clique!", font=("Helvetica",20),\
	bg="#4065A4",fg="black",command=clic)
clic_bouton_cookie.pack()


multiplicateur = Label(left_frame,text="votre multiplicateur de clique : 0", font=("Helvetica",20),\
	bg="#4065A4",fg="black")

bouton_cookie1 = Button(left_frame,text="acheter un multiplicateur pour 20 cookies", font=("Helvetica",20),\
	bg="#4065A4",fg="black",command=ajout_multi)
bouton_cookie1.pack(fill=X)

bouton_cookie2 = Button(left_frame,text="fill", font=("Helvetica",20),\
	bg="#4065A4",fg="black",command=fill_multi)
bouton_cookie2.pack(fill=X)

bouton_cookie3 = Button(left_frame,text="--", font=("Helvetica",20),\
	bg="#4065A4",fg="black",command=ajout_multi)
bouton_cookie3.pack(fill=X)

bouton_cookie4 = Button(left_frame,text="--", font=("Helvetica",20),\
	bg="#4065A4",fg="black",command=ajout_multi)
bouton_cookie4.pack(fill=X)

multiplicateur.pack(side=BOTTOM)


title.grid(row=0,column=0,sticky=N)
var.grid(row=0,column=1,sticky=N)
left_frame.grid(row=1,column=0,sticky=N)
right_frame.grid(row=1,column=1,sticky=N)
main.mainloop()