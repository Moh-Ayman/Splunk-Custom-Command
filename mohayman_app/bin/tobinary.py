import os
import time
import datetime
import splunk.Intersplunk 
import urllib
import httplib2
import re
from time import localtime,strftime
from xml.dom import minidom
import json

def l(data):
        with open ("tobinary.log",'a') as f:    
                f.write(data+"\n")
        f.close()
        
def decimalToBinary(n):
        try:
                l("decimalToBinary Started")
                l(str(n)+str(type(int(n))))
                l(str(bin(int(n)).replace("0b", "")))
                return bin(int(n)).replace("0b", "")  
        except ValueError as e:
                l("Error: "+e)

def process_events():
    l("\nprocess_events() Started")    
    results, dummyresults, settings = splunk.Intersplunk.getOrganizedResults()
    l("results: "+str(results)+"\ndummy results: "+str(dummyresults)+"\nsettings: "+str(settings))
    fields, argvals = splunk.Intersplunk.getKeywordsAndOptions()
    l("\nfields: "+str(fields)+"\nargvals: "+str(argvals))
    for result in results:
        l("\nresult: "+str(result))
        l("\nresult[fields]: "+result[fields[0]])  
        result["Binary"] = decimalToBinary(result[fields[0]]) 
    splunk.Intersplunk.outputResults(results) 

process_events()