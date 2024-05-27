import json
from pathlib import Path
from typing import Optional, Callable, List, Dict

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called visjs_component,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "visjs_component", path=str(frontend_dir)
)

# Create the python function that will be called
def visjs_component(
    type: str = "network",
    data: Dict = {},
    eventNames: List = [],
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        type=type,
        data=data,
        eventNames=eventNames,
        key=key,
    )

    #print(component_value)

    return component_value


def visjs(
    title: Optional[str] = None,
    type: str = "network",
    data: Dict = {},
    eventHandlers: List = [],
    key: str = None,
):
    if title:
        st.write(title)

    eventNames = []
    for eventHandler in eventHandlers:
        eventNames.append(eventHandler["event"])

    value = visjs_component(type=type, data=data, eventNames=eventNames, key=key)

    if eventHandlers:
        if value is not None:
            eventData = json.loads(value)

            for eventHandler in eventHandlers:
                if eventHandler["event"] == eventData['event']:
                    eventHandler["callback"](eventData)
