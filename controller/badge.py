""" 
    @author Ashish patel
    @All the logic for the Badge API's is done in this section
    @since 15-09-2020
"""
from flask import request, redirect
from flask_restful import Resource
import model.badge as BadgeModel
from flask import request
import ast

class Badge(Resource):
    def get(self):
        try:
            #checking for the params in the URL
            BadgeNumber=request.args.get('badge_number', None)
            #Checking the Username and Password Provided in the request
            UserName=request.headers['UserName']
            Password=request.headers['Password']
            if UserName !='Test' or Password !='Password123':
                return "UserName or Password Incorrect", 401
            #if No Params are provided then return all the badges
            if len(request.args) ==0: 
                data=BadgeModel.BadgeAll()
                Final=[]
                #Sending data in Json Format as given in requiremnets
                for i in data['data']:
                    Final.append({
                        'badge_number':i[0],
                        'badge_status':i[1],
                        'badge_expiry_date':str(i[2])
                        })
            else:
                #If Wrong Params are given then reply with 422
                if BadgeNumber is None:
                    return "query param is not correct", 422
                #Checking if the value in Badge_number param is numeric or not
                try:
                    BadgeNumber = ast.literal_eval(BadgeNumber) 
                except:
                    return "the passed value is non numeric", 422
                if isinstance(BadgeNumber, list) is False:
                    BadgeNumber=[BadgeNumber]
                #if there are multiple numbers given as an array then checking if all the numbers are numeric or not
                if (all(isinstance(x, int) for x in BadgeNumber)) is False:
                    return "the passed value is non numeric", 422
                data=BadgeModel.BadgeNumbers(BadgeNumber)
                if len(data['data'])==0:
                    return "No Badge Number Matches", 404
                #Json format as given in requiremnt 
                Final=[]
                for i in data['data']:
                    Final.append({
                        'badge_number':i[0],
                        'badge_status':i[1],
                        'badge_expiry_date':str(i[2])
                        })
            return Final, 200
        except Exception as e:
            return str(e), 500
#This class provides all the active badges 
class BadgeActive(Resource):
    def get(self):
        try:
            #Checking the Username and Password Provided in the request
            UserName=request.headers['UserName']
            Password=request.headers['Password']
            if UserName !='Test' or Password !='Password123':
                return "UserName or Password Incorrect", 401
            data=BadgeModel.BadgeActive()
            Final=[]
            #if the output is 0 then no active badges are present
            if len(data['data'])==0:
                return "No Badges are active", 404
            #Sending data in Json Format as given in requiremnets
            for i in data['data']:
                Final.append({
                    'badge_number':i[0],
                    'badge_status':i[1],
                    'badge_expiry_date':str(i[2])
                    })
            return Final, 200
        #Except block to handle uncatched exceptions
        except Exception as e:
            return str(e), 500


        


