from visjs_component import visjs
import streamlit as st
from math import sin, cos
import numpy as np


st.set_page_config(layout="wide")
c1, c2, c3 = st.columns(3)


with c1:
    def custom(x, y):
        return (sin(x/50) * cos(y/50) * 50 + 50)

    graphData = []
    steps = 50
    axisMax = 314
    axisStep = axisMax / steps

    # python for cycle with step
    for x in np.arange(0, axisMax, axisStep):
        for y in np.arange(0, axisMax, axisStep):
            value = custom(x, y)
            graphData.append({
                "x": x,
                "y": y,
                "z": value,
                "style": value
            })

    data = {
        "data": graphData,
        "options": {
            "width": "400px",
            "height": "400px",
            "style": "surface",
            "showPerspective": True,
            "showGrid": True,
            "keepAspectRatio": True,
            "verticalRatio": 0.5
        }
    }

    def handler1(eventData):
        st.session_state["output1"] = eventData['data']

    eventHandlers = [
        {
            "event": "cameraPositionChange",
            "callback": handler1,
        }
    ]

    visjs(title="# Graph3d Vis", type="graph3d", data=data, eventHandlers=eventHandlers, key="v1")
    st.header("Output")
    if "output1" in st.session_state:
        st.json(st.session_state.get("output1"))
    else:
        st.write("Waiting for event")


with c2:
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

    def handler2(eventData):
        st.session_state["output2"] = eventData['data']

    eventHandlers = [
        {
            "event": "click",
            "callback": handler2,
        }
    ]

    visjs(title="# Network Vis", type="network", data=data, eventHandlers=eventHandlers, key="v2")
    st.header("Output")
    if "output2" in st.session_state:
        st.json(st.session_state.get("output2"))
    else:
        st.write("Waiting for event")


with c3:
    data = {
        "items": [
            {"id": 1, "content": "item 1", "start": "2013-04-20"},
            {"id": 2, "content": "item 2", "start": "2013-04-14"},
            {"id": 3, "content": "item 3", "start": "2013-04-18"},
            {"id": 4, "content": "item 4", "start": "2013-04-16", "end": "2013-04-19"},
            {"id": 5, "content": "item 5", "start": "2013-04-25"},
            {"id": 6, "content": "item 6", "start": "2013-04-27"},
        ],
        "options": {}
    }


    def handler3(eventData):
        st.session_state["output3"] = eventData['data']

    eventHandlers = [
        {
            "event": "click",
            "callback": handler3,
        }
    ]

    visjs(title="# Timeline Vis", type="timeline", data=data, eventHandlers=eventHandlers, key="v3")
    st.header("Output")
    if "output3" in st.session_state:
        st.json(st.session_state.get("output3"))
    else:
        st.write("Waiting for event")
