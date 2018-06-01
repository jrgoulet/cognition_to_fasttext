# Cognition to Fasttext converter

Takes Cognition annotations and converts them into Fasttext format

### Quickstart

Set up a virtual environment
```
virtualenv -p python3 venv
```

Install required packages
```
./venv/bin/python -m pip install -r requirements.txt
```

### Usage

```
./venv/bin/python cognition_to_fasttext.py --input-csv=INPUT_CSV --name=MODEL_NAME --label=LABEL --split=SPLIT
```

**Parameters**

- `--input-csv` - The Cognition annotations file. Must contain text and label rows at minimum.
- `--name` - The name of the model. Just used for generating output filename.
- `--label` - (Optional) Positive annotation label. Defaults to "yes".
- `--split` - (Optional) Test split size. Defaults to `0.2`.
