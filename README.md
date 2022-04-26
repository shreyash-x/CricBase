Data and Applications project based on Cricket Tournament's Database

### How to run:
`python3 script.py`


**We built a CLI where we can choose the command to run from the numbered menu.**

- Selection
1. Get complete list of clubs → will list all the clubs and the number of player in them. 
2. Get complete list of players of a club → List out all the player belonging to a particular club. 
- Projection
1. Players with Age greater than x - Takes x as an input and list all the players whose age is greater than x. 
2. Get a complete list of players sorted by their age - Print the list of players sorted by their age. 
3. Get a complete list of players who are wicket keepers and have stumpings greater than x → This option list all wicket keepers which have no of stumpings greater than x. 
- Aggregate
1. Get a complete list of players who are wicket keepers and have stumpings greater than x
2. Retrieve batsmen with runs in odi greater than avg runs in odi
- Search
1. Partially search name players - Takes string as input and list all players whose name / part of name matches with that string and their info.
2. Search for the name of a coach - Takes string as input (coach's name) and prints the details of coach such as coach Id and club id.
3. Search for the name of a club- Takes string as input(club's name) and prints the club name, club ID, number of players in the club.
4. Search for the name of a team- Takes string as input(team's name) and prints the team id, team name, club id, manager of the team and the number of players in the team.
- Analysis
1. Bowler Analysis - This prints the economies of different bowlers sorted on the basis of matches played (descending) along with the bowler's stats and personal information. It also displays the names of the coaches of the Bowlers.
2. Batsman Analysis - Prints 3 tables analyzing the performance of batsmen sorting them based on the number of runs scored in each format and also prints the batsman type which helps us understand which type of batsman is best for a format.

- Insertion / Creation
1. Add a new Player - Takes info about the player (id , name , phono number , type , coach etc) and add it to the database.
2. Add a new club - Add new club to database
3. Add a new manager- Takes manager info and add it to database
4. Add a new coach - Takes coach info as input and add it to database. 
- Delete
1. Delete player - Takes player id as input and remove all data of that player from database.
2. Delete manager - Takes manager id as input and remove all data of that manager from database.
3. Delete coach - Takes coach id as input and remove all data of that coach from database
- Update
1. Change stats of a player - Takes player id type of player as input and new stats of the player and changes accordingly in the database. 
2. Update phone number - Takes player id/ manager id / coach id and old phone number and update it to new phone number.
