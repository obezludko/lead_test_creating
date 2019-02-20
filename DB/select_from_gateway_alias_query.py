import psycopg2
from DB import connection

connection = psycopg2.connect(user = connection.user,
                              password = connection.password,
                              host = connection.host,
                              port = connection.port,
                              database = connection.database)

cursor = connection.cursor()
print(connection.get_dsn_parameters(), "\n")

cursor.execute("SELECT version();")
version = cursor.fetchone()
print("You are connected to - ", version, "\n")

gateway_aliases_query = 'select * FROM gateway_aliases WHERE id between 32 and 35;'
cursor.execute(gateway_aliases_query)

alias_row = cursor.fetchall()


# row_position = 0
# while row_position != len(alias_row):
#     print(alias_row[row_position])
#     row_position += 1

# for row in alias_row:
#     print("Id = ",row[0], )
#     print("alias = ", row[1])
#     print("gateway_id = ", row[2],"\n")

print (alias_row,"\n")

first_row_response = list(alias_row[0])
print(first_row_response, type(first_row_response))

alias = first_row_response[1]

def select_from(self,column = '*',table):
    self.table = table
    self.column = column
################################################# ///////ДОПИСАТЬ!!!!