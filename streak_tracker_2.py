"""
Implement:

dictionary -> json
contents:

load json...
can load dynamically into objects? classes?
"Key" : [[list of dates streak was kept], [list of dates streak was broken]]


for key in dict:
    prompt y/n
    add to list of dates
    calc_streak_length()
    calc_percentage()


THEN iterate through all keys, find the earliest date and latest date (should be today)
for every day between first/last...
print dot for each key, where dot colour changes based on yes/no/N/A status

calc % for all streaks

"""
import time
import datetime
TODAY = datetime.date.today()

SQUARE = '▩'
CGREEN  = '\33[32m'
CRED    = '\033[91m'
CBOLD   = '\33[1m'

CEND    = '\033[0m'

class Streak:
    def __init__(self, name, true_days = [], false_days = []):
        self.name = name
        self.true_days = true_days
        self.false_days = false_days

    def add_today(self):
        print(f"Did you {self.name} today? (Y/N)")
        yes = input().capitalize() == "Y"
        if yes: self.true_days.append(TODAY)
        else: self.false_days.append(TODAY)

    def print_day(self, day):
        if day in self.true_days: print(CGREEN + SQUARE + CEND)
        elif day in self.false_days: print(CRED + SQUARE + CEND)
        else: print(SQUARE)
    

test = Streak("kill youtself")
test.add_today()
test.print_day(TODAY)
