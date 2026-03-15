import numpy as np
import pandas as pd


def total_YN(outlook, decision):
    """Returns the total yes or no in the Maligo col"""

    count = (outlook == decision).sum()

    return count

def totalYN_col(df, col, val, decision):
    """Returns how many yes or no in a circumstances(cols)"""

    condition = (col == val) & (df['Maligo'] == decision)

    return condition.sum()


df = pd.read_csv("Naive_Ligo/maligo_data.csv")


# Total Yes or No
total_yes = total_YN(df['Maligo'], "Yes")       # 7
total_no = total_YN(df['Maligo'], "No")         # 4


# WEATHER
# Total Yes and No for the Rainy
total_yes_rainy = totalYN_col(df, df['Weather'], "Rainy", "Yes")        # 2
total_no_rainy = totalYN_col(df, df['Weather'], "Rainy", "No")          # 2

# Total Yes and No for the Sunny    
total_yes_sunny = totalYN_col(df, df['Weather'], "Sunny", "Yes")        # 3
total_no_sunny = totalYN_col(df, df['Weather'], "Sunny", "No")          # 1

# Total yes and No for the Cloudy
total_yes_cloudy = totalYN_col(df, df['Weather'], "Cloudy", "Yes")      # 2
total_no_cloudy = totalYN_col(df, df['Weather'], "Cloudy", "No")        # 1



# TIME
# Total Yes and No for the Morning
total_yes_morn = totalYN_col(df, df['Time'], "Morning", "Yes")        # 2
total_no_morn = totalYN_col(df, df['Time'], "Morning", "No")          # 1

# Total Yes and No for the Noon    
total_yes_noon = totalYN_col(df, df['Time'], "Noon", "Yes")        # 2
total_no_noon = totalYN_col(df, df['Time'], "Noon", "No")          # 0

# Total yes and No for the Afternoon
total_yes_af = totalYN_col(df, df['Time'], "Afternoon", "Yes")      # 2
total_no_af = totalYN_col(df, df['Time'], "Afternoon", "No")        # 1

# Total yes and No for the Evening
total_yes_eve = totalYN_col(df, df['Time'], "Evening", "Yes")      # 1
total_no_eve = totalYN_col(df, df['Time'], "Evening", "No")        # 2





print(df)
# print("\n\n\n",total_yes_neu)
# print(total_no_neu)