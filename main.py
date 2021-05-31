ip_dict,error_dict,url_dict={},{},{}        #Created empty dictionaries     
def counting(item,dict1):                   #Created function to count of unique ip,error code and url
    if item not in dict1:
        dict1[item]=0
    dict1[item]+=1
def csv_file(reader):                       #Created funtion to do operations
    for row in reader:
        row=row.split(',')
        counting(row[0],ip_dict)            #Calling the function
        counting(row[2],url_dict)           #Calling the function
        counting(row[3],error_dict)         #Calling the function
    del ip_dict['IP']
    del url_dict['URL']
    del error_dict['Error Code\n']
    print("IP's Count: ",ip_dict)
    print("URL Count: ",url_dict)
    print("Error Code Count: ",error_dict)
    ip_list_values = list(ip_dict.values())     #Converting dictinary into 2 lists for values and keys
    ip_list_keys = list(ip_dict.keys())
    print("Highest reapeted ip address is: ", ip_list_keys[ip_list_values.index(max(ip_list_values))], "count is: ", max(ip_list_values),"times")       #Taking maximum index of values
    print("Lowest reapeted ip address is: ", ip_list_keys[ip_list_values.index(min(ip_list_values))], "count is: ", min(ip_list_values), "times")       #Taking minimum index of values
with open("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\venv\\Scripts\\weblog.csv","r") as reader:        #File Reading
    csv_file(reader)                    #Calling the function

    
