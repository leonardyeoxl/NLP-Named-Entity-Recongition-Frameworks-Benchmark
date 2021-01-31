# FlairNLP Benchmark

## Build Docker Image for FlairNLP

```sh
docker build -t flairnlp .
```

## Run Docker Container for FlairNLP

```sh
docker run -it -v `pwd`:/workspace/ flairnlp:latest bash
```

## Run Named Entity Recongnition model

```sh
cd workspace/src/
python flairnlp-111-chars.py
```

```sh
cd workspace/src/
python flairnlp-1736-chars.py
```