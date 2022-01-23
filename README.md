# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has assigned the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.63.2

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes.
  - Diana DeGette received 73.8% of the vote and 272,892 total votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.
The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 total votes. 

## Overview of Election Audit
Using the same data looking at the candiate results for a Colorado congressional election, the election commission has requested additional information on:

1. The voter turnout for each county.
2. The percentage of votes from each country out of the total count.
3. The county with the highest turnout.

## Election Audit Results
First, it had to be determined how many votes were cast in the election, this was done by initializing a variable: total_votes = 0. The total_votes variable was then used with the following code to find the total number of votes cast in the election:
![Total Votes](https://github.com/baileyvo/Election_Analysis/blob/main/Resources/Total%20Votes.PNG)

In total, **369,711** votes were cast in the election.

To find the number of votes, a county list (county_list = []) and county votes dictionary (county_votes = {}) were created. From there, the following code was used to find the total number of votes and percentage of total votes for each county in the precinct:
![County Votes](https://github.com/baileyvo/Election_Analysis/blob/main/Resources/County%20Votes.PNG)

To find the county with the largest number of votes, a largest_count = 0 variable was initiated. From there, the following code was used to determine the county:
![Largest Count](https://github.com/baileyvo/Election_Analysis/blob/main/Resources/Largest%20Count.PNG)

Overall, the following results were generated:
![Election Results](https://github.com/baileyvo/Election_Analysis/blob/main/Resources/Election%20Results.PNG).

## Election Audit Summary
This script could be used again for further elections. It would require two modifications. The file_to_load variable would have to be changed to reference the correct data set. Similarly, the file_to_save variable would have to be changed to save to the correct folder and have a relevant title.
