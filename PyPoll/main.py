import os
import pandas as pd

cwd = os.getcwd()
file_path = os.path.join(cwd, "PyPoll", "Resources", "election_data.csv")
df = pd.read_csv(file_path)

votes_tot = df["Voter ID"].nunique()
cand_votes = pd.DataFrame(df["Candidate"].value_counts())
cand_votes = cand_votes.reset_index().rename(columns = {"index" : "Candidate_Name", "Candidate" : "Vote_Count"})
cand_votes["Percent_of_Total_Votes"] = round(cand_votes["Vote_Count"]/votes_tot,3) * 100
cand_votes["Percent_of_Total_Votes"] = cand_votes["Percent_of_Total_Votes"].map("{:.1f}%".format)
winner = cand_votes.loc[cand_votes["Vote_Count"] == max(cand_votes["Vote_Count"]), "Candidate_Name"][0]

print("-----------------------------")
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {votes_tot}")
print("-----------------------------")
print(cand_votes)
print("-----------------------------")
print(f"The winner is {winner}!")
print("-----------------------------")

output_path = os.path.join(cwd, "PyPoll", "output.txt")
with open(output_path, "w") as text_file:
    print("Election Results", file= text_file)
    print("-----------------------------", file= text_file)
    print(f"Total Votes: {votes_tot}", file= text_file)
    print("-----------------------------", file= text_file)
    print(cand_votes, file= text_file)
    print("-----------------------------", file= text_file)
    print(f"The winner is {winner}!", file= text_file)
    print("-----------------------------", file= text_file)