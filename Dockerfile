ARG BASE_IMAGE=debian:10.11
FROM ${BASE_IMAGE}

ENV REFRESHED_AT=2022-01-06

LABEL Name="dockter/mock-logging" \
      Version="1.0.0"

USER root

# Install packages via apt.

RUN apt-get update \
 && apt-get -y install \
      python3-pip \
 && rm -rf /var/lib/apt/lists/*

# Install packages via PIP.

COPY requirements.txt ./
RUN pip3 install --upgrade pip \
 && pip3 install -r requirements.txt \
 && rm requirements.txt

# Copy files from repository.

COPY ./mock-logging.py /app/

# Make non-root container.

USER 1001

# Do the work.

WORKDIR /app
ENTRYPOINT ["/app/mock-logging.py"]
