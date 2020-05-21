import bs4, requests, re

stateCapitalsDict = {}
stateCapitalsURL = 'https://simple.wikipedia.org/wiki/List_of_U.S._state_capitals'
stateCapitalsWiki = requests.get(stateCapitalsURL)

stateSoup = bs4.BeautifulSoup(stateCapitalsWiki.text, 'html.parser')

stateTable = stateSoup.findAll('table')[0]

stateRows = stateTable.findAll('tr')

for row in stateRows[2:]:
	cells = row.findAll('td')
	stateCapitalsDict[cells[0].text.lower()] = cells[3].text


while True:
	stateLookup = input('Enter state to find capital of, or type exit to quit: ')
	if stateLookup == 'exit':
		break
	elif stateCapitalsDict.get(stateLookup.lower(), 0) != 0:
		print(stateCapitalsDict[stateLookup.lower()])
	else:
		print('State not found.  Try again')