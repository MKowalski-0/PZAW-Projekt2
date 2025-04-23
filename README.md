Jest to drugi projekt zaliczeniowy DJANGO

Jest możliwość że będzie trzeba pobrać kilka rzeczy:

Pillow:
`python -m pip install Pillow`

Przepisy dodaje się w panelu admina
Aby dodać przepis należy stworzyć superużytkownika za pomocą komendy:
`python manage.py createsuperuser`

Jak uruchomić?:

1. Sklonuj repozytorium za pomocą komendy `git clone https://github.com/MKowalski-0/PZAW-Projekt2.git`

2. Stwórz i uruchom środowisko wirtualne:
   `python -m venv venv`
   `source venv/bin/activate`
   
3. Użyj komendy `cd <NAZWA_FOLDERU>` dopóki nie dotrzesz do folderu zawierającego plik manage.py

4. Strona może wymagać migracji po sklonowaniu z githuba
`python ./manage.py migrate`

5. Wystartuj stronę za pomocą komendy:
   `python ./manage.py runserver`




