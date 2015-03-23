import time,os

try:
	today=time.strftime("%y%m%d")
	now=time.strftime("%H%M%S")
	confFileName  = "C:\\MOS\\config\\formatData.txt"
	confFile = file(confFileName, 'r')
	confList = confFile.readlines()
	tc = confList[0].split("\n")[0]
	long = confList[1].split("\n")[0]
	lat = confList[2].split("\n")[0]
	pic = confList[3].split("\n")[0]
	confFile.close()
	reFileName = "C:\\MOS\\report\\report.txt" 
	reFile=file(reFileName,'a')
	re=""
	try:
		find(pic)
		re = "#"+tc+"||"+today+"||" +now+"||"+long+"|| "+lat+"|| "+pic+"||------ pass\n"
	except:
		re = "#"+tc+"||"+today+"||"+now+"||"+long+"|| "+lat+"|| "+pic+"||------ fail\n"	
	finally:
		reFile.write(re)
		reFile.close()
except Exception,e:
	print e
closeApp("Sikuli")