import sys 
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QHBoxLayout,QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt

class Weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WHEATHER APP")
        self.setGeometry(1000,500,400,400)

        self.city=QLabel("Enter the city:",self)
        self.city_input=QLineEdit(self)
        self.get_wheather=QPushButton("Get Wheather",self)
        self.temp=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)

        vbox=QVBoxLayout()
        vbox.addWidget(self.city)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_wheather)
        vbox.addWidget(self.temp)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city.setAlignment(Qt.AlignHCenter)
        self.city_input.setAlignment(Qt.AlignHCenter)
        self.emoji_label.setAlignment(Qt.AlignHCenter)
        self.temp.setAlignment(Qt.AlignHCenter)
        self.description_label.setAlignment(Qt.AlignHCenter)

        self.setStyleSheet("""
                            QLabel,QLineEdit{
                           font-size:40px;
                           }
                           QPushButton{
                           font-size:30px;
                           background-color:#72d3f4;
                           }
                           QLabel,QPushButton,QLineEdit{
                           font-family:Arial;
                           font-weight:Bold;
                           padding:10px
                           }""")
        self.emoji_label.setStyleSheet("font-size:80px;")

        self.get_wheather.clicked.connect(self.get_wheather_update)

    def get_wheather_update(self):
        api_key="81b34fa3feb53d5ab2b4cc193018a436"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            

            if data["cod"]==200:
                self.display_data(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid Api kry ")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied")  
                case 404:
                    self.display_error("Not Found:\City Not Found")
                case 408:
                    self.display_error("Request Timeout:\Your request has timed out ")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from server")
                case 504:
                    self.display_error("Bad Request:\nPlease check your input")
                case _:
                    self.display_error("Invalid input")    
                 
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nPlease check your internet connection")       
        except requests.exceptions.RequestException:
            self.display_error("Request Error:")        



    def display_data(self,data):
        temperature=data["main"]["temp"]
        self.temp.setStyleSheet("font-size:30px")
        temperature-=273.15
        self.temp.setText(f"{temperature:.2f}°c")

        description=data["weather"][0]["description"]
        self.description_label.setText(f"{description}")
        weather_id=data["weather"][0]["id"]
        emoji=self.get_weather_emoji(weather_id)
        self.emoji_label.setText(emoji)



    def display_error(self,message):
        self.temp.setStyleSheet("font-size:30px")
        self.temp.setText(message)



    def get_weather_emoji(self,weather_id):
        if 200 <= weather_id<=232:
            return "⛈️"
        elif 300<= weather_id<=321:
            return "⛅"
        elif 500<=weather_id<=531:
            return "🌧️"
        elif 600 <=weather_id<=622:
            return "🌨️"
        elif 701<=weather_id<=741:
            return "🌫️"
        elif weather_id==762:
            return "🌋"
        elif weather_id==771:
            return "💨"
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "☀️"    
        elif 801<=weather_id<=804:
            return "☁️"
        else :
            return " "
        



app=QApplication(sys.argv)
wheather=Weather_app()
wheather.show()
sys.exit(app.exec_())  