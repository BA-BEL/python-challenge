

#Dependencies
import os
import csv

#csv directory

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, "r") as csvfile:

    csvreader=csv.reader(csvfile)

    #Store header and iterate csvreader
    csvheader = next(csvreader)

    #Initialize total vote count

    total_votes = 0

    #Initialize candidate vote dictionary

    candidate_vote = {}

    for row in csvreader:

        #Conditional to identify candidates and add to their votes.
        if row[2] not in candidate_vote.keys():
            candidate_vote[row[2]] = 1
        else:
            candidate_vote[row[2]] += 1

        #Add to total votes
        total_votes += 1

    #Calculation of percentages:

    for i in candidate_vote:

        #Store candidate's vote count
        vcount = candidate_vote[i]

        #calculate % of votes
        percentage = round(vcount/total_votes*100,3)

        #add + rearrange vcount and percentage
        candidate_vote[i] = [percentage,vcount]

    #Identification of winner
    
    #initializer
    initial = True

    for candidate in candidate_vote:

        #Initialize greatest value
        if initial == True:
            greatest = candidate[0]
            initial = False


        #Store value
        percentage = candidate[0]

        #Calculate greatest
        if percentage >= greatest:
            winner = candidate
            greatest = percentage
        
        print(winner)
    
    


