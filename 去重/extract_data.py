import pandas as pd
import redis

pool = redis.ConnectionPool(host='120.77.159.174', port=6379, db=12)
r = redis.Redis(connection_pool=pool)

result = []

all_links = r.smembers('guangdong_link')
sum = 0
for each in all_links:
    result.append(each.decode())
    sum=sum+1
    # print(result)
print(sum)
df = pd.DataFrame(result, columns=['link'])
df.to_csv('千里马广东8月11.csv', index=False)


# pool = redis.ConnectionPool(host='120.77.159.174', port=6379, db=12)
# r = redis.Redis(connection_pool=pool)
#
# result = []
#
# all_links = r.smembers('souce_link')
# sum = 0
# for each in all_links:
#     result.append(each.decode())
#     sum=sum+1
# print(result)
# print(sum)
# df = pd.DataFrame(result, columns=['link'])
# df.to_csv('千里马0611.csv', index=False)