from os import environ


print("Hello {0}! Good job using Docker!!!".format(environ.get("NAME", "Nobody")))
