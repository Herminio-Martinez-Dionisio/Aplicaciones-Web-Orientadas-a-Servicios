import web
import requests
import json

render = web.template.render("google_books/")

class Index():

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        book_name = form.book_name

        result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)

        book = result.json()

        items = book["items"]

        encoded = json.dumps(items)
        decoded = json.loads(encoded)

        #url = decoded[0]["volumeInfo"]["infoLink"]
        url_title = decoded[0]["volumeInfo"]["title"]
        url_autores=decoded[0]["volumeInfo"]["authors"]
        url_imagen = decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"]
        url_compra = decoded[2]["saleInfo"]["buyLink"]
        


          
        #print(url_title+ " ".join(url_autores)+url_imagen+url_compra)
        ##print(url_autores)
        print(url_imagen)
        #print(url_compra)
        #link = url_title+ " ".join(url_autores)+url_imagen+url_compra
        #retu_title ="<a>Titulo del libro</a></br>"+url_title+"</br>"
        #retu_autor ="<a>Autores:</a></br>"+url_autores+"</br>"
        #retu_imagen ="img sr='https://i.pinimg.com/originals/b8/5c/8d/b85c8dc964871cf74c53d2896ac001d1.jpg'> </br>"
        #retu_compra ="<a target='blank' href='"+url_compra+"'>Compra</a>"
        autor = " ".join(url_autores)
        link = "<a>Titulo del libro</a></br><a>"+url_title+"</a></br></br><label>Autores:</label>"+autor+"</br> <img src='"+url_imagen+"'> </br><a target='blank' href='"+url_compra+"'>Compra</a>"
        #link ="<a target='blank' href='"+url+"'>"+book_name+"</a>"
        #return retu_title
        #return retu_autor
        #return retu_imagen
        #return retu_compra
        return link