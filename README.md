# OCR API with FastAPI

A simple OCR (Optical Character Recognition) service built with FastAPI, SQLAlchemy, SQLite, and Tesseract OCR.

## Features

* User creation and management
* Image upload support
* File storage on the server
* OCR text extraction from uploaded images
* SQLite database integration
* RESTful API endpoints
* Interactive API documentation via Swagger UI

## Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* PyTesseract
* Python Multipart
* Aiofiles
* Uvicorn


## Installation

### Clone the repository

```bash
git clone https://github.com/Petit-DJ/OCR.git
cd OCR
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Tesseract OCR

Download and install Tesseract OCR on your system and ensure it is added to your system PATH.

## Run the Application

```bash
fastapi dev main.py
```

or

```bash
uvicorn main:app --reload
```

## API Endpoints

### User

| Method | Endpoint | Description        |
| ------ | -------- | ------------------ |
| POST   | `/user`  | Create a new user  |
| GET    | `/user`  | Retrieve all users |

### Files

| Method | Endpoint | Description     |
| ------ | -------- | --------------- |
| POST   | `/file`  | Upload an image |

## Future Improvements

* Authentication and authorization
* OCR history tracking
* AI-powered text processing

## Learning Goals

This project was built to practice:

* FastAPI fundamentals
* Database integration with SQLAlchemy
* File handling and uploads
* REST API design
* OCR workflows
* Backend project architecture

## License

This project is intended for learning and experimentation.
