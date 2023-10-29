FROM    python:3.10
WORKDIR /project
COPY    ./app ./app 
COPY    ./run.py .
COPY    ./requirements.txt .
COPY    ./.env .
RUN     pip install --no-cache-dir --default-timeout=100 -r requirements.txt 

ENTRYPOINT ["python", "run.py", ">", "/dev/null"]
