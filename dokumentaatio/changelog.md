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


## Viikko 6

- Luotu aloitusnäkymä-toiminnallisuus tekemällä tarvittavat metodit renderer-, event_handler- ja ui-luokkiin
- Luotu yläluokka ui_service joka hoitaa event_handler- ja renderer-luokille yhteisten muuttujien alustuksen ja päivittämisen
- Testattu että GroupHandler palauttaa tyhjän ryhmän kun kutsutaan group-metodia, että elements-metodi palauttaa tyhjän listan tyhjälle ryhmälle ja lisätyt elementit sisältävän listan kun ryhmään on lisätty elementtejä, ja että add-metodi lisää elementin ryhmään
- Testattu että CollisionHandlerin handle_plasma_hits-metodi palauttaa ryhmiin lisättyjen yhteentörmäävien plasmojen ja asteroidien määrän

## Viikko 7

- Luotu PointRepository-luokka, joka vastaa pisteiden tallentamisesta ja lukemisesta.
- Luotu pistelistanäkymä-toiminnallisuus tekemällä tarvittavat metodit renderer-, event_handler- ja ui-luokkiin.
- Luotu erillinen lopetusnäkymä-toiminnallisuus tekemällä tarvittavat metodit renderer-, event_handler- ja ui-luokkiin.
  - Tähän kuuluu pisteiden tallentamisen toiminnallisuus.
- Luotu MenuLoop-, GameOverLoop-, ja PointsListLoop-luokat hoitamaan niitä vastaavien näkymien sovelluslogiikasta.
- Luotu Loop-luokka yleisille silmukkatoiminnoille.
- Refaktoroitu UIService-luokan perivät luokat käyttämään yhteistä, UIService-luokassa määriteltyä service_operation-metodia päätoimintojensa ajamiseen.
- Testattu Loop-luokka ja sen periviä luokkia.
