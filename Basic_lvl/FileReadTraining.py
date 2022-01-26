
filePath = r'C:\\Temp\\data_input\\order.csv'

with open(filePath, 'r') as file:
    for line in file:
        line=line.replace('\n','')
        order =line.split(',')
        if len(order) == 3:
            print('Order from "%s", item "%s", amount %s' % (order[0], order[1], order[2]))
        else:
            print('Line %s is malformed.' % line)