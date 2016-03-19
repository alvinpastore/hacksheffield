var express = require("express");
var path = require("path");
var logger = require("morgan");
var bodyParser = require("body-parser");
var helmet = require("helmet");
var compress = require("compression");

var app = express();

app.use(helmet());
app.use(compress());

app.use(logger("dev"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// routes
var mainRoutes = require("./routes/main.js");

app.use("/public", express.static(path.join(__dirname, "/../views/public")));
app.use("/", mainRoutes);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error("Not Found");
  err.status = 404;
  next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get("env") === "development") {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500).send(err);
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render("error", {
    message: err.message,
    error: {}
  });
});

app.listen(3000, function(){
  console.log("Listening on port 3000");
});

module.exports = app;
