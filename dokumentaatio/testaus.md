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

## Integraatiotestaus

## Järjestelmätestaus

### Asennus

### Toiminnallisuus
