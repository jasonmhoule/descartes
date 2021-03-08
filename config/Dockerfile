FROM rocker/verse
MAINTAINER Jason Houle (jasonmhoule@gmail.com)

## Install packages including GCloud SDK
RUN apt-get -qqy update && apt-get install -qqy \
        gnupg \
        openssh-client \
        libxml2 \
        qpdf

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | \
        tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
        apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - &&  apt-get -qqy update \
        && apt-get install -qqy google-cloud-sdk

## Install packages from CRAN
RUN install2.r --error \ 
    -r 'http://cran.rstudio.com' \
    ## -r https://cran.microsoft.com/snapshot/${YYYY-MM-DD} ## Update with MRAN build date to freeze packages
    RSelenium \
    zip \
## clean up
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

COPY fxns.R /home/fxns.R
COPY start.sh tmp/start.sh
RUN chmod +x tmp/start.sh

CMD ["tmp/start.sh"]

## COPY Rprofile.site /usr/local/lib/R/etc/Rprofile.site
## [] This should be replaced using gsutil and service account - perhaps w/ startup script on host VM
## [] Notes in adopting this template:
##    - Configure Dockerfile & GCP build trigger
##    - Update rstudiocontainer.py (#11) accordingly
