def yes_or_no(question):
    while True:
        choice = input( question + "\n").strip().lower()
        if choice in ['yes']:
            return True
        elif choice in ['no']:
            return False
        else:
            print("Invalid input. Pleas type yes or no")
            

def guess_character():
    input(" Welcome to one piece akinitor you can choose between those characters: Franky, Brook, Luffy, Zoro, Sanji, Chopper, Jinbei, Shanks, King cobra, Blackbeard, \n Nami, Robin, Al vida, Vivi, Shiraoshi, Rebecca, Reiju, Big mom, Shaky, Boa hancock \n Press Enter to continue...")
    if yes_or_no("Is this character a female? "):
        if yes_or_no("Is this character a straw hat pirate?"):
            if yes_or_no("Is this character a navigator?"):
                if yes_or_no("Is your character Nami?"):
                    print("Your character is Nami")
                else:
                    print("The character is not in the list")
            else:
                  if yes_or_no("Is your character Robin?"):
                     print("Your character is Robin")
                  else:
                      print("The character is not in the list")
        else:
            if yes_or_no("Is this character currently a pirate?"):
                if yes_or_no("is/was this character a yonko?"):
                    if yes_or_no("Is your character Big mom?"):
                        print("Your character is Big mom")
                    else:
                        print("The character is not in the list")
                else:
                    if yes_or_no("Is she a empress?"):
                        if yes_or_no("Is your character Boa hancock?"):
                            print("Your character is Boa hancock")
                        else:
                            print("The character is not in the list")
                    else:
                        if yes_or_no("is your character Alivda?"):
                          print("Your character is Alvida")
                        else:
                          print("The character is not in the list")
            else:
                if yes_or_no("Is this character a princess?"):
                    if yes_or_no("has your character pink hair?"):
                        if yes_or_no("Is your character Vivi?"):
                            if yes_or_no("is your character a fishman?"):
                                if yes_or_no("Is your character Shirahoshi?"):
                                    print("Your character is Shirahoshi")
                                else:
                                    print("The character is not in the list")
                            else:
                                if yes_or_no("Is your character Reiju?"):
                                    print("Your character is Reiju")
                                else:
                                    print("The character is not in the list")             
                else:
                    if yes_or_no("Is she a gladiator?"):
                        if yes_or_no("Is your character Rebecca?"):
                            print("Your character is Rebecca")
                        else:
                            print("The character is not in the list")
                    else:
                        if yes_or_no("Is your character Shakky?"):
                            print("Your character is Shakky")
                        else:
                            print("The character is not in the list")
                  
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
    
                    
while True:
    guess_character()
    if not yes_or_no("Do you want to play again? (yes/no)"):
        print("Thank you for playing!")
        break
                    
                   
                
               
              
