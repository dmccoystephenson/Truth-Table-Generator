num_vars = 2               # number of variables
num_combos = 2**num_vars    # number of combinations = 2^n

# create an empty list
li = []

# fill with combos-1 and descending
num = num_combos - 1
for item in range(num_combos):
  li.append(num)
  num = num - 1

# convert list items to binary
for item in range(num_combos):
  li[item] = format(li[item], '0{}b'.format(num_vars))     # the [2:] cuts off the 0b

# convert list items to lists themselves
for item in range(num_combos):
  li[item] = list(li[item])

# append answer slot to each list in the listOfLists
for item in range(num_combos):
  li[item].append('2')

# convert all to boolean
for item in range(num_combos):
  for item2 in range(num_vars):
    li[item][item2] = bool(int(li[item][item2], 10))

print(li)


myli = ['x','y']
exec('{}=True'.format(myli[0]))