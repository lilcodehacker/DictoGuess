#!/usr/bin/env python3
from wonderwords import RandomWord
from dictionary.britannica import *
r = RandomWord()
pstat = []
pscore = []
points = 0
exit_conditions = (":q", "quit", "exit", "i'm done", "i quit")
players = input("How Many Players? ")
players = int(players)
for i in range(players):
        pstat.append(True)
        pscore.append(0)
while True in pstat:
  for h in range(players):
    if not pstat[h]:
        break
    print (f"Player {h+1}'s turn")
    word = r.word()
    list = get_definitions(word)
    string = str(list)
    string = string.replace(word, "")
    print(f"{string}")
    for i in range(5):
        query = input("What is the Word?📚 ")
        if query in exit_conditions:
            print ("You quitter👎 the Word was: " + word + "!!")
            if points > 10:
                print (f"Your score was {pscore[h]}!!👍")
            else:
                print (f"Your score was {pscore[h]}👎")
            for i in range(players):
                print (f"Player {i}'s Score was: {pscore[i]}")
            quit()
        if query == "hint" or query == "?":
            hint = get_entries(word)
            print(hint)
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
     print (f"Player {i}'s Score was: {pscore[i]}")
quit()