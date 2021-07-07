# graphite
This container runs the [graphite-web](https://github.com/graphite-project/graphite-web)
application and that's it.

## Running on Docker

This container expects to listen on one port and have two mounted volumes. It
needs to listen on port 8080 TCP. It needs to have `/opt/graphite/conf` and
`/opt/graphite/storage` mounted.

    docker build -t ghcr.io/uwcip/graphite:latest .
    docker run --rm -it -p 8080:8080/tcp -v $PWD/storage:/opt/graphite/storage -v $PWD/example:/opt/graphite/conf ghcr.io/uwcip/graphite:latest

An example configuration file for mounting into `/opt/graphite/conf` is
provided in the `example` directory. There may be other configuration files
that graphite-web supports that may be added to that directory as well.
