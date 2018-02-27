xos = 'Xo' * 4
oxs = 'Ox' * 4

my_list = []
'''
Note that append() returns None, not the list to which the value was appended.
Accordingly, you can't do:
my_list.append(string_1).append(string_2)
because this is equivalent to:
None.append(string_2)

This is also why you can't do something like:
numbers = [1, 2, 3].append(4)
'''
my_list.append(string_1)
my_list.append(string_2)
my_list *= 4

print('\n'.join(my_list))
