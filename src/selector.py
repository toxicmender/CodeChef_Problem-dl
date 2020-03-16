#!/usr/bin/env python3
# -*- encoding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import pdfkit
import sys

def contesturls(flag):
    """
    Returns a dictionary of {"Present": 0, "Future": 1, "Past": 2} Contests {Name: URL}
    """
    req = urllib.request.Request("https://www.codechef.com/contests", headers = {"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        contest_page = BeautifulSoup(response.read(), "html.parser")
        contests = contest_page.find_all("table", class_ = "dataTable")
        # [0] = Present, [1] = Future & [2] = Past
        urls = {}
        links = contests[int(flag)].tbody.find_all("a")
        for link in links:
            urls[link.get_text()] = link.get("href")
        return urls

def problemurls(url):
    """
    Returns a dictionary of Problems {Name: URL} from the contest passed as argument
    """
    req = urllib.request.Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
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
    req = urllib.request.Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
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

tim = input("Past, Present or Future Contest? [Past, Present, Future]: ").lower()
timing = {"present": 0, "future": 1, "past": 2}

if tim not in timing.keys():
    print("Try again with a valid value")
    sys.exit()

# -----------------------------------------------------------------------------
# contests = urldict("https://www.codechef.com/contests", timing) # contesturls(timing)
conurls = contesturls(timing[tim])
enum = enumerate(conurls.keys())
for contest in enum:
    print(contest[0] + 1, contest[1], sep = ". ")

index = int(input("Enter choice of contest [index number]: "))

# -----------------------------------------------------------------------------
print("https://www.codechef.com" + conurls[list(conurls.keys())[index - 1]].split("?")[0])
problems = problemurls("https://www.codechef.com" + conurls[list(conurls.keys())[index - 1]].split("?")[0]) # problems(enum[index - 1][1])

enum = enumerate(problems.keys())
for problem in enum:
    print(problem[0] + 1, problem[1], sep = ". ")

index = int(input("Enter choice of problem [index number]: "))

with urllib.request.urlopen(problems[list(problems.keys())[index - 1]]) as response:
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