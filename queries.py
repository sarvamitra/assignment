create_retro_election_table = '''CREATE TABLE assignment.retro_election ({Year} INT NOT NULL,{Election_Type} VARCHAR(40) NOT NULL,{AC_No} VARCHAR(40) NOT NULL,{AC_Name} VARCHAR(40) NOT NULL,{Rank} VARCHAR(40) NOT NULL,{Party_Name} VARCHAR(40) NOT NULL,{Party_ID} VARCHAR(40) NULL,{Alliance} VARCHAR(40) NOT NULL,{Candidate_Name} VARCHAR(40) PRIMARY KEY,{votes_polled} VARCHAR(40) NOT NULL,{Total_Valid_Votes} VARCHAR(40) NOT NULL);'''

create_candidate_table = '''CREATE TABLE assignment.candidate ({candidate_name} VARCHAR(40) PRIMARY KEY,{party_name} VARCHAR(40) NOT NULL, {candidate_id} VARCHAR(40) NULL,{candidate_category} VARCHAR(40) NULL);'''

retro_election_query = '''INSERT INTO assignment.retro_election VALUES ('{Year}', '{Election_Type}','{AC_No}', '{AC_Name}','{Rank}', '{Party_Name}','{Party_ID}', '{Alliance}','{Candidate_Name}', '{votes_polled}','{Total_Valid_Votes}');'''

candidate_table_query = '''INSERT INTO assignment.candidate VALUES ('{Candidate_Name}', '{Party_name}','{Candidate_ID}','{Candidate_Category}');'''
