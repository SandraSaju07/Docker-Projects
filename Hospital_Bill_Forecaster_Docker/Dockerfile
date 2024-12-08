FROM continuumio/anaconda3:2022.05

RUN pip install virtualenv
ENV VIRTUAL_ENV=/env 
RUN virtualenv venv -p python3 
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app 
ADD . /app  

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]