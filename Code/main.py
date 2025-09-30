def yes_or_no(question):
    while True:
        choice = input( question + "\n").strip().lower()
        if choice in ['yes']:
            return True
        elif choice in ['no']:
            return False
        else:
            print("Invalid input. Pleas type yes or no")
            

def gues_character():
    input("one piece akinitor \n Press Enter to continue...")
    if yes_or_no("Is this character a female? "):
        print("You selected a female character.")
    else:
        if yes_or_no("Is this character a straw hat pirate?"):
           if yes_or_no("Is this character the captain?"):
               print("Is your character Luffy")
           else:
               if yes_or_no("Is this character a swordsman?"):
                 if yes_or_no("Is this character a Skeleton musician?"):
                     print("Is your character Brook")
                 else:
                     print("Is your character Zoro")
                     
gues_character()
                    
                   
                
               
              
