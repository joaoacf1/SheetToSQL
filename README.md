# SheetToSQL
SheetToSQL is a Python-based ETL (Extract, Transform, Load) tool that extracts data from a Google Sheets spreadsheet, processes it using `pandas`, and loads it into a MySQL database. This project utilizes the Google Sheets API for data retrieval and provides a streamlined pipeline for data integration and management.

## Features

- **Read Data:** Retrieve data from a specified Google Sheets spreadsheet using Google Sheets API.
- **Process Data:** Utilize `pandas` to clean and transform the data.
- **Store Data:** Insert the transformed data into a MySQL database.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Script Development](#script-development)
4. [Functionalities](#functionalities)
5. [How to Use](#how-to-use)
6. [Contributing](#contributing)
7. [License](#license)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Google account with access to Google Developers Console
- MySQL server
- Basic knowledge of Python, Google Sheets API, and MySQL

### Step-by-Step Project Process

#### 1. Creating the Project in Google Developers Console

1. Visit [Google Developers Console](https://console.developers.google.com).
2. Create a new project.
3. Enable the **Google Sheets API**.
4. Create credentials:
   - Service account
   - OAuth 2.0 Client ID

Download the `client_secret.json` and `conta.json` files and keep them in the project root directory.

#### 2. Setting Up the Development Environment

1. Install Python from the official [Python website](https://www.python.org/).
2. Create a virtual environment:
   ```bash
   python -m venv venv
3. Activate the virtual environment:
- Windows: venv\Scripts\activate
- Mac/Linux: source venv/bin/activate
4. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
  
## Project Structure
The project consists of the following files:

- main.py: Main script to run the program.
- requirements.txt: List of all dependencies required for the project.
- client_secret.json: Credentials for the OAuth 2.0 Client ID (not included in the repository for security reasons).
- conta.json: Service account credentials for the Google Sheets API (not included in the repository for security reasons).
- token.json: Token file generated for Google Sheets API access (not included in the repository for security reasons).
- .env: File to store environment variables such as database credentials (not included in the repository for security reasons).

## Script Development
The main.py script is organized into the following sections:

Import Required Libraries: Libraries such as pandas, sqlalchemy, google-auth, and googleapiclient.
Define Constants: Set up constants like Google Sheets ID, range, and MySQL connection details.
Implement Functions:
get_credentials(): Obtains service account credentials from conta.json.
get_spreadsheet_data(service): Retrieves data from the specified Google Sheet.
process_data(values): Processes the obtained data using pandas.
save_to_database(df): Saves processed data to the MySQL database.
Main Function (main()): Orchestrates the flow of the program, calling each function in the required order.

## Script Development (main.py)
The main.py script is organized into the following sections:

1. Import Required Libraries: Libraries such as pandas, sqlalchemy, google-auth, and googleapiclient.
2. Define Constants: Set up constants like Google Sheets ID, range, and MySQL connection details.
3. Implement Functions:
- get_credentials(): Obtains service account credentials from conta.json.
- get_spreadsheet_data(service): Retrieves data from the specified Google Sheet.
- process_data(values): Processes the obtained data using pandas.
- save_to_database(df): Saves processed data to the MySQL database.
4. Main Function (main()): Orchestrates the flow of the program, calling each function in the required order.

## Functionalities
1. Get Credentials:
- The function get_credentials() reads the conta.json file and obtains credentials to access the Google Sheets API.
2. Read Data from Google Sheets:
- The function get_spreadsheet_data() connects to the Google Sheets API and retrieves data from a specified spreadsheet and range.
3. Process Data Using Pandas:
- The function process_data() converts the raw data into a pandas DataFrame for further processing.
4. Save Data to MySQL Database:
- The function save_to_database() establishes a connection to the MySQL database using SQLAlchemy and stores the DataFrame.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SheetToSQL.git
   cd SheetToSQL
2. Set up the virtual environment and install dependencies.
3. Configure environment variables in the .env file.
4. Ensure the client_secret.json and conta.json files are correctly set up and placed in the project root.
5. Run the script:
   ```bash
   python main.py

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License
