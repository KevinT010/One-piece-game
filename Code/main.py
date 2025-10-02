from characters_and_traits import characters, traits
 
def yes_or_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer yes or no.")
 
def choose_best_trait( possible_characters, asked_traits):
    best_trait = None
    best_difference = float('inf')
    for trait in traits:
        if trait in asked_traits:
            continue
 
        total_characters_with_trait = sum(1 for char in  possible_characters if characters[char].get(trait, False))
        total_characters_without_trait = len( possible_characters) - total_characters_with_trait
       
        difference = abs(total_characters_with_trait - total_characters_without_trait)
        if 0 < total_characters_with_trait < len( possible_characters) and difference < best_difference:
            best_difference = difference
            best_trait = trait
           
    return best_trait
 
def guess_character():
    print("\nWelcome to One Piece mini games!")
    input("Think of a character, and I will try to guess it. Press Enter to continue...\n")
 
    possible_characters = set(characters.keys())
    asked_traits = set()
 
 
    while len(possible_characters) > 1:
        trait = choose_best_trait(possible_characters, asked_traits)
        if not trait:
            break
        readable_trait = trait.replace("_", " ")
        if trait == "alabasta":
            readable_trait = "from Alabasta"
        answer = yes_or_no(f"Is this character a {readable_trait}?")
        asked_traits.add(trait)
        if answer:
            possible_characters = {char for char in possible_characters if characters[char].get(trait, False)}
        else:
            possible_characters = {char for char in possible_characters if not characters[char].get(trait, False)}
 
    if len(possible_characters) == 1:
        is_character = yes_or_no(f"\nIs your character {list(possible_characters)[0]}?")
        count_asked_traits = len(asked_traits)

        if is_character:
            print(f"\nYour character is: {list(possible_characters)[0]}")
            print(f"I guessed your character in {count_asked_traits} questions!")
        else:
            print("\nThe character is not in the list.")
 
 
while True:
    guess_character()
    if not yes_or_no("\n Do you want to play again?"):
        print("\n Thank you for playing!")
        break