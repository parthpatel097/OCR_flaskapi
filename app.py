from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import os 
import pytesseract
from PIL import Image
# import mysql.connector
import re
from datetime import datetime

app = Flask(__name__)
api = Api(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # path of the app 

# database connection

# mydb = mysql.connector.connect(
# 	host = "184.168.96.176",
# 	user="doc_admin",
#     port=3306,
# 	password="Admin1234!#$",
# 	database="docsender_db"
# 	)
# mydb =  mysql.connector.connect(
# 	host = "localhost",
# 	database='doc_sender',
# 	user = "root",
# 	password = ""
# )
# cursor = mydb.cursor()

# simple get method 
class Index(Resource):
    def get(self):
        return jsonify("Docsender api")

# OCR function to extract the information from the image
def ocr_core(filename):
    text =pytesseract.image_to_string(Image.open(filename)) # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# All functions to find the required text from the images
def date_finder(text_input):
    dates=[]
    reg1=re.compile(r'(?<!\S)[0-3]{1}[0-9]{1}[/][0-9]{2}[/][0-9]{4}')
    res1=reg1.findall(text_input)
    for i in res1:
        d1 = datetime.strptime(i,'%d/%m/%Y').strftime('%Y-%m-%d')
        dates.append(d1)
    reg2=re.compile(r'(?<!\S)[0-3]{1}[0-9]{1}[-][0-9]{2}[-][0-9]{4}')
    res2=reg2.findall(text_input)
    for i in res2:
        d2= datetime.strptime(i,'%d-%m-%Y').strftime('%Y-%m-%d')
        dates.append(d2)
    reg3=re.compile(r'(?<!\S)[0-9]{4}[/][0-9]{2}[/][0-9]{2}')
    res3=reg3.findall(text_input)
    for i in res3:
        d3= datetime.strptime(i,'%Y/%m/%d').strftime('%Y-%m-%d')
        dates.append(d3)
    reg4=re.compile(r'(?<!\S)[0-9]{4}[-][0-9]{2}[-][0-9]{2}')
    res4=reg4.findall(text_input)
    for i in res4:
        d4= datetime.strptime(i,'%Y-%m-%d').strftime('%Y-%m-%d')
        dates.append(d4)
    reg5=re.compile(r'(?<!\S)[0-9]{4}[.][0-9]{2}[.][0-9]{2}')
    res5=reg5.findall(text_input)
    for i in res5:
        d5= datetime.strptime(i,'%Y.%m.%d').strftime('%Y-%m-%d')
        dates.append(d5)
    reg6=re.compile(r'(?<!\S)[0-9]{2}[.][0-9]{2}[.][0-9]{4}')
    res6=reg6.findall(text_input)
    for i in res6:
        d6= datetime.strptime(i,'%d.%m.%Y').strftime('%Y-%m-%d')
        dates.append(d6)
    return dates
    
def amount_finder(text_input):
    amounts=[]
    reg1=re.compile('[1-9]{1}[0-9]{1,12}[.][0-9]{1,2}')
    res1=reg1.findall(text_input)
    for i in res1:
        amounts.append(i)
    reg2=re.compile('[1-9][,][0-9]{1,3}')
    res2=reg2.findall(text_input)
    for i in res2:
        num1=re.sub(',','',i)
        amounts.append(num1)
    reg3=re.compile('[1-9][0-9][,][0-9]{2,5}')
    res3=reg3.findall(text_input)
    for i in res3:
        num2=re.sub(',','',i)
        amounts.append(num2)
    reg4=re.compile('[1-9][,][0-9]{2}[,][0-9]{2,5}')
    res4=reg4.findall(text_input)
    for i in res4:
        num3=re.sub(',','',i)
        amounts.append(num3)
    reg5=re.compile('[1-9][0-9][,][0-9]{2}[,][0-9]{2,5}')
    res5=reg5.findall(text_input)
    for i in res5:
        num4=re.sub(',','',i)
        amounts.append(num4)
    reg6=re.compile('[1-9][,][0-9]{2}[,][0-9]{2}[,][0-9]{2,5}')
    res6=reg6.findall(text_input)
    for i in res6:
        num5=re.sub(',','',i)
        amounts.append(num5)
    reg7=re.compile('[1-9][0-9][,][0-9]{2}[,][0-9]{2}[,][0-9]{2,5}')
    res7=reg7.findall(text_input)
    for i in res7:
        num6=re.sub(',','',i)
        amounts.append(num6)
    reg8=re.compile('[1-9][,][0-9]{1,3}[.][0-9]{1,2}')
    res8=reg8.findall(text_input)
    for i in res8:
        num7=re.sub(',','',i)
        amounts.append(num7)
    reg9=re.compile('[1-9][0-9][,][0-9]{2,5}[.][0-9]{1,2}')
    res9=reg9.findall(text_input)
    for i in res9:
        num8=re.sub(',','',i)
        amounts.append(num8)
    reg10=re.compile('[1-9][,][0-9]{2}[,][0-9]{2,5}[.][0-9]{1,2}')
    res10=reg10.findall(text_input)
    for i in res10:
        num9=re.sub(',','',i)
        amounts.append(num9)
    reg11=re.compile('[1-9][0-9][,][0-9]{2}[,][0-9]{2,5}[.][0-9]{1,2}')
    res11=reg11.findall(text_input)
    for i in res11:
        num11=re.sub(',','',i)
        amounts.append(num11)
    reg12=re.compile('[1-9][,][0-9]{2}[,][0-9]{2}[,][0-9]{2,5}[.][0-9]{1,2}')
    res12=reg12.findall(text_input)
    for i in res12:
        num12=re.sub(',','',i)
        amounts.append(num12)
    reg13=re.compile('[1-9][0-9][,][0-9]{2}[,][0-9]{2}[,][0-9]{2,5}[.][0-9]{1,2}')
    res13=reg13.findall(text_input)
    for i in res13:
        num13=re.sub(',','',i)
        amounts.append(num13)
    amounts=[float(i) for i in amounts]
    if len(amounts)>0:
        final_amount=max(amounts)
    else:
        final_amount=None
    return final_amount

def invoice_finder(text_input):
    invoice_num=[]
    reg1=re.compile('(?<!\S)[0-9]{5,6}[-][0-9]{3,5}')
    res1=reg1.findall(text_input)
    for i in res1:
        invoice_num.append(i)
    reg2=re.compile('(?<!\S)[0-9]{4}[/][A-Za-z]{2,3}[/][0-9]{3,5}')
    res2=reg2.findall(text_input)
    for i in res2:
        invoice_num.append(i)
    reg4=re.compile('(?<!\S)[0-9]{4}[/|-][0-9]{4}')
    res4=reg4.findall(text_input)
    for i in res4:
        invoice_num.append(i)
    reg6=re.compile('(?<!\S)[#][A-Za-z]{3,4}[-|/][0-9]{3,4}')
    res6=reg6.findall(text_input)
    for i in res6:
        invoice_num.append(i)
    reg7=re.compile('(?<!\S)[0-9]{2,3}[-][0-9]{5,6}')
    res7=reg7.findall(text_input)
    for i in res7:
        invoice_num.append(i)
    reg8=re.compile('(?<!\S)[#][0-9]{2,5}(?=\s|$)')
    res8=reg8.findall(text_input)
    for i in res8:
        invoice_num.append(i)
    reg11=re.compile('(?<!\S)[A-Za-z]{2,3}[0-9]{12,14}')
    res11=reg11.findall(text_input)
    for i in res11:
        invoice_num.append(i)
    return invoice_num

def contact_finder(text_input):
    contact_no=[]
    reg1=re.compile('[7-9][0-9]{9}')
    res1=reg1.findall(text_input)
    for i in res1:
        contact_no.append(i)
    reg2=re.compile('[+][9][1][6-9][0-9]{9}')
    res2=reg2.findall(text_input)
    for i in res2:
        contact_no.append(i)
    reg3=re.compile('(?<!\S)[0-9]{3,4}[\s][0-9]{3,4}[\s][0-9]{3,4}')
    res3=reg3.findall(text_input)
    for i in res3:
        contact_no.append(i)
    return contact_no

def email_finder(text_input):
    emails=[]
    reg1 = re.compile(r'[a-zA-Z0-9|.|_]{2,20}@[a-zA-Z]{2,20}.[a-zA-Z|.]{2,20}')
    res1 = reg1.findall(text_input)
    for i in res1:
        emails.append(i)
    return emails

def name_finder(text_input):
    name1 = re.compile(r'([A-Z]{3,10}[\s][A-Z]{3,15})+')
    name=name1.findall(text_input)
    if len(name)>0:
        name=name[0]
    else:
        name=None
    return name

def gst_no_finder(text_input):
    gst_number=[]
    regex=re.compile(r'[0-9A-Z]{10}[0-9A-Za-z]{3}[Z][0-9A-Za-z]{1}')
    gst_no = regex.findall(text_input)
    for i in gst_no:
        gst_number.append(i)
    return gst_number

# Get all the required data and validate them 
def text_to_data(text):
        gst_no = gst_no_finder(text)
        if len(gst_no)>0:
            gst_no=gst_no[0]
        else:
            gst_no=None
        final_amount = amount_finder(text)
        contact_no = contact_finder(text)
        if len(contact_no)>0:
            contact_no=contact_no[0]
        else:
            contact_no=None
        email_id = email_finder(text)
        if len(email_id)>0:
            email=email_id[0]
        else:
            email=None
        date=date_finder(text)
        if len(date)>0:
            result=date[0]
        else:
            result=None
        invoice_no=invoice_finder(text)
        if len(invoice_no)>0:
            invoice_no=invoice_no[0]
        else:
            invoice_no=None
        name=name_finder(text)
        info_get = []
        info_get.extend([gst_no,final_amount,contact_no,email,result,invoice_no,name])
        return info_get
      

#  post request to get the image and extract the relevant information
class OCRInfo(Resource):
    def post(self):
        imagePath = request.files.getlist("image")
        user_id = request.form.get("user_id")
        user_list = []
        try:
            for file in imagePath:
                target = os.path.join(APP_ROOT, 'images')
                file_name = file.filename
                destination = "/".join([target, file_name])
                file.save(destination)
                extracted_text = ocr_core(destination)
                data=text_to_data(text=extracted_text)
                gst,amount,contact_no,email,date,invoice_no,name=data[0],data[1],data[2],data[3],data[4],data[5],data[6]
                data={"user_id":user_id,"gst_no":gst,"Total_amnt":amount,"Contact_no":contact_no,"email_id":email,"date":date,"invoice_number":invoice_no,"name":name}
                user_list.append(data)
                # sql_query = "INSERT INTO doc_sender_user(user_id,filepath,filename,gst_no,total_amount,contact_no,email_id,date,invoice_number,doc_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" # Insert values into database
                # values= (user_id,destination,file_name,gst,amount,contact_no,email,date,invoice_no,name)
                # cursor.execute(sql_query, values)
                # mydb.commit()
                # json_object=json.dumps(data)
                # json_object = json.loads(json_object.replace("\'", '"'))
            
            return user_list,200
        except:
            return "Image not found",401            
                
api.add_resource(OCRInfo, '/upload')
api.add_resource(Index, '/')

if __name__ =="__main__":
    app.run(debug=True)
        