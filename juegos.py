import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import os


def menu_datos():
	sg.theme('DarkAmber')
	columna  = [
	    [sg.Text('Seleccione un juego')],
	    [sg.Text('1- Ahorcado')],
	    [sg.Text('2- Ta - Te - Ti')],
	    [sg.Text('3- Otello')],
	    [sg.Text('4- Salir')],
	    [sg.Button('Elegir')]
	]
	columna1 = [
	    [sg.Text('nombre')],[sg.Input(key='nom')],
	    [sg.Text('apellido')],[sg.Input(key='ape')],
		[sg.Text('Numero')],[sg.Input(key='num')],
	]
	layout = [
	    [
	     sg.Column(columna1), sg.Column(columna)
	     ]
	]
	x=True
	window = sg.Window("Ventana").Layout(layout)
	events,values = window.read()
	if( events== None):
		x=False
	window.close()
	return values['num'],values['nom'],values['ape'],x

def jugando():

	columna  = [
	    [sg.Text('Seleccione un juego')],
	    [sg.Text('1- Ahorcado')],
	    [sg.Text('2- Ta - Te - Ti')],
	    [sg.Text('3- Otello')],
	    [sg.Text('4- Salir')],
		[sg.Input(key='num')],
	    [sg.Button('Elegir')]
	]

	layout = [
	    [
		sg.Frame('Elija otro juego',[[
	     sg.Column(columna)]])
	     ]
	]
	x=False
	window = sg.Window("Ventana").Layout(layout)
	events,values = window.read()
	if events==None:
		x=True
	window.close()
	return values['num'],x

def where_json(file_name):
	return os.path.exists(file_name)

lista=[]
datos={}				#elijo un diccionario para utilizar nombre y apellido del participante como llave del mismo.
tupla = menu_datos()
sigo_jugando=tupla[3]
ant=tupla[3]
if(sigo_jugando):
	key=tupla[2]+' '+tupla[1]
	if where_json('arch_juegos.json'):		#elijo archivo json por ser un archivo de texto, y ser mas facil de leer a la hora de verificar los resultados.
											#Ademas permite guardar estructuras, en este caso un diccionario con los datos de cada jugador.
		archivo=open('arch_juegos.json','r')
		datos=json.load(archivo)
	else:
	    datos[key] =[]
	    with open('data.json', 'w') as outfile:
	        json.dump(datos, outfile)
	if key in datos:
		lista=datos[key]
	else:
		datos[key]=[]
while sigo_jugando:
	if tupla[0] == '1':
		hangman.main()
		lista.append('Jugo al ahorcado')       #elijo una lista para ir agregando los juegos que elije el jugador y luego agregarlo a la llave del diccionario.
	elif tupla[0] == '2':
		tictactoeModificado.main()
		lista.append('Jugo al TaTeTi')
	elif tupla[0] == '3':
		reversegam.main()
		lista.append('Jugo al Otello')
	elif tupla[0]  == '4' or tupla[1]==True :
		break
	if tupla[0] != '4' :
		tupla = jugando()
if(ant):
	datos[key]=lista
	archivo= open('arch_juegos.json', 'w')
	json.dump(datos, archivo, indent=2)
	archivo.close()
