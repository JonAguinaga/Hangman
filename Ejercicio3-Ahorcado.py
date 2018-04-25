import requests

word_site= "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

respuesta = requests.get(word_site)
WORDS = response.content.splitlines()

contador = 5

letra = "o"

inprogress = list("___")

while inprogress != respuesta and contador != 0:
    print("Hola, introduce tu letra")

    respuesta = list("Hoz")

    if letra in respuesta:
        for letra2 in range (0,len(respuesta)):
            if letra == respuesta[letra2]:
                inprogress[letra2]=letra
        print("Enhorabuena, la letra es correcta")
    else:
        contador = contador-1
        print("Esa letra no está en la palabra")
    print("""Te quedan 'contador' intentos
            Tu palabra es 'inprogress'""")



pass
