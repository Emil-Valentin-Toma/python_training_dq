values = [None, 10, 20, 30, None, 50]
checks = []
#looping through values:
for val in values:
    #checking requirements and add True or False in the list "check" accordingly:
    if val is not None and val > 30:
        checks.append(True)
    else:
        checks.append(False)
        
