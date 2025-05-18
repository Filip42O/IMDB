<h1 align="center">
 <strong>IMPERIUM MITÓW, DEZINFORMACJI I BREDNI (IMDB)</strong> 🟧⬛
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/status-alpha-ff9900?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.8+-000000?style=flat-square&logo=python" alt="Python">
</p>

---

## 📖 Opis projektu

Aplikacja do zarządzania rankingiem filmów, która umożliwia użytkownikom organizację, przeglądanie i śledzenie ocen. Dzięki niej każdy kinomaniak może:

- Dodawać filmy do listy obejrzanych  
- Oceniać i komentować tytuły  
- Wyszukiwać filmy po pełnym lub częściowym tytule  
- Filtrować i sortować kolekcję  
- Eksportować dane do pliku tekstowego  
- Generować statystyki (gatunki, średnie oceny, top1) i wizualizować je na co najmniej 3 wykresach  
- Zarządzać kontami użytkowników i systemem logowania  
- Obsługiwać co najmniej 10 różnych wyjątków dla stabilności działania

---

## 🚀 Funkcje

1. **Dodawanie filmów** do listy obejrzanych  
2. **Ocenianie & Komentowanie** – przypisz gwiazdki i zostaw krótką recenzję  
3. **Wyszukiwanie**: „Jurassic” → Jurassic World, Jurassic Park…  
4. **Filtrowanie & Sortowanie** według gatunku, oceny, nazwy  
5. **Eksport** kolekcji do pliku TXT/CSV  
6. **Statystyki & Wykresy** (matplotlib) – min. 3 różne wizualizacje  
7. **Zarządzanie użytkownikami**: dodawanie, edycja, usuwanie, logowanie  
8. **Obsługa wyjątków**: eleganckie komunikaty przy błędach I/O, nieprawidłowych komend itp.

---

## 🧠 F.I.L.T.R.O.N. – Filmowy Indeks Lokalizacji Tytułów i Rekomendacji Organizowany Naukowo™

> *"Widział wszystko. I nadal szuka dalej."*

F.I.L.T.R.O.N. to nasz własny, niepokorny, cyfrowy bibliotekarz.  
Nie tylko wyszukuje tytuły — on **penetruje zakamarki Twojej kolekcji**, wydobywając z niej perły… i te rzeczy, których lepiej już nie pokazywać.

---

### 🔍 Co potrafi?

- **Przeszukuje bazę filmów** błyskawicznie, nawet po fragmentach tytułów  
  – wpisz `matrix`, a dostaniesz całą trylogię i bonusowo coś z VHS  
- **Szanuje Twoje wybory** (nawet jeśli są niezręczne)  
- **Filtruje, sortuje, selekcjonuje**  
- **Współpracuje z eksportem i statystykami** — zero błędów, czysta analiza  
- Działa lepiej, im gorzej traktujesz swoje filmy

---

### 🧪 Dlaczego „Organizowany Naukowo”?

Bo F.I.L.T.R.O.N. nie opiera się na "czuciu", "magii" ani "algorytmach z TikToka".  
On **parsuje**, **indeksuje** i **porządkuje**. W pliku `.txt`. Z dumą.

I robi to szybko. Nawet za szybko.

---

### 💸 Ale czy jest Open Source?

> Tak. Ale tylko dlatego, że jeszcze nie znaleźliśmy nikogo, kto by za to płacił. 🤝

---

### ⚠️ Uwaga końcowa

🔧 Jeśli coś nie działa – to nie F.I.L.T.R.O.N.  
To Ty.

---

## 📂 Struktura katalogów

```text
├── models/          # Klasy encji: Film, Użytkownik, Ocena, Komentarz
├── storage/         # Warstwa zapisu/odczytu (JSON/SQLite)
├── services/        # Logika aplikacji (add, search, filter, export)
├── ui/              # Interfejs CLI (parser komend)
├── stats/           # Generowanie statystyk i wykresów
├── exceptions/      # Definicje własnych wyjątków
├── tests/           # Testy jednostkowe (opcjonalnie)
├── main.py          # Główny punkt wejścia
└── README.md        # Dokumentacja projektu
