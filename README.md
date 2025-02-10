# Exchange Rate Updater

## Overview

Exchange Rate Updater is a Python-based project that fetches exchange rates from the European Central Bank and updates a SQL database with the latest values from the day. This ensures real-time access to currency conversion rates for various applications.

## Features
- Fetches exchange rates from the European Central Bank
- Supports multiple currencies
- Updates an SQL database with the latest rates

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- SQL Database (MySQL, PostgreSQL, SQLite, etc.)
- Required Python libraries (see `requirements.txt`)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/exchange-rate-updater.git
   cd exchange-rate-updater
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure the database connection in `info.py`.

## Usage
Run the script manually:
```sh
python exchange_updater.py
```
Or set up a cron job (Linux) or Task Scheduler (Windows) to run it at regular intervals.

## Configuration

Modify `info.py` to specify:

Database connection details

## License

This project is licensed under the MIT License.

## Contact

For issues or contributions, open a GitHub issue or contact matheusaugustocantos@gmail.com.