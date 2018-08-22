
import re

str1 = "str: AGENT ID 12345    PIN              RES NO. 0786-4376-US-2"

#obj_rex = re.compile('r(RES NO.*)',re.IGNORECASE)

#str_getConfid = re.findall(r'<Conf.*', str_resp, re.MULTILINE)
get_res = re.findall(r'RES NO.*', str1, re.MULTILINE)
print get_res