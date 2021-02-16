import json
print("Formato( (Año)-(Mes)-(Dia))")
print("Ejemplo: 2021-01-01")
print("¿Cual es tu fecha de nacimiento? ")
nombre = input()
separa = nombre.split('-')
#print(f"Me alegro de conocerle, {nombre}")
mes = int(separa[1])
dia = int(separa[2])
if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=19)):
  signo = "Aries"
  elemento = "Fuego"
  numero = "49 43 3 30 48 38"
  color = "Blanco"
  horoscopo = "Tendrás nuevas ideas y empezarás a planificar con mucho ingenio, los asuntos que vas a llevar a cabo durante este día. Organiza tus temas con pragmatismo y paso a paso; será más eficaz."
if ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=21)):
  signo = "Tauro"
  elemento = "Tierra"
  numero = "6 21 1 16 13 32"
  color = "Verde"
  horoscopo = "Realiza una limpieza mental de todo lo que subyace en tu interior desde la infancia; y de esta manera comenzarás desde cero y te quitarás muchas obsesiones y costumbres mal adquiridas."
if ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=20)):
  signo = "Géminis"
  elemento = "Aire"
  numero = "22 55 36 26 44 34"
  color = "Azul"
  horoscopo = "Hoy tu genialidad estará latente con gran fuerza y te ayudará a conseguir todo lo que atraes con tus pensamientos y con tu estado energético."
if ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=22)):
  signo = "Cáncer"
  elemento = "Agua"
  numero = "31 32 9 15 1 28"
  color = "Naranja"
  horoscopo = "Hoy tu mentalidad estará muy abierta y además podrás utilizar tus grandes ideas en los asuntos que hoy estés planificando para poder darles una salida productiva y benéfica. Necesitas ajustar tu manera de ser altruista y de beneficiar a los demás; ya que, si lo realizas con amor y compasión, recibirás en abundancia."
if ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=22)):
  signo = "Leo"
  elemento = "Fuego"
  numero = "20 27 36 1 23 8"
  color = "Amarillo"
  horoscopo = "Deberías evitar implicarte tan intensamente en todo lo que realices, ya que puede ser contraproducente. No trates de ir contracorriente. Mejor fluye, y así será todo más fácil y mucho más productivo."
if ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=22)):
  signo = "Virgo"
  elemento = "Tierra"
  numero = "56 44 17 13 45 24"
  color = "Rosa"
  horoscopo = "Será un día para hacer uso de tu gran ingenio y de la inspiración que sientas en tu interior. Todo ello servirá para que te sientas con gran dinamismo y con tus facultades estén despiertas para poder hacer frente de una manera sencilla a todo lo que se te presente hoy."
if ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=22)):
  signo = "Libra"
  elemento = "Aire"
  numero = "36 5 7 45 32 25"
  color = "Gris"
  horoscopo = "Es un tiempo especial para poder transformarte de una manera muy profunda, y para ello lo más importante es que realices una gran introspección para conectar con tu parte más interna y sacar a la luz tus bloqueos emocionales que proviene de la infancia."
if ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=21)):
  signo = "Escorpio"
  elemento = "Agua"  
  numero = "25 56 11 33 20 14"
  color = "Negro"
  horoscopo = "Será un día para que utilices tu gran capacidad de penetrar en lo más recóndito de la psique y poder ayudar a otros a que utilicen lo mejor de ellos. Tanto para su bienestar, como para que tengan mecanismos para sentirse con mayor seguridad y así poder dar más de sí. Y para ti porque podrás solucionar muchos temas de tu pasado."
if ((mes==11) and (dia>=22)) or ((mes==12) and (dia<=21)):
  signo = "Sagitario"
  elemento = "Fuego"
  numero = "34 33 54 56 45 14"
  color = "Púrpura"
  horoscopo = "Intenta tener un alto grado de motivación para conseguir elaborar un plan que te ayude a conseguir que tu atención este despierta a los pasos que necesitas ir dando para poder conseguir tu objetivo. Tendrás que ceñirte a planes realistas, y que no sean fantasiosos o demasiado inverosímiles. Y además deberás de utilizar tu ingenio y tu gran potencial."
if ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=19)):
  signo = "Capricornio"
  elemento = "Tierra"
  numero = "50 12 34 9 20 16"
  color = "Violeta"
  horoscopo = "Hoy tendrás que intentar elevar tu ánimo y no dejarte llevar por negatividades. Ya que esto es contraproducente para tus intereses y para todo lo que realices durante este día. Es un momento en el que te manejarás con cuidado y evitarás actuaciones improcedentes o fuera de lugar. Así que piensa muy bien antes de realizar cualquier paso."
if ((mes==1) and (dia>=20)) or ((mes==2) and (dia<=18)):
  signo = "Acuario"
  elemento = "Aire"
  numero = "39 6 52 31 20 11"
  color = "Rojo"
  horoscopo = "Para obtener los mejores aciertos deberás utilizar tu gran intuición, y medir bien tus actos y tus expresiones; ya que serán muy visibles en este día."
if ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=20)):
  signo = "Piscis"
  elemento = "Agua"
  numero = "48 40 25 19 33 5"
  color = "Marrón"
  horoscopo = "Hoy, deberás precaverte de la agitación y de las tensiones, ya que tu sistema nervioso estará alterado. Y para ello es importante mantener la calma y practicar la relajación, ya sea con música especial, o de forma tradicional. Notarás que necesitas mucha paz a tu alrededor para tener la suficiente confianza de que todo va a salir positivamente."

print(f"Tu Signo es: {signo}")
print(f"Tu Elemento es: {elemento}")
print(f"Tu Numero de suerte es: {numero}")
print(f"Tu color es: {color}")
print(f"Horoscopo: {horoscopo}")
#signo = "uno"
#elemento = "dos"
#numero = "tres"
#color = "cuatro"
#horoscopo = "cinco"

data = {}
data['Persona'] = []

data['Persona'].append({
    'signo': signo,
    'elemento': elemento,
    'numero_suerte': numero,
    'color': color,
    'horoscopo': horoscopo
})
with open('horoscopo.json', 'w') as file:
    json.dump(data, file, indent=4,ensure_ascii=False)
