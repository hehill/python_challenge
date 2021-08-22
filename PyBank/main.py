import os
import pandas as pd

cwd = os.getcwd()
file_path = os.path.join(cwd, "PyBank", "Resources", "budget_data.csv")
df = pd.read_csv(file_path)

months = df["Date"].nunique()
net = df["Profit/Losses"].sum()

change = []
for i in range(months):
    if i == 0:
        delta = 0
        change.append(delta)
    else:
        current_pl = df.iloc[i,1]
        past_pl = df.iloc[(i-1),1]
        delta = current_pl - past_pl
        change.append(delta)
df["Change"] = change
average_change = round(df["Change"].mean(),2)

increase_df = df.loc[df["Change"] == df["Change"].max(), ["Date", "Change"]]
increase_date = increase_df.iloc[0,0]
increase_change = increase_df.iloc[0,1]

decrease_df = df.loc[df["Change"] == df["Change"].min(), ["Date", "Change"]]
decrease_date = decrease_df.iloc[0,0]
decrease_change = decrease_df.iloc[0,1]

print("-----------------------------")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {months}")
print(f"Net Profits: {net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${increase_change})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_change})")

output_path = os.path.join(cwd, "PyBank", "output.txt")
with open(output_path, "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("-----------------------------", file = text_file)
    print(f"Total Months: {months}", file = text_file)
    print(f"Net Profits: {net}", file = text_file)
    print(f"Average Change: ${average_change}", file = text_file)
    print(f"Greatest Increase in Profits: {increase_date} (${increase_change})", file = text_file)
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_change})", file = text_file)