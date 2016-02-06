#!/usr/bin/python2.7

import os

script = '''
#!/bin/bash
for i in \$(ls)
do
    if [[ ! -z \$(diff \$i temp_files/AAAAAA.html) ]]
    then
        echo \$i ;
    fi
done
'''

def perform(command):
    os.system(command)

perform("mkdir temp_files")
perform("echo \"" + script + "\" > temp_files/test.sh")
perform("chmod +x temp_files/test.sh")

letters = ['A' , 'B' ,'C' , 'D' , 'E' , 'F']

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                for letter5 in letters:
                    for letter6 in letters:
                        perform("cd temp_files && wget http://s3-eu-west-1.amazonaws.com/puzzleinabucket/" + letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + ".html &> /dev/null")

perform("cd temp_files && ./test.sh > ../output.txt")
perform("rm temp_files -rf")
