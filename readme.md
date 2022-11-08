# Przykład użycia biblioteki requests oraz przetwarzanie danych

Moim zadaniem było sprawdzenie średnich widełek płacowych ofert dla programistów Pythona ze strony https://justjoin.it/

Użyłem biblioteki requests aby zaimportować dane z API
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
