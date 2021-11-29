def find_busiest_period(data):
    max_timestamp = data[0][0]
    max_count = curr_count = 0
    for i in range(len(data) - 1):   
        if data[i][2]:
            curr_count += data[i][1]
        else:
            curr_count -= data[i][1]
        if i < len(data) - 1 and data[i + 1][0] != data[i][0]: continue
        if max_count < curr_count:
            max_timestamp, max_count = data[i][0], curr_count

    return max_timestamp

data = [[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,18,1],[1487901013,1,0],[1487901211,7,1],[1487901211,7,0]]   
data = [[1487799426,21,1]]
data = [[1487799425,14,1],[1487799425,4,1],[1487799425,2,1],[1487800378,10,1],[1487801478,18,1],[1487901013,1,1],[1487901211,7,1],[1487901211,7,1]]
print(find_busiest_period(data))
  