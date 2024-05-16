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
        return {stat: 1 for stat in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']}
    elif race == 'Elf':
         return {'Dexterity': 2}
     elif race == 'High Elf':
         return {'Intelligence': 1}
     elif race == 'Wood Elf':
         return {'Intelligence': 1}
     elif race == 'Halflings':
         return {'Dexterity': 2}
     elif race == 'Lightfoot':
         return {'Charisma': 1}
     elif race == 'Stout':
         return {'Constitution': 1}
     elif race == 'Dwarf':
         return {'Constitution': 2}
     elif race == 'Mountain Dwarf':
         return {'Strength': 2}
     elif race == 'Hill Dwarf':
         return {'Wisdom': 1}
     else:
         return{}

def create_character_sheet(name, character_class, race):
    stats = generate_stats()
    race_bonus = apply_race_bonus(race)
    
    for key, value in race_bonus.items():
        stats[key] += value
    
    character_sheet['Name'] = name
    character_sheet['Class'] = character_class
    character_sheet['Race'] = race
    character_sheet['Stats'] = stats

def display_character_sheet():
    print("\nCharacter Sheet:")
    print("Name:", character_sheet['Name'])
    print("Class:", character_sheet['Class'])
    print("Race:", character_sheet['Race'])
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
            race = input("Enter character race (Elf, Night Elf, Wood Elf, Halflings, Lightfoot, Scout, Dwarf, Mountain Dwarf, Hill Dwarf, Human): ")
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
