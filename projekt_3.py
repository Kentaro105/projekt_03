"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Keltner
email: dawekeltner71@gmail.com
discord: davidk8500
"""

import requests
import re
import csv
import sys
from bs4 import BeautifulSoup

link = sys.argv[1]
kraj = re.search(r'kraj=([^&]+)', link).group(1)
numnuts = re.search(r'numnuts=(\d+)', link).group(1)


def get_town_id ():
    get_link_code = requests.get(link)
    soup = BeautifulSoup(get_link_code.text, "html.parser")
    map_tables = soup.find("div", {"id" : "outer"}).find_all("table")
    town_ids = []
    for table in map_tables:
        get_rows = table.find_all("tr")    
        for row in get_rows[2:]:
            get_id = row.find("td").get_text()
            if not get_id == "-": #empty table field check
                town_ids.append(get_id)
    return town_ids          



list_of_values = []
header_created = False #header row created just once

for id in get_town_id():
    town_link = requests.get(f"https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj={kraj}&xobec={id}&xvyber={numnuts}")
    soup = BeautifulSoup(town_link.text, "html.parser")
    city = soup.find("div", {"id" : "publikace"}).find_all("h3")
    city_value = re.sub("Obec: ", "", city[2].get_text()).replace("\n", "")
    header_table = soup.find("div", {"id" : "publikace"}).find("table").find_all("tr")
    header_table_data = header_table[2].find_all("td")
    registered = re.sub("\xa0","",header_table_data[3].get_text())
    envelops = re.sub("\xa0","",header_table_data[6].get_text())
    valid = re.sub("\xa0","",header_table_data[7].get_text()).replace(" ","")

    #Create header row
    if not header_created:
        header_row = ["ID", "City", "Registered", "Envelops", "Valid"]
        votes_tables = soup.find("div", {"id" : "publikace"}).find_all("table")
        for table in votes_tables[1:]:
            find_rows = table.find_all("tr")
            for row in find_rows[2:]:
                find_votes = row.find_all("td")
                party = find_votes[1].get_text()
                if not party == "-": #empty table field check
                    header_row.append(party)
        list_of_values.append(header_row)
        header_created = True

    #Create data rows
    data_row = [id, city_value, registered, envelops, valid]        
    votes_tables = soup.find("div", {"id": "publikace"}).find_all("table")
    for table in votes_tables[1:]:
        find_rows = table.find_all("tr")
        for row in find_rows[2:]:
            find_votes = row.find_all("td")
            votes = re.sub("\xa0","",find_votes[2].get_text())
            if not votes == "-": #empty table field check
                data_row.append(votes)
    list_of_values.append(data_row)

#create csv file 
with open(sys.argv[2], "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(list_of_values)