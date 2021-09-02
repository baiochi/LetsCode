def comprimentaPessoas(*tuplaNomes):
    for nome in tuplaNomes:
        print(f"Olá, {nome}")


# comprimentaPessoas("Brian", "Lari", "Luis")


def montaPizza(**infosPizza):
    print(f"montando pizza de {infosPizza.get('nome', 'nada')}")
    print(f"Borda {infosPizza.get('borda', 'padrão')}")

montaPizza(nome = "Palmito")
print()
montaPizza(borda = "recheada", nome = "Queijo")
print()
montaPizza()