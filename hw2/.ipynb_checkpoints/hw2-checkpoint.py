# some useful python standard libraries
import csv, json, sys
from random import randint
import ipaddress

def readIPData(json_file):
    """(10 pt) Return the a list of dictionary of raw data
    
    json_file : the directory of db.json
    
    e.g. [{
            "ip":"238.167.63.192",
            "city": "Denison"
          },
          {
            "ip": "242.134.236.156",
            "city": "Hackensack"
          },
          ...
            ]
    """
    with open(json_file, "r") as f:
        observe = json.load(f)
    return observe
    pass

def readQuery(query_file):
    """(10 pt) Return a list of query IPs    
    
    query_file : the directory of query.csv
    
    e.g. ["238.167.63.192", "242.134.236.156", ...]
    
    """
    a = []
    with open(query_file) as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            a.append(row['ip'])
    return a
    pass

def writeAns(array, ans_file):
    """(10 pt) Write query answer to csv file
    
    array : response answer of each query 
    ans_file : output file directory
    
    output csv should be in this format:
    
    ip,city
    238.167.63.192,Denison
    242.134.236.156,Hackensack
    8.8.8.8,-1
    ...
    
    """
    with open(ans_file,'w',newline='') as csvfile:
        Writer = csv.writer(csvfile)
        Writer.writerows(array)
    pass

def sortIP(IPList):
    """(25 pt) Sort the list with each IPs and return the sorted list of dictionary
    
    IPList : the list of dictionary generated with readIPData()
    
    """
    def quicksort(data,low,high):
        def partition(data,low,high): 
            i = low              
            j = high
            key = data[low]["ip"]               
            while i != j:                  
                while data[j]["ip"] > key and i < j:   
                    j -= 1
                while data[i]["ip"] <= key and i < j:  
                    i += 1
                if i < j:
                    data[i]["ip"], data[j]["ip"] = data[j]["ip"], data[i]["ip"] 
            data[low],data[i] = data[i],data[low]
            return i
        if low < high: 
            k = partition(data, low, high) 
            quicksort(data, low, k-1) 
            quicksort(data, k+1, high) 
        return data
    return quicksort(IPList,0,len(IPList)-1)
    pass

def binarySearch(array, IP, start, end):
    """(25 pt) perform binary search on a sorted list of dictionaries
    
    return the city of specified IP 
    return -1 if query IP not found
    
    """
    low = start
    high = end

    while low <= high:
        mid = (low+high)//2
        guess = array[mid]['ip']

        if guess == IP:
            return array[mid]['city']
        if guess > IP:
            high = mid -1 
        else:
            low = mid +1
    return -1
    pass

def test_hw2(raw, query, ans):
    """
    combine above works
    (20 pt) if your script complete in 3 seconds 

    """
    db = readIPData(raw)
    query = readQuery(query)
    sortedIP = sortIP(db)
    response = []
    for q in query:
        r = binarySearch(sortedIP, q, 0, len(sortedIP))
        response.append([q, r])
    writeAns(response, ans)

if __name__ == "__main__":
    test_hw2(sys.argv[1], sys.argv[2], sys.argv[3])

