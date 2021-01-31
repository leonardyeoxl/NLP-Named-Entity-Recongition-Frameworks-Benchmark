# NLP Named Entity Recongition (NER) Frameworks Benchmark

## Test Environment

- Ubuntu 16.04 Virtual Machine (AMD Ryzen 5 3600 4x processor cores, 8 GB RAM)
- Docker version 19.03.6, build 369ce74a3c

## Pretrained NER Prediction F1 Accuracy

### AllenNLP
- Conll-03: 92.22%

### spaCy
- OntoNotes: 86.40%

### FlairNLP
- Conll-03: 93.18%
- Ontonotes: 89.3%

### Stanza
- CoNLL03: 92.1% (4 Types)
- OntoNotes: 88.8% (18 Types)

## Pretrained NER Prediction Processing Performance

### AllenNLP 111 characters
Elapsed time: 0.8868 seconds

### AllenNLP 1736 characters
Elapsed time: 9.4914 seconds

### spaCy 111 characters
Elapsed time: 0.0074 seconds

### spaCy 1736 characters
Elapsed time: 0.0398 seconds

### FlairNLP 111 characters
Elapsed time: 0.9661 seconds

### FlairNLP 1736 characters
Elapsed time: 14.5668 seconds

### Stanza 111 characters
Elapsed time: 0.3639 seconds

### Stanza1736 characters
Elapsed time: 2.2698 seconds