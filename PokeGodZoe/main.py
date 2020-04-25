import pokemons
import poketypes
import powers
type = int(input('digite o numero da pokedex do pokemon atacante e veja contra o que ele é forte'))
try:
    print(powers.strong(pokemons.pokedex[type-1]['type'][0]))
except:
    print('numero n encontrado')

