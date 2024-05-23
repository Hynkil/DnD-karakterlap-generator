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
        }
    }

    if race in race_bonuses:
        bonus = race_bonuses[race]
        subspecies = input("Do you want to choose a subspecies (yes/no)? ").lower()
        if subspecies == 'yes':
            chosen_subspecies = input(f"Choose a subspecies: {', '.join(bonus.keys())} ")
            if chosen_subspecies in bonus:
                return bonus[chosen_subspecies]
            else:
                print("Invalid subspecies choice. Defaulting to base Elf bonuses.")
        return {'Subspecies': ''}
    return {}

def create_character_sheet(name, character_class, race):
    stats = generate_stats()
    race_bonus = apply_race_bonus(race)
    
    for key, value in race_bonus.items():
        if key != 'Subspecies':
            stats[key] += value
    
    character_sheet['Name'] = name
    character_sheet['Class'] = character_class
    character_sheet['Race'] = race
    character_sheet['Stats'] = stats
    character_sheet['Subspecies'] = race_bonus.get('Subspecies', '')

def display_character_sheet():
    print("\nCharacter Sheet:")
    print("Name:", character_sheet['Name'])
    print("Class:", character_sheet['Class'])
    print("Race:", character_sheet['Race'])
    print("Subspecies:", character_sheet.get('Subspecies', 'None'))
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
            race = input("Enter character race (Human, Elf, etc.): ")
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
