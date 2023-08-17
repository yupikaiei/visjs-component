# visjs-component

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

visjs(title="# Network Vis", type="network", data=data, eventHandlers=eventHandlers)
```

Supports all vis.js types: 
- network
- timeline
- graph3d