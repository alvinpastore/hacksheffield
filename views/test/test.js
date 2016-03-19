var chai = require("chai");
chai.should();

import createJSX from "../src/tools/createJSX.jsx";

describe("jsonBox parse", function(){

  it("return basic value jsx for single string notes", function(){
    
    var notes = "Hello";
    var jsx = new createJSX(notes);
    var result = jsx.parse();

    jsx.should.be.exactly(<BasicValue />);

  });

});