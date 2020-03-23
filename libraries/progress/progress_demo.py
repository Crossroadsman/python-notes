from progress.bar import Bar
import random
import csv

"""
# Here are three basic examples
# Ex1
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()

# Ex2
from progress.bar import Bar

with Bar('Processing', max=20) as bar:
    for i in range(20):
        # Do some work
        bar.next()

# Ex3
for i in Bar('Processing').iter(it):
    # Do some work
"""

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class CharacterGenerator():

    def generate(self):
        d6 = Die(sides=6)
        attributes = []
        for _ in range(6):
            four_d6 = [d6.roll() for _ in range(4)]
            attribute = sum(four_d6) - min(four_d6)
            attributes.append(attribute)
        return attributes


class MassGenerator():

    def __init__(self):
        self.cg = CharacterGenerator()

    def generate(self, runs=100, outfile=None, totals=False):
        if outfile is not None:
            self.generate_to_csv(runs=runs, outfile=outfile, totals=totals)
        else:  # list output
            return self.generate_to_list(runs=runs, totals=totals)

    def generate_to_list(self, runs=100, totals=False):
        if runs > 1000:
            progressbar = Bar('Processing', max=runs)
        else:
            progressbar = None
        output = []
        
        for _ in range(runs):
            attributes = self.cg.generate()
            if totals:
                attributes.append(sum(attributes))
            output.append(attributes)
            if progressbar is None:
                continue
            else:
                progressbar.next()
        if progressbar is not None:
            progressbar.finish()
        return output

    def generate_to_csv(self, outfile, runs=100, totals=False):
        if runs > 1000:
            progressbar = Bar('Processing', max=runs)
        else:
            progressbar = None

        with open(outfile, 'w', newline='') as fh:
            writer = csv.writer(fh)
            for _ in range(runs):
                attributes = self.cg.generate()
                if totals:
                    attributes.append(sum(attributes))
                writer.writerow(attributes)
                if progressbar is None:
                    continue
                else:
                    progressbar.next()

            if progressbar is not None:
                progressbar.finish()
        

