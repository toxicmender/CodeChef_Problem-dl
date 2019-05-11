#!/usr/bin/env python3
# -*- encoding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import pdfkit
import sys

def contests(flag):
	"""
	Returns a dictionary of Present[0], Future[1] or Past[2] Contests {Name: URL}
	"""
	with urllib.request.urlopen("https://www.codechef.com/contests") as response:
		contest_page = BeautifulSoup(response.read(), "html.parser")
	
	contests = contest_page.find_all("table", class_ = "dataTable")
	# [0] = Present, [1] = Future & [2] = Past
	urls = {}
	links = contests[flag].tbody.find_all("a")
	for link in links:
		urls[link.get_text()] = link.get("href")

	return urls

def problems(url):
	"""
	Returns a dictionary of Problems {Name: URL} from the contest passed as argument
	"""
	with urllib.request.urlopen(url) as response:
		problems_page = BeautifulSoup(response.read(), "html.parser")

	problems = problems_page.find_all("table", class_ = "dataTable")
	urls = {}
	links = problems[0].tbody.find_all("a", class_ = "ember-view")
	for link in links:
		urls[link.get_text()] = link.get("href")

	return urls

def urldict(url, flag):
	"""
	Returns a dictionary of URLs {Name: URL} from the contest passed as argument
	"""
	with urllib.request.urlopen(url) as response:
		problems_page = BeautifulSoup(response.read(), "html.parser")

	problems = problems_page.find_all("table", class_="dataTable")
	urls = {}
	links = problems[flag].tbody.find_all("a")
	for link in links:
		urls[link.get_text()] = link.get("href")

	return urls

# -------------------------------------------------------------------------------------------------
# Main Driver
# -------------------------------------------------------------------------------------------------

timing = input("Past, Present or Future Contest? [Past, Present, Future]: ")
if timing == "Past" or timing == "past":
	timing = 2
elif timing == "Present" or timing == "present":
	timing == 0
elif timing == "Future" or timing == "future":
	timing = 1
else:
	print("Try again with a valid value")
	sys.exit()

# -----------------------------------------------------------------------------
contests = urldict("https://www.codechef.com/contests", timing) # contests(timing)

enum = enumerate(contests.keys())
for contest in enum:
	print(contest[0] + 1, contest[1], sep = ". ")

index = input("Enter choice of contest [index number]: ") 

# -----------------------------------------------------------------------------
problems = urldict(contests[enum[index - 1][1]], 0) # problems(enum[index - 1][1])

enum = enumerate(problems.keys())
for problem in enum:
	print(contest[0] + 1, contest[1], sep = ". ")

index = input("Enter choice of problem [index number]: ") 

with urllib.request.urlopen(problems[enum[index - 1][1]]) as response:
	# pdfkit.from_file(response, str(enum[index - 1][1]) + ".pdf")
	with open("temp.html", "w") as filehandler:
		filehandler.write(response.read())

	# import os
	# os.path.realpath(__file__)
	# os.path.abspath(__file__)
	
	"""
	import sys, os

	print('sys.argv[0] =', sys.argv[0])             
	pathname = os.path.dirname(sys.argv[0])        
	print('path =', pathname)
	print('full path =', os.path.abspath(pathname)) 
	"""
	pdfkit.from_file("pdfs/temp.html", "pdfs/" + str(enum[index - 1][1]) + ".pdf")