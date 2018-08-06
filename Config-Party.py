import sys,os,csv,paramiko,getpass,time, datetime

#Creating Arrays to compare, and some variables
configArray = []
fileArray = []
dirArray = []
hostname = '80.111.55.168'
user = raw_input("Whats your username? ")
passw = getpass.getpass()
port = 2346

i = 1
x = 0
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

#Create an array - In which we'll get the contents of the "config" Folder. All Configs files to be placed in here.
path = "./Configs"
backupPath = "./backups"
arr = os.listdir(path)
for file in arr:
	configArray.append(file)

#Compare this array to the list we want to configure. 
with open('config-list.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		fileArray.append(row['package'])
		dirArray.append(row['location'])
		t = len(dirArray)

		

#Sort and compare the two arrays - Continue if all is fine, Stop and print differences.
configArray.sort()
fileArray.sort()


print configArray
print fileArray


if configArray==fileArray:
	#p = subprocess.Popen(['scp','./Configs','germanshep@server:~/test'])
	#sts = os.waitpid(p.pid, 0)
	print "Something awful"	
	while True:
		print "Trying to connect to %s(%i/5)" % (hostname, i)
	
		try:
			ssh = paramiko.SSHClient()
        		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       			ssh.connect(hostname,port=2346,username=user,password=passw)
			sftp = ssh.open_sftp()
			while x <= t:
				remoteDir = dirArray[x] 
				filename = fileArray[x]
				backupPathFile = str(backupPath + "/" + filename + st )
				remotePath =  str(remoteDir + filename)
				print remotePath + ' >>> ' + backupPathFile
				sftp.get(remotePath,backupPathFile)
				ftp_client.close()
			print "Connected to %s" % hostname
			break
		except paramiko.AuthenticationException:
			print "Failed Auth on %s" % hostname
			sysexit(1)
		except:
			print " Auth failed to %s" % hostname
			i += 1
			time.sleep(2)
	
		if i == 5:
			print "could not connect, Im a failure, going to give up ;-;"
			sys.exit(1)



	# Disconnect from the host
	print "Command done, closing SSH connection"
	ssh.close()


 	
else:
	print "Theres a difference in whats in the folder, and in the config list: %s" % list(set(fileArray) - set(configArray))

