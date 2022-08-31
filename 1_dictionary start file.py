phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
"""
print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)
print(len(phonebook))
mydictionary = dict(m=8, n=9)
print(mydictionary)

print(phonebook['Chris'])
chris_phone = phonebook["Chris"]
print(chris_phone)

print()
print('*****  end section 1 ********')
print()








print()
print('*****  start section 2 - search dictionary ********')
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook")


print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

phonebook["Joe"] = "555-0123"

phonebook["Chris"] = "555-4444"
print(phonebook)

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook["Chris"]

print(phonebook)

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

for k in phonebook:
    print(k)
    print(phonebook[k])

print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()

for v in phonebook.values():
        print(v)


print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

for key,value in phonebook.items():
    print(key)
    print(value)

for item in phonebook.items():
    print(item)

print()
print('*****  end section 7 ********')
print()


"""





print()
print('*****  start section 8 - using random and converting to list ********')
print()

phone = phonebook.get("Chri", "Key not found")

print(phone)

remove = phonebook.pop("Chris", "not found")

print(remove)
print(phonebook)

a = phonebook.popitem()
print(a)
print(phonebook)

print()
print('*****  end section 8 ********')
print()

import random

random_list = list(phonebook)
random_key = random.choice(random_list)
print(random_key)
print(phonebook[random_key])
#OR
print(phonebook[random.choice(list(phonebook))])