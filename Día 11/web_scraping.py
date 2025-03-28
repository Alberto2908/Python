import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, "lxml")
print(sopa.select("title")) # Hace búsqueda por etiqueta
print(len(sopa.select("h1"))) # Contar cuantos elementos tiene con ese nombre
print(sopa.select("title")[0].getText()) # Devuelve el contenido de la etiqueta, sin etiqueta

parrafo_especial = sopa.select("script")[0].getText()
print(parrafo_especial)

columna_lateral = sopa.select("a")
for p in columna_lateral:
    print(p.getText())
