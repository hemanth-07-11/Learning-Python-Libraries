# Write a Python program to get the number of paragraph tags of a given html document.

from bs4 import BeautifulSoup 
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>HEMANTH N</title>
</head>
<body>
<h2>HEMANTH</h2>
<p>
when there are a lot of events possible, the probability of any specific event is very low,virtually zero probablity. But some low probability event is guaranteed to occur.
</p>
<p><a href="https://cricbuzz.com">Check Scores
</a></p>
<p><a href="https://cricbuzz.com">Check Scores
</a></p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
ptag_count = len(soup.find_all('p'))
print(ptag_count)
