""" 
    @author Ashish patel
    @All the logic for the Employee API's is done in this section
    @since 15-09-2020
"""
from flask import request, redirect
from flask_restful import Resource
import model.employee as EmployeeModel
import model.department as DepartmentModel
from flask import request
import requests

class Employees(Resource):
    def get(self):
        try:
            #checking for the parmas 
            DeptName=request.args.get('department_name', None)
            #getting UserName and Password from the header of the request
            UserName=request.headers['UserName']
            Password=request.headers['Password']
            #checking Username and Password
            if UserName !='Test' or Password !='Password123':
                return "UserName or Password Incorrect", 401
            #If No Params were given then return all Employees
            if len(request.args) ==0:
                data=EmployeeModel.EmployeeAll()
            else:
            #checking if the correct Params were given or not
                if (DeptName is None):
                    return "the query param is incorrect", 422
                a=[]
                a.append(DeptName)
                data=DepartmentModel.DptNameAll(a)
            #checking if department given is Correct or Not
                if len(data['data'])==0:
                    return "The Department Does Not Exists", 422
                data=EmployeeModel.DeptNameEmployee(a)
                if (len(data['data'])==0):
                    return "No Employees present for the deprtment name", 404
            #final results to put in jason format as given in the requirement
            Final=[]
            for i in data['data']:
                Final.append({
                    'id':i[0],
                    'firstname':i[1],
                    'lastname':i[2],
                    'badge_number':i[3],
                    'country':Employees.GetCodes(i[4]),
                    'job_title':i[9],
                    'department':i[8],
                    'start_date':str(i[6]),
                    'leave_date':str(i[7])


                    })
            return Final, 200
        #Except Block to catch all the server errors
        except Exception as e:
            return str(e), 500
    #this method takes the country code and returns the complete name of the company
    def GetCodes(code):
        url = "https://restcountries.eu/rest/v2/alpha/"+code
        response = requests.request("GET", url)
        return response.json()["name"]

#This class gives the active employee as the conditions given in the requirements
class GetActiveEmployee(Resource):
    def get(Self):
        try:
            #checking username and password from the headerof the request
            UserName=request.headers['UserName']
            Password=request.headers['Password']
            if UserName !='Test' or Password !='Password123':
                return "UserName or Password Incorrect", 401
            data=EmployeeModel.ActiveEmployee()
            Final=[]
            #final results to put in jason format as given in the requirement
            for i in data['data']:
                Final.append({
                    'id':i[0],
                    'firstname':i[1],
                    'lastname':i[2],
                    'badge_number':i[3],
                    'country':Employees.GetCodes(i[4]),
                    'job_title':i[9],
                    'department':i[8],
                    'start_date':str(i[6]),
                    'leave_date':str(i[7])


                    })
            return Final, 200
        #Except Block to catch all the server errors
        except Exception as e:
            return str(e), 500

