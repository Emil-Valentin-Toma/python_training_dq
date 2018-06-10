name_counts = {}
#iterate through legislators:
for lista in legislators:
    #checking if gender and year columns meet the conditions below:
    if (lista[3] == 'F' and  lista[7] > 1940):
        #asign variable to first name:
        name = lista[1]
        #looping through dictionary in order to check an existing name and increase the counter:
        if name in name_counts:
            name_counts[name] =   name_counts[name] +1
        #adding a new name if looping fails to detect an existing one:    
        else:
            name_counts[name] = 1
