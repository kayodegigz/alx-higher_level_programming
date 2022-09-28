#!/usr/bin/python3
"""Python script that fetches 
   https://alx-intranet.hbtn.io/status"""

    if __name__ == '__main__':
        import urllib.request
    
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        content = r.read()
        print("Body Response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: OK")
