from visjs_component import visjs
import streamlit as st
from math import sin, cos
import numpy as np

def custom(x, y):
    return (sin(x/50) * cos(y/50) * 50 + 50)

graphData = []
steps = 50
axisMax = 314
axisStep = axisMax / steps

print(axisStep)


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


eventHandlers = [
    {
        "event": "cameraPositionChange",
        "callback": lambda eventData: st.json(
            eventData['data']
        ),
    }
]

visjs(title="# Graph3d Vis", type="graph3d", data=data, eventHandlers=eventHandlers)

