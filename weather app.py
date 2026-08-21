import sys
import requests

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QFrame, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setFixedSize(500, 650)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #101827;
                color: white;
                font-family: Arial;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(35, 30, 35, 30)
        main_layout.setSpacing(20)

        title = QLabel("Weather")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 38px;
                font-weight: bold;
                color: white;
            }
        """)

        subtitle = QLabel("Check the current weather anywhere")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            QLabel {
                font-size: 15px;
                color: #94a3b8;
            }
        """)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name...")
        self.city_input.setFixedHeight(55)
        self.city_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e293b;
                border: 2px solid #334155;
                border-radius: 15px;
                padding: 0 18px;
                font-size: 17px;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #38bdf8;
            }
        """)

        self.get_weather = QPushButton("Search")
        self.get_weather.setFixedSize(110, 55)
        self.get_weather.setStyleSheet("""
            QPushButton {
                background-color: #38bdf8;
                color: #082f49;
                border: none;
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7dd3fc;
            }
            QPushButton:pressed {
                background-color: #0ea5e9;
            }
        """)

        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.get_weather)
        main_layout.addLayout(search_layout)

        self.weather_card = QFrame()
        self.weather_card.setMinimumHeight(360)
        self.weather_card.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 25px;
            }
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.weather_card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(25, 25, 25, 25)
        card_layout.setSpacing(10)

        self.city_label = QLabel("Weather")
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setStyleSheet("""
            QLabel {
                font-size: 25px;
                font-weight: bold;
                color: white;
            }
        """)

        self.emoji_label = QLabel("🌤️")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setStyleSheet("font-size: 95px;")

        self.temp = QLabel("--°C")
        self.temp.setAlignment(Qt.AlignCenter)
        self.temp.setStyleSheet("""
            QLabel {
                font-size: 65px;
                font-weight: bold;
                color: #f8fafc;
            }
        """)

        self.description_label = QLabel("Search for a city")
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: #94a3b8;
            }
        """)

        card_layout.addWidget(self.city_label)
        card_layout.addWidget(self.emoji_label)
        card_layout.addWidget(self.temp)
        card_layout.addWidget(self.description_label)

        self.weather_card.setLayout(card_layout)
        main_layout.addWidget(self.weather_card)

        footer = QLabel("Weather data powered by OpenWeather")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("""
            QLabel {
                color: #64748b;
                font-size: 12px;
            }
        """)

        main_layout.addWidget(footer)
        self.setLayout(main_layout)

        self.get_weather.clicked.connect(self.get_weather_update)
        self.city_input.returnPressed.connect(self.get_weather_update)

    def get_weather_update(self):
        api_key = "Enter your API Key"
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city")
            return

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        try:
            self.get_weather.setText("Loading...")
            self.get_weather.setEnabled(False)

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            self.display_data(response.json())

        except requests.exceptions.HTTPError:
            if response.status_code == 401:
                self.display_error("Invalid API key")
            elif response.status_code == 404:
                self.display_error("City not found")
            elif response.status_code == 429:
                self.display_error("Too many requests")
            else:
                self.display_error(
                    f"Server error: {response.status_code}"
                )

        except requests.exceptions.Timeout:
            self.display_error("Request timed out")

        except requests.exceptions.ConnectionError:
            self.display_error("No internet connection")

        except requests.exceptions.RequestException:
            self.display_error("Something went wrong")

        finally:
            self.get_weather.setText("Search")
            self.get_weather.setEnabled(True)

    def display_data(self, data):
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.city_label.setText(f"{city_name}, {country}")
        self.temp.setText(f"{temperature:.0f}°C")
        self.description_label.setText(description.title())
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    def display_error(self, message):
        self.city_label.setText("Weather")
        self.temp.setText("")
        self.emoji_label.setText("⚠️")
        self.description_label.setText(message)

    def get_weather_emoji(self, weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        return "❓"


app = QApplication(sys.argv)
window = WeatherApp()
window.show()
sys.exit(app.exec_())
