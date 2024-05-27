# Streamlit visjs component

Streamlit component that wraps [vis.js](https://visjs.org/).

## Installation instructions 

```sh
pip install visjs-component
```

## Usage instructions

```python
import streamlit as st
from visjs_component import visjs

data = {
    "nodes": [
        {"id": 1, "label": "Node 1"},
        {"id": 2, "label": "Node 2"},
        {"id": 3, "label": "Node 3"},
        {"id": 4, "label": "Node 4"},
        {"id": 5, "label": "Node 5"},
    ],
    "edges": [
        {"from": 1, "to": 3},
        {"from": 1, "to": 2},
        {"from": 2, "to": 4},
        {"from": 2, "to": 5},
    ],
    "options": {
        "nodes": {
            "shape": "dot",
            "size": 16,
        },
        "edges": {
            "color": "#000000",
        },
        "physics": {
            "enabled": True,
        },
        "interaction": {
            "hover": True,
        },
        "height": "500px",
    },
}

eventHandlers = [
    {
        "event": "click",
        "callback": lambda eventData: st.json(
            eventData['data']
        ),
    }
]

visjs(title="# Network Vis", type="network", data=data, eventHandlers=eventHandlers, key="my_network_id")
```

Supports all vis.js types: 
- network
- timeline
- graph3d


## Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [0.2.0] - 2024-05-27
 
### Added
- New `combined.py` example with the 3 types of visualisations
- Support for multiple instances by adding a `key` parameter as shown below

```
visjs(title="# Network Vis", type="network", data=data, eventHandlers=eventHandlers, key="your_unique_key")
```

### Changed

- `title` property is now optional.


## Donate

If you like this project and want to support it, please consider donating.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C4OBZTC)