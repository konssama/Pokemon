import PySimpleGUI as gui
import setup
import random

def playerMoves(player, opponent):
    moveLayout = [
        [gui.Button(button_text=player.moves[0].name, key="-Move1-"), gui.Button(button_text=player.moves[1].name, key="-Move2-")],
        [gui.Button(button_text=player.moves[2].name, key="-Move3-"), gui.Button(button_text=player.moves[3].name, key="-Move4-")] 
    ]
    
    moveWindow = gui.Window("Choose Move", moveLayout, size=(250,200))
    global stopRound
    stopRound = False
    event, values = moveWindow.read()
    
    if event == "-Move1-": 
        chosenMove = player.moves[0]
        player.attack(opponent, chosenMove) 
    elif event == "-Move2-": 
        chosenMove = player.moves[1]
        player.attack(opponent, chosenMove) 
    elif event == "-Move3-": 
        chosenMove = player.moves[2]
        player.attack(opponent, chosenMove) 
    elif event == "-Move4-": 
        chosenMove = player.moves[3]
        player.attack(opponent, chosenMove) 
    elif event == gui.WIN_CLOSED: stopRound = True
    moveWindow.Close()

def opponentMoves(player, opponent):
    randomMove = random.choice(opponent.moves)
    if not(stopRound): opponent.attack(player, randomMove)

def startRound(player:setup.Pokemon, opponent:setup.Pokemon):
    layout = [
    [gui.Text(f"Player: {player.name}")],
    [gui.Text(f"Opponent: {opponent.name}")],

    [gui.Text(f"{player.name}'s health: {player.stats[0]}")],
    [gui.Text(f"{opponent.name}'s health: {opponent.stats[0]}")],

    [gui.Button(button_text="Start")]
    ]
    
    global window
    window = gui.Window(title="Pokemon", layout=layout, size=(500,500))

    while True:
        event, values = window.read()
        if event == "Start": break
        elif event == gui.WINDOW_CLOSED: break

    window.Close()

    if event != gui.WIN_CLOSED:
        if player.stats[5] >= opponent.stats[5]:
            playerMoves(player, opponent)
            opponentMoves(player, opponent)
        else:
            opponentMoves(player, opponent)
            playerMoves(player, opponent)

        if player.stats[0] > 0 and opponent.stats[0] > 0: startRound(player, opponent)