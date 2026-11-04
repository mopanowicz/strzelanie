# AGENTS.md — Wytyczne dla Agentów AI

Ten plik definiuje kontekst, konwencje i reguły spójności dla repozytorium **Systemu Treningu Strzeleckiego (Pistolet Praktyczny / Bojowy)**. Każda modyfikacja plików w tym projekcie musi respektować poniższe założenia.

---

## 1. Kontekst Domenowy i Konfiguracja Sprzętowa

Projekt jest spersonalizowanym, 12-tygodniowym programem treningowym oraz zestawem narzędzi analitycznych dla strzelca na poziomie **średniozaawansowanym**.

* **Broń:** Glock 47 (Gen5), kaliber 9x19 mm (IPSC Minor).
* **Spust / Przerywacz:** Ghost Ultimate 3.5 lb (~1,6–1,8 kg) — charakteryzuje się płynnym przełamaniem (*rolling break*), a nie twardą fabryczną ścianą. Rekomendowana technika pracy na spuście to *Smooth Roll* (płynne przewijanie), a w treningu na sucho tzw. „trik 1 centymetra” (reset bijnika bez wyrzucania zbijaka z komory).
* **Przyrządy celownicze:** Kolimator (Red Dot) — bezwzględny priorytet stanowi *Target Focus* (ostrość wzroku na celu, rozmyta kropka) oraz *Eye-Led Transitions* (oczy przeskakują na kolejny cel przed bronią).
* **Oporządzenie:** Kabura zewnętrzna OWB na pasie strzeleckim/taktycznym, 2–3 ładownice pistoletowe.
* **Narzędzia wspomagające:** Timer strzelecki (Par Time), tarcze redukcyjne (skala 1:3 / 1:4), zbijaki (snap caps), MantisX, system Laser Academy (nabój laserowy).
* **Reżim treningowy:**
  * **Dry Fire (trening bezstrzałowy):** 4–5 sesji w tygodniu po 15–25 minut (Jednostki A, B, C, D oraz opcjonalna E).
  * **Live Fire (trening strzelnicowy):** 1 sesja w miesiącu (łącznie 3 sesje w makrocyklu), ze sztywnym budżetem **200 szt. amunicji na sesję**.

---

## 2. Architektura Repozytorium i Zależności Między Plikami

* `README.md` — Przegląd projektu, specyfika techniczna platformy G47 + Ghost Ultimate + Red Dot oraz 4 złote zasady treningu (18:1 Dry/Live Fire).
* `01-plan-cyklu-12-tygodni.md` — Mapa drogowa podzielona na 3 mezocykle miesięczne (Miesiąc 1: Fundamenty/Odrzut, Miesiąc 2: Przejścia/Rytm, Miesiąc 3: Ruch/Zasłony).
* `02-program-dry-fire.md` — Szczegółowe plany jednostek Dry Fire (A–E), tabela skalowania tarcz w mieszkaniu i metodyka progresji Par Time (3 tryby prędkości).
* `03-karty-treningowe-live-fire.md` — 3 karty treningowe na strzelnicę. **Każda karta musi sumować się dokładnie do 200 szt. amunicji** i zaczynać od testu *Cold Start* (na zimno, bez rozgrzewki).
* `04-atlas-drilli-i-benchmarki.md` — Instrukcje wykonania drilli oraz tabela czasów bazowych, docelowych (12 tyg.) i eksperckich.
* `05-dziennik-postepow.md` — Szablony tabel do logowania wyników *Cold Start*, czasów Par Time oraz podsumowań sesji Live Fire.
* `hit_factor.py` — Skrypt Python 3 (zero zewnętrznych zależności poza biblioteką standardową) do wyliczania *Hit Factor* (IPSC Minor), analizy kosztu czasowego błędów (Charlie/Delta/Miss) oraz logowania wyników do `wyniki_hf.csv`.

---

## 3. Reguły Spójności przy Edycji (Krytyczne!)

1. **Synchronizacja Benchmarków (`04-atlas-drilli-i-benchmarki.md` ↔ `hit_factor.py` ↔ `05-dziennik-postepow.md`):**
   * Jeśli zmieniasz docelowe czasy lub liczbę strzałów dla drilli (`draw`, `pair`, `1r1`, `mozambik`, `bill`, `blake`, `elpres`) w pliku `04-atlas-drilli-i-benchmarki.md`, **musisz** zaktualizować słownik `BENCHMARKS` w pliku `hit_factor.py` (i odwrotnie).
2. **Bilans Amunicji w `03-karty-treningowe-live-fire.md`:**
   * Przy dodawaniu, usuwaniu lub modyfikacji ćwiczeń w kartach Live Fire zawsze przelicz kolumnę `Serie x Strzały` oraz `Suma szt.`. Całkowita liczba strzałów na każdej karcie musi wynosić **dokładnie 200 szt.**
3. **Punktacja IPSC Minor (`hit_factor.py`):**
   * Obowiązuje punktacja Minor (9x19 mm): **Alfa = 5 pkt, Charlie = 3 pkt, Delta = 1 pkt, Miss = -10 pkt, No-Shoot = -10 pkt, Procedura = -10 pkt**.
4. **Higiena Lasera vs Czysty Dry Fire (`02-program-dry-fire.md`):**
   * W pistoletach bijnikowych (Glock) nabój laserowy błyska tylko przy pierwszym strzale (kiedy iglica jest napięta). Wszystkie drille wielostrzałowe (*Doubles*, *Bill Drill*, *Blake Drill*, *El Presidente*) w Dry Fire należy rozpisywać pod pracę ze zwykłym zbijakiem i czytanie kropki kolimatora (*Calling Your Shots*), a nie pod nabój laserowy.

---

## 4. Styl, Język i Narzędzia Techniczne

* **Język komunikacji i dokumentacji:** Polski (z zachowaniem standardowej angielskiej terminologii strzeleckiej w nawiasach lub kursywą, np. *Target Focus*, *Bill Drill*, *Slide-lock*, *Smooth Roll*, *Cold Start*).
* **Wymagania dla kodu Python (`hit_factor.py`):**
  * Kompatybilność z **Python 3.10+** przy użyciu wyłącznie **biblioteki standardowej** (`argparse`, `csv`, `datetime`, `pathlib`, `sys`) — skrypt musi działać od ręki na każdym systemie bez instalacji paczek przez `pip`.
  * Zachowanie kompatybilności wstecznej struktury kolumn pliku `wyniki_hf.csv`:
    `data,tryb,drill,czas_s,strzaly,A,C,D,Miss,NoShoot,Proc,punkty,hit_factor,notatka`.
  * Testowanie zmian w skrypcie przed zakończeniem zadania:
    ```bash
    python3 hit_factor.py --benchmarks
    python3 hit_factor.py --drill bill -t 2.25 -a 6
    ```
