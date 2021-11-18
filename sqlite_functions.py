import sqlite3
import yaml
import glob
import numpy as np
from pathlib import Path


# Query the database and return all records
def show_all():
    # Connect to database
    connection = sqlite3.connect('litterature_data.db')
    # Create a cursor
    c = connection.cursor()
    # Query the database
    c.execute("SELECT rowid, * FROM papers")
    items = c.fetchall()
    # Print them all
    for item in items:
        print(item)
    # Then it needs to be commited to the database
    connection.commit()
    # Close the connection for good practice
    connection.close()

# Add a record to our database
def add_one(title, url, paper_id, year, author):
    # Connect to database
    connection = sqlite3.connect('litterature_data.db')
    # Create a cursor
    c = connection.cursor()
    c.execute("INSERT INTO papers VALUES (?,?,?)", (title, url, paper_id, year, author))
    # Then it needs to be commited to the database
    connection.commit()
    # Close the connection for good practice
    connection.close()

# Delete one record
def delete_one(rowid):
    # Connect to database
    connection = sqlite3.connect('litterature_data.db')
    # Create a cursor
    c = connection.cursor()
    c.execute("DELETE from papers WHERE rowid= (?)", str(rowid))
    # Then it needs to be commited to the database
    connection.commit()
    # Close the connection for good practice
    connection.close()

# Add many record to a table
# TODO : add a length of list option
def add_many(list):
    # Connect to database
    connection = sqlite3.connect('litterature_data.db')
    # Create a cursor
    c = connection.cursor()
    c.executemany("INSERT INTO papers VALUES (?,?,?,?,?)", (list))
    # Then it needs to be commited to the database
    connection.commit()
    # Close the connection for good practice
    connection.close()
    
def query_column(table_name, column_name):
    """Queries a column from a table of litterature_data.db
    
    Parameters
    ----------
    table_name  : str
    column_name : str
    
    Returns
    ----------
    A list containing the column
    """
    table_name = str(table_name)
    column_name = str(column_name)
    # Connect to database
    connection = sqlite3.connect('litterature_data.db')
    # Create a cursor
    c = connection.cursor()
    # Select the column
    c.execute(f"SELECT {column_name} FROM {table_name}")
    column = c.fetchall()
    array = []
    for id in column:
        array += [id[0]]
    return array


def get_column_names(table_name):
    """ Queries the names of the columns of a table 

    Args:
        table_name ([type]): [description]
    """




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
#papers_info = yaml.safe_load(open(glob.glob('papers*.yml')[0]))
#list_paper_database = []
#for key in papers_info.keys():
#    paper = papers_info[key]
#    list_paper_database += [(paper['title'], paper['url'], key, 
#                            paper['year'], paper['author']
#                            )]

#print(list_paper_database)

#c.executemany("INSERT INTO papers VALUES (?,?,?,?,?)", list_paper_database)

# Query the database



# Different ways to search for specific things in the databases
#c.execute("SELECT rowid, * FROM papers")
#c.execute("SELECT * FROM papers WHERE paper_id = 'paredes2013rheology'")
#c.execute("SELECT * FROM papers WHERE paper_id LIKE '%2018%'")
#print(c.fetchone())
#print(c.fetchmany(3)) # get the first 3 elements


#Update records

#Change one thing manually
#c.execute("""UPDATE papers SET paper_id = 'dumb_id'
#             WHERE title LIKE '%rheology%'
#          """)

# Delete records
#c.execute("DELETE from papers WHERE rowid=1")

# Ordering records
# If chosing a string the obtained order will be alphabetical
#c.execute("SELECT rowid, * FROM papers ORDER BY rowid DESC")

# Using AND / OR
#c.execute("SELECT rowid, * FROM papers WHERE rowid=4 AND title LIKE '%rheology%'")

# Limiting the results to a certain number of results
#c.execute("SELECT rowid, * FROM papers LIMIT 2")

# Delete an entire table 
#c.execute("DROP TABLE litterature_data")

# Print the all table
#c.execute("SELECT rowid, * FROM papers")

#papers = c.fetchall()

#print(papers)

#for paper in papers:
#    print(paper)


# Then it needs to be commited to the database
#connection.commit()

# Close the connection for good practice
#connection.close()