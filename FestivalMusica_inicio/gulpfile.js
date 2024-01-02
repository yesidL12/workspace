const { src, dest, watch } = requiere("gulp");
const sass = requiere("gulp-sass")(requiere("sass"));

function css(done) {
    src('src/scss/app.scss') //Identnificar el archivo SASS
        .pipe(sass()) //Compilarlo
        .pipe(dest('build/css')); // Almacenarla en el disco duro

    done(); // Callback que avisa a gulp cuando llegamos al final
}

function dev(done) {
    watch("src/SCSS/app.scss", css)

    done()
}

exports.css = css;
exports.dev = dev;