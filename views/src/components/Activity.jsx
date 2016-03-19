import React from "react";
import ReactDOM from "react-dom";

class Activity extends React.Component{
  render(){
    return (
      <div className="activity">
        <div className="col-sm-1 bar"></div>
        <div className="col-sm-3 info duration">20<br />mins</div>
        <div className="col-sm-3 info distance">80<br />meters</div>
        <div className="col-sm-3 info steps">3000<br />steps</div>
        <div className="col-sm-2 info path">Path</div>
      </div>
      );
  }
}

export default Activity;