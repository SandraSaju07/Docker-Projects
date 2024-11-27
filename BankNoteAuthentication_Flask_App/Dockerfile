# Use the updated Anaconda base image
FROM continuumio/anaconda3:2022.05

# Set up the working directory
WORKDIR /usr/app/

# Copy the project files into the container
COPY . /usr/app/

# Expose the application port
EXPOSE 5000

# Update pip and install dependencies
RUN python -m pip install --upgrade pip setuptools && \
    pip install --no-cache-dir -r requirements.txt

# Run the Flask app
CMD ["python", "app.py"]