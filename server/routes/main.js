var express = require("express");
var router = express.Router();
var path = require("path");

router.get("/", function(req, res){
  res.sendFile(path.join(__dirname+"/../../views/public/index.html"));
});

router.get("/data", function(req, res){
  res.sendFile(path.join(__dirname+"/../../data/hackdata.csv"));
});

router.get("/dataNew", function(req, res){
  res.sendFile(path.join(__dirname+"/../../data/hackdata_post.csv"));
});

module.exports = router;