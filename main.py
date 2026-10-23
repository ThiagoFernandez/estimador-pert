textos = {
    "do": "Ingrese el valor de la duracion optimista: ",
    "mp": "Ingrese el valor de la duracion mas probable: ",
    "dp": "Ingrese el valor de la duracion pesimista: "
}
valores = {
    "do": 0,
    "mp":0,
    "dp": 0
}

def validar_int(x):
    try:
        x=int(x)
    except ValueError:
        print("debe ingresar un numero")
        return False

    if x <=0:
        print("Los valores deben ser mayores a 0")
        return False
    return x

def formula_pert(do, mp, dp):
    return (do+4 * mp + dp) / 6

def desviacion_pert(do, dp):
    return (dp-do)/6

def variaza_pert(desviacion):
    return desviacion**2

def main():
    print("Estimador PERT")
    actividades = {}
    while True:
        nombre_actividad = input("Ingrese el nombre de la actividad: ")

        for k,txt in textos.items():
            valor = input(txt)
            rt = validar_int(valor)
            if rt is False:
                break
            valores[k] = rt

        if rt is False:
            continue

        resultado_1 = formula_pert(valores["do"], valores["mp"], valores["dp"])
        resultado_2 = desviacion_pert(valores["do"], valores["dp"])
        resultado_3 = variaza_pert(resultado_2)
        actividades[nombre_actividad] = {
            "calculo_pert": resultado_1,
            "desviacion": resultado_2,
            "varianza": resultado_3
        }
        print(f"El resultado da: {resultado_1}, su desviacion es de: {resultado_2} y su varianza: {resultado_3}")

        valor = input("Desea continuar(si-no): ").strip().lower()
        if valor != "si":
            break

    for k,v in actividades.items():
        print(f"Resultado para {k}")
        for n,m in v.items():
            print(f"{n}:{m}")  
main()