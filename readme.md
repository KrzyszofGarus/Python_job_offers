# Przykład użycia biblioteki requests oraz przetwarzanie danych

Moim zadaniem było sprawdzenie średnich widełek płacowych ofert dla programistów Pythona ze strony https://justjoin.it/

Użyłem biblioteki requests aby zaimportować dane z API
```py
import requests

# Import danych z API justjoin.it

r = requests.get("https://justjoin.it/api/offers")
dataset = r.json()
```

