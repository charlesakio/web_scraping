from bs4 import BeautifulSoup
import requests


while True:
	user_input = input("Enter url")
	request = requests.get(user_input)
	soup = BeautifulSoup(request.content)

	tag = soup.find_all('div', {"class": "landing-stack-name"})	#tag, {value: attribute}

	output = []
	for link in tag:
		output.append(link.text)	#Append to list called output

	#sorted_list = sorted(output) #Sort list alphabetically

	for word in output[:3]:	#Slice and print three elements only
		print('-' + word.strip('\n'))

	print('\n', user_input




# Resource for scraping ----> http://www.youtube.com/watch?v=3xQTJi2tqgk
# Resources for scraping look at github