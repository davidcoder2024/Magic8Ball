import random

name = "Mr. Dapper"
Question = "Question:"
question = "Will I have luck when I wake up tomorrow?"
answer = ""

random_number = random.randint(1,15)
#print(random_number)

if random_number == 1: 
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "The time to know has not arrived yet"
elif random_number == 11:
  answer = "The answer will shock you, but you'll have to wait for it :D"
elif random_number == 12:
  answer = "Shockingly, YES!!"
elif random_number == 13:
  answer = "Search your feelings and maybe you will kn...no, actually you won't know until later hehe"
elif random_number == 14:
  answer = "Yes, yes yes yes YES!!!"
elif random_number == 15:
  answer = "No, now quit asking...Jk...ask away!"
else:
  answer = "Error"

if name == "":
  print(Question, question)
else:
  print(name, "asks:",  question)

if question == "":
  print("You forgot to ask a question, duhhh!")
else:
  
  print("\n")
  print("Magic 8-Ball's answer:", answer)


