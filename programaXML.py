
from lxml import etree
doc = etree.parse('radares.xml')

#------------------------ Definicion de variable ------------------------------------

dic_provinciaradares = {}
dic_radarescoord = {}
lista_carreteras = []
carreteras = []
lista_radarescoord = [ ]

#---------------------- Lista Municipios (con radares) ------------------------------

lista_municipios = doc.xpath("//NOMBRE/text()")

#----------------------------- Lista carreteras -------------------------------------

lista_carreterastotales = doc.xpath("//DENOMINACION/text()")

for carretera in lista_carreterastotales:

    if carretera not in lista_carreteras:

        lista_carreteras.append(carretera)

#------------------------- Lista de radares totales ---------------------------------

lista_radares = doc.xpath("//RADAR")

#------------------------- Funcion carreteras y radares -------------------------------(opcion 3)

def municipios_radares(carretera,doc):

    carreterastotales = doc.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()'%carretera)

    for carretera in carreterastotales:

        if carretera not in carreteras:

            carreteras.append(carretera)

    for elem in carreteras:
        
        print("")
        print("-----------------------------------")
        print("")
        print("Carretera:",elem)
        print("Nº de radares:",carreterastotales.count(elem))

#------------------------- Funcion Provincias y radares ------------------------------(opcion 4)

def carreteras_radares(carretera,doc):

    municipio = doc.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)[0]
    radares = doc.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR'%municipio)

    dic_provinciaradares[municipio] = len(radares)
    
    return dic_provinciaradares

#------------------------- Funcion Provincias y radares ------------------------------(opcion 5)

def radares_coord(carretera,doc):

    for coord in doc.xpath('//CARRETERA[DENOMINACION="%s"]/.'%carretera):

        latitud = coord.xpath('./RADAR/PUNTO_INICIAL/LATITUD/text()')[0]
        longitud = coord.xpath('./RADAR/PUNTO_INICIAL/LONGITUD/text()')[0]
        provincia = coord.xpath('./../NOMBRE/text()')[0]
        
        dic_radarescoord = {}
        dic_radarescoord[carretera] = [latitud,longitud,provincia]
        lista_radarescoord.append(dic_radarescoord)

    return lista_radarescoord

#--------------------------------- Programa ------------------------------------------

print("")
print("-------------------MENU--------------------")
print("(1) Mostrar provincias con carreteras")
print("(2) Contar todos los radares")
print("(3) Mostrar carreteras y sus radares de una Provincia")
print("(4) Mostrar Provincias y sus radares de una carretera")
print("(5) Link de OpenStreetMap de los radares")
print("(0) Finalizar el programa")
print("-------------------------------------------")
print("")

opcion = int(input("¿Que opcion eliges?   "))
print("")

while opcion != 0:

    if opcion == 1:   

        print("---------------------------------------------------------------------------------")
        print("Opcion 1 elegida (Lista de Provincias que tienen radares)")
        print("---------------------------------------------------------------------------------")
        print("")

        for municipio in sorted(lista_municipios):   

            print(municipio)

    if opcion == 2:     

        print("---------------------------------------------------------------------------------")
        print("Opcion 2 elegida (Mostrar cantidad de radares que hay en el documento XML)")
        print("---------------------------------------------------------------------------------") 
        print("")
        print("---------------------------")
        print("Nº de radares:", len(lista_radares))
        print("---------------------------")
        print("")

    if opcion == 3:     

        print("---------------------------------------------------------------------------------")
        print("Opcion 3 elegida (Introduce una Provincia y te muestra: nombre carreteras y cantidad de radares)")
        print("---------------------------------------------------------------------------------")

        print("")
        nom_municipios = input("Introduce Municipio: ")   
        print("")    

        while nom_municipios not in lista_municipios:

            print("")
            print("--------------------------")
            print("ERROR, no existe Municipio")
            print("--------------------------")
            print("")

            nom_municipios = input("Introduce Municipio: ")

        print(municipios_radares(nom_municipios,doc))

    if opcion == 4:     

        print("---------------------------------------------------------------------------------")
        print("Opcion 4 elegida (Introduce una carretera y te muestra: Provincia y cantidad de radares)")
        print("---------------------------------------------------------------------------------")

        print("")
        carretera = input("Introduce carretera: ")   
        print("")    

        while carretera not in lista_carreteras:

            print("--------------------------")
            print("ERROR, no existe carretera")
            print("--------------------------")
            print("")

            carretera = input("Introduce carretera: ") 
        
        for prov,rad in carreteras_radares(carretera,doc).items():
            
            print("")
            print("-----------------------------------")
            print("")
            print("Provincia:",prov)
            print("Nº de radares:",rad)
            
    if opcion == 5:      

        print("---------------------------------------------------------------------------------")
        print("Opcion 5 elegida (Introduce una carretera y te muestra el link para ver en OpenStreetMap de sus radares)")
        print("---------------------------------------------------------------------------------")

        print("")
        carreteracoord = input("Introduce el punto carretera: ")   
        print("")    

        while carreteracoord not in lista_carreteras:

            print("")
            print("--------------------------")
            print("ERROR, no existe la carretera")
            print("--------------------------")
            print("")

            carreteracoord = input("Introduce el punto carretera: ")

        zoom = input("Introduce el zoom: ")   

        print("")
        print("-------------------- Carretera ----------------------------")
        print("")
        print("                      ",carreteracoord)
        print("")
        print("---------------- Link OpenStreeMap ------------------------")
        print("")
        
        for dicoord in radares_coord(carreteracoord,doc):
            
            latitud = dicoord.get(carreteracoord)[0]
            longitud = dicoord.get(carreteracoord)[1]

            print("Provincia:",dicoord.get(carreteracoord)[2])
            print("Link: https://www.openstreetmap.org/#map=%s/%s/%s" %(zoom,latitud,longitud))
            print("")
            print("-------------------------------------------")
            print("")
            
    if opcion < 0 or opcion > 5:

        print("-----------------------")
        print("ERROR, opcion no valida")
        print("-----------------------")

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("-------------------MENU--------------------")
    print("(1) Mostrar provincias con radares")
    print("(2) Contar todos los radares")
    print("(3) Mostrar carreteras y sus radares de una Provincia")
    print("(4) Mostrar Provincias y sus radares de una carretera")
    print("(5) Link de OpenStreetMap de los radares")
    print("(0) Finalizar el programa")
    print("-------------------------------------------")
    print("")
    
    opcion = int(input("¿Que opcion eliges?   "))
    print("")

print("-----------------------")
print("   FIN DEL PROGRAMA")
print("-----------------------")