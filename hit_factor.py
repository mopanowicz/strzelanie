#!/usr/bin/env python3
"""
Kalkulator Hit Factor (IPSC Minor 9x19) oraz Analizator Drilli Strzeleckich
Zoptymalizowany pod plan treningowy: Glock 47 (Red Dot + OWB)
"""

import argparse
import csv
from datetime import datetime
from pathlib import Path
import sys

# Punktacja IPSC Minor (9x19 mm)
POINTS_MINOR = {
    "A": 5,
    "C": 3,
    "D": 1,
    "M": -10,  # Miss (pudło)
    "NS": -10,  # No-Shoot (zakładnik)
    "P": -10,  # Kara proceduralna
}

# Benchmarki dla Glock 47 + Kolimator + OWB (100% Alfa = max punktów)
BENCHMARKS = {
    "draw": {
        "name": "One-Shot Draw (7m, 1 strzał)",
        "rounds": 1,
        "base_time": 1.50,
        "target_time": 1.20,
        "expert_time": 1.00,
    },
    "pair": {
        "name": "Controlled Pair / Dublet (7m, 2 strzały)",
        "rounds": 2,
        "base_time": 1.80,
        "target_time": 1.45,
        "expert_time": 1.25,
    },
    "1r1": {
        "name": "1R1 Reload (7m, 1+1 strzały z dobyciem)",
        "rounds": 2,
        "base_time": 3.30,
        "target_time": 2.65,
        "expert_time": 2.20,
    },
    "mozambik": {
        "name": "Mozambik / Failure Drill (7m, 2+1 strzały)",
        "rounds": 3,
        "base_time": 2.50,
        "target_time": 1.95,
        "expert_time": 1.65,
    },
    "bill": {
        "name": "Bill Drill (7m, 6 strzałów)",
        "rounds": 6,
        "base_time": 2.85,
        "target_time": 2.25,
        "expert_time": 1.95,
    },
    "blake": {
        "name": "Blake Drill (7m, 3 tarcze x 2 strzały)",
        "rounds": 6,
        "base_time": 3.25,
        "target_time": 2.50,
        "expert_time": 2.15,
    },
    "elpres": {
        "name": "El Presidente (10m, 12 strzałów)",
        "rounds": 12,
        "base_time": 7.80,
        "target_time": 6.00,
        "expert_time": 5.00,
    },
}

LOG_FILE = Path(__file__).parent / "wyniki_hf.csv"


def calculate_hf(
    time_s: float,
    a: int,
    c: int = 0,
    d: int = 0,
    miss: int = 0,
    no_shoot: int = 0,
    proc: int = 0,
) -> dict:
    """Oblicza punkty, Hit Factor oraz ekonomię czasu względem celności."""
    if time_s <= 0:
        raise ValueError("Czas musi być większy od 0 sekund.")

    total_rounds = a + c + d + miss
    max_points = total_rounds * POINTS_MINOR["A"]
    raw_points = (
        a * POINTS_MINOR["A"] + c * POINTS_MINOR["C"] + d * POINTS_MINOR["D"]
    )
    penalties = (
        miss * abs(POINTS_MINOR["M"])
        + no_shoot * abs(POINTS_MINOR["NS"])
        + proc * abs(POINTS_MINOR["P"])
    )
    net_points = max(0, raw_points - penalties)

    hf = net_points / time_s
    accuracy_pct = (raw_points / max_points * 100.0) if max_points > 0 else 0.0

    # Wartość czasowa punktów (ile sekund jest wart 1 punkt przy aktualnym HF)
    sec_per_point = (1.0 / hf) if hf > 0 else 0.0
    charlie_cost_sec = 2.0 * sec_per_point  # Strata 2 pkt (A=5 vs C=3) w przeliczeniu na czas
    delta_cost_sec = 4.0 * sec_per_point  # Strata 4 pkt (A=5 vs D=1)
    miss_cost_sec = 15.0 * sec_per_point  # Strata 5 pkt + 10 pkt kary = 15 pkt

    return {
        "time_s": time_s,
        "total_rounds": total_rounds,
        "a": a,
        "c": c,
        "d": d,
        "miss": miss,
        "no_shoot": no_shoot,
        "proc": proc,
        "max_points": max_points,
        "raw_points": raw_points,
        "penalties": penalties,
        "net_points": net_points,
        "accuracy_pct": accuracy_pct,
        "hf": hf,
        "sec_per_point": sec_per_point,
        "charlie_cost_sec": charlie_cost_sec,
        "delta_cost_sec": delta_cost_sec,
        "miss_cost_sec": miss_cost_sec,
    }


def evaluate_drill(drill_key: str, hf: float) -> str:
    """Porównuje uzyskany Hit Factor z benchmarkami dla danego drilla."""
    if drill_key not in BENCHMARKS:
        return ""

    b = BENCHMARKS[drill_key]
    max_pts = b["rounds"] * 5
    base_hf = max_pts / b["base_time"]
    target_hf = max_pts / b["target_time"]
    expert_hf = max_pts / b["expert_time"]

    if hf >= expert_hf:
        level = "🏆 POZIOM EKSPERT / ZAWODNICZY"
    elif hf >= target_hf:
        level = "✅ CEL 12-TYGODNIOWY OSIĄGNIĘTY!"
    elif hf >= base_hf:
        level = "📈 POZIOM ŚREDNIOZAAWANSOWANY (w drodze do celu)"
    else:
        level = "🔧 PONIŻEJ BAZY (skup się na płynności i czystych Alfach)"

    return (
        f"\n📊 Porównanie z benchmarkiem: {b['name']}\n"
        f"   • Twój Hit Factor:        {hf:.2f} HF\n"
        f"   • Poziom Bazowy (Start):  {base_hf:.2f} HF ({b['base_time']:.2f} s przy 100% A)\n"
        f"   • Cel Cyklu (12 tyg.):    {target_hf:.2f} HF ({b['target_time']:.2f} s przy 100% A)\n"
        f"   • Poziom Ekspert:         {expert_hf:.2f} HF ({b['expert_time']:.2f} s przy 100% A)\n"
        f"   • Ocena: {level}"
    )


def print_report(res: dict, drill_key: str = "custom", notes: str = "") -> None:
    """Wyświetla czytelny raport w terminalu."""
    print("\n" + "=" * 62)
    print(" 🎯 RAPORT HIT FACTOR (IPSC Minor 9x19 - Glock 47)")
    print("=" * 62)
    print(f" ⏱️  Czas przebiegu:   {res['time_s']:.2f} s")
    print(
        f" 🔫 Liczba strzałów:  {res['total_rounds']} "
        f"(A: {res['a']}, C: {res['c']}, D: {res['d']}, Miss: {res['miss']})"
    )
    if res["no_shoot"] or res["proc"]:
        print(f" ⚠️  Kary dodatkowe:  No-Shoot: {res['no_shoot']}, Procedury: {res['proc']}")
    print(
        f" 🏅 Punkty netto:     {res['net_points']} / {res['max_points']} pkt "
        f"({res['accuracy_pct']:.1f}% możliwych punktów)"
    )
    print("-" * 62)
    print(f" 🔥 HIT FACTOR:       {res['hf']:.4f}  ({res['hf']:.2f} HF)")
    print("-" * 62)

    if res["hf"] > 0:
        print(" 💡 Analiza ekonomii czasu vs celności (przy Twoim tempie):")
        print(f"    • 1 punkt jest warty:              {res['sec_per_point']:.2f} s")
        print(
            f"    • Koszt 1x Charlie (zamiast Alfa): {res['charlie_cost_sec']:.2f} s "
            "(tyle musisz urwać na czasie, żeby C się opłaciło)"
        )
        print(f"    • Koszt 1x Delta (zamiast Alfa):   {res['delta_cost_sec']:.2f} s")
        print(f"    • Koszt 1x Miss (pudło = -15 pkt): {res['miss_cost_sec']:.2f} s")

    if drill_key in BENCHMARKS:
        print(evaluate_drill(drill_key, res["hf"]))

    if notes:
        print(f"\n 📝 Notatka: {notes}")
    print("=" * 62 + "\n")


def save_to_csv(res: dict, drill_key: str, mode: str, notes: str) -> None:
    """Zapisuje wynik do pliku CSV z historią treningów."""
    file_exists = LOG_FILE.exists()
    with LOG_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(
                [
                    "data",
                    "tryb",
                    "drill",
                    "czas_s",
                    "strzaly",
                    "A",
                    "C",
                    "D",
                    "Miss",
                    "NoShoot",
                    "Proc",
                    "punkty",
                    "hit_factor",
                    "notatka",
                ]
            )
        writer.writerow(
            [
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                mode,
                drill_key,
                f"{res['time_s']:.2f}",
                res["total_rounds"],
                res["a"],
                res["c"],
                res["d"],
                res["miss"],
                res["no_shoot"],
                res["proc"],
                res["net_points"],
                f"{res['hf']:.4f}",
                notes,
            ]
        )
    print(f"💾 Wynik zapisano do: {LOG_FILE}")


def show_history() -> None:
    """Wyświetla zapisaną historię wyników z pliku CSV."""
    if not LOG_FILE.exists():
        print("Brak zapisanych wyników w pliku wyniki_hf.csv.")
        return

    print("\n" + "=" * 80)
    print(" 📜 HISTORIA WYNIKÓW (wyniki_hf.csv)")
    print("=" * 80)
    with LOG_FILE.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(
                f" [{row['data']}] {row['tryb']:<8} | {row['drill']:<10} | "
                f"Czas: {row['czas_s']:>5}s | A:{row['A']} C:{row['C']} D:{row['D']} M:{row['Miss']} | "
                f"Pkt: {row['punkty']:>2} | HF: {float(row['hit_factor']):>6.2f} | {row['notatka']}"
            )
    print("=" * 80 + "\n")


def interactive_prompt() -> None:
    """Tryb interaktywny krok po kroku."""
    print("\n=== 🎯 KALKULATOR HIT FACTOR (TRYB INTERAKTYWNY) ===")
    print("Dostępne drille: " + ", ".join(BENCHMARKS.keys()) + ", custom")
    drill_key = input("Wybierz drill [domyślnie: bill]: ").strip().lower() or "bill"

    default_rounds = BENCHMARKS[drill_key]["rounds"] if drill_key in BENCHMARKS else None
    if default_rounds:
        print(f"--> Wybrano: {BENCHMARKS[drill_key]['name']} ({default_rounds} strzałów)")

    time_s = float(input("Podaj czas z timera (s), np. 2.35: ").replace(",", "."))
    a_Prompt = f"Liczba trafień ALFA [domyślnie: {default_rounds or 0}]: "
    a_str = input(a_Prompt).strip()
    a = int(a_str) if a_str else (default_rounds or 0)

    c = int(input("Liczba trafień CHARLIE [0]: ").strip() or 0)
    d = int(input("Liczba trafień DELTA [0]: ").strip() or 0)
    miss = int(input("Liczba PUDEŁ (Miss) [0]: ").strip() or 0)

    res = calculate_hf(time_s=time_s, a=a, c=c, d=d, miss=miss)
    print_report(res, drill_key=drill_key)

    save = input("Zapisać wynik do historii CSV? (t/n) [t]: ").strip().lower() or "t"
    if save in ("t", "tak", "y", "yes"):
        mode = input("Tryb (live / dry / cold) [live]: ").strip().lower() or "live"
        notes = input("Notatka (opcjonalnie): ").strip()
        save_to_csv(res, drill_key, mode, notes)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Kalkulator Hit Factor (IPSC Minor 9x19) dla planu treningowego Glock 47."
    )
    parser.add_argument("-t", "--time", type=float, help="Czas przebiegu w sekundach (np. 2.25)")
    parser.add_argument("-a", "--alfa", type=int, default=0, help="Liczba trafień w strefę Alfa (5 pkt)")
    parser.add_argument("-c", "--charlie", type=int, default=0, help="Liczba trafień w strefę Charlie (3 pkt)")
    parser.add_argument("-d", "--delta", type=int, default=0, help="Liczba trafień w strefę Delta (1 pkt)")
    parser.add_argument("-m", "--miss", type=int, default=0, help="Liczba pudeł / Miss (-10 pkt)")
    parser.add_argument("--ns", type=int, default=0, help="Liczba trafień w No-Shoot (-10 pkt)")
    parser.add_argument("--proc", type=int, default=0, help="Liczba kar proceduralnych (-10 pkt)")
    parser.add_argument(
        "--drill",
        choices=list(BENCHMARKS.keys()) + ["custom"],
        default="custom",
        help="Nazwa drilla do porównania z benchmarkami (draw, pair, 1r1, mozambik, bill, blake, elpres)",
    )
    parser.add_argument(
        "--mode",
        choices=["live", "dry", "cold"],
        default="live",
        help="Tryb treningu przy zapisie do logu (live, dry, cold)",
    )
    parser.add_argument("--save", action="store_true", help="Zapisz wynik do pliku wyniki_hf.csv")
    parser.add_argument("--note", type=str, default="", help="Notatka do zapisu w historii")
    parser.add_argument("--history", action="store_true", help="Pokaż historię zapisanych wyników")
    parser.add_argument(
        "--benchmarks", action="store_true", help="Pokaż tabelę docelowych Hit Factorów dla wszystkich drilli"
    )

    args = parser.parse_args()

    if args.history:
        show_history()
        return

    if args.benchmarks:
        print("\n" + "=" * 78)
        print(" 📊 TABELA DOCELOWYCH HIT FACTORÓW (Glock 47 + Red Dot + OWB, 100% Alfa)")
        print("=" * 78)
        print(f" {'Kod':<10} | {'Nazwa Drilla':<38} | {'Baza':>7} | {'Cel 12w':>7} | {'Ekspert':>7}")
        print("-" * 78)
        for k, b in BENCHMARKS.items():
            pts = b["rounds"] * 5
            print(
                f" {k:<10} | {b['name']:<38} | "
                f"{pts/b['base_time']:>5.2f}HF | {pts/b['target_time']:>5.2f}HF | {pts/b['expert_time']:>5.2f}HF"
            )
        print("=" * 78 + "\n")
        return

    # Jeśli nie podano czasu w argumentach CLI, uruchom tryb interaktywny
    if args.time is None:
        try:
            interactive_prompt()
        except (KeyboardInterrupt, EOFError):
            print("\nZakończono.")
            sys.exit(0)
        return

    # Jeśli wybrano znany drill, a nie podano żadnych trafień (ani A, C, D, M), załóż 100% Alfa dla tego drilla
    if args.alfa == 0 and args.charlie == 0 and args.delta == 0 and args.miss == 0 and args.drill in BENCHMARKS:
        args.alfa = BENCHMARKS[args.drill]["rounds"]

    res = calculate_hf(
        time_s=args.time,
        a=args.alfa,
        c=args.charlie,
        d=args.delta,
        miss=args.miss,
        no_shoot=args.ns,
        proc=args.proc,
    )
    print_report(res, drill_key=args.drill, notes=args.note)

    if args.save:
        save_to_csv(res, args.drill, args.mode, args.note)


if __name__ == "__main__":
    main()
