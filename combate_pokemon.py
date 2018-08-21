
pokemon_elegido = input("¿Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasur): ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "Bulbasur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vamos a usar? (Ataque chispazo / Bola voltio) ")

    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12

    print("La vida del {} ahora es de {}".format(nombre_pokemon,vida_enemigo))

    print("te hace un ataque de 8 de daño".format(nombre_pokemon))
    vida_pikachu-= ataque_pokemon

    print("La vida de pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("has ganado")
if vida_pikachu <= 0:
    print("has perdido")

print("el combate ha terminado")