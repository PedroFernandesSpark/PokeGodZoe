# all the functions here has the same structure
# them get a type and return an array of types
# it was based on a switch case from c++ and objects from JS
# I chosed this structure to reduce the ifs in the code

def takeLessDMG(type):
    switch = {
        'Normal': ['Rock', 'Steel'],
        'Fighting': ['Poison', 'Psychic', 'Rock', 'Bug', 'Fairy'],
        'Flying': ['Electric', 'Rock', 'Steel'],
        'Poison': ['Poison', 'Grass', 'Rock', 'Ghost'],
        'Ground': ['Grass', 'Bug'],
        'Rock': ['Fighting', 'Ground', 'Steel'],
        'Bug': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy'],
        'Ghost': ['Dark'],
        'Steel': ['Fire', 'Water', 'Electric', 'Steel'],
        'Fire': ['Fire', 'Water', 'Rock', 'Dragon'],
        'Water': ['Water', 'Grass', 'Dragon'],
        'Grass': ['Water', 'Ground', 'Rock'],
        'Electric': ['Electric', 'Dragon'],
        'Psychic': ['Psychic', 'Steel'],
        'Ice': ['Fire', 'Water', 'Ice', 'Steel'],
        'Dragon': ['Steel'],
        'Fairy': ['Fire', 'Poison', 'Steel'],
        'Dark': ['Fighting', 'Dark', 'Fairy']
    }
    try:
        return switch[type]
    except:
        return 'Type not found'

def takeMoreDMG(type):
    switch = {
        'Normal': ['Fighting'],
        'Fighting': ['Fairy', 'Flying', 'Psychic'],
        'Flying': ['Electric', 'Rock', 'Ice'],
        'Poison': ['Psychic', 'Ground'],
        'Ground': ['Grass', 'Ice', 'Water'],
        'Rock': ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'],
        'Bug': ['Fire', 'Flying', 'Rock'],
        'Ghost': ['Dark', 'Ghost'],
        'Steel': ['Fighting', 'Fire', 'Ground'],
        'Fire': ['Ground', 'Water', 'Rock'],
        'Water': ['Electric', 'Grass'],
        'Grass': ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'],
        'Electric': ['Ground'],
        'Psychic': ['Bug', 'Dark', 'Ghost'],
        'Ice': ['Fire', 'Fighting', 'Rock', 'Steel'],
        'Dragon': ['Steel', 'Fairy', 'Ice'],
        'Fairy': ['Poison', 'Steel'],
        'Dark': ['Fighting', 'Bug', 'Fairy']
    }
    try:
        return switch[type]
    except:
        return 'Type not found'

def dealsMoreDMG(type):
    switch = {
        'Normal': [''],
        'Fighting': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
        'Flying': ['Grass', 'Fighting', 'Bug'],
        'Poison': ['Grass', 'Fairy'],
        'Ground': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
        'Rock': ['Fire', 'Ice', 'Flying', 'Bug'],
        'Bug': ['Grass', 'Psychic', 'Dark'],
        'Ghost': ['Psychic', 'Ghost'],
        'Steel': ['Ice', 'Rock', 'Fairy'],
        'Fire': ['Grass', 'Ice', 'Bug', 'Steel'],
        'Water': ['Fire', 'Ground', 'Rock', 'Steel'],
        'Grass': ['Water', 'Ground', 'Rock'],
        'Electric': ['Water', 'Flying'],
        'Psychic': ['Fighting', 'Poison'],
        'Ice': ['Grass', 'Ground', 'Flying', 'Dragon'],
        'Dragon': ['Dragon'],
        'Fairy': ['Fighting', 'Dragon', 'Dark']
    }
    try:
        return switch[type]
    except:
        return 'type not found'

def dealsNoDMG(type):
    switch = {
        'Normal': ['Ghost'],
        'Fighting': ['Ghost'],
        'Flying': [],
        'Poison': ['Steel'],
        'Ground': ['Flying'],
        'Rock': [],
        'Bug': [],
        'Ghost': ['Normal'],
        'Steel': [],
        'Fire': [],
        'Water': [],
        'Grass': [],
        'Electric': ['Ground'],
        'Psychic': ['Dark'],
        'Ice': [],
        'Dragon': ['Fairy'],
        'Fairy': [],
        'Dark': []
    }
    try:
        return switch[type]
    except:
        return 'Type not found'