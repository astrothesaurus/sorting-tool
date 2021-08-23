#! /usr/bin/env python
# -*- coding: utf-8 -*-

#python default packages
import sys
import re
import urllib2
import json
import os

#sys.path for installed packages, un-comment for web deployment
#sys.path = ['', '/home/jgwlibrary/lib/python/rdflib-3.2.0-py2.7.egg', '/home/jgwlibrary/lib/python/isodate-0.5.1-py2.7.egg', '/home/jgwlibrary/lib/python/SPARQLWrapper-1.6.4-py2.7.egg', '/home/jgwlibrary/lib/python/Flask-0.10.1-py2.7.egg', '/home/jgwlibrary/lib/python/itsdangerous-0.24-py2.7.egg', '/home/jgwlibrary/lib/python/Werkzeug-0.10.1-py2.7.egg', '/home/jgwlibrary/lib/python/Flask_ReCaptcha-0.4.1-py2.7.egg', '/home/jgwlibrary/lib/python/requests-2.9.1-py2.7.egg', '/home/jgwlibrary', '/home/jgwlibrary/lib/python', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-linux2', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PIL', '/usr/lib/pymodules/python2.7']

#packages installed on DreamHost
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import redirect

# Email libraries
import smtplib
from email.mime.text import MIMEText

setupfile = './static/setup.txt'
sf = (open(setupfile, 'r')).read()
line = sf.splitlines()
shortname = line[0].replace("shortname = ","")
longname = line[1].replace("longname = ","")
email = line[2].replace("email = ","")
version = line[3].replace("version = ","")
savefile = line[4].replace("savefile = ","")
meta = line[5].replace("meta = ","")
url = line[6].replace("url = ","")
logo = line[7].replace("logo = ","")
host = line[8].replace("host = ","")
port = line[9].replace("port = ","")
username = line[10].replace("username = ","")
password = line[11].replace("password = ","")
selection =  line[12].replace("selection = ","")

app = Flask(__name__, static_folder='static', static_url_path='')

reload(sys)
sys.setdefaultencoding("utf-8")

@app.route('/')
def sortingpage():

    names = os.listdir(os.path.join(app.static_folder, 'topconcepts'))
    filelist = []
    for y in names:
        filedict = {}
        filedict["name"] = y.capitalize().replace("_"," ").replace(".json","")
        filedict["file"] = y
        filedict["value"] = y.replace(".","").replace("json","")

        filelist.append(filedict)

    filelist.sort()

    return render_template('sorting.html', filelist=filelist, shortname=shortname, longname=longname,logo=logo, version=version, savefile=savefile, meta=meta, url=url, selection=selection)


@app.route('/sort/')
def sortingtool():
    return redirect('/')


@app.route('/topconcepts/')
def send_tc():
    return send_from_directory('topconcepts')

# email host, port, username, password, etc found in the static/setup.txt file
@app.route('/email',methods=['POST'])
def emailchanges():
    val = request.form['testarg']
    msg = MIMEText(val)

    #print msg

    me = username
    you = email
    msg['Subject'] = 'Suggestions from Sorting Tool'
    msg['From'] = me
    msg['To'] = you


    #Test Info
    #s = smtplib.SMTP('127.0.0.1:1025')
    
    #Live Info
    s = smtplib.SMTP()
    s.connect(host,port)
    s.login(username,password)
    
    #Test & Live
    s.sendmail(me, [you], msg.as_string())
    s.quit()

    #return 'Email sent'

if __name__ == '__main__':
    app.run()

