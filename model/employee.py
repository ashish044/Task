""" 
    @author Ashish patel
    @@All the sql querry for Employee API's is done in this section
    @since 15-09-2020
"""
import model.connection as con
#ALL employee
def EmployeeAll():
    sql ="  SELECT a.* ,b.DEPARTMENT_NAME as DEPTNAME, c.JOB_TITLE_NAME  as JOB_TITLE_NAME\
            FROM Employee a \
            INNER JOIN JOB_TITLE c \
              on a.JOB_TITLE_CODE=c.JOB_TITLE_CODE\
            INNER JOIN DEPARTMENT b   \
              on b.DEPARTMENT_CODE=c.DEPARTMENT_CODE"            
    return con.connection(sql, None)
#Active employee with leave date null or less than sysdate
def ActiveEmployee():
    sql="  SELECT a.* ,b.DEPARTMENT_NAME as DEPTNAME, c.JOB_TITLE_NAME  as JOB_TITLE_NAME\
            FROM Employee a \
            INNER JOIN JOB_TITLE c \
              on a.JOB_TITLE_CODE=c.JOB_TITLE_CODE\
            INNER JOIN DEPARTMENT b   \
              on b.DEPARTMENT_CODE=c.DEPARTMENT_CODE\
            WHERE a.leave_date is Null \
            OR a.leave_date < trunc(sysdate)  " 
    return con.connection(sql, None)
#all employee working for that department
def DeptNameEmployee(DeptName):
    sql="  SELECT a.* ,b.DEPARTMENT_NAME as DEPTNAME, c.JOB_TITLE_NAME  as JOB_TITLE_NAME\
            FROM Employee a \
            INNER JOIN JOB_TITLE c \
              on a.JOB_TITLE_CODE=c.JOB_TITLE_CODE\
            INNER JOIN DEPARTMENT b   \
              on b.DEPARTMENT_CODE=c.DEPARTMENT_CODE\
            WHERE b.DEPARTMENT_NAME like :DeptName  " 
    print((DeptName))
    return con.connection(sql,DeptName)
