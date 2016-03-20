import React from "react";
import ReactDOM from "react-dom";
import moment from "moment";

class Bar extends React.Component{
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

    switch(this.props.dataPoint[1].trim().toUpperCase()){
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

    var activityIndex = 1;
    var timeIndex = 2;
    var durationIndex = 3;
    var stepsIndex = 4;
    var distanceIndex = 5;
    var speedIndex = 6;
    var bearingIndex = 7;

    var timeDifference = this.props.timeDifference;

    var dataPoint = this.props.dataPoint;
    var barWidth = (dataPoint[durationIndex] / timeDifference.asSeconds()) * 100;
    var styles = {backgroundColor: this.colour, width: barWidth + "%", float: "left"};
    return (
      <div className="activity" style={styles}>
      </div>
      );
  }
}

Bar.defaultProps = {dataPoint: [0,0,0,0,0,0,0], timeDifference: 0};

export default Bar;