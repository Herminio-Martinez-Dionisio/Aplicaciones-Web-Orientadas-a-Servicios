import requests
import json

resultado = requests.get("https://www.googleapis.com/books/v1/volumes?q=harry+potter")

#print(resultado.status_code)# checa si todo es correcto 200= correcto
#print(resultado.text) devuelve resultado en json diciconario

libro = resultado.json()

#print(libro.keys()) # tres llave principales
articulo = libro["items"]
codificado = json.dumps(articulo)
decodificado = json.loads(codificado)

#print(decodificado[0])
print(decodificado[0]["volumeInfo"]["title"])
print(decodificado[0]["volumeInfo"]["authors"])
print(decodificado[0]["volumeInfo"]["imageLinks"]["thumbnail"])
#print(decodificado[2]["saleInfo"]["buyLink"])
#url_compra = ""#decoded[3]["saleInfo"]["buyLink"]
