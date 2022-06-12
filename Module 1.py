import random
for i in range(10):
    print(random.random())
    print(random.randint(1,105),end=' ')
smileys=('😊','😊','🤣','🤣','❤','❤','💕','😍')
print(random.choice(smileys))
print(random.choices(smileys,k=3))

