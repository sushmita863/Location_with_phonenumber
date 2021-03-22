import  phonenumbers
#test is your file which containg the phonenumber that you want to visit
from test import numbers
from phonenumbers import geocoder

ch_number= phonenumbers.parse(numbers,"CH")  # CH is for Country and History
print(geocoder.description_for_number(ch_number,"en")) # it prints from where the  number is from

from phonenumbers import  carrier
service_number= phonenumbers.parse(numbers,"RO")
print(carrier.name_for_number(service_number,"en")) # it prints the service name for that perticular number