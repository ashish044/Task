""" 
    @author Ashish patel
    @All the logic for the Department API's is done in this section
    @since 15-09-2020
"""
from flask import request, redirect
from flask_restful import Resource
import model.department as DepartmentModel
from flask import request

class Departments(Resource):
    def get(self):
        try:
            #Checking the Username and Password Provided in the request
            UserName=request.headers['UserName']
            Password=request.headers['Password']
            if UserName !='Test' or Password !='Password123':
                return "UserName or Password Incorrect", 401
            data=DepartmentModel.DepartmentAll()
            #Json format as given in requirement
            Final=[]
            for i in data['data']:
                Final.append({
                    'department_code':i[0],
                    'department_name':i[1]
                    })
            return Final, 200
        #except Block to catch the unhandleled exceptions
        except Exception as e:
            return str(e), 500