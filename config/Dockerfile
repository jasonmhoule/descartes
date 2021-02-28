FROM rocker/verse
MAINTAINER Jason Houle (jasonmhoule@gmail.com)

RUN apt-get -qqy update && apt-get install -qqy \
        openssh-client \
        qpdf
        
## Install packages from CRAN
RUN install2.r --error \ 
    -r 'http://cran.rstudio.com' \
    zip \
## clean up
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

## COPY Rprofile.site /usr/local/lib/R/etc/Rprofile.site
## [] This should be replaced using gsutil and service account