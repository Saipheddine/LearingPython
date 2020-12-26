#this is a love calculator programm to help you check if you and your partner can be a great pair, based on your names

#input names
name1 = input("Enter first person's name: ")
name2 = input("Enter second person's name: ")


name1 = name1.lower()
name2 = name2.lower()

love_counter_p1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
love_counter_p2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
true_counter_p1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
true_counter_p2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")    

love_sum = love_counter_p1 + love_counter_p2
true_sum = true_counter_p1 + true_counter_p2

loveScore = int(str(str(true_sum) + str(love_sum)))

if (loveScore < 10 or loveScore > 90):
    print("Your score is {}, you go together like coke and mentos.".format(loveScore))
elif (loveScore >= 40 and loveScore <= 50):
    print("Your score is {}, you are alright together.".format(loveScore))
else:
    print("Your score is {}.".format(loveScore))









