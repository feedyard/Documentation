### How to - circle-ci integration

dependencies:
  pre:
    # update locally with:
    # openssl aes-256-cbc -e -in secret-env-plain -out secret-env-cipher -k $KEY
    - openssl aes-256-cbc -d -in secret-env-cipher -k $KEY >> ~/.circlerc