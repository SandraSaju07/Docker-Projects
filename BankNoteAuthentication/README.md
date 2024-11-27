# Flask API with Swagger Documentation

This repository contains a Flask web application that serves machine learning model predictions. The application is exposed via an API and includes automatic Swagger documentation for easy interaction.

## Features

- Predict the class of a banknote based on input features such as variance, skewness, curtosis, and entropy.
- Predict the class of multiple banknotes by uploading a CSV file.
- Swagger UI for API documentation and testing.

## Prerequisites

- Docker (optional, but recommended for running in a containerized environment)
- Python 3.x (if not using Docker)

## Setup and Installation

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/SandraSaju07/Docker-Projects/tree/main/BankNoteAuthentication
cd BankNoteAuthentication
```
### 2. Using Docker

If you have Docker installed, you can build and run the app in a containerized environment.

- Build the Docker Image

```bash
docker build -t money_api .
```
- Run the Docker Container

```bash
docker run -p 5000:5000 money_api
```

The application will be accessible at http://localhost:5000/apidocs.

### 3. Running Locally (Without Docker)

If you prefer running the app locally without Docker, follow these steps:

- Install Dependencies
  First, create a virtual environment (optional but recommended) and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```
- Run the Flask App
  Run the Flask application:

```bash
python app.py
```
The application will be accessible at http://localhost:5000/apidocs.

