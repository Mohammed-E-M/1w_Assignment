import keyboard
from time import sleep
from playsound import playsound  # Ensure you have playsound installed: pip install playsound

got_key = False  # Global variable to track key possession

def play_blocked_sound():
    try:
        playsound('blocked.wav')
    except:
        print("⚠️ Could not play sound. Check your sound file path and format.")

def play_crackle_sound():
    try:
        playsound('crackle.wav')
    except:
        print("⚠️ Could not play sound. Check your sound file path and format.")

def intro():
    print("""
    You are a treasure hunter on the search for the most valuable treasure known to man!
    Search the house for a key to unlock the chest of gold and jewels!
    But beware there are dangers lurking about...

    Press 'q' at any time to leave the game, Coward!
    """)
    input("Press any key to start your treasure hunt.")
    cellar()

def cellar():
    print("""
    Your search has led you to the fabled Fortnum Mansion.
    You are in the cellar. It's cold and damp and there is a strong earthy smell.
    It is so dark you can barely see your own hand, but you can make out some shapes
    from the moonlight shining through the broken window (your entry point).
    """)
    while True:
        print("Press ← (l), → (r), ↑ (f), ↓ (b), or 'q' to quit.")
        sleep(0.1)
        if keyboard.is_pressed('left') or keyboard.is_pressed('l') or keyboard.is_pressed('right') or keyboard.is_pressed('r') or keyboard.is_pressed('down') or keyboard.is_pressed('b'):
            print("That path is blocked.")
            play_blocked_sound()
            break
        elif keyboard.is_pressed('up') or keyboard.is_pressed('f'):
            print("you have entered the kitchen")
            kitchen()
            break
        elif keyboard.is_pressed('q'):
            quit_game()
            break

def kitchen():
    print("""
    The kitchen smells of rot. Maggots squirm across the floor.
    A trap nearly caught your foot, and the floor feels dangerously weak.
    You see a sink, a fireplace, and a cupboard.
    """)
    
    while True:
        user_choice = input("Explore or move: (s)ink, fire(p)lace, (c)upboard, (l)eft, (r)ight, (b)ack, (f)orward: ").lower()

        if user_choice == 'q':
            quit_game()
            break
        elif user_choice in ['s', 'sink']:
            print("The sink is full of dirty dishes.")
        elif user_choice in ['p', 'fireplace']:
            print("A rusty skeleton key hangs above the fireplace — purely ornamental.")
        elif user_choice in ['c', 'cupboard']:
            print("The cupboard contains delicate china.")
        elif user_choice in ['l', 'left']:
            print("You enter the library.")
            library()
            break
        elif user_choice in ['r', 'right']:
            print("This way is blocked.")
            play_blocked_sound()
        elif user_choice in ['b', 'backward']:
            print("You return to the cellar.")
            cellar()
            break
        elif user_choice in ['f', 'forward']:
            print("You enter the dining room.")
            dining()
            break
        else:
            print("Invalid input.")

def library():
    global got_key
    print("""
    You are in the dusty library. A clean diary catches your attention—
    it's the mansion owner's, and he was a treasure hunter like you!
    There’s a desk, a chair, and a vase.
    """)

    while True:
        user_choice = input("Explore or move: (d)esk, (c)hair, (v)ase, (r)ight, (f)orward: ").lower()

        if user_choice == 'q':
            quit_game()
            break
        elif user_choice in ['d', 'desk']:
            print("Inside the desk, you find a key. You take it.")
            got_key = True
        elif user_choice in ['c', 'chair']:
            print("The chair is surprisingly comfy.")
        elif user_choice in ['v', 'vase']:
            print("Fresh flowers. Someone’s been here recently...")
        elif user_choice in ['r', 'right']:
            print("You return to the kitchen.")
            kitchen()
            break
        elif user_choice in ['f', 'forward']:
            print("You enter the study.")
            study()
            break
        else:
            print("Invalid input.")

def dining():
    print("You are in the dining room. A fireplace glows faintly. A portrait hangs nearby.")
    while True:
        print("Press ← (l), → (r), ↑ (f), ↓ (b), or 'q' to quit.")
        sleep(0.1)
        if keyboard.is_pressed('left') or keyboard.is_pressed('l'):
            print("That path is blocked.")
            play_blocked_sound()
            break
        elif keyboard.is_pressed('right') or keyboard.is_pressed('r'):
            print("The fire is dwindling. Press 't' to throw wood into the fire.")
            sleep(1)
            if keyboard.is_pressed("t"):
                play_crackle_sound()
                print("The fire roars back to life.")
            break
        elif keyboard.is_pressed('down') or keyboard.is_pressed('b'):
            print("That way is blocked.")
            play_blocked_sound()
            break
        elif keyboard.is_pressed('up') or keyboard.is_pressed('f'):
            print("You go back to the study.")
            study()
            break
        elif keyboard.is_pressed('q'):
            quit_game()
            break

def study():
    print("""
    Cujo, the giant St Bernard, blocks your way!
    He growls deeply. A harp, a chain, and a club are nearby.
    """)

    while True:
        user_choice = input("Act: (cl)ub, (ch)ain, (h)arp, or (b)ack: ").lower()

        if user_choice == 'q':
            quit_game()
            break
        elif user_choice in ['cl', 'club', 'ch', 'chain']:
            print("Cujo attacks you brutally...")
            sleep(3)
            game_over()
            break
        elif user_choice in ['h', 'harp']:
            print("The harp's tune soothes Cujo. He falls asleep.")
            input("Press Enter to tiptoe around him...")
            bedroom()
            break
        elif user_choice in ['b', 'back']:
            print("You return to the library.")
            library()
            break
        else:
            print("Invalid input.")

def bedroom():
    global got_key
    print("You enter the bedroom. A large chest sits by the bed.")
    sleep(2)
    if got_key:
        win_game()
    else:
        print("It's locked and you don’t have the key.")
        sleep(2)
        print("Suddenly, Cujo appears. The last thing you see are his teeth...")
        game_over()

def win_game():
    print("You use the key to open the chest...")
    sleep(2)
    for _ in range(5):
        print(".", end=' ')
        sleep(1)
    print("\nYou've found the treasure! You Win!")

def game_over():
    print("""
    Cujo drags your lifeless body away.
    Game Over, brave (but dead) adventurer.
    """)

def quit_game():
    print("You flee the mansion. Maybe next time you'll be braver.")
    exit()

# Game loop
while True:
    intro()
    play_again = input("Play again? (p) or press any other key to exit: ").lower()
    if play_again not in ['p', 'play']:
        print("Thanks for playing!")
        break
