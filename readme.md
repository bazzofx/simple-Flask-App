#Download Youtube Music & Videos from youtube
#exploreflask.com/en/latest/blueprints.html

Thansk to Tim@
https://www.youtube.com/watch?v=WteIH6J9v64&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=10

#Pytube module is broken below fix must be apply as of 20th Oct, 2024

pytube module needs fixing, as the module which downloads using pip is broken, the below regex needs to be updated.
Change in Cipher.py
https://github.com/pytube/pytube/issues/1707
Line 272 & 273 to :
```
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
```
## Windows
```
mv /cypher.py /venv/lib/pytube/cypher.py
```
## Linux
```
mv /cypher.py /venv/lib/python3.12/site-packages/pytube/cypher.py
```

# Pytubefix

## Get Po Token
Get PO token using the below
Save Token Cache on Server
https://colab.research.google.com/drive/190BC9tEc0wTtCsfSbWHY-lT6amjSwFyG#scrollTo=M8mz73yeureD