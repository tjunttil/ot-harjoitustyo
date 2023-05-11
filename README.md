# Asteroidit

Sovellus on peli, jossa käyttäjä ohjaa avaruusalusta. Tavoitteena on tuhota tielle osuneet asteroidit.


## Dokumentaatio

- [Käyttöohje](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Testaus](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)


## Asennus

Sovelluksen ajaminen ongelmitta edellyttää vähintään python version 3.8.

1. `poetry install` asentaa sovelluksen riippuvuudet
2. `poetry run invoke build` alustaa sovelluksen käyttämän pistetiedoston
3. `poetry run invoke start` käynnistää sovelluksen


## Komentorivikomennot

### 1. Käynnistys

Kuten jo edellä todettiin, sovelluksen saa käynnistettyä käskyllä: 

`poetry run invoke start`

### 2. Testaus

Testit saa ajettua käskyllä:

`poetry run invoke test`

Testikattavuusraportti tuotetaan käskyllä:

`poetry run invoke coverage-report`

### 3. Pylint

Sovelluksen pylint-tarkistukset voi selvittää käskyllä:

`poetry run invoke lint`

