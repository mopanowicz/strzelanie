# AGENTS.md — Karta treningowa kontroli odrzutu

Poniższe wytyczne dotyczą wyłącznie karty treningowej kontroli odrzutu i jej wersji do druku w tym katalogu.

## Zawartość treningu

- [pistolet-kontrola-odrzutu.md](./pistolet-kontrola-odrzutu.md) zawiera kartę *Live Fire* dla poziomu D (początkujący): 10 ćwiczeń na 200 sztuk amunicji, wskazówki dotyczące chwytu i *Dot Tracking* oraz diagnostykę przestrzelin na tarczy „Linie prawdy”.
- [pistolet-kontrola-odrzutu.pdf](./pistolet-kontrola-odrzutu.pdf) to dwustronicowa wersja tej karty do druku.
- Powiązany materiał o normach czasowych dla dobycia i dwóch trafień znajduje się w [technika/dobycie-2xAlpha.md](../../technika/dobycie-2xAlpha.md); ten plik nie należy do bieżącego katalogu.

## Spójność karty

- Po zmianie ćwiczeń sprawdź każde mnożenie w kolumnie `Serie x Strzały` względem `Suma szt.` oraz ponownie zsumuj całą kartę. Wynik musi wynosić dokładnie **200 szt. amunicji**.
- Przy zmianie norm czasowych zachowaj spójność wzoru:
  $$\text{Czas całkowity} = t_{\text{1. strzał}} + (n - 1) \times t_{\text{split}} + t_{\text{przeładowanie}}$$
- Punkty odniesienia dotyczą strzelania z 7 m, z kabury OWB, do strefy Alpha:
  * **Klasa D (początkujący):** pierwszy strzał `1.90–2.40 s`, split `0.35–0.50 s`, dublet `2.30–2.90 s`, *Bill Drill* `3.80–4.80 s`.
  * **Klasa C (średniozaawansowany):** pierwszy strzał `1.50–1.75 s`, split `0.25–0.32 s`, dublet `1.75–2.05 s`, *Bill Drill* `2.75–3.35 s`.
  * **Klasa B (zaawansowany):** pierwszy strzał `1.25–1.35 s`, split `0.18–0.22 s`, dublet `1.45–1.55 s`, *Bill Drill* `2.15–2.45 s`.
  * **Klasa A / Master (ekspert):** pierwszy strzał `0.90–1.10 s`, split `0.14–0.17 s`, dublet `1.05–1.25 s`, *Bill Drill* `1.60–1.95 s`.
- Jeśli zmiana karty wpływa na PDF, zaktualizuj również [pistolet-kontrola-odrzutu.pdf](./pistolet-kontrola-odrzutu.pdf). Nie zakładaj istnienia lokalnego szablonu HTML — przed generowaniem ustal źródło użyte do składu PDF.

## Wymagania dla PDF

- Format: A4 poziomo, marginesy `7.5mm 9.5mm`, dokładnie 2 strony.
- **Strona 1:** nagłówek sekcji 1, checklista tarcz w 3 kolumnach oraz pełna tabela ćwiczeń 1–10 z wierszem `SUMA AMUNICJI`; tabela nie może dzielić się między stronami.
- **Strona 2:** sekcja 2 z kluczowymi wskazówkami technicznymi oraz sekcja 3; części A i B diagnostyki w dwóch kolumnach, część C jako wyróżniony blok u dołu strony.
- Czcionka podstawowa: `"Noto Sans", "DejaVu Sans", "Liberation Sans", sans-serif`. Symbole strzałek (`→` / `&rarr;`) składaj czcionką `"DejaVu Sans", sans-serif`.
- Wydruk powinien zachować kolory tła tabel i ramek (`-webkit-print-color-adjust: exact; print-color-adjust: exact;`).
- Po wygenerowaniu sprawdź liczbę stron i wymiary:
  ```bash
  pdfinfo pistolet-kontrola-odrzutu.pdf
  ```
  Oczekiwane: `Pages: 2` oraz `Page size: 841.92 x 594.96 pts (A4)`.
- W razie potrzeby sprawdź wygląd stron, renderując podgląd:
  ```bash
  pdftoppm -png -r 150 pistolet-kontrola-odrzutu.pdf page_preview
  ```
