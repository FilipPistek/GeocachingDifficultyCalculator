# Geocaching Difficulty Calculator

## Autor
**Jméno:** Filip Pištěk  
**Předmět:** Programové vybavení  
**Rok:** 2026  

## Popis projektu
**GeocachingDifficultyCalculator** je desktopová aplikace využívající strojové učení k odhadu obtížnosti geocachingových skrýší. Software řeší problém subjektivity při zakládání keší – na základě reálných dat o poloze, typu, velikosti a terénu predikuje objektivní obtížnost.

Projekt využívá model **Random Forest Classifier**, který byl natrénován na vlastním datasetu s více než 2 500 záznamy. Aplikace striktně odděluje grafické rozhraní od výpočetní logiky a implementuje ochranné UX prvky pro validaci vstupů.

## Struktura repozitáře
Projekt dodržuje přehledné rozdělení zdrojového kódu, modelů a dokumentace:

* `src/` - Autorský zdrojový kód aplikace.
    * `main.py` - Vstupní bod aplikace, implementace GUI.
    * `logic.py` - Business logika, načítání modelů a komunikace s AI.
* `models/` - Serializované objekty strojového učení (.pkl).
    * `GeocachingDifficultyModel` - Kompletní dokumentace trénování a analýzy.
    * `model.pkl` - Natrénovaný klasifikační model.
    * `scaler.pkl` - Normalizace vstupních dat.
    * `le_type.pkl`, `le_size.pkl` - Enkodéry kategorií.
* `data/` - Zdrojový dataset `gsak.csv`.

## Použité knihovny
* pandas
* joblib
* os
* tkinter
* re
* numpy
* sklearn

---

## Návod k instalaci a spuštění

### 1. Příprava prostředí
Aplikace vyžaduje Python 3.13+ a následující knihovny třetích stran. Instalaci provedete příkazem:

```bash
pip install pandas scikit-learn joblib numpy
```

### 2. Spuštění aplikace
Aplikaci lze spustit přímo z terminálu. V kořenové složce projektu spusťte:

```bash
python src/main.py
```

---

## Analýza a Strojové učení
Model byl vyvinut s důrazem na reálnou využitelnost a interpretovatelnost výsledků:

Data: 2500+ záznamů, 7 vstupních atributů.

Předzpracování: Čištění dat, transformace GPS souřadnic pomocí regulárních výrazů a standardizace.

### Výkon:
Přesná shoda: 34.5 %

Tolerance ±0.5 obtížnosti: 59.2 %

Tolerance ±1.0 obtížnosti: 75.3 %
