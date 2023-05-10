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

