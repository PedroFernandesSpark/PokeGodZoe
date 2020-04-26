import pokemons


# It choses what the bot should use based on the defense status
def atk(pokeid):
    base_status = pokemons.pokedex[pokeid - 1]['base']
    if (base_status['Defense'] == base_status['Sp. Defense']):
        print('This pokemon has no difference between Sp. Defence and Defence')
        return 'Use Any'
    if (base_status['Defense'] > base_status['Sp. Defense']):
        print('This pokemon has a better or equal Normal def')
        return 'Use Super'
    else:
        print('This pokemon has a better Super def')
        return 'Use Normal'


# it chose the pokemons that has the best status
def bestAtk(pokeids, use):
    bestPokeIds = []
    if use == 'Use Super':
        for i in pokeids:
            if pokemons.pokedex[i-1]['base']['Sp. Attack'] > pokemons.pokedex[i-1]['base']['Attack']:
                bestPokeIds.append(i)
    if use == 'Use Normal':
        for i in pokeids:
            if pokemons.pokedex[i-1]['base']['Attack'] >= pokemons.pokedex[i-1]['base']['Sp. Attack']:
                bestPokeIds.append(i)
    if use == 'Use Any':
        return pokeids
    return bestPokeIds


# here the bot defines the best pokemon
def better(bestPokemonIds, use):
    best = 0
    bestPokemon = -1
    if use == 'Use Super':
        for i in bestPokemonIds:
            if pokemons.pokedex[i - 1]['base']['Sp. Attack'] > best:
                best = pokemons.pokedex[i-1]['base']['Sp. Attack']
                bestPokemon = i
    if use == 'Use Normal':
        for i in bestPokemonIds:
            if pokemons.pokedex[i - 1]['base']['Attack'] > best:
                best = pokemons.pokedex[i-1]['base']['Attack']
                bestPokemon = i
    if use == 'Use Any':
        for i in bestPokemonIds:
            if pokemons.pokedex[i - 1]['base']['Sp. Attack'] > pokemons.pokedex[i - 1]['base']['Attack']:
                if pokemons.pokedex[i - 1]['base']['Sp. Attack']:
                    best = pokemons.pokedex[i - 1]['base']['Sp. Attack']
                    bestPokemon = i
            else:
                if pokemons.pokedex[i - 1]['base']['Attack']:
                    best = pokemons.pokedex[i - 1]['base']['Attack']
                    bestPokemon = i
    return bestPokemon
