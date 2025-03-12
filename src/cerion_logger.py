### cerion_logger.py

```python
# Basic logging utility for Cerion AI

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    logging.info(f"Event Logged: {event}")

if __name__ == "__main__":
    log_event("Cerion AI initialized successfully.")
```
