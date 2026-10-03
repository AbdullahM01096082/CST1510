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

# ==================================================================== INPUT

host_name = str(input("Enter server name:"))
used = float(input("Enter used GB's:"))
total = float(input("Enter Total GB's:"))
free_storage = total - used
used_percent = (used/total) * 100
if used > total:
    status = "\tOVER LIMIT"
else: status = "OK"
print("=" * 30)
print(f"Record check - {host_name}")
print("=" * 30)
print(f"Used\t:{used:>10.2f}\nTotal\t:{total:>10.2f}\nFree\t:{free_storage:>10.2f}\nPercent\t:{used_percent:>10.2f} %\nStatus\t:{status:>10}")

# ==========================================================================
