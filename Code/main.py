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
    input(" Welcome to one piece akinitor you can choose between those characters: Franky, Brook, Luffy, Zoro, Sanji, Chopper, Jinbei, Shanks, King cobra, Blackbeard, \n Nami, Robin, Al vida, Vivi, Shiraoshi, Rebecca, Reiju, Big mom, Shaky, Boa hancock \n Press Enter to continue...")
    if yes_or_no("Is this character a female? "):
        print("You selected a female character.")
    else:
        if yes_or_no("Is this character a straw hat pirate?"):
           if yes_or_no("Is this character the captain?"):
             if yes_or_no("Is your character Luffy?"):
                print("Your character is Luffy")
             else:
                 print("The character is not in the list")
           else:
            if yes_or_no("Is this character a swordsman?"):
                 if yes_or_no("Is this character a Skeleton musician?"):
                     if yes_or_no("Is your character Brook?"):
                        print("Your character is Brook")
                     else: 
                         print("The character is not in the list")   
                 else:
                     if yes_or_no("Is your character Zoro?"):
                        print("Your character is Zoro")
                     else:
                        print("The character is not in the list")
                     
            else:
               if yes_or_no("Is this character a cook?"):
                  if yes_or_no("Is your character Sanji?"):
                     print("Your character is Sanji")
                  else:
                      print("The character is not in the list") 
               else:      
                if yes_or_no("Is this character a reindeer/doctor?"):
                  if yes_or_no("Is your character Chopper?"):
                     print("Your character is Chopper")
                  else:
                     print("The character is not in the list")
                else:
                 if yes_or_no("Is this character a Fishman?"):
                  if yes_or_no("Is your character Jinbe?"):
                     print("Your character is Jinbe")
                  else:
                     print("The character is not in the list")
                 else:
                  if yes_or_no("Is your character Franky?"):
                     print("Your character is Franky")
                  else:
                     print("The character is not in the list")
        else: 
            if yes_or_no("Is this character a yonko?"):
                if yes_or_no("Does this character have red-hair?"):
                    if yes_or_no("Is your character Shanks?"):
                        print("Your character is Shanks")
                    else:
                        print("The character is not in the list")
                else: 
                    if yes_or_no("Is your character Blackbeard?"):
                        print("Your character is Blackbeard")
                    else:
                        print("The character is not in the list")
            else:
             if yes_or_no("Is this character a King of a kingdom?"):
                if yes_or_no("Is your character King cobra?"):
                    print("Your character is King cobra")
                else:
                    print("The character is not in the list")
                    
gues_character()
                    
                   
                
               
              
