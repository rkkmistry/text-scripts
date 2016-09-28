# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

use = sys.stdin.read()

#gets rid of single \n
use = re.sub(r"([^\n\r])\r\n([^\n\r])", r"\1 \2", use)
use = re.sub(r'  ', " ", use)

# gets rids of (xyz)
use = re.sub(r'\(([^()]*|\([^()]*)\)*\)', "", use)

# gets rids of [xyz]
use = re.sub(r'\s?\[([\*\w]{2,}|\d+)\]\s?', ' ', use)

# text = ""
# text = re.sub(ur'\W\d{1,4}\s[\w\. ]{1,20}\s§?\d{1,4}\W', '', text, re.UNICODE)

# print text

# re.match(r'^/by_tag/(?P<tag>\w+)/(?P<filename>(\w|[.,!#%{}()@])+)$', u'/by_tag/påske/øyfjell.jpg', re.UNICODE)


#for the main citation
use = re.sub(r'\W\d{1,4}\s[\w\. ]{1,20}\s\d{1,4}\W', '', use)
#for the page nums after citation
use = re.sub(r'[.,]\D\d+-?\d+?[.,]', '', use)
#for floating digits
use = re.sub(r'\d{1,4}\s[\w\. ]{1,20},', '', use)
#for "at 139" etc.
# r',\s*?at [^A-Za-z]{1,4},'

#OLD STUFF
# use = re.sub(r'[,.]\ssupra[,.]', " ", use)
# use = re.sub(r'  ', " ", use)

# usetext = '\n'.join(text)


use = re.sub(r'[ ]{2,}', " ", use)
print use