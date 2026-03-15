import numpy as np
import pandas as pd


def total_YN(outlook, decision):
    """Returns the total yes or no in the Maligo col"""

    count = (outlook == decision).sum()

    return count

def totalYN_col(col, val, decision):
    """Returns how many yes or no in a circumstances(cols)"""

    condition = (col == val) & (col == decision)

    return condition.sum()


df = pd.read_csv("Naive_Ligo/maligo_data.csv")


# Total Yes or No
total_yes = total_YN(df['Maligo'], "Yes")       # 7
total_no = total_YN(df['Maligo'], "No")         # 4

# Total Yes and No for the Rainy
total_yes_rainy = totalYN_col(df['Weather'], "" "Yes")
total_no_rainy = totalYN_col(df, "No")

print(df)
print("\n\n\n", total_yes_rainy)
print(total_no_rainy)