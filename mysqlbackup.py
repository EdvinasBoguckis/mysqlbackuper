import os
import sys
import time
import datetime
import pipes
import configparser

runparam = sys.argv[1]

def backuper (db_host, db_name, db_user, db_pass, backup_path, arc_arg, hide_pass):
    backupdate = time.strftime('%Y%m%d-%H%M%S')
    fullpath = backup_path + '/' + backupdate
    

def parseconfig(filelocation):
    localconf = configparser.ConfigParser()
    localconf.read(filelocation)
    db_host = localconf['backuper']['db_host']
    db_name = localconf['backuper']['db_name']
    db_user = localconf['backuper']['db_user']
    db_pass = localconf['backuper']['db_pass']
    backup_path = localconf['backuper']['path']
    arc_arg = localconf['backuper']['archive']
    hide_pass = localconf['extras']['hide_pass']
    backuper()
    

def initialize():
    if (runparam == "fromconfig"):
        location = sys.argv[2]
        parseconfig(location)
    elif (runparam == "singlerun"):
        db_host = sys.argv[2]
        db_name = sys.argv[3]
        db_user = sys.argv[4]
        db_pass = sys.argv[5]
        backup_path = sys.argv[6]
        arc_arg = sys.argv[7]
        hide_pass = False
        backuper(db_host, db_name, db_user, db_pass, backup_path, arc_arg, hide_pass)
    elif (runparam == "help"):
        showhelp()
    elif (runparam == "info"):
        printinfo()
    else:
        print ("No required arguments provided! Use help parameter for help. \nExiting..")
        exit(1)







app_version = 1.2
app_branch = "stage"
isdev = True
initialize()
