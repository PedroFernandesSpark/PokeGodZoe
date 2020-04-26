import pokemons

# search the id based on the name the user has chosen
def searchPokemon(name):
    for i in pokemons.pokedex:
        try:
            if (i['name']['english'] == name):
                return i['id']
        except:
            return -1


def moreDMGTypeArray(type):
    moreDMGAgainst = []
    for i in pokemons.pokedex:
        for x in type:
            if (x in i['type']):
                moreDMGAgainst.append(i['id'])

    return moreDMGAgainst

def weakTypeArray(type):
    weakAgainst = []
    for i in pokemons.pokedex:
        for x in type:
            if (x in i['type']):
                weakAgainst.append(i['id'])

    return weakAgainst

def strongTypeArray(type):
    strongAgains = []
    for i in pokemons.pokedex:
        for x in type:
            if (x in i['type']):
                strongAgains.append(i['id'])

    return strongAgains

def immuneTypeArray(type):
    immuneAgains = []
    for i in pokemons.pokedex:
        for x in type:
            if (x in i['type']):
                immuneAgains.append(i['id'])

    return immuneAgains

def bestPokemon(types):
    # types is an array of arrays, it contains the id of pokemons:
    # types[0] = pokemons that takes less dmg from the pokemon chosen by the user
    # types[1] = pokemons that takes more dmg from the pokemon chosen by the user
    # types[2] = pokemons that takes no dmg from the pokemon chosen by the user
    # types[3] = pokemons that deals more dmg from the pokemon chosen by the user
    bestPokemonIds = []
    for dmg in types[3]:
        if dmg in types[0]:
            if (dmg not in bestPokemonIds):
                bestPokemonIds.append(dmg)
    # this if is used when you cant find a combination of types[0] and types[3]
    if len(bestPokemonIds) == 0:
        print('cant find a perfect combination')
        for dmg in types[3]:
                if (dmg not in bestPokemonIds):
                    bestPokemonIds.append(dmg)
        for str in types[0]:
            if (str not in bestPokemonIds):
                bestPokemonIds.append(dmg)
    for imm in types[2]:
        if (imm not in bestPokemonIds):
            bestPokemonIds.append(imm)
    for wea in types[1]:
        if (wea in bestPokemonIds):
            bestPokemonIds.remove(wea)
    return bestPokemonIds
    # it returns a array of the ids of the best pokemons based on type advantage





