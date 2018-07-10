FROM python:3.7.0

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r /tmp/requirements.txt

RUN python -m gensim.downloader --download fasttext-wiki-news-subwords-300

COPY ./app/ /app/
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD ["app.py"]