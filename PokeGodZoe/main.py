import pokemons
import types
import search
import super

counter = 0
on = True
while (on == True):
    name = (input('Chose one pokemon: '))
    # every pokemon name in the data base starts with a capital letter
    name = name.capitalize()
    # used to stop the program
    if name == 'Stop':
        on = False
    type = []
    name = pokemons.pokedex[search.searchPokemon(name)-1]['name']['english']
    print('The Pokemon', name, ':')
    for i in pokemons.pokedex[search.searchPokemon(name)-1]['type']:
        type.append(search.strongTypeArray(types.takeLessDMG(i)))
        print('Take less Dmg', types.takeLessDMG(i))
    for i in pokemons.pokedex[search.searchPokemon(name) - 1]['type']:
        type.append(search.weakTypeArray(types.dealsMoreDMG(i)))
        print('Deals more Dmg', types.dealsMoreDMG(i))
    for i in pokemons.pokedex[search.searchPokemon(name) - 1]['type']:
        type.append(search.immuneTypeArray(types.dealsNoDMG(i)))
        print('Deals no Dmg', types.dealsNoDMG(i))
    for i in pokemons.pokedex[search.searchPokemon(name) - 1]['type']:
        type.append(search.moreDMGTypeArray(types.takeMoreDMG(i)))
        print('Take more Dmg', types.takeMoreDMG(i))
    for i in pokemons.pokedex[search.searchPokemon(name) - 1]['type']:
        type.append(search.dealLessTypeArray(types.dealsLessDMG(i)))
        print('Deals less Dmg', types.dealsLessDMG(i))

    use = super.atk(search.searchPokemon(name))
    best = search.bestPokemon(type)
    bestPokemonIds = super.bestAtk(best, use)

    # if you want to list all pokemons in the bestPokemonIds array
    #for i in bestPokemonIds:
        # if True:
            # print(pokemons.pokedex[i-1]['name']['english'])
            #counter+=1
    #print(counter)
    #counter = 0
    print('')
    print('The enemy pokemon is:')
    print(pokemons.pokedex[search.searchPokemon(name)-1]['name']['english'])
    print(pokemons.pokedex[search.searchPokemon(name) - 1]['type'])
    print(pokemons.pokedex[search.searchPokemon(name)-1]['base'])
    print('')
    print('The best pokemon is:')
    # if you want to get the best pokemon id, uncomment the next line (it can be useful for debugging)
    # print(pokemons.pokedex[super.better(bestPokemonIds, use) - 1]['id'])
    print(pokemons.pokedex[super.better(bestPokemonIds, use)-1]['name']['english'])
    print(pokemons.pokedex[super.better(bestPokemonIds, use) - 1]['type'])
    print(pokemons.pokedex[super.better(bestPokemonIds, use) - 1]['base'])
    print('')
    print('')
    print('')