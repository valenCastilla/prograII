# main.py
# Script principal para probar el patrón Decorator.

from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel, DobleCaramel

def main():

    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")             


    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()       #AA                                                                 # 1) Creamos una bebida base (en este caso DarkRoast)
    beverage2 = Mocha(beverage2)  #BB                                                                 # 2) Se crea el primero objeto/condimento Mocha que envuelve al DarkRoast. 
    beverage2 = Whip(beverage2)   #CC                                                                 # 3) Se crea el segundo objeto/condimento Whip que envuelve al Mocha.+
    descripcion2 = beverage2.get_description()
    costo2 = beverage2.cost()
    print(f"Pedido 2: {descripcion2} ${costo2:.2f}")
    
    #print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")
    # descripcio2 = Whip(Mocha(DarkRoast)) -- > Whip(beverage2)  -- > Mocha(beverage2)  -- > DarkRoast() 


    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")


    
    ### ------------- TP Nivel 1 ------------- ###
    ### -------------------------------------- ###

    # Pedido 4: Un Espresso con Caramel y Crema.
    beverage4 = Espresso() 
    beverage4 = Caramel(beverage4)
    beverage4 = Whip(beverage4)
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")

    # Pedido 5: Un DarkRoast con doble Caramel y Crema.
    beverage5 = DarkRoast() 
    beverage5 = DobleCaramel(beverage5) 
    beverage5 = Whip(beverage5) 
    print(f"Pedido 5: {beverage5.get_description()} ${beverage5.cost():.2f}")


    

    ### ------------- TP Nivel 2 ------------- ###
    ### -------------------------------------- ###

    beverage6 = HouseBlend()
    beverage6.set_size("Tall")  # Establecemos tamaño Venti
    beverage6 = Soy(beverage6)    # Agregamos condimento
    print(f"Pedido 6: {beverage6.get_description()} ({beverage6.get_size()}) ${beverage6.cost():.2f}")   

    beverage7 = HouseBlend()
    beverage7.set_size("Grande")  # Establecemos tamaño Venti
    beverage7 = Soy(beverage7)    # Agregamos condimento
    print(f"Pedido 7: {beverage7.get_description()} ({beverage7.get_size()}) ${beverage7.cost():.2f}") 

    beverage8 = HouseBlend()
    beverage8.set_size("Venti")  # Establecemos tamaño Venti
    beverage8 = Soy(beverage8)    # Agregamos condimento
    print(f"Pedido 8: {beverage8.get_description()} ({beverage8.get_size()}) ${beverage8.cost():.2f}")   

if __name__ == "__main__":
    main()
