import MySQLdb as mdb
import time

def make_sql():

    start_score = "0000,,1,,0,11,,,100000000jhjk"
    start_time = "," + str(int(time.time()))
    a="bmo"
    b="7120."
    con = mdb.connect(b[1]+b[2]+b[0]+b[4]+b[3]+b[4]+b[3]+b[4]+b[1], 'testuser', 'test623',a[0]+a[2]+a[1]+a[0]);
    return con
"""
single callable
"""
def set_score(con,msg):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Score=10000")
    msg = "\nYou just: Added 10000 to all of the teams"
    return msg

def set_score_minus(con,msg):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Score=Score-1000")
    msg = "\n You just: subtracted 1000 from all teams"
    return msg
def take_thirty_minutes(con,msg):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Time=Time-1800")
    msg = "\n You just: subtracted 30 minutes from everyone else"
    return msg    
"""
multi call start, single end
"""

def test(con):
    pass
    
def reset(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Score=0")
        cur.execute("UPDATE Teams SET Armed=1")    
#-------------------------------------------------------
def disarm_one(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=1")    
def disarm_two(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=2")
def disarm_three(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=3")    
def disarm_four(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=4")    
def disarm_five(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=5")    
def disarm_six(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=6")    
def disarm_seven(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=7")    
def disarm_eight(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=0 where Id=8")    
#-----------------------------------------------------------
def arm_one(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=1")    
def arm_two(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=2")
def arm_three(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=3")    
def arm_four(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=4")    
def arm_five(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=5")    
def arm_six(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=6")    
def arm_seven(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=7")    
def arm_eight(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=1 where Id=8")    
#-----------------------------------------------------------
def blow_one(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=1")    
def blow_two(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=2")
def blow_three(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=3")    
def blow_four(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=4")    
def blow_five(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=5")    
def blow_six(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=6")    
def blow_seven(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=7")    
def blow_eight(con):
    with con:
    
        cur = con.cursor()
        cur.execute("UPDATE Teams SET Armed=2 where Id=8")
        
#-----------------------------------------------------------        
def make_dict():
    a = []
    multi_callable = {\
        'test':test,\
        'reset':reset,\
        'disarm one':disarm_one,\
        'disarm two':disarm_two,\
        'disarm three':disarm_three,\
        'disarm four':disarm_four,\
        'disarm five':disarm_five,\
        'disarm six':disarm_six,\
        'disarm seven':disarm_seven,\
        'disarm eight':disarm_eight,\
        'arm one':arm_one,\
        'arm two':arm_two,\
        'arm three':arm_three,\
        'arm four':arm_four,\
        'arm five':arm_five,\
        'arm six':arm_six,\
        'arm seven':arm_seven,\
        'arm eight':arm_eight,\
        'blow one':blow_one,\
        'blow two':blow_two,\
        'blow three':blow_three,\
        'blow four':blow_four,\
        'blow five':blow_five,\
        'blow six':blow_six,\
        'blow seven':blow_seven,\
        'blow eight':blow_eight}      
        
    with open('sce.txt','r') as inf:
        single_callable = eval(inf.read())
    
    a.append(multi_callable)
    a.append(single_callable)
    
    return a

