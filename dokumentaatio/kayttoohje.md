# Käyttöohje

## Käynnistäminen
Ennen ensimmäistä käyttökertaa, aja komentoriviltä:

```bash 
poetry install
```

ja

```bash
poetry run invoke build
```

Tämä asentaa vaadittavat riippuvuudet ja alustaa pistetilastointitiedoston.

Käynnistäminen onnistuu tämän jälkeen komennolla

```bash
poetry run invoke start
```

## Pelin aloittaminen

Ohjelman aloitusnäkymä on seuraava:

![](./kuvat/aloitusnäkymä.png)

Ohjeistuksen mukaisesti käyttäjä voi tästä Enter-näppäintä painamalla aloittaa uuden pelin, tai L-näppäintä painamalla siirtyä tarkastelemaan pistelistoja. Painamalla Enteriä näkymäksi tulee tämä:

![](./kuvat/pelinäkymä.png)

## Pelaaminen

Alusta liikutetaan nuolinäppäimillä, ylänuolella eteen, alanuolella taakse, ja vasemmalla ja oikealla nuolinäppäimellä alusta saa käännettyä. Pelinäkymään ilmestyy asteroideja, joita pelaajan tulisi yrittää aluksella tuhota. Tämä onnistuu painamalla välilyöntinäppäintä, mikä laukaisee plasma-ammuksia. 

![](./kuvat/asteroidien_ampuminen.png)
