# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 public.ecr.aws/docker/library/python:3.9.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg unixodbc-dev

# Import the Microsoft repository GPG keys
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add the Microsoft SQL Server repository
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update package lists and install the ODBC driver
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "DataPipeline.py"]