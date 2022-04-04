
# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

CMD python3 -m venv env

CMD source env/bin/activate

RUN pip install --upgrade pi

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start flask
CMD python3 run.py
