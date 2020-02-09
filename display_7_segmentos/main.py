"""

    Programado por Luis Cabrera Benito 
  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
    
    Blog:       https://parzibyte.me/blog
    Ayuda:      https://parzibyte.me/blog/contrataciones-ayuda/
    Contacto:   https://parzibyte.me/blog/contacto/
"""
import RPi.GPIO as GPIO
import time
import argparse


diccionario = {
    'A': 10,
    'B': 12,
    'C': 16,
    'D': 11,
    'E': 13,
    'F': 8,
    'G': 32,
}

numeros = {
    '0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110000',
    '8': '1111111',
    '9': '1110011',
}

GPIO.setmode(GPIO.BOARD)

for clave in diccionario:
    valor = diccionario.get(clave)
    GPIO.setup(valor, GPIO.OUT)


parser = argparse.ArgumentParser()
parser.add_argument("numero", help="Número que quieres dibujar")
argumentos = parser.parse_args()
numero = numeros.get(argumentos.numero)

contador = 0
for clave in diccionario:
    valor = diccionario.get(clave)
    bit = numero[contador]
    estado = GPIO.LOW
    if bit == "1":
        estado = GPIO.HIGH
    GPIO.output(valor, estado)
    contador = contador + 1
