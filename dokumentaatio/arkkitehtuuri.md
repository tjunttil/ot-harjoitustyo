# Arkkitehtuurikuvaus

## Rakenne
Koodin rakenne on jakautunut hakemistotasolla seuraavasti: services-kansio sisältää pääasiallisesta sovelluslogiikasta vastaavat luokat, entities sisältää luokat objekteille joita pelilogiikka käsittelee, ja ui-kansio sisältää käyttöliittymän käsittelyyn liittyvät luokat.


## Käyttöliittymä
Käyttöliittymä koostuu tällä hetkellä kolmesta pääasiallisesta näkymästä, aloitusnäyttönäkymästä, pelinäkymästä ja lopetusnäkymästä. Näkymät on toteutettu EventHandler- ja Renderer-luokkien näille eriytetyillä metodeilla. Kunkin näkymän logiikalle on oma silmukkaluokkansa, joka perii Loop-luokan, ja UI-luokka ainoastaan kutsuu näiden silmukoiden aloitusmetodeita aiemman silmukan palautusarvon perusteella.


## Sovelluslogiikka
Pelilogiikka koostuu Space objektin sisältämien Ship-, Plasma-, ja Asteroid-entiteettien välisestä vuorovaikutuksesta. Luokkasuhteet on kuvattu alta löytyvässä kaaviossa.

```mermaid
 classDiagram
      Ship "1" -- "1" Space
      Plasma "*" -- "1" Space
      Asteroid "*" -- "1" Space
      Ship --|> Entity
      Plasma --|> Entity
      Asteroid --|> Entity
      class Entity{
          pos
          image
          rect
          direction
          velocity
      }
      class Ship{
          original_image
          angle
          angular_velocity
      }
      class Plasma{
      }
      class Space{
          all_sprites
      }
      class Asteroid{
          size
      }
```

Pelin korkeamman tason toiminnallisuus on toteutettu enimmäkseen luokan GameLoop kautta. GameLoop pyörittää pelisilmukkaa, kutsuen silmukan jokaisella kierroksella ui-kansion objektien metodeja hakeakseen käyttäjän syötteitä ja piirtääkseen pelinäkymän näytölle, ja näiden välissä kutsuu sille syötetyn Space-objektin metodeja päivittääkseen pelitilaa syötteiden mukaisesti. 

## Päätoiminnallisuudet

Seuraavassa pelin päätoiminnallisuuksia on kuvattu sekvenssikaavioin.

### Aluksen liikuttaminen eteenpäin

Alusta liikutetaan eteenpäin ylösnuolella. Alus liikkuu eteenpäin niin kauan kuin näppäin on painettu alas.

```mermaid

sequenceDiagram
  
    User ->> EventQueue: press up arrow
     
    EventHandler ->> EventQueue: get()
    
    activate EventQueue
    
    EventQueue -->> EventHandler: [pygame.event]
    
    deactivate EventQueue
    
    GameLoop ->> EventHandler: handle_events()
    
    activate EventHandler
    
    EventHandler ->> EventHandler: service_operation(event)
    
    EventHandler ->> EventHandler: handle_movement(event)
    
    EventHandler ->> GameLoop: commands (includes "move": ((1,0),5))
    
    deactivate EventHandler
    
    GameLoop ->> Space: change_ship_velocity((1,0),5)
    
    activate Space
    
    Space ->> Ship: change_velocity((1,0),5)
    
    activate Ship
    
    Ship -->> Space: 
    
    deactivate Ship
    
    Space -->> GameLoop: 
    
    deactivate Space
    
```

Gameloop kutsuu toistuvasti EventHandleriä saadakseen uusia käskyjä, ja EventHandler saa EventQueuen tallentaman napinpainalluksen käsiteltäväksi. Se muuntaa tämän käskyksi muuttaa aluksen nopeutta, jonka se välittää GameLoopille. GameLoop kutsuu Spac-luokan change_ship_velocity-metodia jolla aluksen nopeutta muutetaan, joka taas kutsuu Ship-luokan vastaavaa metodia. 

## Plasman ampuminen

Plasman ampuminen onnistuu välilyöntinäppäimellä. Toisin kuin liikkuessa, näppäimen pitäminen painettuna ei johda tapahtuman toistumiseen. 

```mermaid

sequenceDiagram
  
    User ->> EventQueue: press space bar
     
    EventHandler ->> EventQueue: get()
    
    activate EventQueue
    
    EventQueue -->> EventHandler: [pygame.event]
    
    deactivate EventQueue
    
    GameLoop ->> EventHandler: handle_events()
    
    activate EventHandler
    
    EventHandler ->> EventHandler: service_operation(event)
    
    EventHandler ->> EventHandler: handle_game_event(event)
    
    EventHandler ->> GameLoop: commands (includes "fire": True)
    
    deactivate EventHandler
    
    GameLoop ->> Space: fire_ship_cannon()
    
    activate Space
    
    Space ->> Ship: get_tip()
    
    activate Ship
    
    Ship -->> Space: tip_location
    
    deactivate Ship
    
    Space ->> plasma: Plasma(tip_location, ship.direction)
    
    Space ->> Space: add_entity(plasma)
    
    Space -->> GameLoop: 
    
    deactivate Space
    
    
```

Tapahtumaketjun alku on lähes identtinen aiempaan verrattuna. Ero tulee EventHandlerin lähettämässä käskyssä, joka tällä kertaa sisältää arvon True avaimelle "fire". Nyt GameLoop kutsuu taas Space-luokan metodia fire_ship_cannon, joka luo uuden Plasma-olion Ship-olion palauttamaan kärjen paikkaan, ja tallentaa tämän avaruuden entiteettien joukkoon.  

## Pisteiden tallentaminen

```mermaid

sequenceDiagram

    activate GameOverLoop
  
    User ->> EventQueue: enter username and press Return
     
    EventHandler ->> EventQueue: get()
    
    activate EventQueue
    
    EventQueue -->> EventHandler: [pygame.event]
    
    deactivate EventQueue
    
    GameOverLoop ->> EventHandler: handle_events()
    
    activate EventHandler
    
    EventHandler ->> EventHandler: service_operation(event)
    
    EventHandler ->> EventHandler: game_over_operation(event)
    
    EventHandler -->> GameOverLoop: commands (includes "input": username, "save": True)
    
    deactivate EventHandler
    
    GameOverLoop ->> GameOverLoop: handle_commands(commands)
    
    GameOverLoop ->> PointRepository: add(username, points)
    
    activate PointRepository
    
    PointRepository ->> PointRepository: write()
    
    PointRepository -->> GameOverLoop: 
    
    deactivate PointRepository
    
    deactivate GameOverLoop
    
```
Perustoiminnallisuus pisteiden tallennuksessa käyttöliittymän osalta on sama kuin aiemmin kuvatuissa tapauksissa. Tällä kertaa sovelluslogiikkaa pyörittää GameOverLoop, joka saa EventQueuen ja EventHandlerin välittämänä käskyn ensin ottaa vastaan käyttäjän syöttämän nimen, ja sitten tallentaa tämän ja käyttäjän pelistä saaman pistemäärän. GameOverLoop kutsuu PointRepositoryn add-metodia lisätäkseen käyttäjän tiedot, joka taas kutsuu omaa write-metodiaan tallentaakseen päivitetyn pistetilanteen pysyväistallennukseen.
