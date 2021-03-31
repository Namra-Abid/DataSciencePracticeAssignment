with open('student.csv','r') as rows:
      data_rows=rows.readlines()
print(data_rows[0])#header
def extractheader(header_):
     return header_.strip().split(',')
ourheader=extractheader(data_rows[0])
#print(ourheader)
def extractdata(data_line):
    splitted_data=[]
    #
    for val in zip(data_line.strip().split(',')):
    #for val,z in zip(data_line.strip().split(','),range(1,4)): #for only 4 columns in csv file
        #print(val)
        splitted_data.append(val)
    return splitted_data
#print(extractdata(data_rows[1]))
def  creatingdict(splitted_data,ourheader):
        dictofdata={}
        for values,header in zip (splitted_data,ourheader):
            dictofdata[header]=values
        return dictofdata
data1=extractdata(data_rows[1])
#print(creatingdict(data1,ourheader))
our_dataset_dictionaries=[]
for data_lines in data_rows[1:]:
    values__=extractdata(data_lines)
    dictionary_=creatingdict(values__,ourheader)
    our_dataset_dictionaries.append(dictionary_)
for our in our_dataset_dictionaries:
    print(our)
