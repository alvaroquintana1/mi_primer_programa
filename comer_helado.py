
apetece_helado_input = input("¿Te apetece un helado? (Si/No): ")
tiene_dinero_input = input("¿Tienes dinero para un helado? (Si/No):")
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si/No):")
esta_su_tia_input = input("¿estas con su tia?")

apetece_helado = apetece_helado_input == "si"
puede_permitirselo = tiene_dinero_input == "si" or esta_su_tia_input == "si"
esta_el_senor_helados = esta_el_senor_helados_input == "si"

if apetece_helado and puede_permitirselo:
    if esta_el_senor_helados
        print("pues comete un helado")
    else:
        print("pues nada")
else:
    print("pues nada")