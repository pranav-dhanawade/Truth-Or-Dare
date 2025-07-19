import requests
import json
import random
def deletePlayer(list):
    playerName= input("Name The Person Who Wants To Leave\n--> ")
    changeName = playerName.upper()
    playerList.remove(changeName)
    print(f"\n{playerName} is removed\n")
    choiceNext()
def addPlayers(list):
    playerCount = int(input("Enter How Many Players Do You Want To Play?? --> "))
    for i in range(playerCount):
        playerName = input(f"Enter {i+1} Player Name --> ")
        playerNameUpper = playerName.upper()
        playerList.append(playerNameUpper)
    game(random.choice(playerList))
def choiceNext():
    choose = input("1. Want To Play Again\n2. Add More Players\n3. SomeOne Wants To Leave?\n4. Quit\n-->")
    playAgain(choose)
def playAgain(choice):
    
    match choice:
        case '1':
            game(random.choice(playerList))
        case '2':
            addPlayers(playerList)
        case '3':
            deletePlayer(playerList)
        case '4':
            print("Thanks For Playing")
        case _:
            print("\nEnter Number From Given Options Only\n")
            choiceNext()

    
def choose(challenge):
    match challenge:
        case 'Truth'  |  'truth':
            if requestTruth.status_code==200:
                data = json.loads(requestTruth.text)
                if 'question' in data:
                    print("\n",data['question'],"\n\n")
                    choiceNext()
        case 'Dare' | 'dare':
            if requestDare.status_code==200:
                data = json.loads(requestDare.text)
                if 'question' in data:
                    print("\n",data['question'],"\n\n")
                    choiceNext()
        case _:
            print("Please Enter Correct choice")
def game(name):
    print(f"\n\n--> Task is for {name}\n\n")  
    choice = input(f"What Do You Choose {name} ? \nTruth\nDare\n-->")
    choose(choice)
    


requestTruth = requests.get("https://api.truthordarebot.xyz/v1/truth")
requestDare = requests.get("https://api.truthordarebot.xyz/api/dare")
playerList = []
print("\n\nWelcome In Truth Or Dare\n\n")
addPlayers(playerList)

            




