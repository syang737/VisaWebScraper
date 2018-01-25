from lxml import html
from bs4 import BeautifulSoup
import requests
import re
page = requests.get('https://www.mzv.cz/consulate.newyork/en/visa_and_consular_information/visa/approved_visa/long_term_visa_approved.html')

print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

article_body = soup.find('div', attrs={'class': 'article_body'})

ids = soup.find_all(string=re.compile('NEWY'))

sameDayIds = soup.find_all(string=re.compile('NEWY20171207'))

FileName = 'oldIds.txt'
with open(FileName) as f:
	content = f.read().splitlines()
content = [x.strip() for x in content ]

newContent=[]
for i in ids:
	i = i.strip() # take out whitespaces before and after
	index = i.index('NEW')
	if( index > 0 ):
		i = i[index:len(i)]
	newContent.append(i)

# compare content and newContent
diff = list(set(newContent) - set(content))

if(len(diff) == 0):
	print("No new Ids approved today.")
else:
	print("New Ids approved today:")
	for i in diff:
		print(diff[i])

oldIdFile_w = open(FileName, 'w')
for i in newContent:
	oldIdFile_w.write(i+'\n')

for i in ids:
	if i == 'NEWY201712070014':
		print("Your visa has been approved!")
		exit()

print('Your visa (NEWY20170014) has not been approved yet.')
