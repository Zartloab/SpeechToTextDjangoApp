# Django Speech To Text Project

## Overview

This is a Dockerized Django application for speech-to-text functionality. The project can be accessed via the following environments:

access on mobile via:

![QR Code](speechtotext_qrcode.png)

- **Test Environment:** [https://speechtotextdjangoapp-cxd0cmd2bqgxa2cy.australiaeast-01.azurewebsites.net/](https://speechtotextdjangoapp-cxd0cmd2bqgxa2cy.australiaeast-01.azurewebsites.net/)
- **Local Environment:** [http://localhost:8000//](http://localhost:8000/)

Main app logics are implemented in [https://github.com/Zartloab/SpeechToTextDjangoApp/blob/main/Translation/views.py/](https://github.com/Zartloab/SpeechToTextDjangoApp/blob/main/Translation/views.py)

## Prerequisites

Before running the application, ensure that you have the following installed:

- Docker (if running with Docker)
- Python 3.9+ (if running locally without Docker)
- pip (Python package manager)

## Running the Application with Docker

To run the application using Docker, follow these steps:

1. **Build and start the application**:

   ```bash
   chmod +x run &&
   ./run


   ```

2. **Shutdown the application**:

   ```bash
   chmod +x down &&
   ./down

   ```

## Running the Application Locally (without Docker)

If you prefer to run the application without Docker, follow these steps:

1. **Upgrade pip**:

   ```bash
    pip install --upgrade pip

   ```

2. **Install dependencies**:

   ```bash
    pip install -r requirements.txt

   ```

3. **Run the Django server**:

   ```bash
   python manage.py runserver
   ```

## Deployment

This project is configured to be deployed using Docker and can be hosted on platforms like Azure, AWS, or any cloud provider that supports Dockerized applications.

For testing purposes, it is currently deployed at:
[https://speechtotextdjangoapp-cxd0cmd2bqgxa2cy.australiaeast-01.azurewebsites.net/](https://speechtotextdjangoapp-cxd0cmd2bqgxa2cy.australiaeast-01.azurewebsites.net/).

```

```
