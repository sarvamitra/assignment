from flask import Flask, render_template, request
import csv
import json
from db_connect import create_server_connection, create_database, execute_query, retro_election, candidate_table, entries

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':

        x = request.form['csvfile']
        data = []
        with open(x) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        # data = pd.DataFrame(data)
        print(data)
        data1 = data
        data2 = {'names': []}
        print(data2)
        for row in data1:
            print(row)
            data2['names'].append({'Year': row[0], 'Election Type': row[1],
                                   'AC No': row[2], 'AC Name': row[3],
                                   'Rank': row[4], 'Party Name': row[5],
                                   'Party ID': row[6], 'Alliance': row[7],
                                   'Candidate Name': row[8], 'Candidate ID': row[9],
                                   'Candidate Category': row[10], '% votes polled': row[11],
                                   'Total Valid Votes': row[12]
                                   })
        print(data2)

        with open('data.json', 'w') as outfile:
            json.dump(data2, outfile, indent=4)

        connection = create_server_connection(
            "localhost", "root", "MYSQLlaptop@757")

        create_database_query = "CREATE DATABASE ASSIGNMENT"
        create_database(connection, create_database_query)

        execute_query(connection, retro_election)
        execute_query(connection, candidate_table)

        entries()

        return render_template('data.html', data=data2['names'])


if __name__ == '__main__':
    app.run(debug=True)
