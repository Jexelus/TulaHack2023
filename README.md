# TulaHack2023
 TulaHack2023

<h1>Make env</h1>

```bash

if linux:
    python3 -m venv env
    source env/bin/activate
    pip install -r req.txt
    pip install Werkzeug==2.3.0
else:
    python -m venv env
    env/Scripts/activate<.bat or ps.1>
    pip install -r req.txt
    pip install Werkzeug==2.3.0
```

<h1>Run</h1>

```bash
windows:
    env/Scripts/python run.py

Linux:
    env/bin/python run.py

```
