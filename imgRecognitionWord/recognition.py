# -*- coding: utf-8 -*-
# @Author: lt
# @Date:   2022-09-01 09:17:19
# @Last Modified by:   lt
# @Last Modified time: 2022-09-07 16:21:36
# 导入模块
import easyocr
import os
import time
# 图片路径
imagePath = 'E:\pythonProject\imgRecognitionWord\img'

txtpath='E:\pythonProject\imgRecognitionWord\datatxt'

#生成txt文件
def createText(msg):

	dataTime = int(time.time())

	#生成路径
	#可换成与图片文件一致的文件名（待优化）
	full_path = txtpath+"\\"+str(dataTime) + '.txt'  # 也可以创建一个.doc的word文档

	print(full_path)
	file = open(full_path, 'w' ,  encoding = 'ANSI')

	file.write(msg)   #msg内容


#图片识别，返回字符串
#path 图片全路径
def discernImg(path):
	# 创建ocr的reader对象，识别中英文
	ocr = easyocr.Reader(['ch_sim', 'en'],gpu=False)
	# 识别图片文字
	content = ocr.readtext(path,detail=0)

	msg="";

	for x in content:

	    print(x,end=' ')
	    msg+=x

	createText(msg)


#获取文件夹虾所有文件路径
def getImeger(path):
	
	imgList=os.listdir(path)

	#还需要写个文件过滤…………
	return imgList



#开始识别	
def startRecognition():
	#获取文件夹下所有需要识别的图片
	imgList = getImeger(imagePath);
	#循环识别并且生成文件内容
	for x in imgList:
		path=imagePath+"\\"+x
		print("---------------------"+path)
		discernImg(path)

startRecognition()