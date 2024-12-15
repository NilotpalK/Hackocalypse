import logging
from typing import Dict, Any
import json

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def save_to_json(data: Dict[str, Any], filepath: str):
    """Save data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filepath: str) -> Dict[str, Any]:
    """Load data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)