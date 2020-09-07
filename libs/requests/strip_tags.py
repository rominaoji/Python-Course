#!/usr/bin/python

import requests as req
import re

resp = req.get("http://webcode.me")

content = resp.text

stripped = re.sub('<[^<]+?>', '', content)
print(stripped)
