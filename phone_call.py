# importing twilio package
from twilio.rest import TwilioRestClient

# Number provided by twilio

twilio_phone_number = "+13305XXXXX"

# Provide the number whom you want to call

dail_numbers = ["+9194XXXX","+91XXXXX"]

# Instruction url (paste exactly given below)

twiml_inst_url = "http://static.fullstackpython.com/phone-calls-python.xml"

# Provide the ("account_number","auth_token_code")

client = TwilioRestClient("PASTE ACCOUNT NUMBER HERE","PASTE TOKEN HERE")

def dail_numbers1(numbers_list):
    for number in numbers_list:
        print("Dialing "+ number)
        client.calls.create(to = number,from_ = twilio_phone_number,url=twiml_inst_url,method="GET")

if __name__== "__main__":
    dail_numbers1(dail_numbers)

# end