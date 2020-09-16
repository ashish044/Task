""" 
    @author Ashish patel
    @All the sql querry for Badge API's is done in this section
    @since 15-09-2020
"""
import model.connection as con
def BadgeAll():
    sql ="SELECT * from BADGE"
    return con.connection(sql, None)
#all the badges where status is active and expiry date is greater than sysdate
def BadgeActive():
    sql="SELECT * from BADGE\
         WHERE BADGE_STATUS=:status \
         AND BADGE_EXPIRY_DATE > trunc(sysdate)"
    return con.connection(sql,['Active'])
def BadgeNumbers(badge):
    query = """SELECT * FROM BADGE where badge_number in ('{}') """.format("','".join(map(str, badge)))
    return con.connection(query,None)



