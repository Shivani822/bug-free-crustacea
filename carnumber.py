import mysql.connector
import datetime
from PIL import Image
import cv2
import re
from pytesseract import image_to_string
import glob

#CONNECTING DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="owner"
)
mycursor = mydb.cursor()


#state_code=['MP','AP','AR','PY','LD','DL','DD','DN','CH','AN','WB','UP','UK','TR','TN','SK','RJ','PB','NL','MZ','ML','MN','MH','KL','KA','JH','JK','HP','HR','GJ','GA','CG','BR','AS']
path = 'E:/minor/images/*.*'
for file in glob.glob(path):
    print(file)
    image = cv2.imread(file)
    text = image_to_string(image, config='--psm 12')
    #re.sub(r"\w", "", text, flags=re.I)
    str=''
    for i in text:
        if (i.isalnum()):
            str=str+i
            #print(i, end="")
        else:
            pass
            #print(end="")
    #print("\n")
    number=str


    #print(number)
    #store ho gaya in str number


    sql="SELECT * FROM vehicle_info WHERE reg_no = %s"
    mycursor.execute(sql, (number, ))
    result = mycursor.fetchall()
    for x in result:
        print(x)




'''
The first two letters indicate the state or Union Territory to which the vehicle is registered.
The next two digit numbers are the sequential number of a district.
The third part consists of one ,two or three letters. This shows the ongoing series of an RTO (Also as a counter of the number of vehicles registered) and/or vehicle classification
The fourth part is a 4 digit number unique to each plate. A letter is 

Andhra Pradesh	AP	
Arunachal Pradesh	AR	
Assam	AS
Bihar	BR
Chhattisgarh	CG
Goa	GA	
Gujarat	GJ	
Haryana	HR	
Himachal Pradesh	HP	
Jammu and Kashmir	JK	
Jharkhand	JH
Karnataka	KA	
Kerala	KL
Madhya Pradesh	MP
Maharashtra	MH
Manipur	MN	
Meghalaya	ML	
Mizoram	MZ	
Nagaland	NL	
Odisha	OD[4]	
Punjab	PB
Rajasthan	RJ	
Sikkim	SK	
Tamil Nadu	TN
Telangana	TS[5][6]	
Tripura	TR	
Uttarakhand	UA/UK	
Uttar Pradesh	UP	
West Bengal	WB	
Andaman and Nicobar Islands	AN	
Chandigarh	CH
Dadra and Nagar Haveli	DN	
Daman and Diu	DD	
Delhi	DL
Lakshadweep	LD	
Puducherry	PY	



print '{:10s} {:3d}  {:7.2f}'.format('xxx', 123, 98)
print '{:10s} {:3d}  {:7.2f}'.format('yyyy', 3, 1.0)
print '{:10s} {:3d}  {:7.2f}'.format('zz', 42, 123.34)
will print

xxx        123    98.00
yyyy         3     1.00
zz          42   123.34
'''
'''
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)


cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image', originalImage)
cv2.imshow('Gray image', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
text=image_to_string(blackAndWhiteImage, config='--psm 12')
print("\nBlack n white")
for i in text:
    if(i.isalnum()):
        print(i,end="")
    else:
        print(end="")

text=image_to_string(grayImage, config='--psm 12')
print("\nGray")
for i in text:
    if(i.isalnum()):
        print(i,end="")
    else:
        print(end="")
'''