# spaCy Benchmark

## Build Docker Image for Spacy

```sh
docker build -t spacy .
```

## Run Docker Container for Spacy

```sh
docker run -it -v `pwd`:/workspace/ spacy:latest bash
```

## Run Named Entity Recongnition model

```sh
cd workspace/src/
python spacy-111-chars.py
```

```sh
cd workspace/src/
python spacy-1736-chars.py
```