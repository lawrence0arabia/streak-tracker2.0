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

def next_day(day):
    return day + datetime.timedelta(days=1)

def prev_day(day):
    return day - datetime.timedelta(days=1)

class Streak:
    def __init__(self, name, true_days = [], false_days = []):
        self.name = name
        self.true_days = true_days
        self.false_days = false_days

    def add_today(self):
        if self.day_is_present(TODAY):
            print(f'Skipping "{self.name}", as it has already been tracked today.')
            return
        print(f"Did you {self.name} today? (Y/N)")
        yes = input().capitalize() == "Y"
        if yes: self.true_days.append(TODAY)
        else: self.false_days.append(TODAY)

    def print_day(self, day):
        if day in self.true_days: print(CGREEN + SQUARE + CEND)
        elif day in self.false_days: print(CRED + SQUARE + CEND)
        else: print(SQUARE)

    def num_of_true_days(self):
        return len(self.true_days)
    
    def count_streak(self, start):
        "Counts streak length from a starting position (right to left)"
        count = 0
        pos = start
        while pos > 0:
            count += 1
            if prev_day(self.true_days[pos]) != self.true_days[pos - 1]:
                return count
            pos -= 1

    def find_longest_streak(this):
        pos = len(this.true_days) - 1
        largest = 0
        while pos > 0:
            pos_streak = this.count_streak(pos)
            if pos_streak> largest:
                largest = pos_streak
            pos -= 1
        return largest

    def day_is_present(self, day):
        if day in self.true_days or day in self.false_days: 
            return True
        else:
            return False


test = Streak("kill youtself")
test.add_today()
test.add_today()
test.true_days.append(prev_day(prev_day(prev_day(TODAY))))
test.true_days.append(prev_day(prev_day(TODAY)))
test.true_days.append(prev_day(TODAY))
test.add_today()
# test.print_day(TODAY)

# print(test.count_streak(len(test.true_days) - 1))
print(test.find_longest_streak())