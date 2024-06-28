# Desktop-Language-Translator
This is a desktop language translator to turn text selected on the screen after pressing a keybind into a selected language, via Google Translate. Supports 100+ languages and configurable keybinds.

## Installation

This project requires Tesseract to be installed on your system, along with any language packs that you want to use. You can download Tesseract(Windows) from [here](https://github.com/UB-Mannheim/tesseract/wiki). This only comes with English, so translation from other languages will not work unless you download the language packs from [here](https://github.com/tesseract-ocr/tessdata)

Clone the repository and run the following command in the root directory:

```bash
pip install -r requirements.txt
python main.py
```
