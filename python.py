# if while loops
pocketMoney = input("Your pocket money: ")

if pocketMoney <= 100:
    print(f"{pocketMoney} is your pocket money")
    print("It is ok")
elif pocketMoney <= 500:
    print(f"{pocketMoney} is your pocket money")
    print("You are rich")
elif pocketMoney <= 1000:
    print(f"{pocketMoney} is your pocket money")
    print("You are very rich")
else:
    print(f"{pocketMoney} is your pocket money")
    print("You are super rich")

myFriends = ["Friend1", "friend2", "friend3"]

number = 5

for friend in myFriends:
    print(f"{friend} is your friend")

while number > 0:
    print(number)
    number = number - 1

# counter
your_name = input("Your name: ")
count = print(f"Sentence - (Your name is {your_name})")

intro = f"Your name is {your_name}"

character_count = 0
word_count = 1

for intro_letter in intro:
    character_count = character_count + 1

    if(intro_letter == ' '):
        word_count = word_count + 1

print(f"Number of word in this sentence: {word_count}")
print(f"Number of character in this sentence: {character_count}")
