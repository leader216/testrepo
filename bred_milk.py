def construct_dictionary_from_csv_file(filename):
    my_dictionary = {}
    milk=[]
    bread=[]
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line[0]=='m':
            m,m1,m2,m3=line.strip().split(',')
            l=[]
            l.append(float(m1))
            l.append(float(m2))
            l.append(float(m3))
            milk.append(l)
        if line[0]=='b':
            m,m1,m2,m3=line.strip().split(',')
            l=[]
            l.append(float(m1))
            l.append(float(m2))
            l.append(float(m3))
            bread.append(l)
    my_dictionary['milk']  = milk
    my_dictionary['bread'] = bread
     
                
           
    return my_dictionary
print(construct_dictionary_from_csv_file('E:\\py\\testfile2.csv')) 
