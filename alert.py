import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import hashlib
import time
import datetime
import json
import urllib3
import os
urllib3.disable_warnings()

x = datetime.datetime.now()

def hash_256(json_object, api_key, time_stamp, private_key):
    message = hashlib.sha256()
    message.update(private_key.encode('utf-8'))
    hash_string = "%s%s%s" % (str(json_object), str(api_key), str(time_stamp))
    message.update(hash_string.encode('utf-8'))
    hex_dig = message.hexdigest()
    return (hex_dig)

# Define API credentials and parameters
public_key = 'Sx7DB3Ry98pml8SGJwwMywnVEbvPda'
private_key = 'OkjyNCUUSJKRpqtpznQwfpZvlZlABoMAuDSDoVVhggpkPFmXWzjehvoLXbtX'


#url='https://api.metropol.co.ke:5555/v2_1/identity/verify'
#url='https://api.metropol.co.ke:5555/v2_1/delinquency/status'
#url='https://api.metropol.co.ke:5555/v2_1/score/consumer'
#url='https://api.metropol.co.ke:5555/v2_1/crystobolpromo'
#url='https://api.metropol.co.ke:5555/v2_1/report/pdf'
#url ='https://api.metropol.co.ke:5555/v2_1/report/json' #5,14
#url='https://api.metropol.co.ke:22225/v2_1/identity/scrub' #6
url='https://api.metropol.co.ke:5555/v2_1/identity/listing_partner' #7
#url='https://api.metropol.co.ke:5555/v2_1/report/credit_info'  #8,12,13,16,22
#url='https://api.metropol.co.ke:5555/v2_1/report/credit_info_v2'  #8,12,13
#url='https://api.metropol.co.ke:5555/v2_1/report/creditinfo/internal' #9
#url='https://api.metropol.co.ke:7070/v2_1/report/internal' #15
#url='https://api.metropol.co.ke:5555/v2_1/report' #15
#url='https://api.metropol.co.ke:22225/v2_1/report/credit_info_enhanced' #10
#url='https://api.metropol.co.ke:5555/v2_1/report/creditinfo/mobile' #11
#url='https://api.metropol.co.ke:22225/v2_1/kcb/mobile' #14 a 5
#url='https://api.metropol.co.ke:22225/v2_1/report/internal2' #inter2 with report5 # crystobol credit report
# url='http://10.61.61.25:7070/v2_1/delinquency/status'

#url='https://api.metropol.co.ke:22225/v2_1/report/custom'
#url='https://api.metropol.co.ke:22225/' #health
#url='https://api.metropol.co.ke:22225/v2_1/' #health
#url='https://api.metropol.co.ke:22225/v2_1/consent/callback' #health

#url='https://api.metropol.co.ke:22225/v2_1/score/internal' #
#url='https://api.metropol.co.ke:5555/v2_1/identity/listing_partner'

#url='https://api.metropol.co.ke:5555/v2_1/report/CreditScoreInternal' #33
#json_object = '{"report_type":17,\"identity_number":"29088976",\"identity_type":"001",\"loan_amount":50000,\"report_reason":1}'

#url='https://api.metropol.co.ke:5555/v2_1/open/accounts' #19
#json_object = '{"report_type":19,\"identity_number":"880000088",\"identity_type":"001",\"account_number":"MG1621400708"}'



#json_object='{"report_type":3,\"identity_number":"34958363",\"identity_type":"001"}'
#json_object='{"report_type":3,\"identity_number\":"880000088",\"identity_type":"001",\"mobile_score":false}'
#json_object='{\"report_type":3,\"identity_number":"29088976",\"identity_type":"001",\"as_at":"2022-03-07",\"period":0}'
#json_object='{\"report_type":3,\"identity_number":"29088976",\"identity_type":"001",\"as_at":"2023-04-13",\"period":7,\"mobile_score":false}'
#json_object='{\"report_type":14,\"identity_number":"33154492",\"identity_type":"001",\"loan_amount":1000,\"report_reason":1,\"snap_shot_date":"08-03-2023"}'

#json_object = '{"report_type":0,\"identity_number":"30958178",\"identity_type":"001"}'
#json_object = '{"report_type":1,\"identity_number":"880000088",\"identity_type":"001","mobile_number":"254720123456"}'
#json_object = '{"report_type":1,\"identity_number":"880000088",\"identity_type":"001","mobile_number":"254720123456"}'
#json_object = '{"report_type":2,"identity_number":"880000088","identity_type":"002","loan_amount":50000}'
#json_object = '{"report_type":3,\"identity_number":"34958363",\"identity_type":"002"}'
#json_object = '{"report_type":4,\"identity_number":"880000088",\"identity_type":"001",\"loan_amount":1000,\"report_reason":1}'
#json_object = '{"report_type":5,\"identity_number":"880000088",\"identity_type":"001",\"loan_amount":10000,\"report_reason":1}'
#json_object = '{"report_type":6,\"identity_number":"29088976",\"identity_type":"001"}'
json_object = '{"report_type":7,\"identity_number":"29088976",\"identity_type":"001"}'
#json_object = '{\"report_type\":8,\"identity_number\":\"770000077\",\"identity_type\":\"001\",\"loan_amount\":2000,\"report_reason\":1}'
#json_object = '{"report_type":9,"identity_number":"33154492","identity_type":"001","loan_amount":10000,"report_reason":1}'
#json_object = '{"report_type":14,"identity_number":"39536594","identity_type":"001","loan_amount":20000,"report_reason":1}'
#json_object = '{"report_type":11,"identity_number":"770000077","identity_type":"001","loan_amount":10000,"report_reason":1}'
#json_object = '{"report_type":12,"identity_number":"24696584","identity_type":"001","loan_amount":2000,"report_reason":1}'
#json_object = '{"report_type":13,\"identity_number":"770000077",\"identity_type":"001",\"loan_amount":10000,\"report_reason":1}'
#json_object = '{"report_type":14,"identity_number":"770000077","identity_type":"001","loan_amount":500,"report_reason":1}'
#json_object = '{"report_type":15,"identity_number":"24696584","identity_type":"001","loan_amount":500,"report_reason":1}'
#json_object = '{"report_type":22,"identity_number":"770000077","identity_type":"001","loan_amount":2000,"report_reason":1}'
#json_object = '{"report_type":16,"identity_number":"770000077","identity_type":"001","loan_amount":500,"report_reason":1}'
#json_object = '{"report_type":2,"identity_number":"29088976","identity_type":"001","loan_amount":10000,"mobile_number":"254700754777","callback_url":"https://api.metropol.co.ke:7070/v2_1/consent/callback"}'
#json_object = '{"report_type":12,"identity_number":"880000088","identity_type":"001","loan_amount":10000,"report_reason":1,"mobile_number":"254727802152","callback_url":"https://boost-chapaa.herokuapp.com/metropol_callback/1"}'
#json_object = "{\"report_type\":%s,\"identity_number\":\"%s\",\"identity_type\":\"%s\",\"loan_amount\":%s,\"report_reason\":%s}" % (5, '24890985', '001', '1000', 4)



# Define email settings
def send_email(subject, message, attachment_filename=None):
    from_email = "wkipchumba.wk15@gmail.com"
    to_email = "wkipchumba.wk@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "wkipchumba.wk15@gmail.com"
    smtp_password = "dbzj crid hkdl aqcg"  # Replace with your generated App Password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if attachment_filename:
        attachment = open(attachment_filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_filename)}")
        msg.attach(part)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Function to save the response to a file
def save_response_to_file(response_text, filename):
    with open(filename, "w") as file:
        file.write(response_text)

# Function to perform the API test
def perform_api_test():
    # Get the current timestamp
    metropol_timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')

    # Calculate the hash
    sent_hash = hash_256(json_object=json_object, api_key=public_key, time_stamp=str(metropol_timestamp), private_key=private_key)

    # Prepare request headers
    headers = {
        'Content-Type': 'application/json',
        'X-METROPOL-REST-API-KEY': public_key,
        'X-METROPOL-REST-API-HASH': sent_hash,
        'X-METROPOL-REST-API-TIMESTAMP': metropol_timestamp,
    }

    # Make the API request
    response = requests.post(url, headers=headers, data=json_object, verify=False)

    print('Sent Hash: ' + sent_hash)
    print('Timestamp: ' + str(metropol_timestamp))
    print("Status: " + str(response.text))
    print("Code: " + str(response.status_code))

    # Save the API response to a file
    save_response_to_file(response.text, "api_response.txt")

    # Send the file as an attachment in the email
    send_email("API Response", "Attached is the API response.", "api_response.txt")

# Measure execution time
start_time = time.time()

# Perform the API test
perform_api_test()

end_time = time.time()