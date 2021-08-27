import pyodbc

server = "."
database = "database"
username = "user"
password = "pw"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

sql = """
SELECT TOP (10) [Id], [Name] FROM [SoluAppData].[dbo].[Users]
""" 
cursor.execute(sql) 

result = []
for res in cursor:
    result.append(res)

print('data count', len(result))
print(result)

# data = [[row[0], row[1]] for row in cursor]
# print(list(data)[:20])
