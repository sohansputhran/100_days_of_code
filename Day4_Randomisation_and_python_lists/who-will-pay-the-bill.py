import random

friends = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

print(friends[random.randint(0, len(friends) - 1)] + " is going to buy the meal today!")

# or
print(random.choice(friends) + " is going to buy the meal today!")