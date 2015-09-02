#!/usr/bin/python
#coding:utf-8

import os
import sys
import os.path
import zipfile
import shutil

#ipa文件夹的绝对路径,这里需要指定你ipa所在的绝对路径
root = "/Users/xiaohongjun/Documents/iPhone"



pkgcmd = '/usr/bin/xcrun -sdk iphoneos PackageApplication -v '
srcapp = '/Users/xiaohongjun/Documents/Push/Payload/Meilishuo.app'

#--embed 需要指定你存放配置文件的绝对路径
profile = ' --sign "iPhone Distribution: Meili Works(Beijing)Limited" --embed "/Users/xiaohongjun/Documents/WildCard_InHouse_New.mobileprovision"'

#folder 依次遍历得到的文件夹
for folder,subfolder,filename in os.walk(root):
	fileList = os.listdir(folder)
	for eachFile in fileList:
		ext = os.path.splitext(eachFile)[-1]
		if ext.endswith('.ipa'):
			ipafullpath = os.path.join(folder, eachFile)
			print ipafullpath
			#解压
			cmd = 'unzip ' + ipafullpath + ' -d ' + folder
			os.system(cmd)
			
			#删除ipa文件
			appFolderPath = os.path.join(folder, 'Payload/')
			appName = os.listdir(appFolderPath)[0]
			appFullPath = os.path.join(appFolderPath, appName)
			
			#重签名
			appToIpa = pkgcmd + appFullPath + ' -o ' + ipafullpath + profile
			
			os.system(appToIpa)
			
			payloadPath = os.path.join(folder, 'Payload/');
			if os.path.exists(payloadPath):
				shutil.rmtree(payloadPath)
	
		
		

			
	
			
			
			
		