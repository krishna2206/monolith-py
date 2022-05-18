## monolith-py
A simple python wrapper to [Y2Z's monolith](https://github.com/Y2Z/monolith), a commandline program to download a webpage and bundle into a single HTML file.

**Requires Python 3.7+ installed**.

**Works only on Linux at the moment**.

## How to install
```bash
pip install git+https://github.com/krishna2206/monolith-py.git#egg=monolith-py
```

## Usage
Download a webpage
```python
from monolithpy import Monolith

monolith_opts = {
  "output": "monolith-github.html"
}

monolith = Monolith(monolith_opts)
monolith.download("https://github.com/Y2Z/monolith")
```

## Available options
- `no_audio` (bool) : Exclude audio sources
- `no_css` (bool) : Exclude CSS
- `charset` (str) : Save document using custom charset
- `ignore_network_errors` (bool) : Ignore network errors
- `omit_frames` (bool) : Omit frames
- `no_webfonts` (bool) : Exclude web fonts
- `no_javascript` (bool) : Exclude JavaScript
- `noscript_contents` (bool) : Extract contents of NOSCRIPT elements
- `output` (str) : Write output to file
- `verbose` (bool) : Be quiet
- `timeout` (int) : Adjust network request timeout
- `user_agent` (str) : Provide custom User-Agent
- `no_video` (bool) : Exclude videos
- `no_image` (bool) : Remove images

## Options not yet added
- `-b`: Use custom base URL
- `-I`: Isolate the document
- `-k`: Accept invalid X.509 (TLS) certificates
- `-M`: Don't add timestamp and URL information

## TO-DO
- Support for Windows