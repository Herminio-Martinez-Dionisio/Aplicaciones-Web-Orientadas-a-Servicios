import web
import requests
import json

render = web.template.render("api_openlibra_api/")

class Index():

    def GET(self):
        books = None
        return render.index(books)

    def POST(self):
        form = web.input()
        book_name = form["book_name"]
        #result =requests.get('https://www.googleapis.com/books/v1/volumes?q='+book_name)
        result = requests.get("https://www.etnassoft.com/api/v1/get/?book_title="+book_name)
        books = result.json()

        encoded = json.dumps(books)
        decoded = json.loads(encoded)
        
        #items = books["items"]
        #encoded = json.dumps(items)
        #decoded = json.loads(encoded)
        #print(decoded)
        books = []

        for book in decoded:
            ids = decoded[0]["ID"]
            titul = decoded[0]["title"]
            auto = decoded[0]["author"]
            contenido = decoded[0]["content"]
            dowload = decoded[0]["url_download"]
            imagen = decoded[0]["thumbnail"]

            datos = {
                "id":ids,
                "titulo":titul,
                "autor":auto,
                "descripcion":contenido,
                "url_descargar":dowload,
                "url_imagen":imagen
            }
            books.append(datos)
        
        print(books)

        return render.index(books)