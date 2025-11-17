import React from "react";
import ReactFlow, { Background } from "reactflow";
import "reactflow/dist/style.css";

import TopNode from "./TopNode";
import CircleNode from "./CircleNode";

const nodeTypes = {
  topNode: TopNode,
  circleNode: CircleNode,
};

const nodes = [
  {
    id: "1",
    type: "topNode",
    position: { x: 200, y: 0 },
    data: { label: "Driving a commercial vehicle on a highway" },
  },
  {
    id: "2",
    type: "circleNode",
    position: { x: 200, y: 200 },
    data: { label: "Loss of control over the vehicle at 70 mph" },
  }
];

const edges = [
  { id: "e1-2", source: "1", target: "2", type: "smoothstep" }
];

export default function FlowDiagram() {
  return (
    <div style={{ width: "100%", height: "100vh" }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
      >
        <Background />
      </ReactFlow>
    </div>
  );
}
