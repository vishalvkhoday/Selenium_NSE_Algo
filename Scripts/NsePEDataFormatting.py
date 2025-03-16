import sys

rec = [] 
ll = ""
LineVal = []
ISIN = 0
NsePEVal = open("C:\\Users\\Vishal\\OneDrive\\Desktop\\NSE_PE2.txt","r")
for line in NsePEVal:
    line = line.strip()
    if len(line) <= 2:
        continue
    if ISIN == 0:
        ll= ll+ line+","
        ISIN = 1

    if line.find("Securities Information")>=0 :
        line = line.replace("Securities Information","")
        ll= ll+ line.strip()

    if line.find("Basic Industry") >=0 :
        line = line.replace("Basic Industry ",",")
        rec= ll+ line.strip() +"\n"
        ll = ""
        ISIN = 0
        f = open("C:\\Users\\Vishal\\OneDrive\\Desktop\\NSE_PE2_V1.txt","a")
        f.write(rec)
        f.close()
    
    if line.find("Adjusted P/E")>=0 :
        line = line.replace("Adjusted P/E",",")
        ll= ll+ line
    if line.find("Symbol P/E")>=0 :
        line = line.replace("Symbol P/E",",")
        ll= ll+ line

print(rec)
# f = open("C:\\Users\\Vishal\\OneDrive\\Desktop\\NSE_PE2_V1.txt","a")
# f.write(rec)
# f.close()





