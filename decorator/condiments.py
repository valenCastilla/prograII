# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):                                            # 2.2) Se Crea la clase abstracta que hereda de Beverage
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):                                         # 2.3) El constructor recibe un objeto Beverage que es la bebida que se va a decorar.   
        self._beverage = beverage

    def get_size(self) -> str:                                                     ## --- TP Nivel 2 --- ###                   
        return self._beverage.get_size()

    @abstractmethod
    def get_description(self) -> str:
        pass



# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10



class Mocha(CondimentDecorator):                                                    # 2.1) Se inicia el decorador Mocha que hereda de CondimentDecorator.
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:                                               # 2.4) Mocha utiliza el método get_descripción para obtener la información de _beverage y le añade ", Mocha".
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:                                                         # 2.5) El método cost() llama al método cost() de _beverage y le añade el costo del Mocha.   
        return self._beverage.cost() + 0.20



class Soy(CondimentDecorator):                                                   ## --- TP Nivel 2 --- ###
    """
    Decorador para añadir Soja a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        size = self._beverage.get_size()  
        if size == "Tall":
            return self._beverage.cost() + 0.10
        elif size == "Grande":
            return self._beverage.cost() + 0.15
        elif size == "Venti":
            return self._beverage.cost() + 0.20
        else:
            return self._beverage.cost() + 0.10  



class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.15



class Caramel(CondimentDecorator):                                                        ## --- TP Nivel 1 --- ###

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramel"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20



class DobleCaramel(CondimentDecorator):                                                   ## --- TP Nivel 1 --- ###

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Doble Caramel"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20 + 0.20

