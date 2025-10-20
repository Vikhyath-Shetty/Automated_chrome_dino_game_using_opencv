# Chrome Dino Bot

Chrome Dino Bot that uses OpenCV to detect obstacles and control the game. Works on Windows and Linux.

## Features

- Automatic detection of cactuses and pterodactyls using screenshots + OpenCV
- Automatic jump and duck actions using keyboard control (pyautogui / pynput)
- Lightweight: written in plain Python, configurable via `pyproject.toml`
- Cross-platform: supports Windows and Linux (desktop notifications available on both)

## Step 1 — Clone the repository

```bash
git clone <repo-url>
```

## Step 2 — Install project dependencies (use uv)

```bash
uv sync
```

## Step 3 — Install notification helper

- On Windows (Python package via uv):

```bash
uv add win10toast
```

- On Linux (command-line notifier):

```bash
sudo apt install notify-send
```

## Step 4 — Prepare Chrome

- Open single chrome window and open the dino game tab: `chrome://dino`

- Note: For reliable operation, keep only one Chrome window with the Dino tab visible and avoid moving or resizing the window while the bot runs.

## Step 5 — Run the bot

```bash
uv run bot.py
```

- The bot will try to focus the Chrome window on start and will send a desktop notification on start.

## Step 6 — Stop the bot

- To Kill the bot, press the `'q'` key while the bot is running.
- Or terminate the process from your terminal `Ctrl + C`.
