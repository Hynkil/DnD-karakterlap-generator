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

def create_character_sheet(name, character_class):
    stats = generate_stats()
    
    character_sheet['Name'] = name
    character_sheet['Class'] = character_class
    character_sheet['Stats'] = stats

def display_character_sheet():
    print("\nCharacter Sheet:")
    print("Name:", character_sheet['Name'])
    print("Class:", character_sheet['Class'])
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
            create_character_sheet(name, character_class)
        elif choice == '2':
            display_character_sheet()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()