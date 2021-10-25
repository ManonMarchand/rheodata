import sqlite3 
import yaml
import glob

# Connect to database
connection = sqlite3.connect('litterature_data.db')

# Create a cursor
c = connection.cursor()

# Create a table
# note that sql commands need to be capitalised
# datatypes are : NULL INTEGER REAL TEXT BLOB
# BLOB is everything else, for example images
#c.execute("""CREATE TABLE papers (
#    title text,
#    url text,
#    paper_id text
#    )""")

# Insert values in the table
# the paper id is the one given by google scholar for the bibtext file
#connection.execute("""INSERT INTO papers 
#                    VALUES (
#                    'Scaling of flow curves Comparison between experiments and simulations', 
#                    'https://www.sciencedirect.com/science/article/pii/S0377025718301198',
#                    'dekker2018scaling'
#                    )
#                    """)

# Insert a lot of values at once
#papers_info = yaml.safe_load(open(glob.glob('flow_curve*.yml')[0]))
#list_paper_database = []
#for key in papers_info.keys():
#    list_paper_database += [(papers_info[key]['title'], papers_info[key]['url'], key)]

#connection.executemany("INSERT INTO papers VALUES (?,?,?)", list_paper_database)

# Query the database
c.execute("SELECT * FROM papers")
#print(c.fetchone())
#print(c.fetchmany(3)) # get the first 3 elements
paper = c.fetchall()

for p in paper :
    print(p[0])

# Then it needs to be commited to the database
connection.commit()

# Close the connection
# For good practice
connection.close()