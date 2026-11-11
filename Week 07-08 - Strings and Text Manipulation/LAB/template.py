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

def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
        fields[hostname] = hostname_part.strip().lower()

    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}

with open(r"C:\Users\Bulla\OneDrive\Desktop\UNI_coding_stuff\CST1510\Week 07-08 - Strings and Text Manipulation\LAB\messy_lines.txt") as f:
    total_records = 0
    flagged_records = 0
    for raw_line in f:
        record = parse_line(raw_line)
        print(record["hostname"], record["used"], record["total"], status_of(record["used"], record["total"]))
        total_records += 1

        if status_of(record["used"], record["total"]) == "WARNING" and "OVER LIMIT":
            flagged_records += 1

print("=" * 30)
print(f"There are total of {total_records} records\nFlagged records are {flagged_records}")
print("=" * 30)