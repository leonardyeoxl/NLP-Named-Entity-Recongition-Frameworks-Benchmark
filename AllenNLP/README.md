# AllenNLP-Benchmark

## Build Docker Image for AllenNLP 1.4.0

```sh
docker build -t allennlp-1.4.0 .
```

## Run Docker Container for AllenNLP 1.4.0

```sh
docker run -it -v `pwd`:/workspace/ allennlp-1.4.0:latest bash
```

## Run Named Entity Recongnition model

```sh
cd workspace/src/
python allennlp-111-chars.py
```