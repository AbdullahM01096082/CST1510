"""
RECORD CHECK  -  Abdullah Rashid
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

class Record:

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """gets the percentage of self.value and self.limit for self.status"""
        return (self.value / self.limit) * 100

    def status(self):
        """Returns status according to the percentage"""
        if self.percent() > 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"

    def is_over(self): 
        """returns True or False if self.status is = OVER LIMIT or not"""
        return self.status() == "OVER LIMIT"
        

def load_records(path):
    records = []
    with open(path, "r") as file:

        for line in file:
            label, value, limit = line.strip().split(",")
            record = Record(label, float(value), float(limit))
            records.append(record)
    return records

path = "records_sample.txt"

records = load_records(path)

over_limit_count = 0
for r in records:
    if r.is_over():
        over_limit_count += 1

for r in records:
        print("=" * 34)
        print(f"  RECORD CHECK  -  {r.label}")
        print("=" * 34)
        print(f"Value: {r.value}")
        print(f"Limit: {r.limit}")
        print(f"Status: {r.status()}")
        print(f"{over_limit_count} of {len(records)} records are OVER LIMIT")
        print("=" * 34)
