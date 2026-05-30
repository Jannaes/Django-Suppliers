# Django Suppliers

Django-pohjainen CRUD-sovellus toimittajien, tuotteiden, asiakkaiden ja tilausten hallintaan.

## Projektin kuvaus

Sovelluksen avulla voidaan ylläpitää yrityksen toimittaja-, tuote-, asiakas- ja tilaustietoja. Kirjautuneet käyttäjät voivat lisätä, muokata, hakea ja poistaa tietoja 
selainkäyttöliittymän kautta.

Sovellus sisältää käyttäjätunnistautumisen, jonka avulla tietojen hallinta on rajattu kirjautuneille käyttäjille.

## Käytetyt teknologiat

- Python
- Django
- SQLite (kehitysympäristö)
- PostgreSQL (Render-tuotantoympäristö)
- Bootstrap

## Asennus

Kloonaa repositorio:
git clone https://github.com/Jannaes/Django-Suppliers.git

Luo virtuaaliympäristö:
python -m venv venv

Aktivoi virtuaaliympäristö 

- Windows:
venv\Scripts\activate

- Linux / macOS
source venv/bin/activate

Asenna riippuvuudet:
pip install -r requirements.txt

Suorita tietokantamigraatiot:
python manage.py migrate

Luo ylläpitokäyttäjä:
python manage.py createsuperuser

Käynnistä sovellus:
python manage.py runserver

Avaa selain:
http://127.0.0.1:8000

## Julkaisu

Sovellus on julkaistu myös Render-palveluun:
https://suppliers-9732.onrender.com

## Kehityskohteita

Projektin jatkokehitysideoita:

- Tilausrivit (OrderLine)
- Useita tuotteita yhdelle tilaukselle
- Sivutus (pagination)
- REST API
- Yksikkötestit
- Käyttöliittymän kehittäminen modaalien avulla

## Kehittäjä

Tehty oppimisprojektina ja tavoitteena oli harjoitella:

- Django MVC/MVT -arkkitehtuuria
- CRUD-toimintoja
- Tietokantojen käyttöä
- Käyttäjätunnistautumista
- Sovelluksen julkaisemista pilvipalveluun (Render)

## Lisenssi

Tämä projekti on tarkoitettu oppimiseen ja portfoliokäyttöön.
