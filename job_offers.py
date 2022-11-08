import requests
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Import danych z API justjoin.it

r = requests.get("https://justjoin.it/api/offers")
dataset = r.json()

# Import aktualnego kursu średniego EUR do PLN z API NBP

eur = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
eur_to_pln = eur.json()
eur_to_pln = eur_to_pln["rates"][0]["mid"]

# Import aktualnego kursu średniego GBP do PLN z API NBP

gbp = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/gbp/")
gbp_to_pln = gbp.json()
gbp_to_pln = gbp_to_pln["rates"][0]["mid"]

# Import aktualnego kursu średniego USD do PLN z API NBP

usd = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/") 
usd_to_pln = usd.json()
usd_to_pln = usd_to_pln["rates"][0]["mid"]

# Tylko oferty pythona

i = 0
only_python = []

for job_offer in dataset:
    try: 
        for i in range(len(job_offer["skills"])):
            if (job_offer["skills"][i]["name"] == "Python"):
                   only_python.append(job_offer)
    except:
        pass

# ALL B2B

lower_salaries_b2b = []
higher_salaries_b2b = []

for job_offer in only_python:
    try: 
        if job_offer["employment_types"][0]["salary"]["currency"] == "pln" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["from"])
            higher_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["to"])
            
        if job_offer["employment_types"][0]["salary"]["currency"] == "eur" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["from"] * eur_to_pln)
            higher_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["to"] * eur_to_pln)
            
        if job_offer["employment_types"][0]["salary"]["currency"] == "gbp" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["from"] * gbp_to_pln)
            higher_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["to"] * gbp_to_pln)
            
        if job_offer["employment_types"][0]["salary"]["currency"] == "usd" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["from"] * usd_to_pln)
            higher_salaries_b2b.append(job_offer["employment_types"][0]["salary"]["to"] * usd_to_pln)
    except:
        pass
    
# ALL PERM  
    
lower_salaries_perm = []
higher_salaries_perm = []

for job_offer in only_python:
    try: 
        if job_offer["employment_types"][0]["salary"]["currency"] == "pln" and job_offer["employment_types"][0]["type"] == "permanent":
            lower_salaries_perm.append(job_offer["employment_types"][0]["salary"]["from"])
            higher_salaries_perm.append(job_offer["employment_types"][0]["salary"]["to"])
            
        if job_offer["employment_types"][0]["salary"]["currency"] == "eur" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_perm.append(job_offer["employment_types"][0]["salary"]["from"] * eur_to_pln)
            higher_salaries_perm.append(job_offer["employment_types"][0]["salary"]["to"] * eur_to_pln)
            
        if job_offer["employment_types"][0]["salary"]["currency"] == "gbp" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_perm.append(job_offer["employment_types"][0]["salary"]["from"] * gbp_to_pln)
            higher_salaries_perm.append(job_offer["employment_types"][0]["salary"]["to"] * gbp_to_pln)
            
        if job_offer["employment_types"][0]["salary"]["currency"] == "usd" and job_offer["employment_types"][0]["type"] == "b2b":
            lower_salaries_perm.append(job_offer["employment_types"][0]["salary"]["from"] * usd_to_pln)
            higher_salaries_perm.append(job_offer["employment_types"][0]["salary"]["to"] * usd_to_pln)
            
            
    except:
        pass
      
plt.hist(lower_salaries_b2b, bins = 30, alpha = 0.5, label = "from", color = "red")
plt.hist(higher_salaries_b2b, bins = 30, alpha = 0.5, label = "to", color = "blue")
plt.title("Python - B2B Job offers")
plt.xlabel("Earnings PLN")
plt.ylabel("Number of job offers")
plt.legend(loc = "upper right")
plt.show()

plt.hist(lower_salaries_perm, bins = 30, alpha = 0.5, label = "from", color = "red")
plt.hist(higher_salaries_perm, bins = 30, alpha = 0.5, label = "to", color = "blue" )
plt.title("Python - Permanent contract job offers")
plt.xlabel("Earnings PLN")
plt.ylabel("Number of job offers")
plt.legend(loc = "upper right")
plt.show()
      
