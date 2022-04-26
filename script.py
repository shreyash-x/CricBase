import subprocess as sp
import pymysql
import pymysql.cursors


def printTable(myDict, colList=None):
    """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
    If column names (colList) aren't specified, they will show in random order.
    Author: Thierry Husson - Use it as you want but don't blame me.
    """
    print()
    if not colList:
        colList = list(myDict[0].keys() if myDict else [])
    myList = [colList]  # 1st row = header
    for item in myDict:
        myList.append([str(item[col] if item[col] is not None else '')
                      for col in colList])
    colSize = [max(map(len, col)) for col in zip(*myList)]
    formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
    myList.insert(1, ['-' * i for i in colSize])  # Seperating line
    for item in myList:
        print(formatStr.format(*item))
    print()


def retreival():
    print("1.Selection")
    print("2.Projection")
    print("3.Aggregate")
    print("4.Search")
    print("5.Analysis")
    print("6.Go Back")
    ch = int(input("Enter choice: "))

    if(ch == 1):
        selection()
    elif(ch == 2):
        projection()
    elif(ch == 3):
        aggregate()
    elif(ch == 4):
        search()
    elif(ch == 5):
        analysis()
    else:
        return

    return


def modification():

    print("1.Creation/Insertion")
    print("2.Update")
    print("3.Delete")
    print("4.Go Back")
    ch = int(input("Enter choice: "))

    if(ch == 1):
        creation()
    if(ch == 2):
        update()
    if(ch == 3):
        delete()
    else:
        return
    return


def selection():

    def selection_a():
        try:
            query = "WITH temp AS (SELECT Club_ID , COUNT(*) as Number_of_Players from player GROUP BY Club_ID) select club.Club_ID, club.Club_Name, temp.Number_of_Players FROM temp RIGHT JOIN club ON temp.Club_ID = club.Club_ID;"
            cur.execute(query)
            rows = cur.fetchall()
            printTable(rows)
            con.commit()

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database -", e)
        return

    def selection_b():
        try:
            cid = int(input("Enter Club ID: "))

            query = "SELECT Player_First_Name, Player_Middle_Name, Player_Last_Name from player where Club_ID = '%d'" % (
                cid)
            cur.execute(query)
            con.commit()
            rows = cur.fetchall()
            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database -", e)
        return

    print("1.Get complete list of clubs")
    print("2.Get complete list of players of a club")
    print("3.Return to main menu")
    ch = int(input("Enter choice: "))

    if(ch == 1):
        selection_a()
    elif(ch == 2):
        selection_b()
    else:
        return
    return


def projection():

    def projection_d():
        x = int(input("Enter x:"))
        try:
            query = "WITH age_temp AS (select Player_ID, (2021 - (Date_of_Birth % 10000)) as Age from player_age) SELECT player.Player_First_Name, player.Player_Middle_Name, player.Player_Last_Name, age_temp.Age from player INNER JOIN age_temp ON age_temp.Player_ID = player.Player_ID where age_temp.Age > "
            cur.execute(query + str(x))

            rows = cur.fetchall()
            con.commit()
            # print(query)
            print("Players with Age greater than ", x, ": \n")
            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database -", e)
        return

    def projection_e():
        # sql query
        try:

            query = "WITH age_temp AS (select Player_ID, (2021 - (Date_of_Birth % 10000)) as Age from player_age) SELECT player.Player_First_Name, player.Player_Middle_Name, player.Player_Last_Name, age_temp.Age from player INNER JOIN age_temp ON age_temp.Player_ID = player.Player_ID ORDER BY age_temp.Age"
            cur.execute(query)
            con.commit()
            p_table = cur.fetchall()
            print("Players sorted by Age: \n")
            printTable(p_table)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database - ", e)
        return

    def projection_f():
        x = int(input("Enter x:"))
        try:
            query = "WITH wk_temp AS (SELECT Player_id , Number_of_stumpings FROM Wicket_keeper WHERE Number_of_stumpings > '%d') SELECT wk_temp.Player_id, player.Player_First_Name, player.Player_Middle_Name, player.Player_Last_Name, wk_temp.Number_of_stumpings from player INNER JOIN wk_temp ON wk_temp.Player_id = player.Player_ID" % (x)
            cur.execute(query)
            con.commit()
            w_table = cur.fetchall()
            print("Wicket Keepers with stumpings greater than", x, ": \n")
            printTable(w_table)
        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database -", e)
        return

    print("1.Get a complete list of players with age greater than x.")
    print("2.Get a complete list of players sorted by their age.")
    print("3.Get a complete list of players who are wicket keepers and have stumpings greater than x.")
    print("4.Return to main menu")
    ch = int(input("Enter choice: "))
    if(ch == 1):
        projection_d()
    elif(ch == 2):
        projection_e()
    elif(ch == 3):
        projection_f()
    else:
        return
    return


def aggregate():

    def aggregate_f():
        # sql query
        try:
            query = "WITH avg_speed as (SELECT Player_id, Average_bowling_speed , Bowling_type , Economy  FROM Bowler WHERE Average_bowling_speed > (SELECT AVG(Average_bowling_speed) from Bowler)) SELECT avg_speed.Player_id , player.Player_First_Name, player.Player_Middle_Name, player.Player_Last_Name , avg_speed.Average_bowling_speed , avg_speed.Bowling_type , avg_speed.economy  from player INNER JOIN avg_speed  ON avg_speed.Player_id = player.Player_ID"
            cur.execute(query)
            con.commit()
            rows = cur.fetchall()
            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database - ", e)
        return

    def aggregate_g():
        try:
            query = "WITH avg_runs as (SELECT * FROM Batsman_Total_Runs WHERE Runs_in_ODI  > (SELECT AVG(Runs_in_ODI) from Batsman_Total_Runs)) SELECT avg_runs.Player_id , player.Player_First_Name, player.Player_Middle_Name, player.Player_Last_Name , avg_runs.Runs_in_ODI , avg_runs.Runs_in_T20 , avg_runs.Runs_in_Test from player INNER JOIN avg_runs  ON avg_runs.Player_id = player.Player_ID"
            cur.execute(query)
            con.commit()
            rows = cur.fetchall()
            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database - ", e)
        return

    print("1.Retrieve bowlers with bowling speed greater than avg bowling speed.")
    print("2.Retrieve batsmen with runs in odi greater than avg runs in odi")
    print("3.Return to main menu")
    num = int(input("Enter choice: "))
    if(num == 1):
        aggregate_f()
    elif(num == 2):
        aggregate_g()
    else:
        return
    return


def search():

    def search_h():
        # sql query
        try:
            exer = input("Enter player to be partially searched: ")

            query = "SELECT * FROM `player` WHERE `Player_First_Name` LIKE '%s%%' OR `Player_Middle_Name` LIKE '%s%%' OR `Player_Last_Name` LIKE '%s%%'" % (
                exer, exer, exer)
            cur.execute(query)
            rows1 = cur.fetchall()
            con.commit()
            printTable(rows1)
        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database:", e)
        return

    def search_coach():

        try:

            name = input("Name of coach :")
            query = "SELECT * from `coach` WHERE Coach_Name = '%s'" % name
            cur.execute(query)
            rows = cur.fetchall()
            # print(rows)
            con.commit()
            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database: ", e)
        return

    def search_club():

        try:

            name = input("Name of club :")
            query = "WITH temp AS (SELECT Club_ID , COUNT(*) as Number_of_Players from player GROUP BY Club_ID) select temp.Club_ID, club.Club_Name, temp.Number_of_Players FROM temp INNER JOIN club ON temp.Club_ID = club.Club_ID WHERE club.Club_Name = '%s'" % name
            cur.execute(query)
            rows = cur.fetchall()
            # print(rows)
            con.commit()

            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database: ", e)
        return

    def search_team():

        try:

            name = input("Name of team :")
            query = "SELECT * from `Team` where Team_Name = '%s'" % name
            cur.execute(query)
            rows = cur.fetchall()
            # print(rows)
            con.commit()

            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database: ", e)
        return

    print("1.Partially search name players.")
    print("2.Search for the name of a coach")
    print("3.Search for the name of a club")
    print("4.Search for the name of a team")
    print("5.Return to main menu")
    ch = int(input("Enter choice: "))
    if(ch == 1):
        search_h()
    elif(ch == 2):
        search_coach()
    elif(ch == 3):
        search_club()
    elif(ch == 4):
        search_team()
    else:
        return
    return


def analysis():

    def analysis_j():
        try:
            query = "WITH b AS (select player.Player_ID, player.Player_First_Name, player.Player_Middle_Name, player.Player_Last_Name, player.Number_of_matches_played, Bowler.Bowling_type, Bowler.Economy, Bowler.Average_bowling_speed from player INNER JOIN Bowler ON Bowler.Player_id = player.Player_ID), c AS (select player_Coaches_id.Player_ID, player_Coaches_id.Coach_id, coach.Coach_Name from player_Coaches_id INNER JOIN coach ON coach.Coach_ID = player_Coaches_id.Coach_id) Select b.Player_ID, b.Player_First_Name, b.Player_Middle_Name, b.Player_Last_Name, b.Number_of_matches_played, b.Bowling_type, b.Economy, b.Average_bowling_speed, c.Coach_id, c.Coach_Name from b INNER JOIN c ON b.Player_ID = c.Player_ID ORDER BY b.Number_of_matches_played DESC;"
            # print(query)
            cur.execute(query)
            con.commit()
            rows = cur.fetchall()
            print("Bowler Analysis: ")
            printTable(rows)

            # query = "SELECT b_num as 'Branch Number', count(member_id) as 'Members', avg(fee) as 'Average Fees', count(employee_id) as 'Employees', avg(salary) as 'Average Salary' FROM ( (branch JOIN member ON b_num = works_out) JOIN Employee ON b_num = works_in) GROUP BY b_num ;"
            # # print(quer
            # cur.execute(query)
            # con.commit()
            # rows = cur.fetchall()
            # # print(rows)
            # printTable(rows)
        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database -", e)
        return

    def analysis_k():
        # sql query
        try:

            query = "SELECT player.Player_ID , concat(Player_First_Name,' ',Player_Middle_Name,' ',Player_Last_Name) as player_name , Runs_in_ODI,Batsman_Type from Batsman_Total_Runs inner join Batsman on Batsman_Total_Runs.Player_id = Batsman.Player_id inner join player on player.Player_ID = Batsman_Total_Runs.Player_id order by Runs_in_ODI DESC;"

            cur.execute(query)
            con.commit()
            print("Bowler Analysis: ")
            print("ODI: ")
            rows = cur.fetchall()
            printTable(rows)

            query = "SELECT player.Player_ID , concat(Player_First_Name,' ',Player_Middle_Name,' ',Player_Last_Name) as player_name , Runs_in_T20,Batsman_Type from Batsman_Total_Runs inner join Batsman on Batsman_Total_Runs.Player_id = Batsman.Player_id inner join player on player.Player_ID = Batsman_Total_Runs.Player_id order by Runs_in_T20;"

            cur.execute(query)
            con.commit()
            print("T20: ")
            rows = cur.fetchall()
            printTable(rows)

            query = "SELECT player.Player_ID , concat(Player_First_Name,' ',Player_Middle_Name,' ',Player_Last_Name) as player_name , Runs_in_Test,Batsman_Type from Batsman_Total_Runs inner join Batsman on Batsman_Total_Runs.Player_id = Batsman.Player_id inner join player on player.Player_ID = Batsman_Total_Runs.Player_id order by Runs_in_Test DESC;"

            cur.execute(query)
            con.commit()
            print("Test: ")
            rows = cur.fetchall()
            printTable(rows)

        except Exception as e:
            con.rollback()
            print("Error Occured: Unable to retreive from database - ", e)
        return

    print("1.Bowler Analysis")
    print("2.Batsman Analysis")
    print("3.Return to main menu")
    ch = int(input("Enter choice: "))
    if(ch == 1):
        analysis_j()
    elif(ch == 2):
        analysis_k()
    else:
        return
    return


def creation():
    print("1.Add a new Player")
    print("2.Add a new club")
    print("3.Add a new manager")
    print("4.Add a new coach")
    print("5.Return to main menu")

    ch = int(input("Enter choice: "))
    if (ch == 1):
        add_player()
    elif(ch == 2):
        add_club()
    elif(ch == 3):
        add_manager()
    elif(ch == 4):
        add_coach()
    else:
        return
    return


def update():
    print("1.Change stats of a player")
    print("2.Update Phone Number")
    print("3.Return to main menu")

    ch = int(input("Enter choice: "))
    if(ch == 1):
        update_player()
    elif(ch == 2):
        update_phonenum()
    else:
        return
    return


def delete():
    print("1.Delete player")
    print("2.Delete manager")
    print("3.Delete coach")
    print("4.Return to main menu")
    ch = int(input("Enter choice: "))
    if(ch == 1):
        delete_player()
    elif(ch == 2):
        delete_manager()
    elif(ch == 3):
        delete_coach()
    else:
        return
    return


############ Addition ###############


def add_player():
    row = {}
    try:
        print("Enter New Player's details")
        row["Player_ID"] = int(input("Player ID: "))
        row["Team_ID"] = int(input("Team ID: "))
        row["Club_ID"] = int(input("Club ID: "))
        row["f_name"] = input("First Name: ")
        row["m_init"] = input("Middle Name: ")
        row["l_name"] = input("Last Name: ")
        row["Number_of_matches_played"] = int(
            input("Number of matches played: "))
        row["phone_number"] = input("Phone Numbers separated by ',' : ")
        phone_nos = row["phone_number"].split(",")
        row["coaches"] = input("Coach IDs seperated by ',' : ")
        coach = row["coaches"].split(",")
        row["dob"] = int(input("Date of birth (ddmmyyyy) :"))

        player_type = input(
            "Enter Player Type (Batsman/Bowler/Wicket-keeper) :")
        if(player_type == 'Batsman'):
            batsman_type = input("Enter Batsman Type:")
            query = "INSERT into Batsman VALUES (%s,%d)" % (
                batsman_type, row["Player_ID"])
            odi = int(input("Enter Runs in ODI:"))
            t20 = int(input("Enter Runs in T20:"))
            test = int(input("Enter Runs in Test:"))
        elif (player_type == 'Bowler'):
            bowling_type = input("Enter Bowling Type:")
            avg_bowling_speed = float(input("Enter Average Bowling Speed:"))
            economy = float(input("Enter Economy:"))
            query = "INSERT into Bowler VALUES ('%s','%f','%f',%d')" % (
                bowling_type, avg_bowling_speed, economy, row["Player_ID"])
        elif (player_type == 'Wicket-keeper'):
            num_stumpings = int(input("Enter Number of stumpings:"))
            query = "INSERT into Wicket_keeper VALUES (%d,%d)" % (
                num_stumpings, row["Player_ID"])
        else:
            print("Invalid Player Type")
            return

        query1 = "INSERT into player VALUES ('%d','%d','%d','%s','%s','%s','%d')" % (
            row["Player_ID"], row["Team_ID"], row["Club_ID"], row["f_name"], row["m_init"], row["l_name"], row["Number_of_matches_played"])
        cur.execute(query1)
        cur.execute(query)

        if(player_type == "Batsman"):
            quer = "INSERT into Batsman_Total_Runs VALUES (%d,%d,%d,%d)" % (
                odi, t20, test, row["Player_ID"])
            cur.execute(quer)

        for num in phone_nos:
            query = "INSERT INTO player_Phone_NO VALUES ('%d', '%s')" % (
                row["Player_ID"], num)
            cur.execute(query)
        for num in coach:
            query = "INSERT INTO player_Coaches_id VALUES ('%d', '%s')" % (
                row["Player_ID"], num)
            cur.execute(query)
            query5 = "INSERT INTO Coached_by VALUES ('%s', '%d')" % (
                num, row["Player_ID"])
            cur.execute(query5)
        query2 = "INSERT into player_age VALUES ('%d','%d')" % (
            row["dob"], row["Player_ID"])
        cur.execute(query2)

        con.commit()
        print("Successfully inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database:", e)
    return


def add_club():
    row = {}
    try:
        print("Enter New Club's details")
        row["Club_ID"] = int(input("Club ID: "))
        row["Club_Name"] = input("Club Name: ")

        # query1="SELECT COUNT(*) as 'final_count',trainer_id from member WHERE trainer_id='%s'  GROUP BY trainer_id " % row["trainer_id"]
        # cur.execute(query1)
        # table=cur.fetchall()
        # for r in table:
        #     trainer_limit=r['final_count']
        # if trainer_limit>=20:
        #     print("Error: This trainer is already overloaded. Max members allowed under a trainer is 20. Please assign a new trainer ")
        #     return

        query = "INSERT INTO club VALUES('%d', '%s')" % (
            row["Club_ID"], row["Club_Name"])

        cur.execute(query)
        con.commit()
        print("Successfully inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database:", e)
    return


def add_manager():
    row = {}
    try:
        print("Add New Manager's Details")
        row["Manager_ID"] = int(input("Manager ID: "))
        row["Club_ID"] = int(input("Club ID: "))
        row["Team_ID"] = int(input("Team ID: "))
        row["Manager_First_Name"] = input("First Name: ")
        row["Manager_Middle_Name"] = input("Middle Name: ")
        row["Manager_Last_Name"] = input("Last Name: ")
        row["Manager_phone_number"] = input("Phone Number(s): ")

        # sql query
        query1 = "INSERT into Manager VALUES ('%d','%s','%s','%s','%d','%d')" % (
            row["Manager_ID"], row["Manager_First_Name"], row["Manager_Middle_Name"], row["Manager_Last_Name"], row["Club_ID"], row["Team_ID"])
        # print(query)
        cur.execute(query1)

        phone_numbers = row["Manager_phone_number"].split(",")
        for num in phone_numbers:
            query = "INSERT into Manager_Phone_No VALUES ('%d','%s')" % (
                row["Manager_ID"], num)
            cur.execute(query)

        con.commit()
        print("Successfully inserted into Database\n")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database:", e)

    return


def add_coach():
    try:
        row = {}
        row["name"] = input("Coach Name: ")
        row["coach id"] = int(input("Coach ID: "))
        row["coach Phone no"] = input("Coach Phone no: ")
        row["club_name"] = input("Club Name: ")
        row["club id"] = int(input("Club ID: "))
        row["coach type"] = input("Coach type: ")

        phone_nos = row["coach Phone no"].split(', ')

        # sql query
        query1 = "INSERT into coach(Coach_ID,Club_ID , Coach_Name) VALUES ('%d','%d' , '%s')" % (
            row["coach id"], row["club id"], row["name"])

        query3 = "INSERT into coach_type(Coach_id,Type_name) VALUES ('%d','%s')" % (
            row["coach id"], row["coach type"])

        # print(query)
        cur.execute(query1)
        cur.execute(query3)
        for num in phone_nos:
            query = "INSERT INTO Coach_Phone_NO(Coach_ID,Phone_Numbers) VALUES ('%d', '%s')" % (
                row["coach id"], num)
            cur.execute(query)
        con.commit()
        print("Successfully inserted into Database\n")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database:", e)

    return


############# Deletion ##############

def delete_player():
    try:
        # sql query
        id = int(input("Player ID whose info is to be deleted: "))
        query1 = "DELETE FROM player WHERE Player_ID='%d'" % id
        query2 = "DELETE FROM player_Coaches_id WHERE Player_ID='%d'" % id
        query3 = "DELETE FROM player_age WHERE Player_ID='%d'" % id
        query4 = "DELETE FROM Batsman WHERE Player_id='%d'" % id
        query5 = "DELETE FROM Wicket_keeper WHERE Player_id='%d'" % id
        query6 = "DELETE FROM Matches_played WHERE Player_id='%d'" % id
        query7 = "DELETE FROM Bowler WHERE Player_id='%d'" % id
        query8 = "DELETE FROM Coached_by WHERE Player_id='%d'" % id
        query9 = "DELETE FROM player_Phone_NO WHERE Player_ID='%d'" % id
        query10 = "DELETE FROM Batsman_Total_Runs WHERE Player_ID='%d'" % id
        cur.execute(query4)
        cur.execute(query5)
        cur.execute(query7)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute(query6)
        cur.execute(query8)
        cur.execute(query9)
        cur.execute(query10)
        cur.execute(query1)

        con.commit()
        print("Successfully deleted from Database\n")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database:", e)

    return


def delete_manager():
    try:
        # sql query
        mid = int(input("Enter Manager ID: "))
        query = "DELETE FROM Manager WHERE Manager_ID= '%s'" % mid
        # print(query)

        query1 = "DELETE FROM Manager_Phone_No WHERE Manager_ID= '%s'" % mid
        cur.execute(query1)
        cur.execute(query)
        con.commit()
        print("Successfully deleted from Database\n")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database:", e)

    return


def delete_coach():
    try:
        # sql query
        cid = int(input("Enter Coach id: "))
        query1 = "DELETE from coach WHERE Coach_ID = '%d'" % cid

        query2 = "DELETE from Coach_Phone_NO WHERE Coach_ID = '%d'" % cid
        cur.execute(query2)
        query3 = "DELETE from player_Coaches_id WHERE Coach_id = '%d'" % cid
        cur.execute(query3)
        query4 = "DELETE from Coached_by WHERE Coach_id = '%d'" % cid
        cur.execute(query4)
        query5 = "DELETE from coach_type WHERE Coach_id = '%d'" % cid
        cur.execute(query5)
        cur.execute(query1)

        con.commit()
        print("Successfully deleted from Database\n")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database:", e)

    return

################ Update ##################


def update_player():
    player_type = input("Enter Player type (Batsman/Bowler/Wicket Keeper): ")
    player_id = int(input("Enter player id: "))
    try:
        row = {}
        # sql query

        if player_type == 'Batsman':

            print("1.Change No of matches played")
            print("2.Change Batsman type")
            print("3.Change runs")

            ch = int(input("Enter choice: "))

            if(ch == 1):
                Test_matches_played = int(
                    input("No. of Test Matches played: "))
                One__matches_played = int(
                    input("No. of One day Matches played: "))
                T20_matches_played = int(input("No. of T20 Matches played: "))

                query = "UPDATE `Matches_played` SET `Test_match` = '%d', `One_day` = '%d' ,`T20` = '%d'  WHERE `Player_id` = '%d'" % (
                    Test_matches_played, One__matches_played, T20_matches_played, player_id)
                cur.execute(query)
                con.commit()
                print("Successfully updated details into Database\n")

            elif(ch == 2):
                Type = input("Enter Batsman type: ")
                query = "UPDATE `Batsman` SET `Batsman_type` = '%s'  WHERE `Player_id` = '%d'" % (
                    Type, player_id)
                cur.execute(query)
                con.commit()
                print("Successfully updated details into Database\n")

            elif(ch == 3):
                Runs_in_ODI = int(input("Enter ODI runs: "))
                Runs_in_T20 = int(input("Enter runs in T20: "))
                Runs_in_Test = int(input("Enter runs in test: "))

                query = "UPDATE `Batsman_Total_Runs` SET `Runs_in_ODI` = '%d' , `Runs_in_T20` = '%d' , `Runs_in_Test` = '%d'   WHERE `Player_id` = '%d'" % (
                    Runs_in_ODI, Runs_in_T20, Runs_in_Test,  player_id)
                cur.execute(query)
                con.commit()
                print("Successfully updated details into Database\n")

        elif player_type == 'Bowler':

            print("1.Change Bowling_type")
            print("2.Change Avg Bowling Speed")
            print("3.Change economy")

            ch = int(print("Enter choice: "))

            if(ch == 1):
                Bowling_type = input("Enter new Bowling type")
                query = "UPDATE `Bowler` SET `Bowling_type` = '%s'  WHERE `Player_id` = '%d'" % (
                    Bowling_type,  player_id)
                cur.execute(query)
                con.commit()
                print("Successfully updated details into Database\n")

            elif(ch == 2):
                Avg_Bowling_speed = float(input("Enter new Avg bowling speed"))
                query = "UPDATE `Bowler` SET `Average_bowling_speed` = '%f'  WHERE `Player_id` = '%d'" % (
                    Avg_Bowling_speed,  player_id)
                cur.execute(query)
                con.commit()
                print("Successfully updated details into Database\n")

            elif(ch == 3):
                Economy = float(input("Enter new economy"))
                query = "UPDATE `Bowler` SET `Economy` = '%f'  WHERE `Player_id` = '%d'" % (
                    Economy,  player_id)
                cur.execute(query)
                con.commit()
                print("Successfully updated details into Database\n")

        elif player_type == 'Wicket Keeper':
            stumpings = int(input("Enter new number of stumpings: "))
            query = "UPDATE `Wicket_keeper` SET `Number_of_stumpings` = '%d'  WHERE `Player_id` = '%d'" % (
                stumpings,  player_id)
            cur.execute(query)
            con.commit()
            print("Successfully updated details into Database\n")

    except Exception as e:
        con.rollback()
        print("Failed to updated details into database:", e)

    return


def update_phonenum():
    print("1.Player")
    print("2.Manager")
    print("3.Coach")

    ch = int(input("Enter choice: "))
    prev_pnum = input("Enter previous Phone Number:")
    new_pnum = input("Enter new Phone Number:")

    if(ch == 1):
        pid = int(input("Enter Player ID:"))
        query = "UPDATE player_Phone_NO SET Phone_Number = '%s' WHERE Player_ID = '%d' AND Phone_Number = '%s'" % (
            new_pnum, pid, prev_pnum)
    elif(ch == 2):
        mid = int(input("Enter Manager ID:"))
        query = "UPDATE Manager_Phone_No SET Phone_Number = '%s' WHERE Manager_ID = '%d' AND Phone_Number = '%s'" % (
            new_pnum, mid, prev_pnum)
    elif(ch == 3):
        cid = int(input("Enter Coach ID:"))
        query = "UPDATE Coach_Phone_NO SET Phone_Numbers = '%s' WHERE Coach_ID = '%d' AND Phone_Numbers = '%s'" % (
            new_pnum, cid, prev_pnum)
    else:
        print("Invalid Input")
        return

    try:
        cur.execute(query)
        con.commit()
        print("Successfully updated details into Database\n")
    except Exception as e:
        con.rollback()
        print("Failed to updated details into database:", e)

    return


def displayTable():
    table = input("Enter table name: ")
    query = "SELECT * from %s ;" % (table)
    cur.execute(query)
    rows = cur.fetchall()
    printTable(rows)


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    # print("Entered: ", ch)
    if(ch == 1):
        retreival()
    elif(ch == 2):
        modification()
    elif(ch == 4):
        displayTable()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    # tmp=sp.call('cls', shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="ak0909",
                              db='cricket',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('cls', shell=True)

        if(con.open):
            print("Connected with the database.")
        else:
            print("Failed to connect.")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('cls', shell=True)
                print(
                    "Welcome to the Cricket Database! What do you want to do?")
                # Here taking example of Employee Mini-world
                print("1.Retrieval")  # Hire an Employee
                print("2.Modification")  # Fire an Employee
                print("3.Logout")
                print("4.Show table")
                ch = int(input("Enter choice> "))
                tmp = sp.call('cls', shell=True)
                if ch == 3:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE> ")

    except Exception as e:
        tmp = sp.call('cls', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
