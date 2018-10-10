#!/usr/bin/env python2
import yagmail
from bs4 import BeautifulSoup
soup = BeautifulSoup('html.parser')
import urllib2

def sendJobs(to, subject, body, mail, password):
    """ For sending results of a web scraping to email"""
    yag = yagmail.SMTP(mail, password)
    # --sending the message
    yag.send(to = to, subject = subject, contents = body)

if __name__ == "__main__":
    #--receiver email address
    mail = "kzabuk@gmail.com"
    #--long string that stores raw list of jobs found on a website
    jobs = ""
    #--url of a job hunting website which is used for webscraping
    url = 'https://slo-tech.com/delo'
    #--raw HTML response from a website
    response = urllib2.urlopen(url)
    #--new BS object for dealing with a HTML response
    soup = BeautifulSoup(response)
    #--each job is stored in a 'tr' tag which have an 'a' tag for every information
    table = soup.findAll('tr')
    #--looping throu all the job listings and retriving links that containes the desired info.
    #--result is then appended to 'jobs' string and every job is starting with '$' for later string processing.
    for row in table:
        tabeldata = row.findAll("td")
        jobs = jobs + "\n" + "$"
        for oglas in tabeldata:
            naziv = oglas.findAll('a')
            for a in naziv:
                jobs = jobs + a.text.encode('utf-8') + "\n"
                    
    #--one log string 'jobs' gets separated in a list of separate jobs
    separateJobs = jobs.split("$")
    #--technology parameters for displaying the jobs I had worked before
    listOfPosition = ['junior', 'backend', 'html', 'css', 'js', 'javascript', 'frontend', 'Java', 'python', 'github']
    body = ""
    for job in separateJobs:
        job = job.lower()
        #--looping over parameters in a list and adding them to a string 'body'
        if any(x in job for x in listOfPosition):
            subject = "Job positions for today."
            body = body + job
        else:
            subject = "No job positions."


sendJobs(mail, subject, body, email, password )