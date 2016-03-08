#!/Users/julia_mav/anaconda/bin/python
import re

filename_in = '/Users/julia_mav/Code/Python/webcode.txt'
file = open(filename_in,'r')

filename_out = '/Users/julia_mav/Code/Python/fellows-cleaned.txt'
file_o = open(filename_out,'w')


entry = ''
string_read = False
str = ''
c = ' '
while len(c) > 0:
        c = file.read(1)

        entry = entry+c
        if entry.find("});") != -1:
            file_o.write(str+' \n')
            entry = ''

        if c.find("<") != -1:
            string_read = False
            if len(str) > 1:
                if str.find("Insight Project") != 0 and str.find("Background") != 0 :
                    if str.find("&#39;") != -1:
                        print str
                        str=str.replace("&#39;","\'")
                    if str.find("&#8211;") != -1:
                        print str
                        str=str.replace("&#8211;","-")
                    if str.find("&#232;") != -1:
                        print str
                        str=str.replace("&#232;","e")
                    if str.find("&#39") != -1:
                        print str
                        str=str.replace("&#39","\'")
                    if str.find("&#38") != -1:
                        print str
                        str=str.replace("&#38","\&")
                    if str.find("&#47") != -1:
                        print str
                        str=str.replace("&#47","/")
                    if str.find("&#40") != -1:
                        print str
                        str=str.replace("&#40","(")
                    if str.find("&#41") != -1:
                        print str
                        str=str.replace("&#41",")")
                    if str.find("&#36") != -1:
                        print str
                        str=str.replace("&#36","\$")
                    if str.find("#") != -1:
                        print str, entry
                        raw_input('check')
                    file_o.write(str+' |')
            str = ''
    
        if c.find("'") != -1:
            string_read = False
            str = ''
        
        if string_read == True:
            str += c

        if c.find(">") != -1:
            string_read = True
   
        #print str
        #x += 1
#print entry
file_o.close()


