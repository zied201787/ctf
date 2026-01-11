# TryHackMe - Crylo4a Room

Time-Based Blind SQL Injection exploit for the [Crylo4a room](https://tryhackme.com/room/crylo4a) on TryHackMe.

## Requirements

```bash
pip install requests
```

## Usage

```bash
python sqli_exploit.py <TARGET_IP>
```

## How It Works

Extracts the database name using Time-Based Blind SQL Injection:

- Tries each character one by one
- If the character matches, `sleep(1)` executes → response is slow
- If it doesn't match → response is fast
- Builds the database name character-by-character
