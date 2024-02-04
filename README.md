# Dokumentacja Projektu Gry "2048" w Pygame

## Spis Treści

- [Wprowadzenie](#wprowadzenie)
- [Technologie](#technologie)
- [Struktura Projektu](#struktura-projektu)
- [Opis Głównych Funkcji](#opis-głównych-funkcji)
- [Uruchamianie Gry](#uruchamianie-gry)
- [Sterowanie](#sterowanie)
- [Rozgrywka](#rozgrywka)
- [Rozwój Projektu](#rozwój-projektu)
- [Autor](#autor)

## Wprowadzenie

Projekt przedstawia implementację popularnej gry "2048" w języku Python, wykorzystując bibliotekę Pygame. Celem gry jest łączenie płytek z takimi samymi liczbami w celu osiągnięcia płytki o wartości 2048.

## Technologie

- Python 3.x
- Pygame
- Numpy

## Struktura Projektu

Projekt składa się z jednego pliku źródłowego, który zawiera całą logikę gry, w tym inicjalizację Pygame, logikę gry, rysowanie interfejsu użytkownika oraz obsługę zdarzeń.

## Opis głównych funkcji

- `add_new_tile()`: Funkcja odpowiedzialna za dodawanie nowej płytki na planszy.
- `can_combine_tiles()`: Sprawdza, czy istnieją płytki, które mogą zostać połączone.
- `is_game_over()`: Określa, czy gra została zakończona.
- `has_won()`: Określa, czy gracz osiągnał kafelek 2048.
- `update_score(value)`: Aktualizuje wynik gracza.
- `combine_tiles(row)`: Łączy płytki.
- `move_tiles(direction)`: Obsługuje logikę przesuwania płytek w zadanym kierunku.
- `handle_input(event)`: Obsługuje wejście interakcyjne klawiszy klikanych przez użytkownika.
- `draw_ui()`: Rysuje interfejs użytkownika, w tym planszę gry i wynik, gdy gracz wygrał rysuję odpowiednią wiadomość i możliwość resetowania gry, tak samo w przypadku przegranej.
- `reset_game()`: Resetuje grę, tablicę i wszystkie zmienne.
- `show_start_screen()`: Pokazuje ekran startowy.
- `main()`: Główna pętla gry.

## Uruchamianie Gry

Aby uruchomić grę, wystarczy uruchomić plik źródłowy w interpreterze Pythona z zainstalowanymi bibliotekami z pliku requirements.txt.

```bash
py -m pip install -r requirements.txt

py 2048.py
```

Jeżeli nie posiadasz zainstalowanego Pythona na swoim komputerze -> plik 2048.exe znajduję się w folderze dist oraz utoworzony jest skrót w głównym folderze. Możesz włączyć aplikację bez Pythona i instalowania potrzebnych bibliotek.
Pamiętaj, jeżeli włączasz aplikację .exe, musisz mieć, również pobrane foldery z dist (images i fonts), aby poprawnie odpalić aplikację. Najlepiej cały folder dist wrzuć na pulpit. W folderach znajdują się niezbędne czcionki i ikony do włączenia aplikacji.

## Sterowanie

- Spacja - rozpoczęcie gry na ekranie początkowym.
- Strzałki Góra/Dół/Lewo/Prawo - do łączenia kafelek.
- Enter - resetowanie gry na ekranie końcowym po przegranej.

## Rozgrywka

- Uzyskaj jak największy wynik, uważaj abyś logicznie łączył kafelki i nie przegrał poprzez maksymalne wypełnienie tablicy (bez możliwości łączenia następnych sąsiadujących kafelek jeżeli nie mają tych samych wartości). Zdobądź kafelek 2048 a wygrasz grę.

## Rozwój Projektu

W przyszłości projekt może zostać rozwinięty o dodatkowe funkcjonalności, takie jak tablica wyników, możliwość cofania ruchów czy różne poziomy trudności.

## Autor

- Jakub Mączka 52737 Ćw5N INF. I. sem.
