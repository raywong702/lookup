# lookup
Provides corresponding ip address or hostname for given input

## Usage
Lookup will write EXCEPTION if cannot be resolved
Inputs need not be uniform. Can be a mixture of ip and hostname

### Pass in hostnames file
```
./lookup.py hostnames
facebook.com             31.13.69.228
twitter.com              104.244.42.129
google.com               172.217.12.142
youtube.com              172.217.12.142
linkedin.com             108.174.10.10
...
```

### Pass in ip file
```
./lookup.py ips
31.13.69.228     edge-star-mini-shv-01-iad3.facebook.com
104.244.42.1     104.244.42.1
172.217.11.14    lga25s60-in-f14.1e100.net
172.217.11.46    lga25s61-in-f14.1e100.net
108.174.10.10    108-174-10-10.fwd.linkedin.com
...
```

### Command line pass in hostname
```
./lookup.py facebook.com
facebook.com 31.13.69.228
```

### Command line pass in mixture of ip and hostnames
```
./lookup.py 31.13.69.228 twitter.com google.com
31.13.69.228 edge-star-mini-shv-01-iad3.facebook.com
twitter.com  104.244.42.65
google.com   172.217.10.14
```

### Print only inputs
```
./lookup.py hostnames | awk '{print $1}'
facebook.com
twitter.com
google.com
youtube.com
linkedin.com
...
```

### Print only outputs
```
./lookup.py hostnames | awk '{print $2}'
31.13.69.228
104.244.42.1
172.217.12.206
172.217.6.238
108.174.10.10
...
```

### Write to file
```
./lookup.py hostnames | tee hostnames.out
twitter.com              104.244.42.129
google.com               172.217.12.142
youtube.com              172.217.12.142
linkedin.com             108.174.10.10
...
```