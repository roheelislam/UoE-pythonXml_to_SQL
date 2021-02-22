from xml.dom import minidom

#   Week 3 programming exercise - stored procedure call
#    - insert project

# odbc driver
import pyodbc

# Connect to HR database using Windows authentication
cnxn = pyodbc.connect('Trusted_Connection=yes',
                      driver='{ODBC Driver 17 for SQL Server}', server='.\SQLEXPRESS', database='MDB')
# Declare the cursor:
cursor = cnxn.cursor()

# read xml line by line


# # Create 5 projects
# SQLCommand = ("EXEC dbo.createManufacturerRecord @Name = 'ali', @City = 'lahore',  @Country = 'Pakistan', @Established = '1937-08-28T00:00:00' ")
# cnxn.execute(SQLCommand)
# cnxn.commit()


# parse an xml file by name
# mydoc = minidom.parse("books.xml")


doc = minidom.parse("XMLsampleinvoice2.xml")

name = doc.getElementsByTagName("Manufacturers_Table")[0]
print(name.firstChild.data)

Manufacturers = doc.getElementsByTagName("Manufacturer_row")
for Manufacturer in Manufacturers:
    Name = Manufacturer.getElementsByTagName("Name")[0]
    Established = Manufacturer.getElementsByTagName("Established")[0]
    City = Manufacturer.getElementsByTagName("City")[0]
    Country = Manufacturer.getElementsByTagName("Country")[0]
    # print("Name:%s,\n Established:%s,\n City:%s,\n Country:%s \n\n" %
    #       (Name.firstChild.data, Established.firstChild.data, City.firstChild.data, Country.firstChild.data))

    SQLCommand = ("EXEC dbo.createManufacturerRecord \
    @Name = '" + str(Name.firstChild.data)+"',\
    @City = '" + str(City.firstChild.data)+"',\
    @Country = '" + str(Country.firstChild.data)+"',\
    @Established = '" + str(Established.firstChild.data)+"' ")
    cnxn.execute(SQLCommand)
    cnxn.commit()

# SQLCommand = ("EXEC dbo.insProject 'Third Project', 15000.00")
# cnxn.execute(SQLCommand)
# cnxn.commit()

# SQLCommand = ("EXEC dbo.insProject 'Fourth Project', 150.00")
# cnxn.execute(SQLCommand)
# cnxn.commit()

# SQLCommand = ("EXEC dbo.insProject 'Fifth Project', 12.00")
# cnxn.execute(SQLCommand)
# cnxn.commit()

# SQLCommand = ("EXEC dbo.insProject 'Sixth Project', 23.00")
# cnxn.execute(SQLCommand)
# cnxn.commit()

# #Declare the cursor:
# cursor = cnxn.cursor()
# #Execute SQL:
# cursor.execute("select * from Project")
# #Show data returned
# rows = cursor.fetchall()
# for row in rows:
# 	print(row)


cnxn.close()
