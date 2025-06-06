from setuptools import setup
import sys, os, glob

APP = ["cocoa_pet.py"]
# Ship only the Pepe animation frames (skip hidden files such as .DS_Store)
DATA_FILES = [
    (
        "assets/pepe",
        [
            f for f in glob.glob("assets/pepe/**/*", recursive=True)
            if os.path.isfile(f) and not os.path.basename(f).startswith(".")
        ],
    ),
]

OPTIONS = {
    # remove Dock icon / menu-bar by running as a background-only app
    # comment this line if you *do* want a Dock icon
    "plist": {"LSUIElement": True,  # or "LSBackgroundOnly": True on older macOS
              "CFBundleName": "Desktop Pepe",
              "CFBundleDisplayName": "Desktop Pepe",
              "CFBundleIdentifier": "com.yourname.desktop-pepe",
              "CFBundleShortVersionString": "1.0",
              "CFBundleVersion": "1.0",
              "NSHighResolutionCapable": True,
              # leave icon assignment to the separate "iconfile" option
              },
    "packages": ["requests", "openai"],
    # include any modules py2app might fail to discover automatically
    "includes": ["Quartz", "objc"],
    # resources copied verbatim in Contents/Resources/
    "resources": ["assets/pepe"],
    # optional icon – build one with `iconutil -c icns Pepe.iconset`
    "iconfile": "assets/pepe/Pepe.icns",
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
