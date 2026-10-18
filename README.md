# Emotion Detection

A small Python app that reads a piece of text and tells you which emotion it shows.
It uses the Watson NLP emotion model to score five emotions: anger, disgust, fear, joy and sadness.

## Project structure

```
EmotionDetection/
  emotion_detection.py   # calls the Watson API and returns the scores
test_emotion_detection.py  # unit tests
templates/index.html       # web page
static/mywebscript.js      # script for the web page
```

## Setup

You need Python 3.11 and the `requests` package.

```bash
python3.11 -m pip install requests
```

## Usage

Run Python from the project folder:

```python
from EmotionDetection.emotion_detection import emotion_detector

emotion_detector("I am very glad")
```

It returns the score for each emotion and the strongest one:

```python
{
    'anger': 0.008,
    'disgust': 0.006,
    'fear': 0.007,
    'joy': 0.974,
    'sadness': 0.068,
    'dominant_emotion': 'joy'
}
```

If the text is empty, you get an error message instead.

## Tests

```bash
python3.11 test_emotion_detection.py
```

## License

See [LICENSE](LICENSE).
