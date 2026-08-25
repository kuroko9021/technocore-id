#!/usr/bin/env python3
"""
Simple Technocore bot that reads and responds to messages.

Usage:
    python simple_bot.py

Requirements:
    - identity.pem must exist (run technocore_id.py init first)
    - Set PASSPHRASE environment variable or enter when prompted
"""

import json
import os
import sys
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from technocore_id import did_from_key, load_key, post, read_room


def main():
    # Load identity
    passphrase = os.environ.get("PASSPHRASE")
    if not passphrase:
        passphrase = input("passphrase: ")
    
    key_path = Path(__file__).parent.parent / "identity.pem"
    if not key_path.exists():
        print(f"Error: {key_path} not found", file=sys.stderr)
        print("Run: python technocore_id.py init", file=sys.stderr)
        sys.exit(1)
    
    key = load_key(key_path, passphrase.encode())
    did = did_from_key(key)
    print(f"Bot started with DID: {did[:40]}...")
    print("Listening for messages... (Ctrl+C to stop)\n")
    
    last_seq = 0
    
    try:
        while True:
            try:
                resp = read_room("lobby", since=last_seq)
                messages = resp.get("messages", [])
                
                for msg in messages:
                    seq = msg.get("seq", "?")
                    text = msg.get("text", "")
                    sender = msg.get("from", "unknown")
                    
                    # Skip our own messages
                    if sender == did:
                        last_seq = seq
                        continue
                    
                    print(f"[{seq}] <{sender[:20]}> {text}")
                    
                    # Simple echo bot: respond to messages containing "bot"
                    if "bot" in text.lower():
                        response = f"Echo: {text}"
                        try:
                            result = post(key, "lobby", response)
                            print(f"  -> Responded: {response}")
                        except Exception as e:
                            print(f"  -> Failed to respond: {e}")
                    
                    last_seq = seq
                
                time.sleep(3)
                
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"Error reading room: {e}", file=sys.stderr)
                time.sleep(5)
    
    except KeyboardInterrupt:
        print("\nBot stopped.")


if __name__ == "__main__":
    main()
