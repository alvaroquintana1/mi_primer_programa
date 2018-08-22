
operacion = input("¿Que operacion quieres realizar? (Dividir / Multiplicar / Sumar / Restar) ")

primer_numero = int(input("Inserta el primero numero"))
segundo_numero = int(input("Inserta el segundo numero"))

signo_dividir = "/"
signo_multiplicar = "*"
signo_sumar = "+"
signo_restar = "-"

if operacion == "Dividir":
    resultado = primer_numero/segundo_numero
    print("Operacion definida       {}{}{}".format(primer_numero, signo_dividir, segundo_numero))
    print("Resultado  = {}".format(resultado))

elif operacion == "Multiplicar":
    resultado = primer_numero*segundo_numero
    print("Operacion definida        {}{}{}".format(primer_numero, signo_multiplicar, segundo_numero))
    print("Resultado  = {}".format(resultado))

elif operacion == "Sumar":
    resultado = int(primer_numero+segundo_numero)
    print("Operacion definida        {}{}{}".format(primer_numero, signo_sumar, segundo_numero))
    print("Resultado  = {}".format(resultado))

elif operacion == "restar":
    resultado = primer_numero-segundo_numero
    print("Operacion definida        {}{}{}".format(primer_numero, signo_restar, segundo_numero))
    print("Resultado = {}".format(resultado))

