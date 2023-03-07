# Projekt NBP Exchange Rates
Projekt NBP Exchange Rates jest aplikacją webową służącą do pobierania i 
przechowywania danych kursów walut z API Narodowego Banku Polskiego za pomocą bazy 
danych PostgreSQL i ich wyświetlania przy wykorzystaniu końcówki GET.
Projekt wykonany za pomocą biblioteki Django REST Framework


## ***Instalacja***

Aby zainstalować projekt, wykonaj następujące kroki:

1. Sklonuj repozytorium z GitHuba:
```bash
git clone https://github.com/NazwaTwojegoRepozytorium.git
```
2. Przejdź do katalogu projektu:
```bash
cd nbp-exchange-rates
```
3. Zainstaluj wymagane pakiety za pomocą poetry:
```bash
poetry install
```
4. Zainicjuj bazę danych Postgres za pomocą docker-compose
```bash
sudo docker-compose up -d
```
5. Przeprowadź migracje bazy danych:
```bash
python manage.py migrate
```

## ***Użycie***
Aby uruchomić aplikację, wykonaj poniższe kroki:

1. Uruchom serwer deweloperski:
```bash
python manage.py runserver
```
2. Przejdź do przeglądarki internetowej i wpisz w pasek adresu
```http request
http://localhost:8000/ 
```
Zostaniesz przekierowany na stronę główną aplikacji.
Jeżeli chcesz przejść bezpośrednio do API to na pasku adresu przejdź do 
```http request
http://127.0.0.1:8000/nbp/exchange_rates/
```
## ***Endpoints***
#### POST 
```
nbp/exchange_rates/
```
Endpoint służący do pobierania danych kursów walut z API NBP. Dane zostaną zapisane w bazie danych.

#### GET
```
nbp/exchange_rates/
```
Endpoint służący do pobierania danych kursów walut z bazy danych.

## ***Management commands***
Projekt zawiera dodatkową komendę Django **clear_db**, która usuwa wszystkie rekordy z 
bazy danych. Aby uruchomić tę komendę, należy wpisać następujące polecenie w konsoli:

```bash
python manage.py clear_db --confirm
```
Komenda ta może być przydatna podczas testowania aplikacji lub przywracania 
początkowych danych w bazie. **Pamiętaj jednak, że wykonanie tej komendy spowoduje 
trwałe usunięcie danych i nie może być cofnięte.** 

Używaj jej z ostrożnością!


# Autorzy
Projekt został stworzony przez Michała Nowaka.