import web
import requests
import json

render = web.template.render("diseño/")
urls = (
    "?","Read"
)
app = web.application(urls, globals())
class Archivos():

    def __init__(self):
        pass

    def leer(self, archivo):
        file = open(archivo, 'r')
        for line in file:
            print(line)
        file.close()

    def escribir(self, archivo, texto):
        file = open(archivo, 'a')
        texto = texto + "\n"
        file.write(texto)
        file.close()
class Index():

    def GET(self):
        return render.index()

    def POST(self):
        try:
          data = web.input()

          nombre = data.nombre
          fecha = data.fecha_nacimiento
          separa = fecha.split('-')
          edad = (2021)-int(separa[0])
          if edad < 0 :
              edad = "Acabas de nacer"
          print(edad)
          result = {}
          data = {}

          obt = Archivos()
          obt.escribir("archivo.txt", "Nombre:"+nombre)
          obt.escribir("archivo.txt", "Fecha_nacimiento:"+fecha)
          obt.escribir("archivo.txt", "Edad:"+str(edad))
          #obt.leer("archivo.txt")
          file = open("archivo.txt", 'r')
          contador = 1
          contador_p = 1
          enumerador = 0
          for line in file:
              parte = line.split(':')
              parte2 = parte[1].split('\n')
              ids = str(parte[0])+str(contador)
              result[str(ids)] = str(parte2[0])
              contador=contador+1
                
          result = json.dumps(result)
          file.close()
          with open('persona.json', 'w') as file:
            json.dump(result, file, indent=4,ensure_ascii=False)          
          return result
          
        except Exception as error:
          result = {}
          result["status"] = 400
          result["message"] = "Verifique los datos de entrada"
          result["status"] = json.dumps(result)
          return result
    