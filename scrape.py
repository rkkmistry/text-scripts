from lxml import html
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

text = list()

for x in range(11):
    page = requests.get("http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=master-of-none-2015&episode=s01e" + str(x).zfill(2))
    tree = html.fromstring(page.content)
    printbuyers = tree.xpath('//div[@class="scrolling-script-container"]/text()') 
    for line in printbuyers:
        line = line.replace("\r", "")
        re.sub(r'[^\x00-\x7F]+',' ', line)
        text.append(line.strip())


print "\n".join(text)
