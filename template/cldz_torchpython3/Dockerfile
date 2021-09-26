FROM clouderizer/cldz_baseimage:p3.8-node12-torch

WORKDIR /home/app/

USER root

COPY function           function
COPY function/asset/otherfiles/ .
COPY function/index.html node-service/index.html

RUN while read requirement; do pip install $requirement || conda install -c conda-forge -c fastai -c pytorch --yes $requirement || exit 1; done < function/requirements.txt
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
