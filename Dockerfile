FROM python:3.13

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/code"

# Set working directory
WORKDIR /code/

# Copy and install Python dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy application code
COPY . /code/
