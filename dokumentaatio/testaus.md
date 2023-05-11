# Testausdokumentti

## Yksikkötestaus

### Sovelluslogiikka

Sovelluslogiikka on jaoteltu useamman luokan välille:
- Loop
- GameLoop
- MenuLoop
- GameOverLoop
- ScoreListLoop
- Space
- Ship
- GroupHandler
- CollisionHandler
- CoordinateSystem

Näille kullekin on tehty omat yksikkötestinsä omilla testausluokillaan toiminnallisuuden testaamiseksi, ja varmistettu että perustoiminnallisuus vastaa odotuksia myös poikkeuksellisissa tilanteissa. 

### Repositoriot

Sovelluksessa on yksi repositorio, PointRepository, johon tallennetaan ja josta luetaan pelaajien pistetuloksia. Tätä on testattu TestPointRepository-luokassa, jossa käydään läpi yleisimmät perustoiminnallisuudelta vaadittavat tilanteet.  

### Testauskattavuus

Haarautumakattavuudeksi testeille saatiin 87%

![](./kuvat/coverage-report.png)

Testauksen ulkopuolelle jäivät käyttöliittymästä vastaavat luokat. Testauksessa on puutteita erityisesti ongelmallisten syötteiden käsittelyn tarkistamisessa.

## Integraatiotestaus

Korkeamman tason luokkien, kuten Loop-tyypin-, ja Space-luokkien testit sisältävät väkisinkin useamman luokan yhteentoimivuuden testaamista. Näissä oli joskus kuitenkin tarpeen määritellä erillisiä testeihin käytettäviä paikanpitäjiä (esim StubRenderer tai FakeSpace) testauksen yksinkertaistamiseksi.

## Järjestelmätestaus

Järjestelmätestaus on tapahtunut manuaalisesti kehittäjän toimesta.

### Asennus

Asennus ja käyttö on testattu macOS- ja Linux-koneilla. 

### Toiminnallisuus

Suurin osa vaatimusmäärittelyssä mainitusta toiminnallisuudesta on testattu sekä automaattisin unittestein että manuaalisesti. Ainoastaan pistelistanäkymän aikajänteen vaihtaminen jäi kokonaan testaamatta.
