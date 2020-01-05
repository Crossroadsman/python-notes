import random


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def rolls(self, quantity=2):
        results = []
        for i in range(quantity):
            results.append(self.roll())
        return (results, sum(results))

    def rolls_drop_lowest(self, quantity=2):
        results = self.rolls(quantity)[0]
        sorted_results = sorted(results)
        dropped_results = sorted_results[1:]
        return (dropped_results, sum(dropped_results))


class Parser:

    def decode(self, string):
        dice, remainder = string.split('D')
        dice = int(dice)
        if '+' in remainder:
            die_type, constant  = remainder.split('+')
            constant = int(constant)
        elif '-' in remainder:
            die_type, constant = remainder.split('-')
            constant = int(constant) * -1
        else:
            die_type = remainder
            constant = 0
        die_type = int(die_type)
        return (dice, die_type, constant)

    def encode(self, dice, die_type, constant=0):
        if constant == 0:
            constant = ''
        elif constant > 0:
            constant = f'+{constant}'
        return f'{dice}D{die_type}{constant}'

    def roll(self, dice, die_type, constant):
        d = Die(die_type)
        total_so_far = constant
        for i in range(dice):
            total_so_far += d.roll()
        return total_so_far

    def rolls(self, string):
        dice, die_type, constant = self.decode(string)
        return self.roll(dice, die_type, constant)


class CharacterGenerator(Die):

   def generate(self):
       attributes = []
       for i in range(6):
           attribute = self.rolls_drop_lowest(4)
           print(f'attribute #{i}: {attribute}')
           attributes.append(attribute[1])
       return sorted(attributes, reverse=True)


def roll_test(string, runs):

    p = Parser()
    dice, die_type, constant  = p.decode(string)
    min_value = dice * 1 + constant
    max_value = dice * die_type + constant
    results = []
    histogram = [0 for i in range(max_value + 1)]
    for i in range(runs):
        result = p.rolls(string)
        results.append(result)
        histogram[result] += 1
    print(f'Results of running {runs} runs of {string}:')
    for i, result in enumerate(results):
        print(f'run #{i + 1}: {result}')
    print('value | count')
    print('------|------')
    for i in range(min_value, max_value + 1):
        print(f'{i}  | {histogram[i]}')
    return (results, histogram)



d4 = Die(4)
d6 = Die(6)
d8 = Die(8)
d10 = Die(10)
d20 = Die(20)
d100 = Die(100)

