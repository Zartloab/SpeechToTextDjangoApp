# Use an official Python runtime as a base image
FROM python:3.9

# Install dependencies required for psycopg2 and other packages
RUN apt-get update && apt-get install -y \
    python3-venv \
    python3-dev \
    build-essential \
    libpq-dev \
    qtbase5-dev \
    qt5-qmake \
    qtchooser \
    libqt5gui5 \
    libqt5webkit5-dev \
    libqt5svg5-dev \
    qtmultimedia5-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update pip
RUN pip install --upgrade pip

# Update pip
RUN pip --version

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Expose port 8000 (default for Django)
EXPOSE 8000

# Define environment variable for production
ENV DJANGO_ENV=production

# Run the Django development server (for local testing)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]