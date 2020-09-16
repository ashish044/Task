""" 
    @author Ashish patel
    @All the logic for the Job tilte API's is done in this section
    @since 15-09-2020
"""
from flask import request, redirect
from flask_restful import Resource
import model.Job_title as JobTitleModel
import model.department as DepartmentModel
from flask import request
import base64

class JobTitle(Resource):
    def get(self,DptName=None):
        try:
            #Checking the Username and Password Provided in the request
            UserName=request.headers['UserName']
            Password=request.headers['Password']
            if UserName !='Test' or Password !='Password123':
                return "UserName or Password Incorrect", 401
            #checking if department name given in URL, if no then return all the job titles
            if DptName==None:
                data=JobTitleModel.JobTitleAll()
                Final=[]
                for i in data['data']:
            #Json Format as given in requirement
                    Final.append({
                        'job_title_code':i[0],
                        'job_title_name':i[1],
                        'department_name':i[3]
                        })
            else:
                #if department name is given in url then converting it back form base64 encoding
                DptName = base64.b64decode(DptName)
                DptName=(DptName.decode("utf-8"))
                #checking if department name is valid or not
                data=DepartmentModel.DptNameAll([DptName])
                if len(data['data'])==0:
                    return "The Department Does Not Exists", 422
                data=JobTitleModel.JobTitleDept(DptName)
                Final=[]
                #checking if job title for the department is present or not
                if len(data['data'])==0:
                    return "No Job Tile Matches To deprtment name", 404
                
                for i in data['data']:
                    #Json Format as given in requiremnt
                    Final.append({
                        'job_title_code':i[0],
                        'job_title_name':i[1],
                        'department_name':DptName
                        })


            return Final, 200
        #Except Block to handle the unhandeled errors
        except Exception as e:
            return str(e), 500