''' Elementary cellular automaton

https://en.wikipedia.org/wiki/Elementary_cellular_automaton


Cool  numbers: 18, 150s

'''

import sys
import time


class Automata():

    def __init__(self, limit=80, cols=80):
        self.nbrows = limit
        self.nbcols = cols

    def run(self, number):
        self.gen = 0
        self.number = number
        self.binary = f"{number:08b}"

        print("# Elementary cellular automaton - Number: " + str(self.number) + " ( " + self.binary + ' )')
        self.data = [1 if i == 39 else 0 for i in range(self.nbcols)]
        self.render()

        for i in range(1, self.nbrows):
            self.next()
            time.sleep(0.01)

    def next(self):
        self.data = [int(self.next_cell(i)) for i in range(self.nbcols)]
        self.render()

    def next_cell(self, c):
        l = c - 1 if c != 0 else self.nbcols - 1
        r = c + 1 if c != self.nbcols - 1 else 0
        pat = f"{self.data[l]}{self.data[c]}{self.data[r]}"
        return self.binary[7 - int(pat, 2)]

    def render(self):
        for i in self.data:
            print('#' if i == 1 else '.', end='')
        print(f' [{self.gen}]')
        self.gen += 1


# Run


if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = 0

automate = Automata()
automate.run(number)

'''
for n in range(number, 256):
    automate.run(n)
'''
