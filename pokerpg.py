import random
poke_very_common = ["Caterpie", "Weedle", "Pidgey", "Rattata", "Ekans", "Sandshrew", "Nidoran(Female)", 
    "Nidoran(Male)", "Zubat", "Geodude", "Bellsprout", "Machop", "Poliwag", "Mankey", 
    "Meowth", "Venonat", "Paras", "Oddish", "Slowpoke", "Magnemite", "Gastly", "Krabby", 
    "Voltorb", "Goldeen", "Magikarp", "Eevee"]

poke_common = ["Bulbasaur", "Charmander", "Squirtle", "Metapod", "Kakuna", "Pidgeotto", "Raticate", 
    "Spearow", "Arbok", "Psyduck", "Persian", "Diglet", "Golbat", "Jigglypuff", "Vulpix", 
    "Clefairy", "Sandslash", "Pikachu", "Growlithe", "Abra", "Machoke", "Tentacool", 
    "Graveler", "Ponyta", "Magneton", "Doduo", "Seel", "Koffing", "Hitmonlee", "Cubone", 
    "Exeggcute", "Electrode", "Drowzee", "Haunter", "Shellder", "Grimer", "Rhyhorn", 
    "Horsea", "Staryu", "Jynx"]

poke_unusual = ["Butterfree", "Fearow", "Nidorina", "Nidorino", "Wigglytuff", "Gloom", "Parasect", 
    "Dugtrio", "Kabuto", "Golem", "Tentacruel", "Machamp", "Kadabra", "Poliwhirl", 
    "Chansey", "Primeape", "Golduck", "Dratini", "Dodrio", "Cloyster", "Scyther", 
    "Hypno", "Seadra", "Seaking", "Starmie"
]

poke_rare = ["Beedrill", "Pidgeot", "Weepinbell", "Pinsir", "Snorlax", "Mr. Mime", "Farfetch'd", 
    "Onix", "Exeggutor", "Muk", "Arcanine", "Rapidash", "Rhydon", "Kingler", "Magmar", 
    "Flareon", "Jolteon", "Tangela"]

poke_very_rare =["Gyarados", "Lapras", "Vaporeon", "Kabutops", "Ivysaur", "Charmeleon", "Wartortle", 
    "Porygon", "Omanyte", "Dragonair", "Raichu", "Nidoqueen", "Nidoking", "Vileplume", 
    "Gengar", "Marowak", "Dewgong", "Kangaskhan", "Victreebel", "Electabuzz", "Alakazam", 
    "Poliwrath", "Venomoth"
]

poke_epic = [ "Aerodactyl", "Venusaur", "Charizard", "Blastoise", "Clefable", "Tauros", "Omastar", "Dragonite"]

poke_legendary = ["Ditto", "Articuno", "Zapdos", "Moltres", "Mewtwo", "Mew"]



escolha = int(input('Bem-vindo ao PokePG, Comece a caçada:\n [1]Caçar\n\n'))

def capturaOunão():
  dt = 10
  if roll >= dt:
    print(f'Você capturou {global_choice} com sucesso')
  else:
    print(f'O {global_choice} FUGIU...')



def juntandolistas():
  conj_lists= [poke_very_common, poke_common, poke_unusual,         
  poke_rare, poke_very_rare, poke_epic, poke_legendary]

  concatenate_lists = []

  for list in conj_lists:
    concatenate_lists += list

  choice = random.choice(concatenate_lists)
  return choice

global_choice = juntandolistas()
  



if escolha == 1:
  print(f'Um {global_choice} apareceu o que você faz?')
  escolha2 = int(input('Escolha sua opção:\n [2]Capturar\n [3]Fugir\n\n'))
if escolha2 == 2:
  print('Rolando seu dado...')
  roll = random.randint(1,20)
  print(f'O seu dado saiu no valor de {roll}')
  capturaOunão()
elif escolha2 == 3:
  print('Você fugiu..')
  exit()


