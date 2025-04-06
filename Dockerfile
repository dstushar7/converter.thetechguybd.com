# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file first, install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose port 
EXPOSE 8000

# Define environment variable for Python
# Prevents Python from writing .pyc (bytecode) files to disk.
ENV PYTHONDONTWRITEBYTECODE=1 

# Forces Python to run in unbuffered mode, 
# so all logs (stdout/stderr) are sent straight to the container’s output without being held in a buffer.
ENV PYTHONUNBUFFERED=1

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
