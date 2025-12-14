#Programacion utilizando el paradigma de las POO para determinar el promedio semanal del clima
#Diseña una solución utilizando el paradigma de POO.
#Crea una clase que represente la información diaria del clima.
#Utiliza métodos de la clase para ingresar datos y calcular el promedio semanal.
#Asegúrate de aplicar conceptos como encapsulamiento, herencia o polimorfismo según sea apropiado.

class Clima:
    def __init__(self, temperaturas):
        self.__temperaturas = temperaturas  # Atributo privado para encapsulamiento

    def calcular_promedio(self):
        suma_temperaturas = sum(self.__temperaturas)
        promedio = suma_temperaturas / len(self.__temperaturas)
        return promedio
# Puedes agregar más métodos o clases si es necesario para mejorar la funcionalidad.
# Por ejemplo, podrías crear una clase base para diferentes tipos de datos climáticos.
# Sin embargo, para este caso específico, una sola clase es suficiente.
# Ejemplo de uso:
#Lista de temperaturas diarias durante una semana
temperaturas_semanales = [22.5, 24.0, 19.5, 21.0, 23.5, 20.0, 25.0]
clima_semanal = Clima(temperaturas_semanales)
promedio_semanal = clima_semanal.calcular_promedio()
print(f"El promedio semanal del clima es: {promedio_semanal:.2f} °C")


