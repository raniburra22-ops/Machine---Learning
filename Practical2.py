import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "-----",database="SampleDB")

# Creating the cursor object
cur = myconn.cursor()

# Executing the query
cur.execute("SELECT * FROM student")

# Fetching the rows from the cursor object
result = cur.fetchall()

# Printing the result
print("Student Details are :")

for x in result:
    print(x);

# Close the connection
cur.close
myconn.close()