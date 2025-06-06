#!/usr/bin/env python3
"""Standalone chat input dialog for Pepe GPT"""

import sys
import AppKit
from AppKit import NSApplication, NSAlert, NSTextField
from PyObjCTools import AppHelper

class ChatInputApp:
    def __init__(self):
        self.app = NSApplication.sharedApplication()
        self.result = ""
    
    def show_input_dialog(self):
        # Create alert dialog
        alert = NSAlert.alloc().init()
        alert.setMessageText_("Chat with Pepe 🐸")
        alert.setInformativeText_("What would you like to say to Pepe?")
        
        # Create text field
        text_field = NSTextField.alloc().initWithFrame_(((0, 0), (350, 30)))
        text_field.setFont_(AppKit.NSFont.systemFontOfSize_(16))
        text_field.setPlaceholderString_("Type your message here...")
        text_field.setBezeled_(True)
        text_field.setBezelStyle_(AppKit.NSTextFieldRoundedBezel)
        text_field.setEditable_(True)
        text_field.setSelectable_(True)
        alert.setAccessoryView_(text_field)
        
        alert.addButtonWithTitle_("Send")
        alert.addButtonWithTitle_("Cancel")
        
        # Show dialog
        response = alert.runModal()
        
        if response == AppKit.NSAlertFirstButtonReturn:
            self.result = text_field.stringValue().strip()
        else:
            self.result = ""
        
        return self.result

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Test mode
        chat_app = ChatInputApp()
        message = chat_app.show_input_dialog()
        print(f"RESULT:{message}")
    else:
        print("Usage: python3 chat_input.py test")

if __name__ == "__main__":
    main() 