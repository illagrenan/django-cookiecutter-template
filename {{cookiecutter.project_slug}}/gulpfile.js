'use strict';

require('es6-promise').polyfill();

var gulp = require('gulp');

var gulpLoadPlugins = require('gulp-load-plugins');
var plugins = gulpLoadPlugins();

plugins.pngquant = require('imagemin-pngquant');
plugins.cleancss = require('gulp-clean-css');
plugins.browserSync = require('browser-sync').create();
plugins.del = require('del');
plugins.argv = require('yargs').argv;

var production = !!plugins.argv.production;
var runserver_arg = !!plugins.argv.runserver;
var watch_argv = !!plugins.argv.watch;


/**
 * Activate virtualenv and run Django server
 */
gulp.task('runserver', function () {
    plugins.util.log(plugins.util.colors.bgGreen('Starting Django server...'));

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
        .pipe(plugins.exec(cmdToRun + ' && python src/manage.py runserver', options))
        .pipe(plugins.exec.reporter(reportOptions));
});

gulp.task('browser-sync', function () {
    plugins.browserSync.init({
        notify: true,
        proxy: "127.0.0.1:8000"
    });
});

gulp.task('browser-reload', function () {
    plugins.browserSync.reload();
});

gulp.task('less', function () {
    gulp.src(['src/static/less/**/*.less'])
        .pipe(plugins.plumber())
        .pipe(plugins.if(!production, plugins.sourcemaps.init()))
        .pipe(plugins.less())
        .pipe(plugins.addSrc('src/static/css/**/*.css'))
        .pipe(plugins.if(production, plugins.cleancss({compatibility: 'ie8'})))
        .pipe(plugins.autoprefixer({
            browsers: ['last 4 versions'],
            cascade: false
        }))
        .pipe(plugins.if(!production, plugins.sourcemaps.write('.', {
            'includeContent': true,
            'sourceRoot': '.'
        })))
        .pipe(plugins.plumber.stop())
        .pipe(gulp.dest('data/build/css'));
});

gulp.task('js', function () {
    gulp.src('src/static/js/**/**.js')
        .pipe(plugins.plumber())
        .pipe(plugins.if(!production, plugins.sourcemaps.init()))
        .pipe(plugins.jshint('.jshintrc'))
        .pipe(plugins.jshint.reporter('jshint-stylish'))
        .pipe(plugins.eslint())
        .pipe(plugins.eslint.format())        
        .pipe(plugins.babel({presets: ['es2015']}))
        .pipe(plugins.ngAnnotate())
        .pipe(plugins.if(production, plugins.uglify()))
        .pipe(plugins.if(!production, plugins.sourcemaps.write('.', {
            'includeContent': true,
            'sourceRoot': '.'
        })))
        .pipe(plugins.plumber.stop())
        .pipe(gulp.dest('data/build/js'));
});

gulp.task('images', function () {
    return gulp.src('src/static/images/**')
        .pipe(plugins.imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [plugins.pngquant()]
        }))
        .pipe(gulp.dest('data/build/images'));
});

gulp.task('clean:js', function () {
    return plugins.del([
        'data/build/js/*'
    ]);
});

gulp.task('clean:css', function () {
    return plugins.del([
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

    plugins.util.log(plugins.util.colors.bgGreen('Watching for changes...'));
});
