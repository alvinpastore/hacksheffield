import React from "react";
import ReactDOM from "react-dom";

import Activity from "./components/Activity.jsx";

class App extends React.Component {
	render() {
		return (
      <div>
        <header><h1>Activity Data</h1></header>
        <div className="container-fluid" style={{height: 100 + '%'}}>
          <Activity />
        </div>
      </div>
      );
	}
}

ReactDOM.render(<App />, document.getElementById("mountPoint"));