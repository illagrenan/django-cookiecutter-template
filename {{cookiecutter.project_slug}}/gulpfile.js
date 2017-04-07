'use strict';

const gulp = require('gulp');

const less = require('gulp-less');
const autoprefixer = require('gulp-autoprefixer');
const cleanCSS = require('gulp-clean-css');
const gIf = require('gulp-if');
const argv = require('yargs').argv;
const del = require('del');
const exec = require('gulp-exec');
const browserSync = require('browser-sync').create();
const plumber = require('gulp-plumber');
const gutil = require('gulp-util');
const imagemin = require('gulp-imagemin');
const imageminPngquant = require('imagemin-pngquant');
const sourcemaps = require('gulp-sourcemaps');
const addsrc = require('gulp-add-src');

const jshint = require('gulp-jshint');
const eslint = require('gulp-eslint');
const babel = require('gulp-babel');
const ngAnnotate = require('gulp-ng-annotate');
const uglify = require('gulp-uglify');

const watch_argv = !!argv.watch;
const runserver_arg = !!argv.runserver;
const production = !!argv.production;

/**
 * Activate virtualenv and run Django server
 */
gulp.task('runserver', function () {
    gutil.log(gutil.colors.bgGreen('Starting Django server...'));

    var isWindows = /^win/.test(process.platform);
    var cmdToRun = 'data/.venv/bin/activate';

    if (isWindows) { // for Windows
        cmdToRun = 'data\\.venv\\Scripts\\activate';
    }

    var options = {
        continueOnError: false, // default = false, true means don't emit error event
        pipeStdout: false // default = false, true means stdout is written to file.contents
    };

    var reportOptions = {
        err: true, // default = true, false means don't write err
        stderr: true, // default = true, false means don't write stderr
        stdout: true // default = true, false means don't write stdout
    };

    gulp.src('src/**')
        .pipe(exec(cmdToRun + ' && python src/manage.py runserver', options))
        .pipe(exec.reporter(reportOptions));
});

gulp.task('browser-sync', function () {
    browserSync.init({
        notify: true,
        proxy: "127.0.0.1:8000"
    });
});

gulp.task('browser-reload', function () {
    browserSync.reload();
});

gulp.task('less', function () {
    gulp.src(['src/static/less/**/*.less'])
        .pipe(plumber())
        .pipe(gIf(!production, sourcemaps.init()))
        .pipe(less())
        .pipe(addsrc('src/static/css/**/*.css'))
        .pipe(gIf(production, cleanCSS({compatibility: 'ie8'})))
        .pipe(autoprefixer({
            browsers: ['last 4 versions'],
            cascade: false
        }))
        .pipe(gIf(!production, sourcemaps.write('.', {
            'includeContent': true,
            'sourceRoot': '.'
        })))
        .pipe(plumber.stop())
        .pipe(gulp.dest('data/build/css'));
});

gulp.task('js', function () {
    gulp.src('src/static/js/**/**.js')
        .pipe(plumber())
        .pipe(gIf(!production, sourcemaps.init()))
        .pipe(jshint('.jshintrc'))
        .pipe(jshint.reporter('jshint-stylish'))
        .pipe(eslint())
        .pipe(eslint.format())
        .pipe(babel({presets: ['es2015']}))
        .pipe(ngAnnotate())
        .pipe(gIf(production, uglify()))
        .pipe(gIf(!production, sourcemaps.write('.', {
            'includeContent': true,
            'sourceRoot': '.'
        })))
        .pipe(plumber.stop())
        .pipe(gulp.dest('data/build/js'));
});

gulp.task('images', function () {
    gulp.src('src/static/images/**')
        .pipe(plumber())
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [imageminPngquant()]
        }))
        .pipe(plumber.stop())
        .pipe(gulp.dest('data/build/images'));
});

gulp.task('clean:js', function () {
    return del([
        'data/build/js/*'
    ]);
});

gulp.task('clean:css', function () {
    return del([
        'data/build/css/*'
    ]);
});

gulp.task('clean', function () {
    gulp.start(['clean:js', 'clean:css']);
});

gulp.task('build', function () {
    gulp.start(['less', 'js', 'images']);

    if (watch_argv) {
        gulp.watch('src/static/less/**/*.less', ['less']);
        gulp.watch('src/static/js/**/*.js', ['js']);
        gulp.watch('src/static/images/**', ['images']);
    }

});

gulp.task('default', function () {
    var prompt = ['less', 'js', 'images', 'browser-sync'];

    if (runserver_arg) {
        prompt.push('runserver');
    }

    gulp.start(prompt);

    gulp.watch('src/static/less/**/*.less', ['less', 'browser-reload']);
    gulp.watch('src/static/js/**/*.js', ['js', 'browser-reload']);
    gulp.watch('src/static/images/**', ['images', 'browser-reload']);

    gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});
