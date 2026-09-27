"""
RECORD CHECK  -  my version
===========================

Name  :  Abdullah Rashid
Lane  :  IT
Date  :  23/9/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
label = input("Label: ")
used = float(input("Used: "))
total = float(input("Total: "))

# ================================================================== PROCESS

difference = total - used
percentage = (used / total) * 100

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print("=" * 34)
print(f"RECORD CHECK  -  {label}")
print("=" * 34)
print(f"Used: {used:>12.2f}")
print(f"Total:{total:>12.2f}")
print(f"Difference: {difference:+.2f}")
print(f"Percentage: {percentage:.2f}%")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
