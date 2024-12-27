import sys

rec = [] 
ll = ""
LineVal = []

NsePEVal = open("C:\\Users\\Vishal\\OneDrive\\Desktop\\NSE_PE2.txt","r")
for line in NsePEVal:
    line = line.replace("\n",",")
    if line.find(":Securities Information")>=0 :
        line = line.replace(":Securities Information","")
        ll= ll+ line

    if line.find("Basic Industry") >=0 :
        line = line.replace("Basic Industry","")
        rec= ll+ line +"\n"
        ll = ""
        f = open("C:\\Users\\Vishal\\OneDrive\\Desktop\\NSE_PE2_V1.txt","a")
        f.write(rec)
        f.close()
    
    if line.find("Adjusted P/E")>=0 :
        line = line.replace("Adjusted P/E","")
        ll= ll+ line
    if line.find("Symbol P/E")>=0 :
        line = line.replace("Symbol P/E","")
        ll= ll+ line

print(rec)
# f = open("C:\\Users\\Vishal\\OneDrive\\Desktop\\NSE_PE2_V1.txt","a")
# f.write(rec)
# f.close()





