import setup
import TypeList as types
import MoveList as moves

venusaur = setup.Pokemon(
    name="Venusaur", 
    sprite=None, 
    types=[types.grass, types.poison], 
    moves=[moves.razorLeaf, moves.seedBomb, moves.takeDown, moves.solarBeam], 
    stats=[80, 82, 83, 100, 100, 80])
charizard = setup.Pokemon(
    name="Charizard", 
    sprite= None,
    types=[types.fire, types.flying], 
    moves=[moves.fireFang, moves.dragonClaw, moves.airSlash, moves.flamethrower], 
    stats=[78, 84, 78, 109, 85, 100])
blastoise = setup.Pokemon(
    name="Blastoise", 
    sprite=None, 
    types=[types.water], 
    moves=[moves.waterGun, moves.rapidSpin, moves.hydroPump, moves.skullBash], 
    stats=[79, 83, 100, 86, 105, 78])

allPokemon = [venusaur, charizard, blastoise]