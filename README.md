# weatherapp
# Weather Application (Tkinter)

A simple desktop weather app built with **Python + Tkinter** that:
- Takes a city name as input
- Fetches current weather using **OpenWeatherMap API**
- Displays weather details (temperature, pressure, humidity, wind, cloudiness, description)
- Speaks the weather summary using **pyttsx3**
- Shows a text forecast via **wttr.in**
- Includes a **Reset** button to clear fields

---

## Features
- **GUI** built with Tkinter
- **Text-to-Speech** (non-blocking with a background thread)
- **Current Weather** (OpenWeatherMap)
- **Forecast** (wttr.in)
- **Background image** support (edit path in the code)

---

## Prerequisites

### 1) Python packages
Install dependencies:

```bash
pip install requests pillow pyttsx3
```

> Note: `pyttsx3` may require additional OS speech drivers. On Windows it usually works after installing the package.

### 2) OpenWeatherMap API key
The app uses an API key in the code:

```python
api_key='YOUR_API_KEY_HERE'
```

Replace it with your own key.

---

## How to Run

```bash
python "weather app.py"
```

---

## Usage
1. Enter a **city name** (e.g., `London`).
2. Click **Get weather**.
3. Read the results in the fields and listen to the spoken weather report.
4. Click **Weather forecast** to fetch the forecast from wttr.in (response is printed to console).
5. Click **Reset** to clear all fields.

---

## Notes / Customization

### Background image path
The code currently loads an image from an absolute Windows path:

```python
bg_image = Image.open("C://WEATHER//climate.jpg")
```

Update this path to your local image (or place the image inside the project folder and reference it relative to the script).

### Forecast output
The forecast function fetches data from wttr.in and prints the raw response:

```python
print(response1.text)
```

If you want it displayed in the GUI, you can add a label/text widget.

---

## Project Files
- `weather app.py` — Main application
- `forecast.mp3` — (Optional) placeholder/static asset
- `hello,py` — (Unspecified) additional file

---

## Troubleshooting
- **“City Not Found”**: Check spelling and ensure your API key is valid.
- **Image not found**: Update the `climate.jpg` path.
- **No speech**: Verify `pyttsx3` installation and Windows speech support.

---

## License
Add a license file if needed (not included by default).
