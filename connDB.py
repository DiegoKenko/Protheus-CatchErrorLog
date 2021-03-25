import pyodbc 

def Conecta():
     server = '10.0.0.1' 
     database = 'DATABASE' 
     username = 'logreader' 
     password = '123456' 
     cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
     return cnxn
