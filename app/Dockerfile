FROM python:3.8-slim-buster
# Add the wait script to the image (Does not work with username and password)
# ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
# RUN chmod +x /wait
RUN python -m pip install -U pip
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
ADD app.py .
# ENTRYPOINT [ "python", "app.py" ]
# CMD /wait && python app.py
CMD python app.py
