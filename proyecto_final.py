import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficacion_2D(a, b, c):
    #Valores para X
    x = np.linspace(-10, 10, 400)
    
    #Fórmula de la ecuación
    y = a * x**2 + b * x + c
    
    #Crea la gráfica en 2D
    plt.figure()
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.title('Gráfica 2D de la función cuadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def graficacion_3D(a, b, c):
    #Valores para X e Y
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    
    # Creación de la malla
    X, Y = np.meshgrid(x, y)
    
    # Modificación: función cuadrática en 3D (ejemplo: Z = aX² + bY² + c)
    Z = a * X**2 + b * Y**2 + c  # Ahora Y tiene un efecto cuadrático para visualizar mejor en 3D
    
    #Crear la grafica en 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    
    ax.set_title('Gráfica 3D de la función cuadrática')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def main():
    #Solicitud de datos
    print("Ecuación cuadrática: ax² + by² + c (en 3D), o ax² + bx + c (en 2D)")
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    
    #Elección de muestra en 2D o 3D
    print("Elija el tipo de gráfica que desea ver:")
    print("1. Gráfica 2D")
    print("2. Gráfica 3D")
    opcion = int(input("Ingrese el número de su opción: "))
    
    if opcion == 1:
        graficacion_2D(a, b, c)
    elif opcion == 2:
        graficacion_3D(a, b, c)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
