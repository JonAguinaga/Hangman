import requests
import random

word_site= "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()

respuestabyte = WORDS[random.randint(0, len(WORDS))]

respuesta = list(respuestabyte.decode("utf-8"))


contador = 5

#letra = input()

inprogress = list()

for char in respuesta:
    inprogress.append("_")

print(respuesta)
print(inprogress)
#
# while inprogress != response and contador != 0:
#     print("Hola, introduce tu letra")
#
#     respuesta = list("Hoz")
#
#     if letra in respuesta:
#         for letra2 in range (0,len(respuesta)):
#             if letra == respuesta[letra2]:
#                 inprogress[letra2]=letra
#         print("Enhorabuena, la letra es correcta")
#     else:
#         contador = contador-1
#         print("Esa letra no está en la palabra")
#     print("""Te quedan 'contador' intentos
#             Tu palabra es 'inprogress'""")
#
#
#
# pass
