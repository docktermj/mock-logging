# mock-logging

## Synopsis

A program and Docker image that simply spits out log messages

## Demonstrate using Command Line Interface

1. :pencil2: Locate git repository.
   Example:

    ```console
    export GIT_ACCOUNT=docktermj
    export GIT_REPOSITORY=mock-logging
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    ```

1. Run command.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    ./mock-logging.py
    ```

## Demonstrate using Docker

1. Deploy using [docker run](https://docs.docker.com/engine/reference/run/).
   Example:

    ```console
    sudo docker run \
      dockter/mock-logging
    ```
