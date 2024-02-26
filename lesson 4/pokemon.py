import requests
pokemons = {}
# Get pokemon by name
# Get pokemon by name
def get_pokemon_by_name(pokemon_name):
    # Make a request to the Pokemon API
    pokemon_API = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

    # Check if the request was successful (status code 200)
    if pokemon_API.status_code == 200:
        # Parse the JSON data
        pokemon_data = pokemon_API.json()

        # Store the Pokemon data in the dictionary
        pokemons[pokemon_name.lower()] = pokemon_data
        print(f'Fetched data for {pokemon_name}')

        return pokemon_data  # Return the fetched data

    else:
        print(f'Failed to fetch data for {pokemon_name}')
        return None  # Return None in case of failure


def display_pokemon(pokemon_data):
    # Check if pokemon_data is not None
    if pokemon_data:
        print(f'Name: ' + pokemon_data['name'])
        print(f'Base Experience: ' + str(pokemon_data['base_experience']))
        types = pokemon_data.get('types', [])
        for entry in types:
            type_info = entry.get('type', {})
            type_name = type_info.get('name', 'Unknown Type')
        print(f'Type: {type_name}')
        print("Stats: ", end="")
        print()
        for stat in pokemon_data['stats']:
            stat_name = stat['stat']['name'].capitalize().replace('-', ' ')
            base_stat = stat['base_stat']
            print(f"  - {stat_name}: {base_stat}")
pokemon_name = input("Enter Pokémon name: ")
pokemon_data = get_pokemon_by_name(pokemon_name)
display_pokemon(pokemon_data)

# Loop to search for more Pokémon
while True:
    choice = input("Search for another Pokémon? (yes/no): ")
    if choice.lower() == "yes":
        pokemon_name = input("Enter Pokémon name: ")
        pokemon_data = get_pokemon_by_name(pokemon_name)
        display_pokemon(pokemon_data)
    else:
        break

