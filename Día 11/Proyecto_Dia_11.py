import bs4
import requests

# Crear url sin número de página
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar páginas
for pagina in range(1,51):

    # Crear sopa
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # Seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    # Iterar en los libros
    for libro in libros:
        # Revisar 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            # Guardar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]
            #Agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

# Ver libros 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)

print(len(titulos_rating_alto))