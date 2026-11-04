# System Treningu Strzeleckiego: Pistolet Praktyczny / Bojowy (Red Dot + OWB)

Kompleksowy, 12-tygodniowy (3-miesięczny) program treningowy zaprojektowany pod kątem **maksymalnego transferu umiejętności z codziennego treningu bezstrzałowego (Dry Fire 4–5x w tygodniu) na comiesięczną sesję weryfikacyjną na strzelnicy (Live Fire 1x w miesiącu, 200 szt. amunicji)**.

---

## 🎯 Profil Strzelca i Konfiguracja
* **Poziom:** Średniozaawansowany (opanowane bezpieczeństwo i statyka, budowanie dynamiki).
* **Zastosowanie:** Pistolet praktyczny / obronny / bojowy.
* **Platforma:** **Glock 47 (Gen5)** + przerywacz **Ghost Ultimate 3.5 lb**, kolimator (**Red Dot**), kabura zewnętrzna (**OWB**) na pasie strzeleckim/taktycznym, 2–3 ładownice pistoletowe.
* **Narzędzia treningowe:** Timer strzelecki (Par Time), tarcze redukcyjne (mini IPSC/IDPA), zbijaki, system MantisX / Laser Academy.
* **Struktura czasowa:**
  * **Dry Fire:** 4–5 sesji tygodniowo po 15–25 minut.
  * **Live Fire:** 1 sesja w miesiącu (90–120 minut, ok. 200 szt. amunicji).

---

## 🔫 Specyfika Platformy: Glock 47 + Ghost Ultimate 3.5 + Kolimator

Glock 47 łączy pełnowymiarowy zamek i lufę (jak w G17) ze skróconym występem szkieletu (dust cover) i krótszym urządzeniem powrotnym (jak w G19/G45). W połączeniu z lżejszym przerywaczem **Ghost Ultimate 3.5 lb** daje to bardzo szybki zestaw, który wymaga uwzględnienia 3 detali technicznych:

1. **Kąt chwytu Glocka (22°) a szukanie kropki „nad oknem”:**
   * Najczęstszy błąd przy przesiadce na Glocka z kolimatorem to wyprowadzanie broni z lufą zadartą lekko w górę – kropka znika wtedy ponad górną krawędzią szybki.
   * **Rozwiązanie:** Wbij ostrogę chwytu maksymalnie głęboko w błonę między kciukiem a palcem wskazującym prawej dłoni, a **małym i serdecznym palcem dłoni wspomagającej (lewej) mocno dociśnij dół przedniej ścianki chwytu**, blokując nadgarstki w dół (tzw. *camming the wrists*). Kropka sama wskoczy w środek okna.
2. **Charakterystyka przerywacza Ghost Ultimate 3.5 lb (*Rolling Break* vs twarda ściana):**
   * Fabryczny przerywacz Glocka ma twardą ścianę, którą trzeba „przebić”. Przerywacz **Ghost Ultimate** ma łagodniejszy kąt rampy – obniża opór do ok. **1,6–1,8 kg** i zamienia twardą ścianę w płynne, gładkie przełamanie (*rolling break*).
   * **Jak to wykorzystać:** To ogromna zaleta przy strzelaniu w ruchu i na dystansie 10–15 m (znacznie mniejsza tendencja do zerwania strzału w lewo-dół). Zamiast metody „zatrzymaj się na ścianie i szarpnij”, stosuj metodę **płynnego przewinięcia (*Smooth Roll*)**: podczas wypychania broni wybierasz jałowy luz (do wyczucia początku oporu przerywacza), a gdy kropka wchodzi w cel – jednostajnie przewijasz spust do końca bez zatrzymywania ruchu palca.
3. **Dynamika zamka G47 i praca na resecie w dubletach:**
   * Krótsza sprężyna powrotna sprawia, że zamek G47 wraca bardzo szybko, natomiast łagodniejszy kąt Ghost Ultimate daje nieco bardziej miękki (mniej „kopiący” w palec) reset niż twardy przerywacz fabryczny.
   * **Zasada w dubletach:** Nie próbuj „kleić” palca na milimetrze resetu, bo przy szybkim strzelaniu (splity **0.17–0.20 s**) łatwo wtedy o *trigger freeze* (niedopuszczenie spustu do pełnego resetu). W momencie strzału odpuszczaj palec swobodnie tuż przed próg kliknięcia resetu (nadal nie odrywając opuszka od języka!) i od razu płynnie przewijaj drugi strzał.

---

## 📂 Struktura Repozytorium

1. **[01-plan-cyklu-12-tygodni.md](./01-plan-cyklu-12-tygodni.md)** – Mapa drogowa całego 3-miesięcznego makrocyklu, podział na mezocykle i cele tygodniowe.
2. **[02-program-dry-fire.md](./02-program-dry-fire.md)** – Konkretne jednostki treningowe (A, B, C, D, E) do wykonania w domu, zasady progresji Par Time oraz metodyka pracy z kolimatorem i trenażerem MantisX/laserem.
3. **[03-karty-treningowe-live-fire.md](./03-karty-treningowe-live-fire.md)** – 3 gotowe karty treningowe na strzelnicę (Miesiąc 1, 2 i 3), rozpisane co do naboju na budżet **200 szt. amunicji**.
4. **[04-atlas-drilli-i-benchmarki.md](./04-atlas-drilli-i-benchmarki.md)** – Instrukcje wykonania kluczowych drilli (m.in. *Doubles*, *Bill Drill*, *Blake Drill*, *1R1*, *El Presidente*, *Box Drill*) wraz z docelowymi czasami dla konfiguracji OWB + Red Dot.
5. **[05-dziennik-postepow.md](./05-dziennik-postepow.md)** – Szablon do zapisywania czasów Par Time, testów *Cold Start* (na zimno) oraz wyników ze strzelnicy.
6. **[hit_factor.py](./hit_factor.py)** – Skrypt CLI / interaktywny do wyliczania **Hit Factor (IPSC Minor 9x19)**, ekonomii czasu względem celności (ile ułamków sekundy kosztuje trafienie Charlie/Delta/Miss) oraz logowania wyników do pliku `wyniki_hf.csv`.

---

## ⚠️ Złote Zasady: Jak trenować 4–5x na sucho i 1x na ostro (bez złych nawyków)

Przy proporcji **~18 treningów Dry Fire na 1 trening Live Fire**, trening na sucho buduje 90% Twojej motoryki (dobycie, indeksowanie kropki, przejścia wzroku, wymiana magazynka, praca na nogach). Ma jednak jedno zagrożenie: **brak odrzutu w domu sprzyja oszukiwaniu na chwycie i spuście**.

Aby każda wizyta na strzelnicy przynosiła skokowy progres, stosuj 4 żelazne reguły:

### 1. Uczciwy chwyt w Dry Fire (Siła 100%, nie „na pół gwizdka”)
W domu łatwo wyjąć broń luźną dłonią, żeby urwać 0.1 s na timerze. Na strzelnicy taki chwyt rozsypie się po pierwszym strzale w dublecie.
* **Zasada:** W Dry Fire ręka wspomagająca (support hand) miażdży chwyt z taką samą siłą, jak przy strzelaniu serii 6 strzałów (*Bill Drill*). Ręka strzelająca pozostaje rozluźniona w nadgarstku i palcu spustowym (ok. 30–40% siły), a ręka wspomagająca wykonuje 70–80% pracy.

### 2. Kolimator = 100% Target Focus (Ostrość wzroku na celu)
Nigdy nie patrz na szybkę kolimatora i nie szukaj kropki wzrokiem.
* **Zasada:** Wbijasz wzrok w konkretny, mały punkt na tarczy (np. literę „A” w strefie Alfa lub naklejkę 2 cm). Broń wyprowadzasz na linię wzrok–cel, a kropka pojawia się jako rozmyty hologram nałożony na ostry cel. Podczas przejść między tarczami **najpierw przeskakują oczy**, a broń podąża za nimi z opóźnieniem ułamka sekundy.

### 3. Higiena pracy z laserem i MantisX
Systemy typu Laser Academy i MantisX są świetnymi narzędziami diagnostycznymi, ale używane w każdym ćwiczeniu mogą wyrobić nawyk „polowania na błysk lasera” na tarczy (spoglądania nad kolimator w momencie strzału) lub czekania z drugim strzałem na pisk aplikacji.
* **Zasada podziału:**
  * **MantisX:** Używaj w blokach technicznych (praca na spuście jednej ręki, dobycie z pierwszym strzałem, strzelanie w ruchu – analiza stabilności łuku ruchu).
  * **Nabój laserowy:** Używaj tylko do weryfikacji pierwszego trafienia z dobycia oraz strzałów precyzyjnych (Hostage / Headbox).
  * **Czysty Dry Fire (ze zbijakami, bez lasera):** Stosuj do wszystkich ćwiczeń wielostrzałowych (*Doubles*, *Bill Drill*, *Blake Drill*), gdzie kluczowe jest ciągłe widzenie kropki kolimatora w okienku i agresywne przejścia wzroku.

### 4. Zasada bezpieczeństwa (Rygor 4 kroków przed każdym Dry Fire)
1. Wyjmij wszystkie magazynki z ostrej amunicji i wynieś ją do **innego pomieszczenia**.
2. Sprawdź komorę nabojową wizualnie i dotykowo (palcem).
3. Przygotuj wyłącznie magazynki treningowe załadowane zbijakami (dla zachowania realnej masy magazynka przy wymianach).
4. Wyznacz w pokoju jedną bezpieczną ścianę („kulochwyt”), w stronę której zawsze kierujesz lufę. Po zakończeniu sesji powiedz na głos: *„Koniec treningu bezstrzałowego”* i schowaj sprzęt.
