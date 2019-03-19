'''
This program will pull number facts from the Numbers API
'''

import urllib.request
import bs4

base_link = "http://numbersapi.com" 

#---------------------------------------------------------------------------------
def get_html_on_page(link):
    response = urllib.request.urlopen(link)
    html = response.read().decode()
    return html
    
def get_number_trivia(number):
    number=str(number)
    link = base_link+"/"+number
    return get_html_on_page(link)

def get_date_trivia(month, day):
    month=str(month)
    day=str(day)
    link=base_link+"/"+month+"/"+day+"/date"
    return get_html_on_page(link)

def get_random_fact(type):
    link=base_link+"/random/"+type
    return get_html_on_page(link)

# num = get_number_trivia(42)
# print(num)
#
# date = get_date_trivia(2,13)
# print(date)
#
# trivia = get_random_fact("trivia")
# print(trivia)
#
# year = get_random_fact("year")
# print(year)
#
# randate = get_random_fact("date")
# print(randate)
#
# math = get_random_fact("math")
# print(math)
