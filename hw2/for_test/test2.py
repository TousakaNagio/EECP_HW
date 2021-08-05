a = [
  {
    "ip": "238.167.63.192",
    "city": "Denison"
  },
  {
    "ip": "242.134.236.156",
    "city": "Hackensack"
  },
  {
    "ip": "198.240.146.134",
    "city": "West Allis"
  }
]
if a[1]['ip'] > a[2]['ip']:
    print('t')
print(a[1]['ip'])
a[1],a[2] = a[2],a[1]
print(a[2]['ip'])