# Weather Project

This is a simple Python script that fetches weather information for a specified city using the OpenWeatherMap API.

I have made two project files, Weather_project.py can be used for a simple code without GUI and weather_project_with_gui.py can be used when user requires a GUI with the code.
## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

- Python installed on your machine
- An OpenWeatherMap API key

### Installation

1. Clone the repository to your local machine:

bash-
    git clone https://github.com/your-username/weather-project.git
    cd weather-project

2. Create a virtual environment (optional but recommended):

bash-
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies

4. Set up your OpenWeatherMap API key:

. Copy the `.env.example` file to create a new file named `.env` :

bash- 
    cp .env.example .env


. Open the '.env' file and replace "your_actual_api_key" with your real OpenWeatherMap API key.

### Important Note

Ensure that you keep your API key secure. Do not share it publicly or commit it to version control.

### Usage

1. When prompted, enter the name of the city for which you want to retrieve weather information.
2. View the current temperature, weather, humidity, cloudiness, wind speed, and pressure for the          specified city.

### Contributing
If you'd like to contribute to this project, please follow the standard GitHub flow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request


NOTE : Replace `your-username` with your GitHub username in the clone URL, and update any placeholder values accordingly.

This README provides users with information on how to set up and run the project, as well as guidance on contributing. Make sure to customize it further based on your specific project details.
