FROM continuumio/anaconda3

WORKDIR /app
Add . /app

RUN conda install -c conda-forge phantomjs
RUN conda install --file requirements.txt

RUN pip install -e .

ENV FLASK_APP luigimetrics

EXPOSE 5000

CMD flask run
