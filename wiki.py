#!/usr/bin/python
import webbrowser
import json
import urllib
import urllib.request

title = []
linkId = []


def getinfo():
    
    results = []
    global title
    global linkId
    title = []
    linkId = []
    
    print('Retriving information please wait')
    
    rawdata = urllib.request.urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json').read()
    jsonData = json.loads(rawdata.decode('utf8'))
    results = jsonData['query']['random']
    
    print('Completed')
    print('-'*10)
    
    for eachResult in results:
        title.append(eachResult['title'])
        linkId.append(eachResult['id'])


def wiki():
    counter = len(title)
    linkCounter = 0
    for er in title:
        print(er)
        choice = input('Are you sure you want to visit this page?(y/n)')
        if choice.lower() == 'y':
            webbrowser.open_new('http://en.wikipedia.org/wiki?curid='+str(linkId[linkCounter]))
            input('Program will now close..Press enter to continue')
            exit(0)
        else:
            print('Next result incoming')
            print('-'*10)
            counter -= 1
            linkCounter += 1
            if counter == 0:
                refresh_choice = input('Would you like to try again?(y/n)')
                if refresh_choice.lower() == 'y':
                    getinfo()
                    wiki()
                else:
                    print("Goodbye")
                    exit(0)

getinfo()
wiki()


