const { src, dest, watch, series } = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');

// function scssTask() {
//     return src('app/static/scss/style.scss', { sourcemaps: true })
//     .pipe(sass())
//     .pipe(postcss([cssnano()]))
//     .pipe(dest('./app/static/css', { sourcemaps: '.'}));
// }
// function watchTask() {
//     watch(['./app/static/scss/*.scss', './app/static/scss/about/*.scss', './app/static/scss/components/*.scss'], series(scssTask));
// }
function scssTaskCgo() {
    return src('citizengo/static/scss/style.scss', { sourcemaps: true })
    .pipe(sass())
    .pipe(postcss([cssnano()]))
    .pipe(dest('./citizengo/static/css', { sourcemaps: '.'}));
}
function watchTaskCgo() {
    watch(['citizengo/static/scss/*.scss', 'citizengo/static/scss/components/*.scss'], series(scssTaskCgo));
}

exports.default = series(scssTaskCgo, watchTaskCgo);