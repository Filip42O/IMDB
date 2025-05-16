<h1>
 IMPERIUM MITÓW, DEZINFORMACJI I BREDNI (IMDB) 🟧⬛
</h1>


<p align="center">
  <img src="https://img.shields.io/badge/status-alpha-ff9900?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.8+-000000?style=flat-square&logo=python" alt="Python">
</p>

---

## <span style="color:#ff9900;">📖 Opis projektu</span>

Aplikacja do zarządzania rankingiem filmów, która umożliwia użytkownikom organizację, przeglądanie i śledzenie ocen. Dzięki niej każdy kinomaniak może:

- Dodawać filmy do listy obejrzanych  
- Oceniać i komentować tytuły  
- Wyszukiwać filmy po pełnym lub częściowym tytule  
- Filtrować i sortować kolekcję  
- Eksportować dane do pliku tekstowego  
- Generować statystyki (gatunki, średnie oceny, top1) i wizualizować je na co najmniej 3 wykresach  
- Zarządzać kontami użytkowników i systemem logowania  
- Obsługiwać co najmniej 10 różnych wyjątków dla stabilności działania :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## <span style="color:#ff9900;">🚀 Funkcje</span>

1. **Dodawanie filmów** do listy obejrzanych  
2. **Ocenianie & Komentowanie** – przypisz gwiazdki i zostaw krótką recenzję  
3. **Wyszukiwanie**: „Jurassic” → Jurassic World, Jurassic Park… :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
4. **Filtrowanie & Sortowanie** według gatunku, oceny, nazwy  
5. **Eksport** kolekcji do pliku TXT/CSV  
6. **Statystyki & Wykresy** (matplotlib) – min. 3 różne wizualizacje  
7. **Zarządzanie użytkownikami**: dodawanie, edycja, usuwanie, logowanie  
8. **Obsługa wyjątków**: eleganckie komunikaty przy błędach I/O, nieprawidłowych komend itp.

---

## <span style="color:#ff9900;">📂 Struktura katalogów</span>

```text
├── models/          # Klasy encji: Film, Użytkownik, Ocena, Komentarz
├── storage/         # Warstwa zapisu/odczytu (JSON/SQLite)
├── services/        # Logika aplikacji (add, search, filter, export)
├── ui/              # Interfejs CLI (parser komend)
├── stats/           # Generowanie statystyk i wykresów
├── exceptions/      # Definicje własnych wyjątków
├── tests/           # Testy jednostkowe (opcjonalnie)
└── README.md        # Dokumentacja projektu
