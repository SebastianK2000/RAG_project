# Projekt RAG: Asystent Dokumentacji NAS Synology (Closed-Domain AI)

## Cel projektu
Zbudowanie systemu działającego w domenie zamkniętej (Closed-Domain AI), opartego o technologię Retrieval-Augmented Generation (RAG). System odpowiada na pytania wyłącznie na podstawie dostarczonej dokumentacji serwerów Synology NAS.
Zaimplementowano wariant, który eliminuje ryzyko halucynacji – asystent nie wymyśla płynnych zdań, a jedynie ściśle cytuje źródła, podając nazwę pliku i numer fragmentu (chunka).

## Funkcje specjalne
**Zapobieganie halucynacjom (Thresholding):** System wektorowy FAISS posiada matematyczny próg odcięcia odległości (`max_distance = 1.54`). Jeśli zadane zostanie pytanie spoza domeny (np. kulinaria, kursy walut), system odmówi odpowiedzi i poinformuje o braku informacji w bazie.

## Struktura projektu
* `data/raw/` - surowe instrukcje obsługi w formacie PDF.
* `index/` - skompilowana wektorowa baza danych FAISS i metadane.
* `src/` - logika aplikacji (wczytywanie, chunking, embeddingi, próg odcięcia, QA).
* `tests/sample_questions.txt` - zbiór 15 pytań testowych (faktograficzne, proceduralne, porównawcze i negatywne).

## Instrukcja uruchomienia (Windows)

1. **Aktywacja środowiska wirtualnego:**
   Otwórz terminal w głównym folderze projektu i wpisz:

  ```bash
  .\.venv\Scripts\activate
  ```

2. Instalacja zależności (Tylko za pierwszym razem):
  ```bash
  pip install -r requirements.txt
  ```
3. Budowa Bazy Wiedzy (Jeśli podmieniono pliki PDF):
  Uruchamia cały pipeline od czyszczenia pypdf do zapisu bazy FAISS. (Zajmie kilkadziesiąt sekund).

  ```bash
  python main.py
  ```

4. Uruchomienie Aplikacji:
  ```bash
  streamlit run src/app.py
  ```

5. Aplikacja otworzy się automatycznie w domyślnej przeglądarce pod adresem http://localhost:8501.

