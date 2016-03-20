import React from "react";
import ReactDOM from "react-dom";

import moment from "moment";

import Parse from "csv-parse";

import Activity from "./components/Activity.jsx";
import DateComponent from "./components/DateComponent.jsx";

import Bar from "./components/Bar.jsx";

class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {data: [], date: 0, dataType: 'old'};
  }
  componentDidMount(){
    this.loadData("/data");
  }
  loadData(url){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.send();
    console.log("request sent");
    Parse(xhttp.responseText, function(err, output){
      if(err) return console.log(err);
      console.log("request parsed");
      this.setState({data: output});
    }.bind(this));
  }
  toggleData(){
    if(this.state.dataType == 'old'){
      this.state.dataType = 'new';
      this.loadData("/dataNew");
      // this.setState({dataType: 'new'});
    }else{
      this.state.dataType = 'old';
      this.loadData('/data');
      // this.setState({dataType: 'old'});
    }
  }
  addDays(date, days){
    var dat = new Date(date.valueOf())
    dat.setDate(dat.getDate() + days);
    return dat;
  }
  getAllDates(startDate, stopDate){
    var dateArray = new Array();
    var currentDate = startDate;
    while (currentDate <= stopDate) {
        dateArray.push( new Date (currentDate) )
        currentDate = this.addDays(currentDate, 1);
    }
    return dateArray;
  }
	render() {
    var data = this.state.data;
    var activityNodes = [];
    var dateNodes = [];

    var activityIndex = 1;
    var timeIndex = 2;
    var durationIndex = 3;
    var stepsIndex = 4;
    var distanceIndex = 5;
    var speedIndex = 6;
    var bearingIndex = 7;

    if(data.length > 0){
      console.log("data length > 0");

      var index1 = 798;
      var index2 = 1105;

      if(this.state.dataType == 'old'){
        index1 = 862;
        index2 = 1189;
      }

      var firstDate = new Date(parseInt(data[index1][timeIndex].trim()));
      var lastDate = new Date(parseInt(data[index2][timeIndex].trim()));

      var firstDateMoment = moment(firstDate);
      var lastDateMoment = moment(lastDate);

      var timeDifference = moment.duration(lastDateMoment.diff(firstDateMoment));

      console.log(timeDifference.asSeconds());

      for(var i=index1; i<index2; i++){
        var dataPoint = data[i];
        
        activityNodes.push(<Bar key={i} dataPoint={dataPoint} timeDifference={timeDifference} />)
      }

      console.log(dateNodes.length);

      console.log("pushed nodes");
    }

    var walkingStyle = {backgroundColor: "#A1D490"};
    var runningStyle = {backgroundColor: "#90C3D4"};
    var cyclingStyle = {backgroundColor: "#C390D4"};
    var stillStyle = {backgroundColor: "#ccc"};
    var vehicleStyle = {backgroundColor: "#D4A190"};
    var unknownStyle = {backgroundColor: "#A6705E"};
    var tiltingStyle = {backgroundColor: "#825EA6"};

		return (
      <div>
        <header><h1>Activity Data</h1></header>
        <div className="button-container">
          <button className="btn btn-primary" onClick={this.toggleData.bind(this)}>Toggle Data</button>
        </div>
        <div className="container-fluid legend-container">
          <div className="col-xs-1 legend" style={walkingStyle}>Walking</div>
          <div className="col-xs-1 legend" style={runningStyle}>Running</div>
          <div className="col-xs-1 legend" style={cyclingStyle}>Cycling</div>
          <div className="col-xs-1 legend" style={stillStyle}>Still</div>
          <div className="col-xs-1 legend" style={vehicleStyle}>Vehicle</div>
          <div className="col-xs-1 legend" style={unknownStyle}>Unknown</div>
          <div className="col-xs-1 legend" style={tiltingStyle}>Tilting</div>
        </div>
        <div className="container-fluid">
          {activityNodes}
        </div>
      </div>
      );
	}
}

ReactDOM.render(<App />, document.getElementById("mountPoint"));