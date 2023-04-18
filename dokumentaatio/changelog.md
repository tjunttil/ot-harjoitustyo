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
