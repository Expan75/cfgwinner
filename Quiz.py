#Recording player name:
print("ARE YOU A SEAGULL? The official quiz")
print("----------------")
print("if you identify with some of these situations, Science says you could be a seagull!!!!!")
print("Enter player name: ")
player_name = input()



#Question lists
print("Please answer the questions with A, B or C")

Questionset_1 =  ["Do you look at food waste and think of what a good meal that would be?\n(a) Yes, Trash is such a waste of good food\n(b) Ew no, wtf mate\n(c) I mean, maybe, depends on how it looks",
"Are you very territorial?\n(a) Come into my room, I stab you\n(b) I let close friends use my things and come into my room\n(c) Communism is great"]
Questionset_2 = ["Do you expect to live more than 15 years?\n(a) Yes\n(b) No\n(c) Questionable", "Do you have a strong body and weirdly elongated legs?\n(a) Nah, I think I have good proportions\n(b) Well, yeah I guess\n(c) I don't but I think it looks pretty good\n(d) Uhhh"]
Questionset_3 = ["Could you easily chug a glass of seawater for a bet?\n(a) for a Tenner? Sure\n(b) I could but I don't want to, so no\n(c) I would drink it for free\n(d) Just no"]

print(Questionset_1[1])
answer = input()

print(Questionset_2[0])
answer = input()

print(Questionset_1[0])
answer = input()

print(Questionset_3[0])
answer = input()

print(Questionset_2[1])
answer = input()



Counter = 0
for Question in Questionset_1:
    if answer == "a":
        Counter = Counter + 1

for Question in Questionset_2:
    if answer == "b":
        Counter = Counter + 1

for Question in Questionset_3:
    if answer == "c":
        Counter = Counter + 1

if Counter >= 3:
    print ("CONGRATULATIONS YOU ARE A SEAGULL!!!")
else:
    print ("oops, sorry you CANNOT be a seagull :( maybe start looking for a dayjob")
