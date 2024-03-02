# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /ligaPWr

# Install dependencies
COPY requirements.txt /ligaPWr/
RUN pip3 install -r requirements.txt

# Copy the project code into the container
COPY . /ligaPWr/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]