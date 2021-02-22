import  web
import json

urls = (
    "/read?","Read"
)

app = web.application(urls, globals())

class Read():

  def GET(self):
    try:
        data = web.input()

        num1 = int(data.num1)
        num2 = int(data.num2)

        add = num1 -num2

        result = {}
        result["status"] = 200
        result["message"] = add
        result = json.dumps(result)
        return result


    except Exception as error:
      result = {}
      result["status"] = 400
      result["message"] = "Verifique los datos de entrada"
      result["status"] = json.dumps(result)
      return result


if __name__ == "__main__":
    app.run()