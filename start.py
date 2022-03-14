#All: 325 lines
#Pure Code: 140 lines

import PySimpleGUI as gui
import main
import PokemonList as pokemon
import random

layout = [
    [gui.Button("Fire"), gui.Button("Water")],
    [gui.Button("Grass"), gui.Button("Random")]
    ]
startingWindow = gui.Window(title="Pokemon", layout=layout, size=(500,500))

while True:
    event, values = startingWindow.read()
    if event == "Fire": player = pokemon.charizard
    elif event == "Water": player = pokemon.blastoise
    elif event == "Grass": player = pokemon.venusaur
    elif event == "Random": player = random.choice(pokemon.allPokemon)
    
    if event == gui.WIN_CLOSED: 
        startingWindow.Close()
        break

    startingWindow.Close()
    main.startRound(player, opponent=random.choice(pokemon.allPokemon))