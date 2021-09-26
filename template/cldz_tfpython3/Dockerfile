FROM clouderizer/cldz_baseimage:p3.8-node12-tf

# Add non root user
#RUN groupadd app && useradd -r -g app app

#RUN mkdir -p function && \
 #   touch ./function/__init__.py

#RUN pip install -r requirements.txt --target=/home/app/python

WORKDIR /home/app/

USER root
#RUN while read requirement; do pip install $requirement; done < function/requirements.txt && \
COPY function           function
COPY function/asset/otherfiles/ .
COPY function/index.html node-service/index.html
#RUN pip install -q tf-models-official==2.3.0
RUN while read requirement; do pip install $requirement || conda install -c conda-forge --yes $requirement || exit 1; done < function/requirements.txt && \
    chown -R app:app ./ && \
    chmod -R 777 /home/app/python

USER app

ENV cgi_headers="true" fprocess="node /home/app/node-service/app.js" mode="http" upstream_url="http://127.0.0.1:9090"

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
