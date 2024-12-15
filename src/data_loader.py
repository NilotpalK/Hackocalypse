import json
from pathlib import Path
from typing import List, Dict

class DataLoader:
    def __init__(self, map_dir: str = "data/map_descriptions"):
        self.map_dir = Path(map_dir)

    def load_initial_map(self) -> List[str]:
        """Load the initial map description."""
        with open(self.map_dir / "initial_map.txt", "r") as f:
            return f.read().strip().split("\n")

    def load_updates(self, updates_file: str = "data/updates/sample_updates.json") -> List[Dict]:
        """Load real-time updates."""
        with open(updates_file, "r") as f:
            return json.load(f)

    def parse_map_data(self, map_text: str) -> Dict:
        """Parse map text into structured data."""
        nodes = {}
        edges = []
        safe_zones = []
        obstacles = []

        # Add parsing logic here based on your map format
        return {
            "nodes": nodes,
            "edges": edges,
            "safe_zones": safe_zones,
            "obstacles": obstacles
        }