""" 
    @author Ashish patel
    @@This is the main/ driver script for the flask application 
    @since 15-09-2020
"""
from flask import Flask 
from flask_restful import Api
import os


#cx_Oracle=cx_Oracle


app = Flask(__name__) 
app.config['BaseDir']=os.getcwd()
#username and password for oracle connection to be entered here manually which were given to the candidate
app.config['Username']='*********'
app.config['Password']='*********'
api = Api(app)
#importing all the necessary libraries
import routes
import model.connection
import controller.badge as badge
import controller.department as department
import controller.job_title as job_title
import controller.employee as employee
#this section below is only required when running on windows devices
###############################################################################################
#@app.before_first_request
#def do_something_only_once():
#    import cx_Oracle
#    cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\ashis\Downloads\instantclient-basiclite-windows.x64-19.8.0.0.0dbru\instantclient_19_8")
###############################################################################################################
api.add_resource(badge.Badge, "/badges", endpoint="BadgesGetAll")
api.add_resource(badge.BadgeActive,"/badges/active", endpoint="BadgesActive")

api.add_resource(department.Departments,"/department", endpoint="DepartmentAll")

api.add_resource(job_title.JobTitle,"/job_titles", endpoint="JobTitlesAll")
api.add_resource(job_title.JobTitle,"/job_titles/<DptName>", endpoint="JobTitlesDeptName")

api.add_resource(employee.Employees,"/employees", endpoint="Employees")
api.add_resource(employee.GetActiveEmployee,"/employees/active", endpoint="EmployeesActive")

if __name__ == "__main__":
  app.run(debug=True)