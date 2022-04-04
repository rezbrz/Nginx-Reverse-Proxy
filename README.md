# Nginx-Reverse-Proxy

1-Run "docker-compose up --build"

2-Run bellow curl command:

	curl -H "apikey:7B5zIqmRGXmrJTFmKa99vcit" http://api.userslocation.com:81/api/userslocation/users?userId=a2c
	
	possible values:{"a1b","a2c","b1b"}
	
	curl -XGET http://api.userslocation.com:81/api/userslocation/locations/1 
	
	possible values:{"1","2","3"}
	
3-possible values for apikey:{"7B5zIqmRGXmrJTFmKa99vcit","QzVV6y1EmQFbbxOfRCwyJs35","mGcjH8Fv6U9y3BVF9H3Ypb9T"}
