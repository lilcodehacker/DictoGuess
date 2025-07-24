import json
import requests
pstat = []
pscore = []
points = 0
phint = []
welcome = '''Welcome to DictoGuess, the fun word guessing game.
Object: Go as far as you can without getting out, OR be the last one standing.
Gameplay: Player(s) take turns guessing a word with only the definition as a clue.
Rules: 
    ·Each Player gets 5 hints.
    ·Each Player gets 5 strikes before becoming out.

This program is under the GNU GPL 3.0+ license.
If you have any problems or questions, please contact me via GitHub @lilcodehacker
'''
exit_conditions = (":q", "quit", "exit", "i'm done", "i quit")
print(welcome)
players = input("How Many Players? ")
players = int(players)
for i in range(players):
        pstat.append(True)
        pscore.append(0)
        phint.append(5)
while True in pstat:
  for h in range(players):
    if not pstat[h]:
        break
    print (f"Player {h+1}'s turn")   
    def setword():
     global word     
     word = requests.get("https://random-word-api.herokuapp.com/word")
     word = word.text
     word = str(word)
     word = word.replace("[", "")
     word = word.replace("}", "")
     word = word.replace(":", "")
     word = word.replace("word", "")
     word = word.replace("{", "")
     word = word.replace("]", "")
     word = word.replace("\"", "")
     api_url = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
     list = requests.get(api_url, headers={'X-Api-Key': 'aixp2s2d4P8jS0pCmemNJQ==GrNeuNie5ClyabJ9'})
     list = list.text
     string = str(list)
     string = string.replace(word, "_____")
     string = string.replace("[", "")
     string = string.replace("]", "")
     string = string.replace("\"", "")
     string = string.replace("{", "")
     string = string.replace("}", "")
     string = string.replace("valid: false", "")
     if ": false" in string:
         setword()
     else:
         print(f"{string}")
    setword()
    for i in range(5):
        query = input("What is the Word?📚 ")
        if query in exit_conditions:
            print ("You quitter👎 the Word was: " + word + "!!")
            if points > 10:
                print (f"Your score was {pscore[h]}!!👍")
            else:
                print (f"Your score was {pscore[h]}👎")
            pstat[h] = False
        if query == "hint" or query == "?":
          if phint[h] > 0:
            hint = word[:3]
            print(hint)
            print(f"{phint[h]} Hints left")
          else:
            print("No more hints left☹️")
        else:
            if query == word:
                print (f"You Did it👍 the Word was: {word}!!")
                break
            else:
                if i == 4:
                    print (f"You LOSE!!!!👎 the word was {word}!!!")
                    if points > 10:
                        print (f"Your score was {pscore[h]}!!👍")
                    else:
                        print (f"Your score was {pscore[h]}👎")
                    pstat[h] = False
                else:
                    print (f"WRONG!!!!👎")
    pscore[h] = pscore[h]+1
for i in range(players):
     print (f"Player {i+1}'s Score was: {pscore[i]}")
quit()
