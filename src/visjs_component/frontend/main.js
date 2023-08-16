// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.
const TYPE_NETWORK = "network"
const TYPE_TIMELINE = "timeline"
const TYPE_GRAPH3d = "graph3d"

function formatedEvent(type, event, data) {
  return sendValue(JSON.stringify({
    type: type,
    event: event,
    data: data
  }))
}

function renderGraph3d(data, eventNames) {
  let graphData = data.data
  let options = data.options

  var graphDataset = new vis.DataSet();

  graphData.forEach(function (item) {
    graphDataset.add(item);
  });

  var container = document.getElementById('my_render');
  var graph3d = new vis.Graph3d(container, graphDataset, options);

  eventNames = eventNames || []

  eventNames.forEach(event => {
    graph3d.on(event, (params) => formatedEvent(TYPE_GRAPH3d, event, params))
  })
}

function renderTimeline(data, eventNames) {
  let items = new vis.DataSet(data.items);
  let groups = data.groups
  let options = data.options

  // DOM element where the Timeline will be attached
  var container = document.getElementById('my_render');

  // Create a Timeline
  if (groups) {
    var timeline = new vis.Timeline(container, items, groups, options);
  } else {
    var timeline = new vis.Timeline(container, items, options);
  }

  eventNames = eventNames || []

  eventNames.forEach(event => {
    timeline.on(event, (params) => formatedEvent(TYPE_TIMELINE, event, params))
  })
}


function renderNetwork(data, eventNames) {
  let nodes = data.nodes
  let edges = data.edges
  let options = data.options

  // create an array with nodes
  var vis_nodes = new vis.DataSet(nodes);

  // create an array with edges
  var vis_edges = new vis.DataSet(edges);

  // create a network
  var container = document.getElementById('my_render');

  // provide the data in the vis format
  var data = {
    nodes: vis_nodes,
    edges: vis_edges
  };
  var vis_options = options;

  // initialize your network!
  var network = new vis.Network(container, data, options);

  eventNames = eventNames || []

  eventNames.forEach(event => {
    network.on(event, (params) => formatedEvent(TYPE_NETWORK, event, params))
  })

}


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

    const { type, data, eventNames } = event.detail.args;

    if (type == TYPE_NETWORK) {
      renderNetwork(data, eventNames)
    } else if (type == TYPE_TIMELINE) {
      renderTimeline(data, eventNames)
    } else if (type == TYPE_GRAPH3d) {
      renderGraph3d(data, eventNames)
    }

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
