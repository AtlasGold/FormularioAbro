import pyodbc 

server = 'DESKTOP-JURKHLT\SQLEXPRESS'
database = 'pacientes' 
username = 'sa' 
password = 'tesT123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
