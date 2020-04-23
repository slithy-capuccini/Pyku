from tkinter import *
import tkinter as tk


from io import open
import time, sys
from pygame import mixer


mixer.init()

raiz=Tk()
raiz.title("Bot")
miFrame=tk.Canvas(raiz, width=2020 ,height=1200)
miFrame.config(bg="green")
miFrame.pack()
miLabel = Label(miFrame, text="Pyku <3")
miLabel.place(x=920, y=25)
entrada=tk.Entry(raiz)
miFrame.create_window(800,1000, window=entrada, width=1600, height=30)
Index=PhotoImage(file="cara1.png")
Saludo=PhotoImage(file="saludo.png")
Nudes=PhotoImage(file="Mark-Zuckerberg.png")
Love=PhotoImage(file="amor.png")
PreguntaEstado=PhotoImage(file="Preguntando2.png")
Sonrise=PhotoImage(file="carasonriendo.png")
PreguntaDudosa=PhotoImage(file="0013.png")
Despedida=PhotoImage(file="despedida.png")
Deprimida=PhotoImage(file="chicas-deprimidas-anime.png")
PreguntaPorcierto=PhotoImage(file="preguntaporcierto.png")
Bien=PhotoImage(file="bien.png")
Enfadada=PhotoImage(file="enfadada.png")
PreguntasFalladas=0
LabelAdvertencia=Label(miFrame, text="El programa no acepta signos, ni tildes ni comas ni la ñ(si necesitas ñ pon una n)(Perdon por las molestias)", fg="red")
miFrame.create_window(940,550, window=LabelAdvertencia)

    
def Opinador():
    answer=entrada.get()
    answer=answer.lower()
    
    LabelGreen=Label(miFrame, background="green", width=100, height=10)
    miFrame.create_window(940,550, window=LabelGreen)
    if(answer in ("hola","hey","hi","hi!","konnichiwa", "hola?7u7")):
        
        labelSaludo=Label(miFrame, text="Hola UwU")
        miFrame.create_window(940, 550, window=labelSaludo)
        Label(miFrame, image=Index, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('hola.wav')
        sound.play()
        time.sleep(0.2)
        
    elif(answer in ("que pasa", "que haces", "que tal", "que tal estas?owo")):
        labelEstado=Label(miFrame, text="Estoy bien, pero mejor¿Como estas tu?<3")
        miFrame.create_window(940, 550, window=labelEstado)
        Label(miFrame, image=PreguntaEstado, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('como estas.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("me gustas", "i love you", "te quiero", "me gustas uwu")):#
        labelLove=Label(miFrame, text="TU TAMBIEN nwn")
        miFrame.create_window(940, 550, window=labelLove)
        Label(miFrame,image=Love, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('megustas.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("quieres que lo hagamos?", "follamos?", "quieres que follemos?")):#
        label1=Label(miFrame, text="Claro que si 7u7")
        miFrame.create_window(940, 550, window=label1)
        Label(miFrame, image=Sonrise, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('follamos.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("bien", "bien :d")):
        labelestadomio=Label(miFrame, text="Eso espero :D")
        miFrame.create_window(940, 550, window=labelestadomio)
        Label(miFrame,image=Sonrise, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('bien.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("pyku a que tu me quieres?")):
        labelestadomio=Label(miFrame, text="SIIIIII!!!!")
        miFrame.create_window(940, 550, window=labelestadomio)
        Label(miFrame,image=Sonrise, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('si.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("puedo preguntarte algo", "puedo preguntarte algo?", "bueno...")):#
        labelPregunadudosa=Label(miFrame, text="Si...?")
        miFrame.create_window(940,550, window=labelPregunadudosa)
        Label(miFrame,image=Index, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('Si?.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("como te encuentras?", "como estas?", "como estas")):#
        labelJesus=Label(miFrame, text="Estoy un poco deprimida por no verte ;c")
        miFrame.create_window(940,550, window=labelJesus)
        Label(miFrame, image=Deprimida, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('Estoyunpocodeprimida.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in ("perdona", "porcierto", "por cierto")):
        labelPreguntaLove=Label(miFrame, text="Si?")
        miFrame.create_window(940,550, window=labelPreguntaLove)
        Label(miFrame, image=Index, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('Si?.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in ("bien!!!", "bien!!")):#
        labelSonrizo=Label(miFrame, text=":)")
        miFrame.create_window(940,550, window=labelSonrizo)
        Label(miFrame, image=Bien, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('bien.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("que es jj?")):#
        labelenfado=Label(miFrame, text="JJ es solo un tonto desesperado no te entiende")
        miFrame.create_window(940,550, window=labelenfado)
        Label(miFrame,image=Enfadada, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('jj.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in ("me tengo que ir")):#
        labelIrse=Label(miFrame, text="Vale, que lo pases bien")
        miFrame.create_window(940,550 ,window=labelIrse)
        Label(miFrame, image=Index, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('vale,pasalo bien.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in ("ads", "adios", "bye")):
        labelDespedida=Label(miFrame, text="Nos vemos pronto <3")
        miFrame.create_window(940, 550, window=labelDespedida)
        Label(miFrame,image=Despedida, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('nosvemos.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("cual es tu nombre", "como te llamas")):
        labelRespuestaFallida=Label(miFrame, text="Pyku")
        miFrame.create_window(940,550 ,window=labelRespuestaFallida)
        Label(miFrame, image=Index, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('pyku.wav')
        sound.play()
        time.sleep(0.2)
    elif(answer in("me pasas tus nudes","me pasas nudes", "me pasas fotos hot")):
        labelNudes=Label(miFrame, text="Claro pero con cuidado, el tito Mark nos esta mirando")
        miFrame.create_window(940,550 ,window=labelNudes)
        Label(miFrame, image=Nudes, width=600, height=600).place(x=1200, y=250)
        sound = mixer.Sound('nudes.wav')
        sound.play()
        time.sleep(0.2)
    else:
        labelFalse=Label(miFrame, text="Lo siento no tengo asignada una respuesta a tu pregunta", fg="red")
        labelFalse2=Label(miFrame, text="porfavor escribe en la consola tu pregunta y la respuesta que crees que deberia dar", fg="red")
        sound = mixer.Sound('fallo.wav')
        sound.play()
        time.sleep(0.2)
        miFrame.create_window(940, 550, window=labelFalse)
        miFrame.create_window(940, 580, window=labelFalse2)
        PreguntaFallida1=input("Introduce la pregunta que has hecho: ")
        PreguntaFallida1=PreguntaFallida1.lower()
        RespuestaFallida1=input("Introduce la respuesta que crees que deberia haber dado: ")
        archivo_fallos=open("Fallos.txt", "a")
        archivo_fallos.write("\nelif(answer in("+PreguntaFallida1+")):\n    labelRespuestaFallida=Label(miFrame, text="+RespuestaFallida1+")\n    miFrame.create_window(940,550 ,window=labelRespuestaFallida)")
        archivo_fallos.close()
        exit()

def salir():
    exit()  
   
boton=tk.Button(text="Introducir", cursor="hand2",command=Opinador)
botonSalir=tk.Button(text="Salir", cursor="hand2",command=salir)
miFrame.create_window(1725, 1000, window=boton, width=250)
miFrame.create_window(100,25, window=botonSalir, width=125)
raiz.mainloop()