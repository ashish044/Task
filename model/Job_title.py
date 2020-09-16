""" 
    @author Ashish patel
    @@All the sql querry for Employee API's is done in this section
    @since 15-09-2020
"""
import model.connection as con
#all jobtitle
def JobTitleAll():
    sql ="SELECT a.*, b.DEPARTMENT_NAME \
            FROM JOB_TITLE a \
            INNER JOIN  DEPARTMENT b \
            ON a.DEPARTMENT_CODE=b.DEPARTMENT_CODE "
    return con.connection(sql, None)
#All Job Titles related to Department
def JobTitleDept(DptName):
    sql="SELECT * from JOB_TITLE \
        WHERE DEPARTMENT_CODE \
        IN ( SELECT DEPARTMENT_CODE \
            FROM DEPARTMENT \
            WHERE DEPARTMENT_NAME like :DptName)"
    return con.connection(sql,[DptName])
