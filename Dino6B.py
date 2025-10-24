#🦖biblioteca de dinosaurios 

#lista prellenada de dinosaurios con su informacion
#nombre,alimentacion,tamaño,priodo,caracteristica 

dinosaurios=[
("tiranosaurio rex , "carnivoro" , 12 metro , "cretacio " , "tenia brasos muy cortos pero mandibulas muy poderosas ") (Tiranosaurio Rex","Carnivoro","Cretacico","Tenia brazos muy cortos pero mandibulas poderosas")
("triceratops , herviboro, , 9 metros , cretacio , tenia tenia tres cuernos y un gran volante oseo")
 ("brachiosauros , herviboro , 25 metros , jurasico , tenia u cuello larguisiumo para alcanzar hojas")
 ("stegosaurio , herviboro , 9 metros , jurasico , tenia placas en lka espalda y puas en la cola ")
 ("spinosaurus , carnivoro , 15 metros , cretacio , tenia una vela en la espalda y era semiacuatico")
 ("ankylosaurus , herviboro , 8 metros ,  cretacio , estaba acorazado y tenia una maza en la cola ") 
 ("pterandon, carnivoro , 7 metros de ala a ala , cretacio , era un reptil volador, pero no era un dinosaurio ")
 ("diplodocus , hervivoro , 10 metros , jurasico , uno de los dinosaurios mas largos que existieron")
 ("parasaurolophus , hervivoro , 10 metros , cretacio  , tenia una cresta hueca para hacer sonidos")
 
       
 print("=*60")
 print("🦖bienvenido a la biblioteca de dinosaurios🦕")
 print("=*60")
 print ("preguntapor cualquier dinosaurio y te dare su informacion")
 print("escribe lista para ver todos los dinosaurios disponibles")
 print ("escribe salir para terminar, \n")

while true:
    consulta=input("¿que dinosaurio quieres consultar?").strip().lower()
    
    if consulta=="salir"  
    print("👌¡hasta luego,  explorador de dinosaurios!")
    break
    
    if consulta=="lista":
         print("\n📋 dinosaurios disponibles")
         for i, (nombre,_,_,_,_) in enumerate(dinosaurios, 1):
             print(f("{i}.{nombre}"))
         print()
         
         continue
         
         encontrado=false
         for nombr,dieta,tamaño,periodo,dato_curioso in dinosaurios
         if consulta in nombre.lower():
              print("\n" + "=*60")
              print ("f🦖{nombre}")
              print("="*60)
              print(f"🍬 dieta: {dieta}")
              print(f"tamaño: {tamaño}")
              print(f"periodo: {periodo}")
              print(f"dato curioso: {dato_curioso}")
              print("="*60 + "\n")
              encontrado=true 
              
              if not encontrado
                print(f"❎ no encontre informacion sobre ;{consulta};.")
                print("💡 intenta escribir"lista" para ver os dinosaurios disponibles. \n")
                