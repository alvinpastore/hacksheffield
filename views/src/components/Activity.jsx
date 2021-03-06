import React from "react";
import ReactDOM from "react-dom";
import moment from "moment";

class Activity extends React.Component{
  constructor(props){
    super(props);
    this.colour = "#222";
    this.walkingColour = "#A1D490";
    this.runningColour = "#90C3D4";
    this.cyclingColor = "#C390D4";
    this.stillColour = "#ccc";
    this.vehicleColour = "#D4A190";
    this.unknownColour = "#A6705E";
    this.tiltingColour = "#825EA6";
  }
  render(){

    switch(this.props.type){
      case "WALKING":
        this.colour = this.walkingColour;
        break;
      case "RUNNING":
        this.colour = this.runningColour;
        break;
      case "IN_VEHICLE":
        this.colour = this.vehicleColour;
        break;
      case "ON_BICYCLE":
        this.colour = this.cyclingColour;
        break;
      case "STILL":
        this.colour = this.stillColour;
        break;
      case "UNKNOWN":
        this.colour = this.unknownColour;
        break;
      case "TILTING":
        this.colour = this.tiltingColour;
        break;
      default:
        this.colour = this.unknowColour;
        break;
    }
    var activityStyles = {backgroundColor: this.colour}
    var date = moment.unix(this.props.time / 1000).format("hh:mm");
    return (
      <div className="activity" style={activityStyles}>
        <div className="col-xs-1 info date">{date}</div>
        <div className="col-xs-2 info type">{this.props.type}</div>
        <div className="col-sm-2 info duration">{this.props.duration} mins</div>
        <div className="col-sm-2 info distance">{this.props.distance} meters</div>
        <div className="col-sm-2 info steps">{this.props.steps} steps</div>
        <div className="col-sm-2 info path">Path</div>
      </div>
      );
  }
}

Activity.defaultProps = {time: 0, duration: 0, distance: 0, steps: 0, type: "UNKNOWN"};


export default Activity;