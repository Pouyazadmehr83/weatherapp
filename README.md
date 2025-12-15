# SkyPulse – Django Weather Experience

SkyPulse is a sleek weather experience built with Django that mixes a polished UI with real-time weather insights from the Open‑Meteo platform. Type any city, hit search, and you immediately get temperature, wind, and metadata in a glassmorphism-inspired card that feels modern on both desktop and mobile.

## Features
- Instant city search with graceful error handling (invalid spellings included)
- Geocoding + current weather via the free Open‑Meteo APIs (no API keys required)
- Curated UI/UX: blurred cards, dark gradient background, responsive layout, and subtle micro-interactions
- Fully server-rendered (Django templates) so it runs anywhere Python does

## Tech Stack
- **Framework:** Django 6
- **Styling:** Custom CSS (glassmorphism, responsive grid, Inter font)
- **APIs:** Open‑Meteo Geocoding + Forecast
- **Runtime:** Python 3.13+

## Getting Started
1. **Install dependencies**
   ```bash
   python -m pip install "django>=6.0,<7.0"  # or run `poetry install`
   ```
2. **Run migrations**
   ```bash
   python manage.py migrate
   ```
3. **Launch the dev server**
   ```bash
   python manage.py runserver
   ```
4. Open `http://127.0.0.1:8000/` and start searching for cities.

## Project Notes
- The app talks directly to Open‑Meteo; no keys or secrets are needed.
- All copy, validation messages, and UI affordances are in English for consistency.
- To customize the look, edit `weather/templates/weather/home.html`; all styling lives inside the same file for easy theming.

## Next Ideas
- Map Open‑Meteo weather codes to friendly icons/descriptions.
- Add historical charts or hourly forecasts for richer storytelling.
- Introduce offline caching (Redis) to save the most recent searches.

Enjoy the breeze with SkyPulse! ✨
