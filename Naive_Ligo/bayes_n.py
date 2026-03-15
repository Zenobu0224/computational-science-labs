import numpy as np
import pandas as pd


def total_YN(outlook, decision):
    count = (outlook == decision).sum()

    return count


df = pd.read_csv("Naive_Ligo/maligo_data.csv")


# Total Yes or No
total_yes = total_YN(df['Maligo'], "Yes")
total_no = total_YN(df['Maligo'], "No")



print(df)
