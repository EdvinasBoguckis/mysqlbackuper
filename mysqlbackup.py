DB_HOST = sys.argv[1]
DB_NAME = sys.argv[2]
DB_USER = sys.argv[3]
DB_USER_PASSWORD = sys.argv[4]
BACKUP_PATH = sys.argv[5]
print ("============================================================================")
print ("Using current settings: ")
print ("Database Host: " + DB_HOST)
print ("Database Name: " + DB_NAME)
print ("Database User: " + DB_USER)
print ("Database User Password: " + DB_USER_PASSWORD)
print ("Backup directory: " + BACKUP_PATH)
DATETIME = time.strftime('%Y%m%d-%H%M%S')
FULLBACKUPPATH = BACKUP_PATH + '/' + DATETIME
print ("Full Path: " + FULLBACKUPPATH)
print ("============================================================================")

try:
    print ("Checking if root backup folder exists...")
    os.stat(BACKUP_PATH)
except:
    try:
        print ("Root backup folder does not exist... creating...")
        os.mkdir(BACKUP_PATH)
    except:
        print ("Folder already exists, skipping")
os.mkdir(FULLBACKUPPATH)
print ("Creating full backup folder")

db = DB_NAME
dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(FULLBACKUPPATH) + "/" + db + ".sql"
os.system(dumpcmd)
gzipcmd = "gzip " + pipes.quote(FULLBACKUPPATH) + "/" + db + ".sql"
os.system(gzipcmd)

print ("============================================================================")
print ("Backup script completed")
print ("Backup has been created in '" + FULLBACKUPPATH + "' directory")
