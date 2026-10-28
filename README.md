# Plant Disease Detection and Autonomous Spraying Robot — Safe Demo

This is a starter workflow for an agriculture-assistance project. It accepts a leaf image, but **does not identify disease** because no trained image-classification model is included. It also simulates a robot decision without controlling physical hardware.

## Technologies
Python, Flask, HTML/CSS; optional future Arduino/IoT integration.

## Run
```bash
python -m venv .venv
```
Activate the environment, then:
```bash
pip install -r requirements.txt
python app.py
```
Visit http://127.0.0.1:5000.

## To extend
Integrate a properly licensed, trained, and evaluated plant-leaf classifier. Document your dataset and measured test results. Do not claim accuracy without testing on held-out data.

## Safety
The Arduino sketch is a non-actuating placeholder. It does not activate a pump, valve, or sprayer. Do not use this demo for pesticide decisions or real hardware control.
