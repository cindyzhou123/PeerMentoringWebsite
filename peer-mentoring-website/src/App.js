import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import HeadingComponent from "./components/HeadingComponent";

function App() {
  return (
    <Router>
      <Route exact path="/" component={HeadingComponent} />
    </Router>
  );
}

export default App;
