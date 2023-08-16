from pathlib import Path
from typing import Optional, Callable
import json

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
    type: [str] = "network",
    data: dict = {},
    eventNames: list = [],
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

    # print(component_value)

    return component_value


def visjs(
    title: [str] = "Data Vis",
    type: [str] = "network",
    data: [dict] = {},
    eventHandlers: [list] = [],
):
    st.set_page_config(layout="wide")
    st.write(title)

    eventNames = []
    for eventHandler in eventHandlers:
        eventNames.append(eventHandler["event"])

    value = visjs_component(type=type, data=data, eventNames=eventNames)

    if eventHandlers:
        if value is not None:
            eventData = json.loads(value)

            for eventHandler in eventHandlers:
                if eventHandler["event"] == eventData['event']:
                    eventHandler["callback"](eventData)


# if __name__ == "__main__":
#     main(title="# Data Vis", type="network", data={
#         "nodes": [
#             {"id": 1, "label": 'Node 1'},
#             {"id": 2, "label": 'Node 2'},
#             {"id": 3, "label": 'Node 3'},
#             {"id": 4, "label": 'Node 4'},
#             {"id": 5, "label": 'Node 5'}
#         ],
#         "edges": [
#             {"from": 1, "to": 3},
#             {"from": 1, "to": 2},
#             {"from": 2, "to": 4},
#             {"from": 2, "to": 5}
#         ],
#         "options": {
#             "nodes": {
#                 "shape": "dot",
#                 "size": 16,
#             },
#             "edges": {
#                 "color": "#000000",
#             },
#             "physics": {
#                 "enabled": True,
#             },
#             "interaction": {
#                 "hover": True,
#             },
#             "height": "500px",
#         }
#     })
