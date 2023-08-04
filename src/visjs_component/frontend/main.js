// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
  Streamlit.setComponentValue(value)
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    // You most likely want to get the data passed in like this
    // const {input1, input2, input3} = event.detail.args

    const { nodes, edges, options } = event.detail.args;
    console.log(nodes)
    console.log(edges)
    console.log(options)

    // create an array with nodes
    var vis_nodes = new vis.DataSet(nodes);

    // create an array with edges
    var vis_edges = new vis.DataSet(edges);

    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: vis_nodes,
        edges: vis_edges
    };
    var vis_options = options;

    // initialize your network!
    var network = new vis.Network(container, data, options);

    network.on("selectNode", function (params) {
      console.log(params)
      sendValue(params.nodes[0])
    })

    network.on("deselectNode", function (params) {
      sendValue(null)
    })



    // You'll most likely want to pass some data back to Python like this
    // sendValue({output1: "foo", output2: "bar"})
    window.rendered = true
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(550)
