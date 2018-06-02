
#with open("legislators.csv", "r") as f:
#    legislators = f.read()
#    #checking for corect reading of file:
#    print(legislators[0:53]) #last_name,first_name,birthday,gender,type,state,party

# turning the file into a list of lists:
#legis_split = legislators.split('\n')
#legis_list = []
#for element in legis_split:
#    row = element.split(',')
#    legis_list.append(row)

#replacing a missing year with the previous field:    
last_value = 1

#for x in legislators:
#    last_value = x[7]
#    index(x)
    
    
for i in range(1,len(legislators)):
    last_value = legislators[i-1][7]
    if legislators[i][7] == 0:
        legislators[i][7]  = last_value
        
print(legislators[4:6])
