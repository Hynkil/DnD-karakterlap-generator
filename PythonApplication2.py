import random

character_sheet = {}

def generate_stats():
    stats = {
        'Strength': random.randint(3, 18),
        'Dexterity': random.randint(3, 18),
        'Constitution': random.randint(3, 18),
        'Intelligence': random.randint(3, 18),
        'Wisdom': random.randint(3, 18),
        'Charisma': random.randint(3, 18)
    }
    return stats

def apply_race_bonus(race):
    race_bonuses = {
        'Human': {
            'Calishite': {'Charisma': 1},
            'Damarai': {'Strength': 1},
            'Forest': {'Dexterity': 1},
            'Mountains': {'Constitution': 1}
        },
        'Elf': {
            'High Elf': {'Intelligence': 1},
            'Wood Elf': {'Wisdom': 1},
            'Dark Elf': {'Dexterity': 1}
        },
        'Halflings': {
            'Lightfoot': {'Charisma': 1},
            'Stout': {'Constitution': 1}
        },
        'Dwarf': {
            'Mountain Dwarf': {'Strength': 1},
            'Hill Dwarf': {'Wisdom': 1}
        }
    }

    if race == 'Homebrew':
        custom_race_name = input("Enter your custom race name: ")
        custom_bonuses = {}
        while True:
            stat = input("Enter a stat (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) (or type 'done' when finished): ").capitalize()
            if stat == 'Done':
                break
            value = int(input(f"Enter bonus value for {stat}: "))
            custom_bonuses[stat] = value
        return {'Custom Race': custom_race_name, **custom_bonuses}

    if race in race_bonuses:
        bonus = race_bonuses[race]
        subspecies = input("Do you want to choose a subspecies (yes/no)? ").lower()
        if subspecies == 'yes':
            chosen_subspecies = input(f"Choose a subspecies: {', '.join(bonus.keys())}: ")
            if chosen_subspecies in bonus:
                return {'Subspecies': chosen_subspecies, **bonus[chosen_subspecies]}
            else:
                print("Invalid subspecies choice. Defaulting to base race bonuses")
        return {'Subspecies': ''}
    return {}

def create_character_sheet(name, character_class, race):
    stats = generate_stats()
    race_bonus = apply_race_bonus(race)
    
    for key, value in race_bonus.items():
        if key != 'Subspecies' and key != 'Custom Race':
            stats[key] += value
    
    character_sheet['Name'] = name
    character_sheet['Class'] = character_class
    character_sheet['Race'] = race
    character_sheet['Stats'] = stats
    character_sheet['Subspecies'] = race_bonus.get('Subspecies', '')
    character_sheet['Custom Race'] = race_bonus.get('Custom Race', '')

def display_character_sheet():
    print("\nCharacter Sheet:")
    print("Name:", character_sheet['Name'])
    print("Class:", character_sheet['Class'])
    print("Race:", character_sheet['Race'])
    print("Subspecies:", character_sheet.get('Subspecies', 'None'))
    print("Custom Race:", character_sheet.get('Custom Race', 'None'))
    print("Stats:")
    for stat, value in character_sheet['Stats'].items():
        print(stat + ':', value)

def main_menu():
    print("\nMenu:")
    print("1. Create Character Sheet")
    print("2. Display Character Sheet")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            name = input("Enter character name: ")
            character_class = input("Enter character class: ")
            race = input("Enter character race (Human, Elf, Halflings, Dwarf, Homebrew.): ")
            create_character_sheet(name, character_class, race)
        elif choice == '2':
            display_character_sheet()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
