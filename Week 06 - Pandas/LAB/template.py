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

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Bulla\OneDrive\Desktop\UNI_coding_stuff\CST1510\Week 06 - Pandas\LAB\my_df.csv")

df["percent"] = ( df["used_gb"] / df["total_gb"]) * 100

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK"
)

print(df)

rows_filter = df[df["status"] != "OK"]
print(rows_filter)

group = df.groupby("status").count()
df.to_csv("my_df_save.csv", index=False)
df["status"].value_counts().plot(kind="bar")
plt.title("Status Counts")
plt.show()

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.



# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
