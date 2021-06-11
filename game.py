def rps():
    print('Hello! I am marrie')
    print("Welcome! Felling exiting to play rock paper scissor with you")

    name = input("Would you like to tell you name: ")

    print("Hello " +name)
    print("Let's start playing")

    while True:
        import random

        print("ITS COMPUTER'S TURN TO CHOOSE")

        rand = random.randint(1,4)
        if rand == 1:
            comp = "rock"
        elif rand == 2:
            comp = "paper"
        elif rand == 3:
            comp = "scissor"

        print("YOUR COMPUTER HAS DECIDED HIS CHOICE.")

        you = input('''Now its your turn {}:
        1. Rock
        2. Paper
        3. Scissor
        To exit press exit
        Enter your choice: '''.format(name))
        
        you_lower = you.lower()

        if ("rock" in you_lower) or ("patthar" in you_lower) or ("rack" in you_lower) or ("rok" in you_lower) or ("roc" in you_lower) or ("r" in you_lower) or ("ro" in you_lower) or ("1" in you_lower):
            your = "rock"
        elif ("paper" in you_lower) or ("kagaj" in you_lower) or ("panna" in you_lower) or ("kaagaz" in you_lower) or ("kaagaj" in you_lower) or ("p" in you_lower) or ("pa" in you_lower) or ("papr" in you_lower) or ("peper" in you_lower) or ("2" in you_lower):
            your = "paper"
        elif ("scissor" in you_lower) or ("scisor" in you_lower) or ("sisor" in you_lower) or ("seasor" in you_lower) or ("scissors" in you_lower) or ("sezor" in you_lower) or ("3" in you_lower):
            your = "scissor"
        elif ("exit" in you_lower) or ("bye" in you_lower) or ("good" in you_lower) or ("byee" in you_lower) or ("ok" in you_lower):
            your = "exit"
        else:
            print("{} you have entered a wrong choice try one again")

        if your == "exit":
            break
        
        print("Your choice is {}".format(your))
        print("Let us check who wins")

        if comp == your:
                  print("Oh no its tie you both cooses {}".format(your))
        elif your == "rock":
            if comp == "paper":
                print("Oh No! You Loose {}".format(name))
            elif comp == "scissor":
                print("Hurry! You Win {}".format(name))
        elif your == "paper":
            if comp == "scissor":
                print("Oh No! You Loose {}".format(name))
            elif comp == "rock":
                print("Hurry! You Win {}".format(name))
        elif your == "scissor":
            if comp == "rock":
                print("Oh No! You Loose {}".format(name))
            elif comp == "paper":
                print("Hurry! You Win {}".format(name))
   
        print("Your Computer chooses {}".format(comp))
        print("**************************************************\n" * 3)
