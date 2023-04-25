# Changelog

## Viikko 2

- vaatimusmäärittelyn laatiminen


## Viikko 3

- Luotu GameLoop-luokka, joka vastaa sovelluksen käyttöliittymästä
- Luotu Space-luokka, joka vastaa sovelluslogiikasta ja pitää kirjaa erilaisista sprite-olioista
- Luotu Ship-luokka, joka vastaa avaruusaluksen toiminnallisuudesta
- Luotu testejä Ship- ja Space-olioiden luomiselle ja Ship-olion liikuttamiselle.


## Viikko 4

- Saatu alus liikkumaan ja kääntymään oikein


## Viikko 5

- Luotu Plasma-luokka, joka edustaa aluksen ampumia plasmapalluroita.
- Lisätty toiminnallisuus, jossa Ship-olio pystyy välilyöntinäppäimellä ampumaan 
Plasma-olioita.
- Luotu Entity-luokka käytettävien sprite-olioiden yläluokaksi, joka hoitaa näille 
yhteiset alustustoimenpiteet ja määrittelee yhteiset päivitys- ja liikkumismetodit 
joita Space-olio voi kutsua.
- Korjattu testejä vastaamaan uutta luokkarakennetta.
- Luotu Asteroid-luokka, joka edustaa asteroideja.
- Lisätty toiminnallisuus asteroid-olioiden tuottamiselle ja niiden piirtämiselle näytölle.
- Lisätty toiminnallisuus asteroidien, aluksen ja plasmojen törmäämisen tarkistamiseen.
- Lisätty toiminnallisuus pelin päättymiseen asteroidin ja aluksen törmätessä.
- Lisätty toiminnallisuus asteroidin tuhoutumiselle plasman osuessa ja tästä pisteiden saamiselle.
- Lisätty pisteiden näkyminen pelinäytöllä.
- Lisätty pelin lopetusnäkymä, jossa näkyy pelaajan saamat pisteet.
- Refaktoroitu koodia merkittävästi, seuraavalla tavalla:
  - Luotu uudet luokat yleisimmille pygame-toiminnoille: Clock, Renderer, Event_handler, Event_queue.
  - Luotu erillinen UI-luokka joka alustaa ja käynnistää käyttöliittymän.
- Testattu että gameloop aiheuttaa oikeat muutokset kun käskyinä tulee pelin lopettaminen tai aluksen nopeuden muutos.
- Testattu että plasman ampuminen lisää plasman Space-luokan plasmas-ryhmään, ja että tuotetun plasman suunta on sama kuin aluksen.
