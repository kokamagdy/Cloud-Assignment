FROM python:3.11.7

WORKDIR /app

COPY CloudAssignment.py /app/
COPY random_paragraphs.txt /app/

RUN pip install nltk
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

CMD ["python", "CloudAssignment.py"]





