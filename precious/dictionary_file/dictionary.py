# chatbot to answer series of questions
# chat_bot name : precious
# answer : date and time of day
# question_1: what is the time of the day?
# question_2: how old are you?
# question_3: how old are you?
# question_4: do you love me? yes or no
# question_5: why am i still single?
import datetime
import random


array_list = {

        "time": ["The time of day is: ", datetime.datetime.now().time()],
        "love": ["Yes, i love you", "No, I dont love you", "What is love?", "love is wicked"],
        "name": ["precious", "amarachi", "lois", "delight", "daniel", "jahson", "jahzeal", "jada"],
        "age old": [number for number in range(1, 100)],
        "relationship": ["i am single", "i am not single", "i am married", "i am not married", "i am engaged",
                         "i am not engaged", "its complicated", "i am confused"],
        "eaten": [" no i have not eaten", "i'm actually starving", "Yes i have eaten"],
        "eat": ["i ate eba and egusi soup", "i ate rice and stew", "i drank garri", "jollof rice"],
        "happy": ["Yes i am happy been your best_friend", "No i am not happy because you are too busy to play with me"],
        "friends": ["Yes we can be best buddies", " Yes i would love that too",
                    "No please i'm too busy to have a friend"],
        "gender": ["female", "male", "transgender"],
        "hate": ["i dont love you because you ugly", "i dont love you because i love " + random.choice("name"),
                    "i dont love because you're not my best friend"],
        "meet": ["the pleasure is all mine", "i dont know you but i hate you already"],
        "why": ["men are scam", "i found love once and then i lost him to other bitch"],
        "country": ["uk", "Nigeria", "USA", "Canada", "Germany", "france", "Ghana", "India"],
        "break": ["seem like this relationship is not working and you want to break up bye it was fun while its lasted"]
    }

print("Hello, my name is ", random.choice(array_list["name"]), "How may i be of help to you")
#continue_chat_bot = "yes"
#while continue_chat_bot == "yes":

  #  print("what would you like to know")
play = True
while play:

    search = input().split()

    for key in search:
        if key in array_list.keys():
            print(random.choice(key))
            print("Please ask another question")
            break
        if "break" in array_list.keys():
            print(key)
            break
    else:
        print("i dont understand your question Please ask another question")

    if not play:
        break
