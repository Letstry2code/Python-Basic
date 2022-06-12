import random

def generate_name():
    list1=['red','green','blue','yellow','orange','black','white','brown','orange']
    list2=['apple','kiwi','strawberry','mango','grape','pear','watermellon','banana','peach','avacardo']
    list3=['cat','dog','bird','fish','lion','tiger','bear','wolf','panda']

    p1=random.choice(list1)
    p2=random.choice(list2)
    p3=random.choice(list3)
    return f'{p1}-{p2}-{p3}'