#deficion de funcion
def promediocalificaciones(p1,p2,p3):
    promedio=(p1+p2+p3)/3
    return promedio

#generar el codigo principal
def main():
    calificacionparcial1 = float(input("Ingrese la calificacion del parcial 1 "))
    calificacionparcial2 = float(input("Ingrese la calificacion del parcial 2 "))
    calificacionparcial3 = float(input("Ingrese la calificacion del parcial 3 "))

    #llamar a la funcion
    total= promediocalificaciones(calificacionparcial1, calificacionparcial2, calificacionparcial3)

    #imprimir valor
    print(f"la calificacion del alumno es: {total:.3f}")

if __name__=="__main__":
    main()