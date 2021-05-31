ip_dict,error_dict,url_dict={},{},{}
def counting(item,dict1):
    if item not in dict1:
        dict1[item]=0
    dict1[item]+=1
def csv_file(reader):
    for row in reader:
        row=row.split(',')
        ipaddress=row[0]
        url=row[2]
        error=row[3]
        counting(ipaddress,ip_dict)
        counting(url,url_dict)
        counting(error,error_dict)
    del ip_dict['IP']
    del url_dict['URL']
    del error_dict['Error Code\n']
    print("IP's Count: ",ip_dict)
    print("URL Count: ",url_dict)
    print("Error Code Count: ",error_dict)
    ip_list_values = list(ip_dict.values())
    ip_list_keys = list(ip_dict.keys())
    print("Highest reapeted ip address is: ", ip_list_keys[ip_list_values.index(max(ip_list_values))], "count is: ", max(ip_list_values),"times")
    print("Lowest reapeted ip address is: ", ip_list_keys[ip_list_values.index(min(ip_list_values))], "count is: ", min(ip_list_values), "times")
with open("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\venv\\Scripts\\weblog.csv","r") as reader:
    csv_file(reader)
#f=open("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\venv\\Scripts\\weblog.csv","r")
    #print("{0}".format(reader.readline().split()))
    #for x in reader:
        #x = x.split(',')
        #print(x[3])


