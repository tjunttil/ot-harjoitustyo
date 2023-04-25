# Asteroidit

Sovellus on peli, jossa käyttäjä ohjaa avaruusalusta. Tavoitteena on tuhota tielle osuneet asteroidit.

## Asennus

1. `poetry install` asentaa sovelluksen riippuvuudet
2. `poetry run invoke start` käynnistää sovelluksen

## Komentorivikomennot

1. ### Käynnistys

Kuten jo edellä todettiin, sovelluksen saa käynnistettyä käskyllä 

`poetry run invoke start`

2. ### Testaus

Testit saa ajettua käskyllä

`poetry run invoke test`

Testikattavuusraportti tuotetaan käskyllä

`poetry run invoke coverage-report`

3. ### Pylint

Sovelluksen pylint-tarkistukset voi selvittää komennolla
`poetry run invoke lint`


## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/tjunttil/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
