# Desktop Pepe GPT – macOS desktop pet

![demo-gif](demo.gif)

A tiny Pepe **desktop-pet** that lives on your Mac, chats with GPT-4o and
shows the live Pepe price.
Built entirely with **Cocoa / PyObjC** – no Tkinter required.

---

## Quick start (macOS)

1. Download the ready-made DMG → **[Pepe GPT.dmg](https://github.com/ozzyozzz/pepe-gpt/releases/download/v1.0/PepeGPT.zip)**
2. Open it and drag __Pepe GPT.app__ into _Terminal_
3. Double-click the app; grant network permission on first run
4. Paste your OpenAI key when asked – done!

---

## Features

• Drag-and-drop border-less 128 × 128 Pepe (left-click & drag)

• Double-click → ask Pepe anything – runs an OpenAI chat request in a safe
background thread and shows the reply in a speech bubble (≤ 25 words)

• GPT replies carry a mood tag (`<mood:HAPPY|LAUGH|WOW|SAD|THINK>`) and Pepe's
animation swaps automatically

• Right-click menu with _Exit_

• Single-tap → blue bubble with the current Pepe price

• Live web context: DuckDuckGo Instant-Answer snippet is passed to GPT; if the
query is about price Pepe quotes the live value fetched from CoinGecko

• Idle helper: every 10 min (configurable) Pepe shows the price bubble while no
chat is active; animations revert to the idle spinning-coin after 6 s

• First launch modal prompts for your OpenAI API key and stores it securely in
`~/.openai_api_key` (0600) – no Terminal needed

---

## Build from source

```bash
# macOS 13 or newer
brew install python@3.12 pyenv        # or use the system Python 3.12
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt       # PyObjC, openai, requests, py2app …

# clean build
rm -rf build dist
python setup.py py2app
open dist/Desktop\ Pepe.app           # test run
```

---

## Customising Pepe

Animations and prompts live in `assets/pepe/`:

- `pepe-smart.gif` – idle loop and thinking animation
- `pepe-silly.gif` – happy/silly mood animation
- `pepe-clown.gif` – laugh/talking animation
- `pepe-disappears.gif` – wow/surprise animation
- `pepe-sad.gif` – sad mood animation
- `pepe-boxing.gif` – intense/angry animation
- `config.json` – personality prompt template (advanced)

---

## Requirements

- macOS 13 or later (Apple Silicon & Intel)
- Python 3.12 when building from source (the DMG is self-contained)
- OpenAI account with API key (first 5 USD free)

---

## Credits

Based on the open-source idea by [Shirros/desktop-pet](https://github.com/Shirros/desktop-pet).
Re-implemented in Cocoa & PyObjC by @yourname.

Pepe ❤ and frog meme art belong to their respective creators.
