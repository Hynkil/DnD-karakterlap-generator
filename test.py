import random

RACE_BONUSES = {
    'human': {
        'calishite': {'charisma': 2, 'strength': 1, 'dexterity': 1, 'constitution': 1, 'intelligence': 1, 'wisdom': 1},
        'damarai': {'strength': 2, 'charisma': 1, 'dexterity': 1, 'constitution': 1, 'intelligence': 1, 'wisdom': 1},
        'forest': {'dexterity': 2, 'strength': 1, 'constitution': 1, 'charisma': 1, 'intelligence': 1, 'wisdom': 1},
        'mountains': {'constitution': 2, 'charisma': 1, 'strength': 1, 'dexterity': 1, 'intelligence': 1, 'wisdom': 1},
        'base': {'constitution': 1, 'charisma': 1, 'strength': 1, 'dexterity': 1, 'intelligence': 1, 'wisdom': 1}
    },
    'elf': {
        'high elf': {'intelligence': 1, 'dexterity': 2},
        'wood elf': {'wisdom': 1, 'dexterity': 2},
        'base': {'dexterity': 2}
    },
    'halflings': {
        'lightfoot': {'charisma': 1, 'dexterity': 2},
        'stout': {'constitution': 1, 'dexterity': 2},
        'base': {'dexterity': 2}
    },
    'dwarf': {
        'mountain dwarf': {'strength': 1, 'constitution': 2},
        'hill dwarf': {'wisdom': 1, 'constitution': 2},
        'base': {'constitution': 2}
    }
}

STATS = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

def generate_stats():
    return {stat: random.randint(3, 18) for stat in STATS}

def apply_race_bonus(race):
    race = race.lower()
    if race == 'homebrew':
        custom_race_name = input("Enter your custom race name: ")
        custom_bonuses = {}
        while True:
            stat = input("Enter a stat (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) "
                         "(or type 'done' when finished): ").capitalize()
            if stat == 'Done':
                break
            if stat.lower() not in STATS:
                print("Invalid stat name.")
                continue
            value = int(input(f"Enter bonus value for {stat}: "))
            custom_bonuses[stat.lower()] = value
        return {'Custom Race': custom_race_name, **custom_bonuses}

    if race in RACE_BONUSES:
        subspecies_choice = input(f"Do you want to choose a subspecies for {race} (yes/no)? ").lower()
        if subspecies_choice == 'yes':
            subspecies = input(f"Choose a subspecies: {', '.join(RACE_BONUSES[race].keys())}: ").lower()
            if subspecies in RACE_BONUSES[race]:
                return {'Subspecies': subspecies, **RACE_BONUSES[race][subspecies]}
            else:
                print("Invalid subspecies choice. Applying base race bonuses.")
        
        base_bonuses = RACE_BONUSES[race].get('base', {})
        return {'Subspecies': '', **base_bonuses}
    else:
        print("Invalid race.")
        return {}

def create_character_sheet(name, character_class, race):
    stats = generate_stats()
    race_bonus = apply_race_bonus(race)

    for key, value in race_bonus.items():
        if key in STATS:
            stats[key] += value

    return {
        'Name': name,
        'Class': character_class,
        'Race': race,
        'Stats': stats,
        'Subspecies': race_bonus.get('Subspecies', ''),
        'Custom Race': race_bonus.get('Custom Race', '')
    }

def save_character_sheet(character_sheet):
    filename = f"{character_sheet['Name']}_character_sheet.txt"
    with open(filename, 'w') as file:
        file.write("Character Sheet:\n")
        file.write(f"Name: {character_sheet['Name']}\n")
        file.write(f"Class: {character_sheet['Class']}\n")
        file.write(f"Race: {character_sheet['Race']}\n")
        file.write(f"Subspecies: {character_sheet.get('Subspecies', 'None')}\n")
        file.write(f"Custom Race: {character_sheet.get('Custom Race', 'None')}\n")
        file.write("Stats:\n")
        for stat, value in character_sheet['Stats'].items():
            file.write(f"{stat.capitalize()}: {value}\n")
    print(f"Character sheet saved as {filename}")

def display_character_sheet(character_sheet):
    print("\nCharacter Sheet:")
    print("Name:", character_sheet['Name'])
    print("Class:", character_sheet['Class'])
    print("Race:", character_sheet['Race'])
    print("Subspecies:", character_sheet.get('Subspecies', 'None'))
    print("Custom Race:", character_sheet.get('Custom Race', 'None'))
    print("Stats:")
    for stat, value in character_sheet['Stats'].items():
        print(f"{stat.capitalize()}: {value}")

def main_menu():
    print("\nMenu:")
    print("1. Create Character Sheet")
    print("2. Display Character Sheet")
    print("3. Save Character Sheet")
    print("4. Quit")
    return input("Enter your choice: ")

def main():
    character_sheet = None
    while True:
        choice = main_menu()

        if choice == '1':
            name = input("Enter character name: ")
            character_class = input("Enter character class: ")
            race = input("Enter character race (Human, Elf, Halflings, Dwarf, Homebrew): ")
            if race.lower() == 'homebrew':
                print("Creating custom race...")
            character_sheet = create_character_sheet(name, character_class, race)
            display_character_sheet(character_sheet)
        elif choice == '2':
            if character_sheet is None:
                print("No character sheet created yet.")
            else:
                display_character_sheet(character_sheet)
        elif choice == '3':
            if character_sheet is None:
                print("No character sheet created yet.")
            else:
                save_character_sheet(character_sheet)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
