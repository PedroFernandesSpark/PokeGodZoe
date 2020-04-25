def strong(type):
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
    try :
        return switch[type]
    except :
        return 'type not found'