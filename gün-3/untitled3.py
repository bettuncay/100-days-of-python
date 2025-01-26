# ASCII Art - Welcome Message
print(r"""
 __        __   _                            _        
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
""")
print(r"""
             88                                 88  
             88                                 88  
             88                                 88  
88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
""")

print("Welcome to the The Black Island!")
first = input("Do you want to take a boat or a car to get to the hotel?\n")
if first == "boat":
    print("The sea looks beautiful.")
    second = input("Go for a 'walk' or stay in a hotel?\n")
    if second == "walk":
        print("It wasn't a good idea to walk alone on an island with no one around. You fell into the sea. You died.")
    else:
        print("The hotel fascinates with its vintage design and sunlight.")
        third = input("Where is the host? 'will come' or 'not come'?")
        if third == "will come":
            print("He/She already here.Be carefully. Upps. You died.")
        else:
            print("Are you sure? Do you remember why you accepted the invitation?")  
            fourth = input("Would you like 'wine' or 'water'?")
            if fourth == "wine":
                print("It might be nice to enjoy a glass of wine, if only your dead body were not reflected in it. You died.")
            else:
                print("Drinking water is important for our health. It can even cost our lives.")
                fifth = input("You look tired, don't you want a painkiller?,'yes' or 'no'")
                if fifth == "yes":
                    print("You know, when we die, our pain goes away. you died")
                else:
                    print("Sometimes we have to fight our own pain. I appreciated that.")
                    sixth = input("Which room do you want 11,13,49?")
                    if sixth == "11":
                        print("While you were sitting on the terrace, someone pushed you from behind. You died.")
                    elif sixth == "49":
                        print("You were found hanging in a hotel room. With seaweed. Do you have a problem with the sea?")
                    else:
                        print("Oh my god, you're the only one who survived.\n Congratulations.\n But we have a little problem.\n You couldn't stand what happened and killed yourself, because you were the murderer.")  
else:
    print("You were speeding too much. You died.")
