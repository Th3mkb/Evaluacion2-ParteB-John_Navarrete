import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "XqbHupn2Tugdz49lxe1JGzByiyJSXbFG"

while True:
   origen = input("Ciudad de origen: ")
   if origen == "Salir de la busqueda" or origen == "s":
       break
   destino = input("Ciudad de destino: ")
   if destino == "Salir de la busqueda" or destino == "s":
        break

   url = main_api + urllib.parse.urlencode({"key" :key, "from" :origen, "to" :destino})
   print("URL: " + (url))
   
   json_data = requests.get(url).json()
   json_status = json_data ["info"] ["statuscode"]
   
   if json_status == 0:
       print("Estado de API: " + str(json_status) + "= Direccion de ruta encontrada.\n")
       print("=============================================")
       print("ubicacion actual " + (origen) + " hacia " + (destino))
       print("Tiempo del viaje:   " + (json_data["route"]["formattedTime"]))
       print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("=============================================")
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
           print("=============================================\n")
           
           
   elif json_status == 402:
        print("**********************************************")
        print("Estado de codigo: " + str(json_status) + "; informacion no valida para las ubicaciones.")
        print("**********************************************\n")
   elif json_status == 611:
        print("**********************************************")
        print("Estado de codigo: " + str(json_status) + "; Falta de informacion en las ubicaciones.")
        print("**********************************************\n")
   else:
        print("************************************************************************")
        print("Para cogigo de estado: " + str(json_status) + "; Referencia:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")