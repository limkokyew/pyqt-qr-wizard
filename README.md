# pyqt-qr-wizard
This is a simple PyQt5 application to generate and decode
[QR codes](https://en.wikipedia.org/wiki/QR_code). Here's a glimpse of the
app:

<p align="center">
 <img src=".github/preview_image.png" alt="Screenshot of application">
</p>

## Run with ``python``
While not entirely necessary, I would recommend setting up a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment using:

```bash
. venv/bin/activate
```

From here, install all requirements needed using ``pip``:

```bash
pip install -r requirements.txt
```

Finally, run ``qr_main.py`` with ``python``:

```bash
python qr_main.py
```

A PyQt window should pop up. Switch between generating and decoding QR codes
using the tabs at the top and enjoy!
