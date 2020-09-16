""" 
    @author Ashish patel
    @@All the sql querry for Department API's is done in this section
    @since 15-09-2020
"""
import model.connection as con
def DepartmentAll():
    sql ="SELECT * from DEPARTMENT"
    return con.connection(sql, None)
def DptNameAll(DptName):
    sql="SELECT * from DEPARTMENT where DEPARTMENT_NAME like :DptName"
    return con.connection(sql, DptName)

