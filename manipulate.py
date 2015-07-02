from bs4 import BeautifulSoup
import requests

def scrape():
	"""
	Request http from specified url and parse it through BeautifulSoup
	"""
	#url = "http://stackshare.io/languages-and-frameworks"
	url = input("Enter url")
	request = requests.get(url)
	soup = BeautifulSoup(request.content)
	return soup

def url_add(word):
	return 'http://stackshare.io/%s' % word

def manipulate(sorted_list):
	"""
	Replaces space on each element of sorted_list into '-'
	and changes every element into lowercase
	"""
	new_list = []

	for word in sorted_list:
		url = url_add(word)
		new_list.append(url.replace(' ', '-').lower().strip('(...)'))
	return new_list


def print_name_and_url(sorted_list, manipulated_list):
	for sort, man in zip(sorted_list, manipulated_list):
		print(sort, " -----\n", man)


#-----------------------------------------------------------------------------------------
soup = scrape() 
tag = soup.find_all('a', {"class": "stack-service-name-under"})	#tag, {value: attribute}


output = []
for word in tag:
	output.append(word.text)

sorted_list = output
manipulated_list = manipulate(sorted_list)

print_name_and_url(sorted_list, manipulated_list)
print("Length of list :", len(sorted_list))

