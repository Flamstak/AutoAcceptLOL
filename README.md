# Skrypt do akceptacji gry w League of Legends

Prosty skrypt napisany w języku Python do automatycznego akceptowania gry w League of Legends w języku polskim.

## Jak to działa?

Skrypt używa biblioteki `pyautogui` do lokalizacji przycisku "akceptuj" na ekranie gry. Po znalezieniu przycisku, kliknięcie zostaje zasymulowane, co powoduje akceptację gry. Skrypt jest uruchamiany w pętli, aż zostanie <b>przytrzymany</b> klawisz 'q', co kończy jego działanie.

## Wymagania

1. Python 3.x
2. Biblioteka `pyautogui`
3. Biblioteka `keyboard`

## Instrukcje

1. Zainstaluj wymagane biblioteki, uruchamiając poniższą komendę:

    ```bash
    pip install pyautogui keyboard
    ```

2. Uruchom skrypt za pomocą poniższej komendy:

    ```bash
    python nazwa_twojego_skryptu.py
    ```

3. Aby przerwać działanie skryptu, <b>prztrzymaj</b> klawisz 'q'.

## Uwagi

1. Upewnij się, że obrazek `accept.png` znajduje się w tym samym folderze co skrypt.
   <br>![accept.png](accept.png)
2. Skrypt może wymagać dostosowania współczynnika pewności (confidence) w przypadku problemów z lokalizacją obrazka na ekranie.

## Autor

[Flamstak]

---

Dziękuję za skorzystanie z tego skryptu! Jeśli masz pytania lub sugestie, proszę daj mi znać.
