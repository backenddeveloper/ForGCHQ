#!/usr/bin/python2.7

import requests

previous_request = None

url = 'http://s3-eu-west-1.amazonaws.com/puzzleinabucket/'

letters = ['A' , 'B' ,'C' , 'D' , 'E' , 'F']

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                for letter5 in letters:
                    for letter6 in letters:
                        request = requests.get(url + letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + '.html')
                        if previous_request and request.body != previous_request:
                            print "Found: " + letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + '.html'
                            exit(0)
                        else:
                            previous_request = request.body
