import itertools

# infinite iterators
counter = itertools.count(start=5, step=5)

data = [100, 200, 300, 400]
daily_data = itertools.zip_longest(range(10), data)

counter2 = itertools.cycle(('on', 'off'))

counter3 = itertools.repeat(2, times=3)

squares = map(pow, range(10), itertools.repeat(2))  # pow: pow(a, b) == a ** b
squares2 = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)]) # starmpa(func, iter줄)

# Combination: group w/o order
# Permutation: group w/ order

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2)
result2 = itertools.permutations(letters, 2)
result3 = itertools.product(numbers, repeat=2)
result4 = itertools.combinations_with_replacement(numbers, 3)

combined = letters + numbers + names # heavy memory burden
combined1 = itertools.chain(letters, numbers, names)

result5 = itertools.islice(range(10), 3, 9, 2)


with open('test.log', 'r') as f:
     
    header = itertools.islice(f, 3) # f.readline()
    
    # for line in header:
    #     print(line, end='')

selectors = [True, True, False, True]
result6 = itertools.compress(letters, selectors)

def lt_2(n) :
    if n < 2:
        return True
    return False

result7 = filter(lt_2, numbers)

numbers = [2, 3, 2, 1, 0]

result8 = itertools.filterfalse(lt_2, numbers)
result9 = itertools.dropwhile(lt_2, numbers)
result10 = itertools.takewhile(lt_2, numbers)

import operator
result11 = itertools.accumulate(numbers, operator.pow)

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
]

def get_state(person):
    return person['state']

person_group = itertools.groupby(people, get_state) # func doesn't sort

copy1, copy2 = itertools.tee(person_group)

# for key, group in person_group:
#     print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()