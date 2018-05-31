with open("legislators.csv", "r") as f:
    legislators = f.read()
    #checking for corect reading of file:
    print(legislators[0:53]) #last_name,first_name,birthday,gender,type,state,party

# turning the file into a list of lists:
legis_split = legislators.split('\n')
legis_list = []
for element in legis_split:
    row = element.split(',')
    legis_list.append(row)
# checking the legis list:
#print (legis_list[0:2])#[['last_name', 'first_name', 'birthday', 'gender', 'type', 'state', 'party'],
                       # ['Bassett', 'Richard', '1745-04-02', 'M', 'sen', 'DE', 'Anti-Administration']]
    '''
#trying unsuccesfully to cope with the bug
for x in legis_list:
    if x[3] == '':
        x[3] = 'M'
'''

birth_day = []
for item in legis_list:
    #building the list of birthdays only:
    birth_day.append(item[2])
#deleting the column header, which is text- we need numbers:
del legis_list[0]
del birth_day[0]
#checking the parsed DOB:
#print (birth_day[0:2]) #['1745-04-02', '1742-03-21']
#splitting parsed birth_day column:
DOB_split = []
for element in birth_day:
    DOB_split.append(element.split('-'))
##print(DOB_split[0:5])#[['1745', '04', '02'], ['1742', '03', '21'], ['1743', '06', '16'], ['1730', '07', '22'], ['1739', '03', '16']]
#separating the year of birth from the DOB:
birth_year=[]
for lista in DOB_split:
    try:
        birth_year.append(int(lista[0]))
    except Exception:
        birth_year.append(0)
#print(birth_year[0:2]) #[1745, 1742]

#birth_year.insert(0,'birth_year') -actually not clear if needed aheader or not

#merging the two lists:
for x in list(range(0,len(legis_list))):
    legis_list[x].append(birth_year[x])
legislators = legis_list

'''
#transforming the list of lists in simple list:
legislators = []
for x in legis_list:
    for y in x:
        legislators.append(y)
        '''
print(legislators[0:10])
