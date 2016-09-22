#!/usr/bin/env python
# -*- coding: utf-8 -*-

import regex
import sys
from textblob import TextBlob as tb

use = ""

for line in sys.stdin:
		use += line.strip() + " "

#gets rids of [xyz]
use = regex.sub(r'\s?\[[\*\w]+\]\s?', '', use)
#gets rids of (xyz)
use = regex.sub(r'\s?\([^)]+\)\s?', "", use)
use = regex.sub(r'\s\s', " ", use)
# #gets rid of Supreme Court case numbers
# use = re.sub(r',\s\d{2,3}\sU\.S\.\s\d{2,3}[;,.]\s(?P<nums>\d{2,3})?-?(?P=nums)?[.,;]?', "", use)

# use = re.sub(r'[,.]\ssupra[,.]', " ", use)
# use = re.sub(r'  ', " ", use)

# print regex.findall(r'(blah\s)+', test)

# final = regex.findall(r'\s^(\.)*(\w\.)', use)

print use

# usetext = '\n'.join(text)

# usetext = usetext.split("OPIN", 1)[1]
# if "ordnote" in usetext:
# 	usetext = usetext.split("ordnote", 1)[0]
# else:
# 	usetext = usetext.split("ORDBV", 1)[0]

# usetext = re.sub(r'[^\x00-\x7F]', '', usetext)
# usetext = re.sub(r'[\n]{3,5}.*[\n]{3,5}', "", usetext)
# usetext = re.sub(r'\n{3,5}.*\n.*\n.*\n{3,5}', "", usetext)
# usetext = re.sub(r'\n\n', "\n", usetext)

# print usetext

# usetext = re.sub(r'[\n\r]{3,5}.*[\n]{3,5}', '', usetext)
# print usetext

# print re.findall(r'\n\x0c[502-561]+.*\n[502-561].*S\.\n', usetext, re.DOTALL)
