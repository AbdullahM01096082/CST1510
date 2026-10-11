"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percentage = (value/limit) * 100
    return difference, percentage

def print_report(label, value, limit, difference, percent, status):
    """Print the complete formatted report."""
    print("=" * 40)
    print(f"RECORD CHECK - {label}")
    print("=" * 40)
    print(f"Used    : {value:>10}")
    print(f"Total   : {limit:>10}")
    print(f"Free    : {difference:>10}")
    print(f"Percent : {percent:>9.1f}%")
    print(f"Status  : {status:>10}")
    print("=" * 40)

over_limit_count = 0

while True:
    label = input("Enter label (or 'quit' to stop): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)


print("=" * 40)
print(f"Total records OVER LIMIT: {over_limit_count}")
print("=" * 40)

# while running it with 0 as a value and limit it give division by zero error because in math division by zero is not possible