# Stanza Benchmark

## Build Docker Image for Stanza

```sh
docker build -t stanza .
```

## Run Docker Container for Stanza

```sh
docker run -it -v `pwd`:/workspace/ stanza:latest bash
```

## Run Named Entity Recongnition model

```sh
cd workspace/src/
python stanza-111-chars.py
```

```sh
cd workspace/src/
python stanza-1736-chars.py
```