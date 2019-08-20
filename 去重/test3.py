import csv,re
with open('剑鱼0611.csv', newline='') as f:
    reader = csv.reader(f)
    data = []
    for i in reader:
        for j in i:
            try:
                if j != 'link':
                    j = re.sub(r'http://|https://', '', j).strip()
                    j = re.sub(r'[%|?|:|）|（|。|、|→|【|】|“|”|,|，|(]\w*', '', j).strip()
                # print(row)
                    data.append(''.join(j))
            except:
                pass
    # print(data)
with open('千里马0611.csv',newline='') as file:
    reader = csv.reader(file)
    data2 = []
    for i in reader:
        for j in i:
            try:
                if j != 'link':
                    j = re.sub(r'http://|https://', '', j).strip()
                    j = re.sub(r'[%|?|:|）|（|。|、|→|【|】|“|”|,|，|(|@]\w*', '', j).strip()
                    data2.append(''.join(j))
            except:
                pass
    # print(data2)
# 把剑鱼相同的链接从千里马中去重
    for List in data:
        for List2 in data2:
            if List2 in List:
                data2.remove(List2)
    print ("List : ", data2)
    sum = 0
    for i in data2:
        sum = sum+1
    print(sum)
