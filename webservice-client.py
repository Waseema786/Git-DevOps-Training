import requests
# import json	


if __name__ == "__main__":
	api_url = "http://localhost:8080/search?term="
	while True:
		key = input("Insert keyword to search (\\0 to exit): ")
		if key == "\\0":
			break
		request = api_url + key
		response = requests.get(request)
		# print("Result: %s", response.json().loads(data.decode("utf-8")))
		print("Result: ", response.text)

		
	