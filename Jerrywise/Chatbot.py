import datetime
import random

# chat_bot to answer a series of questions
# chatbot name: bolu
#
# question 1: what is the time? current time
# question 2: how old are you? between 1 to 100
# question 3: have you eaten? yes or no
# question 4: do you love me?
# question 5: why am i still single?
# question 6: what is your daddy name?
# question 7: what is your mummy name?
# question 8: when last do you have sex?
# question 9: what is my hobby?
# question 10: what is your plan for life?


print("this is bolu, what is your question please ask")
love = ["yes, i love you", "No, i dont love you", "what is love", "love is wicked"]
age = [num for num in range(1, 50)]
eat = ["No, i haven't", "yeah, i have had breakfast", "yeah, i had eba and egusi", "no, i am fasting."]
ralationships = ["wow, even the gods do not know.", "yes, i am single", "yes, i am in a relationship",
                 "it is complicated"]
daddy_name = ["tife", "toye", "isreal", "dimeji"]
mummy_name = ["mojoyin", "precious", "yetunde", "damilola"]
sex = [sex for sex in range(1, 10)]
hobby = ["playing", "singing", "dancing", "jumping", "reading"]
plan_for_life = ["doctor", "nurse", "prophet", "pastor","software engineers"]

while True:
    question = input().split("-")
    if "time" in question:
        print("the time of day is:", datetime.datetime.now().time())
    elif "name" in question:
        print("my name is bolu, how can i help you")
    elif "old" in question or "age" in question:
        print(random.choice(age))
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "love" in question:
        print(random.choice(love))
    elif "single" in question or "relationship" in question:
        print(random.choice(ralationships))
    elif "daddy" in question or "dad" in question:
        print(random.choice(daddy_name))
    elif "mummy" in question or "mum" in question:
        print(random.choice(mummy_name))
    elif "sex" in question or "knack" in question:
        print(random.choice(sex))
    elif "hobby" in question:
        print(random.choice(hobby))
    elif "career" in question or "future_goal" in question:
        print(random.choice(plan_for_life))
    elif "break" in question:
        print("seems you want to break up, boy bye!!")
        break
    else:
        print("i dont understand you. do you mean 'what is the time of the day?'")



