## Luokkakaavio monopolille

'''mermaid
  classDiagram
        Peli "1" --> "2..8" Pelaaja
        Peli "1" --> "2" Noppa
        Peli "1" --> "1" Pelilauta
        Ruutu "40" --> "1" Pelilauta
        Ruutu "1" --> "*" Pelinappula
        Pelaaja "1" --> "1" Pelinappula
        class Peli {
        }
        class Pelaaja {
        }
        class Pelilauta {
        }
        class Ruutu {
            seuraava_ruutu
        }
        class Pelinappula {
        }
        class Noppa {
        }
