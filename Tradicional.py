# Programacion tradicional para determinar el promedio semanal del clima

def calcular_promedio_clima(temperaturas):
    suma_temperaturas = 0
    for temperatura in temperaturas:
        suma_temperaturas += temperatura
    promedio = suma_temperaturas / len(temperaturas)
    return promedio
# Lista de temperaturas diarias durante una semana
temperaturas_semanales = [22.5, 24.0, 19.5, 21.0, 23.5, 20.0, 25.0]
promedio_semanal = calcular_promedio_clima(temperaturas_semanales)
print(f"El promedio semanal del clima es: {promedio_semanal:.2f} °C")