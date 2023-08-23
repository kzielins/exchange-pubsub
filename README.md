# Task
Potrzebujemy ściągać aktualny kurs waluty (EUR) ze strony dowolnego kantoru internetowego (proponujemy https://internetowykantor.pl/kurs-euro/).
Chcemy mieć możliwość modyfikacji waluty (np zmiana na USD) oraz zmiany częstotliwości odpytywania w jakimś miejscu gdzie przechowywana jest konfiguracja.

Pobrane dane powinny trafić na topic Kafki.

Aplikacja powinna być zdockeryzowana. (Kontener w aplikacji Docker/K8s).

Prezentacja - uruchomienie aplikacji w dockerze i zaprezentowanie działania (czyli odpalenie, pokazanie ze Kafka stworzyła topic, ze producer coś do niego wysyła i że consumer może odczytać kolejne Message(s) )

## english
Download actual exchange rate, from any online exchange. Parametrize all variables like exange src, frequency, xpath

Store downloaded in kafka topic (Parmetrize kafka like: address and topic)
