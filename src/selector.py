#!/usr/bin/env python3
# -*- encoding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import argparse
import pdfkit

def contests(flag):
	"""
	Returns a dictionary of Present[0], Future[1] or Past[2] Contests {Name: URL}
	"""
	with urllib.request.urlopen("https://www.codechef.com/contests") as response:
		contest_page = BeautifulSoup(response.read(), "html.parser")
	
	contests = contest_page.find_all("table", class_="dataTable")
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

	problems = problems_page.find_all("table", class_="dataTable")
	urls = {}
	links = problems[0].tbody.find_all("a")
	for link in links:
		urls[link.get_text()] = link.get("href")

	return urls

def save():
	pdfkit.from_file("test.html", "out.pdf") 



parser = argparse.ArgumentParser(description='Get CodeChef Problems')
parser.add_argument("-s", "--set", choices=[0, 1, 2], default=2, type=int, 
					help="Select Past(2) or Present(0) Contest Problems")

args = parser.parse_args()

