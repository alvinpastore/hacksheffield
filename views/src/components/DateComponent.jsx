import React from "react";
import ReactDOM from "react-dom";
import moment from "moment";

class DateComponent extends React.Component{
  constructor(props){
    super(props);
  }
  render(){

    var momentDate = moment(this.props.date).format("MMMM Do YYYY")

    return (
      <div className="date">{momentDate}</div>
      );
  }
}

DateComponent.defaultProps = {date: new Date()};


export default DateComponent;