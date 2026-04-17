import os
import shutil
source="C:/Users/rites/Downloads"
destination="C:/Users/rites/Downloads/test"
list=os.listdir(source)
print(list)
for fileName in list:
    name,extension=os.path.splitext(fileName)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in [".png",".jpg",".jpeg",".gif",".jfif",".webp",".html",".htm"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"imagefiles"
        path3=destination+"/"+"imagefiles"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
    elif extension in [".pdf",".PDF"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"pdf_files"
        path3=destination+"/"+"pdf_files"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
    elif extension in [".docx",".xlsx"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"DOCfiles"
        path3=destination+"/"+"DOCfiles"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
    elif extension in [".exe",".msi"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"EXEfiles"
        path3=destination+"/"+"EXEfiles"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
    elif extension in [".zip"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"ZIPfiles"
        path3=destination+"/"+"ZIPfiles"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
    elif extension in [".mp4"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"Soundfiles"
        path3=destination+"/"+"Soundfiles"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
#try:
 #   connection = mysql.connector.connect(
  #      host='localhost',     
   #     user='root',      
    #    password='admin'    
    #)
    #if connection.is_connected():
     #   print("Connected to MySQL database")
    #cursor=connection.cursor()
    #cursor.execute("create database filetypes")
    #cursor.execute("use database filetypes")
    #cursor.execute("create table movedfiles( file_name varchar(50), extention varchar(10) )")
    #for fileName in list:
     #   cursor.execute(f"insert into movedfiles (file_name,extention) values ({name,extension})")
    #data=cursor.fetchall()
    #for row in data:
     #   print(row)
#except Error as e:
 #   print(f"Error: {e}")
    
