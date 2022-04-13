import json
import mysql.connector
from mysql.connector import Error
from queries import *


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            auth_plugin='mysql_native_password'
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


connection = create_server_connection("localhost", "root", "MYSQLlaptop@757")


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# create_database_query = "CREATE DATABASE ASSIGNMENT"
# create_database(connection, create_database_query)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


with open('data.json', 'r') as f:
    data = json.load(f)


column = data['names'][0]


retro_election = create_retro_election_table.format(Year=column['Year'],
                                                    Election_Type=column['Election Type'].replace(
    " ", ""),
    AC_No=column['AC No'].replace(" ", ""),
    AC_Name=column['AC Name'].replace(
    " ", ""),
    Rank='`' + column['Rank'] + '`',
    Party_Name=column['Party Name'].replace(
    " ", ""),
    Party_ID=column['Party ID'].replace(
    " ", ""),
    Alliance=column['Alliance'],
    Candidate_Name=column['Candidate Name'].replace(
    " ", ""),
    votes_polled=column['% votes polled'].replace(" ", "")[
    1:],
    Total_Valid_Votes=column['Total Valid Votes'].replace(" ", ""))


candidate_table = create_candidate_table.format(candidate_name=column['Candidate Name'].replace(" ", ""),
                                                party_name=column['Party Name'].replace(
    " ", ""),
    candidate_id=column['Candidate ID'].replace(
    " ", ""),
    candidate_category=column['Candidate Category'].replace(
    " ", "")
)


# execute_query(connection, retro_election)
# execute_query(connection, candidate_table)


i = 0
for x in data['names']:
    i = i
    datax = []
    for i in range(18):
        q = data['names'][i]
        final = q['Year'], q['Election Type'], q['AC No'], q['AC Name'], q['Rank'], q['Party Name'], q['Party ID'], q[
            'Alliance'], q['Candidate Name'], q['Candidate ID'], q['Candidate Category'], q['% votes polled'], q['Total Valid Votes']
        datax.append(final)
    else:
        pass


def entries(datax=datax, connection=connection):
    datax.pop(0)
    i = 0
    for j in datax:
        retro_election_entries = retro_election_query.format(
            Year=datax[i][0],
            Election_Type=datax[i][1],
            AC_No=datax[i][2],
            AC_Name=datax[i][3],
            Rank=datax[i][4],
            Party_Name=datax[i][5],
            Party_ID=datax[i][6],
            Alliance=datax[i][7],
            Candidate_Name=datax[i][8],
            votes_polled=datax[i][11],
            Total_Valid_Votes=datax[i][12])

        candidate_table_entries = candidate_table_query.format(
            Candidate_Name=datax[i][8],
            Party_name=datax[i][5],
            Candidate_ID=datax[i][9],
            Candidate_Category=datax[i][10]
        )
        i += 1

        execute_query(connection, retro_election_entries)
        execute_query(connection, candidate_table_entries)

        print('Success')
