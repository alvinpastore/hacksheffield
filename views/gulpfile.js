var gulp = require("gulp");
var browserify = require("browserify");
var babelify = require("babelify");
var reactify = require("reactify");
var source = require("vinyl-source-stream");
var connect = require("gulp-connect");
var sass = require("gulp-sass");
// var gutil = require("gulp-util");
 
gulp.task("build", function() {
  bundleApp();
});

gulp.task("connect", function() {
  connect.server({
    root: "public",
    livereload: true
  });
});

gulp.task("sass", function(){
  gulp.src("src/sass/*.scss")
        .pipe(sass().on("error", sass.logError))
        .pipe(gulp.dest("public/css"));
});

gulp.task("watch", function(){
  gulp.watch(["src/**/*.jsx"], ["build"]);
  gulp.watch(["src/sass/**/*.scss"], ["sass"]);
});
 
gulp.task("default", ["build", "sass", "watch"]);

function bundleApp(){
  browserify({
    entries: "src/App.jsx",
    extensions: [".jsx"],
    debug: true
  })
  .transform("babelify", {presets: ["es2015", "react"]})
  .bundle()
  .pipe(source("build.js"))
  .pipe(gulp.dest("public/js"));
}