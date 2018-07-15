import pandas as pd

csv_path = "Resources/election_data.csv"
election = pd.read_csv(csv_path)

election.head()
count = len(election["Voter ID"].unique())
count
election["Candidate"].unique()
separatecount = election["Candidate"].value_counts()
separatecount
percent = election["Candidate"].value_counts()/ count
percent
winner = separatecount.idxmax()
winner
text_file = open("Output.txt", "w")                 
text_file.write("Total Votes: " + str(count)+"\n")
text_file.write("Winner: " + str(winner)+"\n")
text_file.write("Percent:" +"\n" + str(percent)+"\n")
text_file.write("Votes Counting:" +"\n" + str(separatecount)+"\n")