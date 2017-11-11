import json
import random

with open('C:\\users\\sravan\\Desktop\\sra2\\aspiriants.json') as json_data:
    data = json.load(json_data)
print "Enter the number of teams to be formed:"
form = input()  #number of teams to be formed
info = len(data['ASPIRIANTS'])  #data stored in info
value = 1                       # the value
maximum = info/form         # max members in a team 
minimum = 1                     # min members in a team
ctemp = 1                       # temp remaining members arrange
if(info % form == 0):
    while value<=form:
        print "team "
        print value
        while minimum<=maximum:
            x = random.choice(data['ASPIRIANTS'])
            print (x) #persons
            data['ASPIRIANTS'].remove(x)
            minimum = minimum+1
            if minimum>maximum:
                minimum=1
                break
        value = value+1
        if value>form:
            value=1
            break
else:
    z=info%form
    if (info%form == 1):
        print "teams cannot be divided equally reply :"
    check = input("1/0:")
    if(check == 1):
        while value<=form:
                print "team "
                print value
                print "ok"
                while minimum<=maximum:
                    x = random.choice(data['ASPIRIANTS'])
                    print (x)
                    data['ASPIRIANTS'].remove(x)
                    minimum = minimum+1
                    if minimum>maximum:
                        minimum=1
                        break
                value = value+1
                if value>form:
                    value=1
                    break
        while value<=form:
            while ctemp<=z:
                print "team number:"
                print value
                x = random.choice(data['ASPIRIANTS'])
                print (x)
                data['ASPIRIANTS'].remove(x)
                ctemp = ctemp+1
                value = value+1
                if ((ctemp>z)|(value>form)):
                    break
            if ((ctemp>z)|(value>form)):
                ctemp=1
                value=1    
                break

    else:
        print "thanku"
