#!/usr/bin/env python2
import datetime
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
    mail = "kzabuk@gmail.com"
    jobs = ""
    url = 'https://slo-tech.com/delo'
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response)
    table = soup.findAll('tr')
    for row in table:
        tabeldata = row.findAll("td")
        jobs = jobs + "\n" + "$"
        for oglas in tabeldata:
            naziv = oglas.findAll('a')
            for i, a in enumerate(naziv):
                jobs = jobs + a.text.encode('utf-8') + "\n"
                    

    separateJobs = jobs.split("$")
    listOfPosition = ['junior', 'backend', 'html', 'css', 'js', 'javascript', 'frontend']
    body = ""
    for job in separateJobs:
        job = job.lower()
        if any(x in job for x in listOfPosition):
            # if any(x in str for x in a):
            subject = "Job positions for today."
            body = body + job
        else:
            subject = "No job positions."
            


sendJobs(mail, subject, body, email, password )