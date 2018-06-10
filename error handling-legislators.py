
#the better version of opening the file:
with open("C:\\Users\\Emil\\Dropbox\\programare\\python\\DATAQUEST\\resources\\legislators.csv", "r") as f:
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

birth_day = []
for item in legis_list:
    #building the list of birthdays only:
    birth_day.append(item[2])
#deleting the column header, which is text- we need numbers:
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

birth_year.insert(0,'birth_year')
#for x in birth_year:
 #   x= str(x)
  #  x=list(x)
  #good! sane reference is used for both lists:
for x in list(range(0,len(legis_list))):
    legis_list[x].append(birth_year[x])
#print(birth_year[0:3])
#print(list(range(len(legis_list)))[0:5])
#legislators = []
#bdindex = int(range(0, len(legislators)))
#for x in legislators:
#    x = x+birth_year[legislators.index(x)]
#legislators = legis_list + birth_year
#birth_year = str(birth_year)
##print(birth_year[0:30])
#for x in range(0,len(legis_list)):
#    legislators.append(concatenate birth_year[x]+legis_list[x])
print(legislators[0:90])
