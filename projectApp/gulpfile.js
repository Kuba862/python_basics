const { src, dest, watch, series } = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');

function scssTask() {
    return src('app/static/scss/style.scss', { sourcemaps: true })
    .pipe(sass())
    .pipe(postcss([cssnano()]))
    .pipe(dest('./app/static/css', { sourcemaps: '.'}));
}
function watchTask() {
    watch(['./app/static/scss/*.scss', './app/static/scss/about/*.scss', './app/static/scss/components/*.scss'], series(scssTask));
}

exports.default = series(scssTask, watchTask);