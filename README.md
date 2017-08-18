# lookup
provides corresponding ip address or hostname for given input

## Usage
```
./lookup.py list
facebook.com             31.13.69.228
twitter.com              104.244.42.65
google.com               172.217.6.238
youtube.com              172.217.12.206
linkedin.com             108.174.10.10
```


```
./lookup.py google.com
google.com 172.217.6.238
```


```
./lookup.py list | awk '{print $1}'
facebook.com
twitter.com
google.com
youtube.com
linkedin.com
```

```
./lookup.py list | awk '{print $2}'
31.13.69.228
104.244.42.1
172.217.12.206
172.217.6.238
108.174.10.10
```