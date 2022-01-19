#add dependencies
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#create a filename variable to a direct or indirect path to the tile
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

#declare a new list
candidate_options = []

#declare an empty dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    #to do read and analyze the data here
    file_reader = csv.reader(election_data)
    #read the header row
    headers=next(file_reader)
    #print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to candidate's count
        candidate_votes[candidate_name] += 1

#save the results to our text file
with open(file_to_save, "w") as txt_file:

    #print the final vote count to the terminal
    election_results = (
            f"\nElection Results\n"
            f"-----------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")
    print(election_results, end="")

    #save the final vote count to the text file
    txt_file.write(election_results)

    #determine the percentage of votes for each candidate by looping through the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100
        #create candidate results the candidate name, vote count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage >winning_percentage):
            # if true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #and set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        
    

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------------------\n")
    #save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    #print(winning_candidate_summary)


#print the candidate list
#print(candidate_options)
# print the total votes
#print(total_votes)
#print candidate votes
#print(candidate_votes)
#print the candidate name and percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote. ")


# the data we need to retrieve
#1. the total number of votes cast
#2. a complete list of candidates who received votes
#3. the percentage of votes each candidate won
#4. the total number of votes each candidate won
#5. the winner of the election based on popular vote