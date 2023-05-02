# Vaatimusmäärittely


## Sovelluksen tarkoitus

Sovellus on peli, jossa käyttäjän tavoitteena on tuhota näytöllä lipuvia 
asteroideja ohjaamallaan avaruusaluksella. Sovellus myös pitää kirjaa pelaajan 
saamista pisteistä ja pelissä käytetystä ajasta, joista molemmista on saatavilla 
sijoituslistaukset.

## Perusversion tarjoama toiminnallisuus


### Ennen pelin aloitusta

- Käyttäjä voi aloittaa uuden pelin painamalla Enteriä (tehty)
- Käyttäjä voi valita haluaako hän tarkastella tuloslistoja vai aloittaa uuden 
pelin

### Tuloslistan tarkastelu

- Listassa on pelaajat ja heidän saamansa pistemäärät listattuna pistemäärien mukaisessa järjestyksessä suurimmasta pienimpään

### Pelin aloituksen jälkeen

- Käyttäjä pystyy ohjaamaan avaruusalusta nuolinäppäimillä (tehty)
- Käyttäjä pystyy ampumaan avaruusaluksen lasertykillä välilyöntinäppäimellä (tehty)
- Asteroideja ilmestyy ruudun reunojen takaa satunnaisesti (tehty)
- Avaruusalus tuhoutuu ja peli päättyy jos alus törmää asteroidiin (tehty)
- Asteroideja pystyy tuhoamaan lasertykillä, mistä saa pisteitä (tehty)
- Pelaajan pistemäärä näkyy näytöllä (tehty)
- Pelin päätyttyä käyttäjä voi tallentaa tuloksensa tuloslistaan syöttämällä 
pelaajanimen


## Jatkokehitysideoita

- Avaruusaluksen liikemäärä vähenee tasaisesti
- Pelikentän topologia on torus
- Näytön taustana on tähtitaivas
- Asteroideja on erikokoisia, joista pienempiä on vaikeampi tuhota
- Suuremmat asteroidit eivät vain häviä, vaan hajoavat pienemmiksi (jotka 
säilyttävät suuremman asteroidin liikemäärän)
- Asteroideja ilmestyy yhä useammin pelin edetessä, eli peli vaikeutuu
- Näytöllä näkyy pelin kesto
- Tuloslistassa on listattuna myös pelaajien pelissä selviämä aika, ja käyttäjä voi 
valita kumman mukaan lista järjestetään
