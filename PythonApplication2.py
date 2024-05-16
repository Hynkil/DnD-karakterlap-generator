import random

character_sheet = {}

def generate_stats():
    stats = {
        'Strength': random.randint(3, 18),
        'Dexterity': random.randint(3, 18),
        #ügyesség
        'Constitution': random.randint(3, 18),
        #állóképesség
        'Intelligence': random.randint(3, 18),
        'Wisdom': random.randint(3, 18),
        #bölcsesség
        'Charisma': random.randint(3, 18)
    }
    return stats

def apply_race_bonus(race):
    if race == 'Human':
        bonus = {stat: 1 for stat in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']}
        if input("Do you want to choose a subspecies (yes/no)? ") == 'yes':
            subspecies = input("Choose a subspecies: (Calishite, Damarai, Forest, or Mountains) ")
            if subspecies == 'Calishite':
                bonus['Charisma'] += 1
                bonus['Subspecies'] = subspecies
            elif subspecies == 'Damarai':
                bonus['Strength'] += 1
                bonus['Subspecies'] = subspecies
            elif subspecies == 'Forest':
                bonus['Dexterity'] += 1
                bonus['Subspecies'] = subspecies
            elif subspecies == 'Mountains':
                bonus['Constitution'] += 1
                bonus['Subspecies'] = subspecies
            else:
                print("Invalid subspecies choice. Defaulting to base Human bonuses.")
        return bonus
    elif race == 'Elf':
        bonus = {stat: 2 for stat in ['Dexterity']}
        if input("Do you want to choose a subspecies (yes/no)? ") == 'yes':
            subspecies = input("Choose a subspecies: (High Elf or Wood Elf) ")
            if subspecies == 'High Elf':
                bonus['Intelligence'] += 1
                bonus['Subspecies'] = subspecies
            elif subspecies == 'Wood Elf':
                bonus['Intelligence'] += 1
                bonus['Subspecies'] = subspecies
            else:
                print("Invalid subspecies choice. Defaulting to base Human bonuses.")
        return bonus
    elif race == 'Halflings':
        bonus = {stat: 2 for stat in ['Dexterity']}
        if input("Do you want to choose a subspecies (yes/no)? ") == 'yes':
            subspecies = input("Choose a subspecies: (Lightfoot or Stout) ")
            if subspecies == 'Lightfoot':
                bonus['Charisma'] += 1
                bonus['Subspecies'] = subspecies
            elif subspecies == 'Stout':
                bonus['Constitution'] += 1
                bonus['Subspecies'] = subspecies
            else:
                print("Invalid subspecies choice. Defaulting to base Human bonuses.")
        return bonus
    elif race == 'Dwarf':
        bonus = {stat: 2 for stat in ['Constitution']}
        if input("Do you want to choose a subspecies (yes/no)? ") == 'yes':
            subspecies = input("Choose a subspecies: (Mountain Dwarf or Hill Dwarf) ")
            if subspecies == 'Mountain Dwarf':
                bonus['Strength'] += 2
                bonus['Subspecies'] = subspecies
            elif subspecies == 'Hill Dwarf':
                bonus['Wisdom'] += 1
                bonus['Subspecies'] = subspecies
            else:
                print("Invalid subspecies choice. Defaulting to base Human bonuses.")
        return bonus
    else:
        return{}

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
            race = input("Enter character race (Elf, Human, Halflings, Dwarf): ")
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
