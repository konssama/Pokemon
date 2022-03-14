import setup

normal = setup.Type(
    name="Normal", 
    double=[], 
    half=["Rock", "Steel"], 
    zero=["Ghost"])
fire = setup.Type(
    name="Fire", 
    double=["Grass", "Ice", "Bug", "Steel"], 
    half=["Fire", "Water", "Rock", "Dragon"], 
    zero=[])
water = setup.Type(
    name="Water", 
    double=["Fire", "Ground", "Rock"], 
    half=["Water", "Grass", "Dragon"], 
    zero=[])
grass = setup.Type(
    name="Grass", 
    double=["Water", "Ground", "Rock"], 
    half=["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"], 
    zero=[])
electric = setup.Type(
    name="Electric", 
    double=["Water", "Flying"], 
    half=["Grass", "Electric", "Dragon"], 
    zero=["Ground"])
ice = setup.Type(
    name="Ice", 
    double=["Grass", "Ground", "Flying", "Dragon"], 
    half=["Fire", "Water", "Ice", "Steel"], 
    zero=[])
fighting = setup.Type(
    name="Fighting", 
    double=["Normal", "Ice", "Rock", "Dark", "Steel"], 
    half=["Poison", "Flying", "Psychic", "Bug", "Fairy"], 
    zero=["Ghost"])
poison = setup.Type(
    name="Poison", 
    double=["Grass", "Fairy"], 
    half=["Poison", "Ground", "Rock", "Ghost"], 
    zero=["Steel"])
ground = setup.Type(
    name="Ground", 
    double=["Fire", "Electric", "Poison", "Rock", "Steel"], 
    half=["Grass", "Bug"], 
    zero=["Flying"])
flying = setup.Type(
    name="Flying", 
    double=["Grass", "Fighting", "Bug"], 
    half=["Electric", "Rock", "Steel"], 
    zero=[])
psychic = setup.Type(
    name="Psychic", 
    double=["Fighting", "Poison"],
    half=["Psychic", "Steel"], 
    zero=["Dark"])
bug = setup.Type(
    name="Bug", 
    double=["Grass", "Psychic", "Dark"], 
    half=["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"], 
    zero=[])
rock = setup.Type(
    name="Rock", 
    double=["Fire", "Ice", "Flying", "Bug"], 
    half=["Fighting", "Flying", "Steel"], 
    zero=[])
ghost = setup.Type(
    name="Ghost", 
    double=["Psychic", "Ghost"], 
    half=["Dark"], 
    zero=["Normal"])
dragon = setup.Type(
    name="Dragon", 
    double=["Dragon"], 
    half=["Steel"], 
    zero=["Fairy"])
dark = setup.Type(
    name="Dark", 
    double=["Psychic", "Ghost"], 
    half=["Dark", "Fairy"], 
    zero=[])
steel = setup.Type(
    name="Steel", 
    double=["Ice", "Rock", "Fairy"], 
    half=["Fire", "Water", "Electric", "Steel"], 
    zero=[])
fairy = setup.Type(
    name="Fairy", 
    double=["Fighting", "Dragon", "Dark"], 
    half=["Fire", "Poison", "Steel"], 
    zero=[])

allTypes = [normal, fire, water, grass, electric, ice,
            fighting, poison, ground, flying, psychic,
            bug, rock, ghost, dragon, dark, steel, fairy]