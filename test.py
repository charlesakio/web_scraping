import re

string = ' http://stackshare.io/object-document-mapper-(odm)'
pattern = re.compile('/-\(com\)/')
print(pattern.match(string))