from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called visjs_component,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"visjs_component", path=str(frontend_dir)
)

selected_node = None
all_nodes = None

def find_selected_node():
    global selected_node
    global all_nodes

    for node in all_nodes:
        if node["id"] == selected_node:
            return node

def selected_node_details():
    global selected_node
    global all_nodes

    if selected_node is None:
        return 
    
    node = find_selected_node()
    title = node["label"]
    description = node["description"]
    noveltyScore = node["noveltyScore"]
    marketScore = node["marketScore"]
    usefulnessScore = node["usefulnessScore"]
    easeOfImplementationScore = node["easeOfImplementationScore"]
    impactScore = node["impactScore"]
    createdAt = node["createdAt"]

    st.write(f"## {title}")
    # st.write(f"**Title**: {title}")
    st.write(f"**Description**: {description}")
    st.write(f"**Novelty Score**: {noveltyScore}")
    st.write(f"**Market Score**: {marketScore}")
    st.write(f"**Usefulness Score**: {usefulnessScore}")
    st.write(f"**Ease of Implementation Score**: {easeOfImplementationScore}")
    st.write(f"**Impact Score**: {impactScore}")
    st.write(f"**Created At**: {createdAt}")


# Create the python function that will be called
def visjs_component(
    nodes: [list] = [],
    edges: [list] = [],
    options: dict = {},
    key: Optional[str] = None,
):
    global selected_node
    global all_nodes

    all_nodes = nodes
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        nodes=nodes,
        edges=edges,
        options=options,
        key=key,
    )

    selected_node = component_value

    # st.write(component_value)

    return component_value

# def main(
#     nodes: [list] = [],
#     edges: [list] = [],
#     options: dict = {},
# ):
#     st.set_page_config(layout="wide")

#     st.write("## Data Vis")
#     # value = visjs_component(nodes=nodes, edges=edges, options=options)

#     # st.write(value)


# if __name__ == "__main__":
#     main()
