# Local TTS App

## Overview
This project implements a fully local Text-to-Speech (TTS) application using pretrained models (e.g., Coqui TTS) with a focus on modularity and extensibility. The application is built primarily in Python using PyTorch for the TTS engine, enabling the synthesis of speech from text inputs. It initially offers a Command Line Interface (CLI) and will later feature a Flask-based web interface.

## Features
- Core TTS Engine:
    - Utilizes Coqui TTS via PyTorch.
    - Supports pitch and speed adjustments.
    - Designed for easy swapping of models and future feature expansion.

- Input Handling Module:
    - Supports plain text files, EPUBs, and PDFs.
    - Uses appropriate libraries (Python’s built-in file IO, ebooklib for EPUB, and PyMuPDF/pdfminer.six for PDFs) to extract text.
- Command Line Interface (CLI):

    - Accepts direct text input or paths to input files.
    - Provides options to adjust speech parameters (e.g., pitch, speed).
    - Outputs synthesized audio either to a file or plays it directly.

- Future Flask Interface:
 
    - REST endpoints wrapping core functionalities.
    - Web upload functionality for text or document files.
    - Simple HTML form for text input and parameter selection.