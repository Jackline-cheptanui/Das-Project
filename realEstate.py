import csv
from abc import ABC,abstractmethod

# initializing the titles and rows list
fields = []
rows = []
data=[]

with open('real-estate.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)

	for row in csvreader:
		rows.append(row)

	print("Total no. of rows: %d"%(csvreader.line_num))

class SortCSV(ABC):

    @abstractmethod
    def sortData(self):
        pass

class SortData(SortCSV):
    def  __init__(self, data):
        self.data = data
    def sortData(self):
        if len(self.data) >1:
            m = len(self.data)
            l =  self.data[1:m]
            r = self.data[m:]

            lSort = SortData(l)

            rSort = SortData(r)

            p = m=k=0
            while p< len(l) and m < len(r):
                if l[p][1] < r[m][1]:
                    self.data[k] = l[p]
                    p +=1
                
                else:
                    self.data[k]=r[m]
                    m+=1
                k+=1
            
            while p < len(l):
                self.data[k] = l[p]
                p+=1
                k+=1
            
            while m < len(r):
                self.data[k] = r[m]
                m+=1
                k+=1
        
        print(self.data)

with open('real-estate.csv', 'r') as file:
            reader = csv.reader(file)
            data.extend(list(reader))
sorted = SortData(data)
print(sorted.sortData())



# field names
fields = ['zpid', 'statusType', 'statusText', 'CountryCurrency','price','badgeInfo','list','beds']

# data rows of csv file
rows =  [['5336782189', 'FOR_SALE', 'House for sale', '$','$600000','forsale','FALSE','9'],
		['3444847889', 'FOR_SALE', 'House for sale', '$','$440000','Null','TRUE','3'],
		['77585785', 'FOR_SALE', 'New', '$','$550000','forsale','FALSE','4'],
		['99980492', 'FOR_SALE', 'Active', '$','$220000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','FALSE','2'],
        ['23434456', 'FOR_SALE', 'Land for sale', '$','$4500000','Null','FALSE','5'],
		['77585785', 'FOR_SALE', 'New', '$','$100000','forsale','FALSE','4'],
		['999898776', 'FOR_SALE', 'Active', '$','$300000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$960000','Forsale','TRUE','2'],
        ['23434456', 'FOR_SALE', 'Land for sale', '$','$4500000','Null','FALSE','5'],
        ['112766566', 'FOR_SALE', 'House for sale', '$','$4230000','Forsale','TRUE','7'],
        ['748378846', 'FOR_SALE', 'New', '$','$33078789','Null','FALSE','4'],
        ['564876872', 'FOR_SALE', 'House for sale', '$','$7493789','Forsale','TRUE','3'],
        ['884938394', 'FOR_SALE', 'NotActive', '$','$6876878','Null','FALSE','4'],
        ['5336782189', 'FOR_SALE', 'House for sale', '$','$600000','forsale','FALSE','5'],
		['3444847889', 'FOR_SALE', 'House for sale', '$','$440000','Null','TRUE','3'],
		['77585785', 'FOR_SALE', 'New', '$','$550000','forsale','FALSE','4'],
		['999898776', 'FOR_SALE', ' NotActive', '$','$220000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','TRUE','2'],
        ['23434456', 'FOR_SALE', 'House for sale', '$','$4500000','Null','FALSE','5'],
        ['112766566', 'FOR_SALE', 'House for sale', '$','$4230000','Forsale','TRUE','7'],
        ['564876872', 'FOR_SALE', 'House for sale', '$','$7493789','Forsale','TRUE','3'],
        ['884938394', 'FOR_SALE', 'Active', '$','$6876878','Null','FALSE','4']]

#  csv file
filename = "realstatehouse.csv"

# csv file
with open(filename, 'w') as csvfile:
	# program showing  csv writer objec
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(rows)