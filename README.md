# Text To Speech

Text to speech is a Python program and can be used to read text. Currently it has English and Hindi language reading support via CLI arguments. For other language support you need to configure the code accordingly.

## Requirements

##### System requirements:

- You must have [Python 3](https://www.python.org) installed in your system.

##### Prerequisite knowledge:

- Basic understanding of [Python](https://www.python.org)
- Basic understanding of **Terminal** or **Command Prompt**

### Getting Started

1. _Install the required python packages_

```sh
pip install pyttsx3
pip install pypiwin32 # Windows only
```

2. _Run the project_

```sh
python main.py
```

#### Command Line Options

1. **-t** or **--text** for cli input of text.

```sh
python main.py -t "This is input from command line"
```

2. **-l** or **--language** for cli input of language. Currently it support Hindi and English. Available inputs are **english** and **hindi**.

```sh
python main.py -t Hello -l english
```

3. **-a** or **--accent** for cli input of language accent. Only available for english language. Available accents are **indian**, **australian**, **us** and **uk**. For Hindi it is default set to **indian** accent.

```sh
python main.py -t Hello -l english -a uk
```

4. **-g** or **--gender** for cli input of voice gender. Available inputs are **male** and **female**. By default it is set to **male**.

```sh
python main.py -t Hello -l english -a uk -g female
```

5. **-i** or **--index** to select rank of the reader form the output list. It starts from 0 (Zero). If you don't select any index it will automatically take the first one.

```sh
python main.py -t Hello -l english -a us -g female -i 1
```

**NOTE :** _Sometimes there might be chances that the readers are not available for specific gender or language or accent. In that case, it tries to find alternative or else it will read by the default reader which has **English** language, **US** accent and voice gender is **male**._

#### Dependencies

- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/)

#### Contributing

1. Fork it ( https://github.com/vishalnagda1/text-to-speech/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new pull request.
