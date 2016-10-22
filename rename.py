import os
import sys
 
path = "D:\emojis"
 
for (path,dirs,files) in os.walk(path):
    for filename in files:
        newname = "emoji_"+filename
        os.rename(path+"\\"+filename , "D:\\emojis"+"\\"+newname)