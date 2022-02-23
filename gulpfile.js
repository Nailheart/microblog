import gulp from 'gulp';
import del from 'del';
import sass from 'gulp-dart-sass';
import csso from 'gulp-csso';
import rename from 'gulp-rename';
import browserSync from 'browser-sync';
import autoprefixer from 'gulp-autoprefixer';
import svgstore from 'gulp-svgstore';
import sourcemaps from 'gulp-sourcemaps';
import cheerio from 'gulp-cheerio';
import notify from 'gulp-notify';
import plumber from 'gulp-plumber';
import svgmin from 'gulp-svgmin';
import uglifyes from 'uglify-es';
import uglifycomposer from 'gulp-uglify/composer.js';

const { src, dest, series, parallel, watch } = gulp;
const uglify = uglifycomposer(uglifyes, console);

/**
 *  Основные директории
 */
const dirs = {
  app: 'app',
  static: 'app/static'
};

/**
 * Пути к файлам
 */
const path = {
  styles: {
    root: `${dirs.app}/scss/`,
    compile: `${dirs.app}/scss/styles.scss`,
    save: `${dirs.static}/css/`
  },
  templates: {
    root: `${dirs.app}/templates/`,
  },
  scripts: {
    root: `${dirs.app}/js/`,
    save: `${dirs.static}/js/`
  },
  img: {
    root: `${dirs.app}/img/`,
    save: `${dirs.static}/img/`
  }
};

/**
 * Основные задачи
 */
export const styles = () => src(path.styles.compile)
  .pipe(sourcemaps.init())
  .pipe(sass.sync().on('error', sass.logError))
  .pipe(autoprefixer())
  .pipe(csso())
  .pipe(rename({
    suffix: `.min`
  }))
  .pipe(sourcemaps.write('.'))
  .pipe(dest(path.styles.save));

export const scripts = () => src([`${path.scripts.root}*.js`, `!${path.scripts.root}*.min.js`])
  .pipe(uglify())
  .pipe(rename({
    suffix: '.min'
  }))
  .pipe(dest(path.scripts.save));

export const sprite = () => src([`${dirs.static}/img/**/*.svg`, `!${dirs.static}/img/sprite.svg`])
  .pipe(plumber({errorHandler: notify.onError("Error: <%= error.message %>")}))
  .pipe(svgmin({
    multipass: true,
    plugins: [
      'removeStyleElement',
      'removeScriptElement',
      'removeXMLNS',
    {
      removeViewBox: false
    }]
  }))
  .pipe(cheerio({
    run: function ($) {
      $('[fill]').attr('fill', 'currentColor');
      $('[stroke]').attr('stroke', 'currentColor').attr('fill', 'transparent');
      $('[style]').removeAttr('style');
    },
    parserOptions: { xmlMode: true }
  }))
  .pipe(svgstore({ inlineSvg: true }))
  .pipe(rename('sprite.svg'))
  .pipe(dest(path.img.save))

export const clean = () => del(path.styles.save);

export const devWatch = () => {
  const bs = browserSync.init({
    proxy: '127.0.0.1:5000',
    cors: true,
    notify: false,
    ui: false,
    open: false,
    scrollThrottle: 100,
  });
  watch(`${path.styles.root}**/*.scss`, styles).on('change', bs.reload);
  watch(`${path.templates.root}**/*.html`).on('change', bs.reload);
  watch(`${path.scripts.root}**/*.js`, scripts).on('change', bs.reload);
  watch(`${path.img.root}**/*.svg`, sprite).on('change', bs.reload);
};

/**
 * Задачи для разработки
 */
export const dev = series(clean, parallel(styles, scripts, sprite), devWatch);

/**
 * Для билда
 */
export const build = series(clean, parallel(styles, scripts, sprite));

export default dev;
