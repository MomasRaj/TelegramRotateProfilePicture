# RotateProfilePicTg
This project automatically updates a Telegram profile picture **exactly at the start of every hour** by 30 degrees.

You can run it on your **local PC** or on a **VM**.

## How it works

- At startup, the script waits until the next `HH:00`
- Every hour:
  - Rotates a base image by `hour × 30°`
  - Deletes the current Telegram profile photo
  - Uploads the newly rotated image
  
## How to run

---

## Requirements

- Python **3.9+**
- Telegram API credentials (`apiId`, `apiHash`)
- Telethon session file already authenticated

### Python dependencies
```yaml
telethon>=1.30.0
Pillow>=9.0.0
```
## Setup

### Create virtual environment

```bash
python3 -m venv
source bin/activate
pip install -r requirements.txt
```
### Configure Telegram credentials
Edit script.py and set:
```python
apiId = 123456
apiHash = "YOUR_API_HASH"
```
With your credentials obtained at 
[https://my.telegram.org/apps](https://my.telegram.org/apps).

## Telethon session file (`session.session`)

The first time you run the script it will ask for you to authenticate 

```bash
python main.py
```

You will be asked for:

- Your phone number

- The login code sent by Telegram

After successful login, the session.session file will be created automatically.
From then on, the script will reuse this file and will not ask for a login code again.
