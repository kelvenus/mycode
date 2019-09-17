#!/usr/bin/env python3

## working with dictionary and loop
names =  ['fluffy', 'spot', 'cujo']
ages  =  [3, 7, 12]
animal_type = ['cat', 'dog', 'mean dog ']

num=[0, 1, 2]

pets = {}

for pet in num:
    pets.update({names[pet]: {'ages': ages[pet], 'animal_type': animmal_type[pet]} )

#print for loop of pets 
print(pets)
