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


#sundir 是相对与ipa根目录的子目录
def resignipa(srcipa,sundir):
	rootdir = ''
	#在rootdir下
	if '' == sundir:
		rootdir = root
	else:
		rootdir = os.path.join(root, sundir)
	if not os.path.exists(rootdir):
		print '包含ipa的根目录没找到，你先看看你的根目录是不是对的。谢谢'
	ipaFullPath = os.path.join(rootdir, srcipa)
	print ipaFullPath
	if not os.path.exists(ipaFullPath):
		print 'ipa的绝对路径有误，你先看看你的根目录是不是对的。谢谢'
	#删除当前路径中的Payload文件夹，因为解压ipa时会产生一个payload文件夹
	payloadPath = os.path.join(rootdir, 'Payload/');
	if os.path.exists(payloadPath):
		shutil.rmtree(payloadPath)
	#将ipa解压成payload文件夹
	cmd = 'unzip ' + ipaFullPath + ' -d ' + rootdir
	os.system(cmd)
	#解压完成之后删除原来的ipa文件
	os.remove(ipaFullPath)
	#解压完成后的app的全路径
	appname = os.listdir(payloadPath)[0]
	appFullPath = os.path.join(payloadPath, appname)
	
	#print appFullPath
	appToIpa = pkgcmd + appFullPath + ' -o ' + ipaFullPath + profile
	
	print appToIpa
	
	os.system(appToIpa)
	#最后一次解压出来的payload也需要删除掉
	if os.path.exists(payloadPath):
		shutil.rmtree(payloadPath)
	
	
#folder 依次遍历得到的文件夹
for folder,subfolder,filename in os.walk(root):
	#print 'folder ' + folder
	#print  subfolder
	#print filename
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
	
		
		

			
	
			
			
			
		