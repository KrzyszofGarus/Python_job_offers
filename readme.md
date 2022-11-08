# Przykład użycia biblioteki requests oraz przetwarzanie danych

Moim zadaniem było sprawdzenie widełek płacowych ofert dla programistów Pythona ze strony https://justjoin.it/

Użyłem biblioteki requests aby zaimportować dane z API co dało mi 17441 ofert na moment wykonania zapytania
```py
import requests

# Import danych z API justjoin.it

r = requests.get("https://justjoin.it/api/offers")
dataset = r.json()
```

Niektóre oferty były w innych walutach niż PLN co popchnęło mnie do zapoznania się z API NBP - wynikiem czego jest poniższy kod dający średni kurs EUR do PLN
```py
# Import aktualnego kursu średniego EUR do PLN z API NBP

eur = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
eur_to_pln = eur.json()
eur_to_pln = eur_to_pln["rates"][0]["mid"]
```

Aby przefiltrować dataset i wyłowić oferty z Pythona użyłem prostej pętli - musiałem dodać licznik "i" aby dokładnie przejrzeć "skills" - nie zawsze Python był na tej samej pozycji - otrzymałem 1488 ofert

```py
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
```

Kolejnym krokiem było rozdzielenie ofert B2B i analogicznie ofert na umowę o pracę wraz przeliczeniem walut

```py
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
```
Poniższe dwa histogramy są wynikiem przetworzenia ofert - im wyższy słupek tym więcej ofert z taką stawką - kolorem czerwonym oznaczono wartości początkowe widełek
a końcowe niebieskim

![b2b_python](https://user-images.githubusercontent.com/117105005/200651885-0ab41fd2-7a19-47b6-92c1-de6c8b3d1745.png)
![perm_python](https://user-images.githubusercontent.com/117105005/200651894-749f2ce2-8782-4ca8-a2fa-c826191b1d81.png)


Wnioski są proste - opłaca się być programistą ;)

![python_army](https://user-images.githubusercontent.com/117105005/200650987-9574ae0f-8ff9-4203-8b7a-cfb2a2d23c30.jpg)



