# Script that generates an HTML document with extracted information

import json

f = open("data.json")
db = json.load(f)

print("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Artículos Adbusters en español</title>
</head>
<body>
<table>
<tr>
  <th>Title</th>
  <th>Summary</th>
  <th>Author</th>
  <th>tags</th>
  <th>Date</th>
  <th>Image URL</th>
</tr>
""")
for article in db:
  print("<tr>")
  print("<td><a href=\"" + article['url'] + "\">" + "".join(article['title']).strip() + "</a></td>")
  print("<td>" + "".join(article['summary']).strip() + "</td>")
  print("<td>")
  for author in article['author']: print(author + ", ")
  print("</td>")
  print("<td>")
  for tag in article['tags']: print(tag + ", ")
  print("</td>")
  print("<td>" + "".join(article['pubdate']).strip() + "</td>")
  print("<td>" + "".join(article['picture_url']) + "</td>")
  print("</tr>")

print("""
</table>
</body>
""")
