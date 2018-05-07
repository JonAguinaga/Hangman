print("Un momento, el programa se está cargando")

import requests
import random

word_site= "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()

respuestabyte = WORDS[random.randint(0, len(WORDS))]

respuesta = list(respuestabyte.decode("utf-8"))


contador = 5

inprogress = list()

for char in respuesta:
    inprogress.append("_")

#print(respuesta)
#print(inprogress)

while inprogress != respuesta and contador != 0:

    print("Introduce una letra")

    letra = input()

    if letra in respuesta:
        for letra2 in range (0,len(respuesta)):
            if letra == respuesta[letra2]:
                inprogress[letra2]=letra
        print("Enhorabuena, la letra es correcta")
    else:
        contador = contador-1
        print("Esa letra no está en la palabra")
    print("Te quedan", contador, """intentos
            Tu palabra es""", " ".join(inprogress))

pass

if inprogress == respuesta:
    print("Enhorabuena. Tu palabra es", "".join(respuesta))

else:
    print("Lo sentimos, tu palabra era", "".join(respuesta))
