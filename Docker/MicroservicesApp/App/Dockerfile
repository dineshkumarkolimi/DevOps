FROM python

WORKDIR /home/app/

COPY . /home/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["python", "main.py"]
