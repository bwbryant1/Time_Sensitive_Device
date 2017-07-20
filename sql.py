#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
start_score = "0000,,1,,0,11,,,100000000jhjk"
start_time = "," + str(int(time.time()))
a="bmo"
b="7120."
con = mdb.connect(b[1]+b[2]+b[0]+b[4]+b[3]+b[4]+b[3]+b[4]+b[1], 'testuser', 'test623',a[0]+a[2]+a[1]+a[0]);

with con:
    
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS teams")
    cur.execute("CREATE TABLE teams(Id INT PRIMARY KEY AUTO_INCREMENT, Team VARCHAR(50),Score INT,Time INT,Armed INT)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Bowser'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Conker'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Funky Kong'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Glados'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Kirby'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('R.O.B.'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Shadow'" +start_score[15:20] + start_time+ ",1)")
    cur.execute("INSERT INTO teams(Team,Score,Time,Armed) VALUES('Shodan'" +start_score[15:20] + start_time+ ",1)")
