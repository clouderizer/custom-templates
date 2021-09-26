FROM clouderizer/cldz_baseimage:p3.8-java11-node12

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/function/
COPY function/requirements.txt	.

RUN pip install -r requirements.txt --target=/home/app/python

WORKDIR /home/app/

USER root

COPY function           function
COPY function/asset/otherfiles/ .
COPY function/index.html node-service/index.html
# Allow any user-id for OpenShift users.
RUN chown -R app:app ./ && \
    chmod -R 777 /home/app/python

USER app

ENV cgi_headers="true"
ENV fprocess="node /home/app/node-service/app.js"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:9090"

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
