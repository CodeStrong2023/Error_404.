let ataqueJugador;
let ataqueEnemigo;
let vidasJugador = 3;
let vidasEnemigo = 3;

function iniciarJuego() {
    const botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    const botonesAtaque = document.querySelectorAll('.boton-ataque');
    botonesAtaque.forEach(boton => {
        boton.addEventListener('click', (e) => seleccionarAtaque(e.target.id));
    });

    const botonReiniciar = document.getElementById('boton-reiniciar');
    botonReiniciar.addEventListener('click', reiniciarJuego);
}

function seleccionarPersonajeJugador() {
    const personajes = document.querySelectorAll('input[name="personaje"]');
    const spanPersonajeJugador = document.getElementById('personaje-jugador');
    const imagenJugador = document.getElementById('imagen-jugador');
    let personajeSeleccionado = false;

    personajes.forEach(personaje => {
        if (personaje.checked) {
            personajeSeleccionado = true;
            spanPersonajeJugador.innerHTML = personaje.nextElementSibling.alt;
            imagenJugador.src = personaje.nextElementSibling.src;
        }
    });

    if (!personajeSeleccionado) {
        alert('Selecciona un personaje');
        return;
    }

    seleccionarPersonajeEnemigo();
    document.getElementById('seleccionar-personaje').style.display = 'none';
    document.getElementById('seleccionar-ataque').style.display = 'block';
}

function seleccionarPersonajeEnemigo() {
    const personajes = ['Zuko', 'Katara', 'Aang', 'Toph'];
    const personajeAleatorio = personajes[aleatorio(0, personajes.length - 1)];
    const spanPersonajeEnemigo = document.getElementById('personaje-enemigo');
    const imagenEnemigo = document.getElementById('imagen-enemigo');

    spanPersonajeEnemigo.innerHTML = personajeAleatorio;
    imagenEnemigo.src = `images/${personajeAleatorio.toLowerCase()}.png`;
}

function seleccionarAtaque(ataqueId) {
    ataqueJugador = ataqueId.replace('boton-', '');
    ataqueEnemigoAleatorio();
    combate();
}

function ataqueEnemigoAleatorio() {
    const ataques = ['puño', 'patada', 'barrida'];
    ataqueEnemigo = ataques[aleatorio(0, ataques.length - 1)];
}

function combate() {
    const mensajeBatalla = document.getElementById('mensaje-batalla');

    if (ataqueJugador === ataqueEnemigo) {
        mensajeBatalla.innerHTML = '¡Empate!';
    } else if (
        (ataqueJugador === 'puño' && ataqueEnemigo === 'barrida') ||
        (ataqueJugador === 'patada' && ataqueEnemigo === 'puño') ||
        (ataqueJugador === 'barrida' && ataqueEnemigo === 'patada')
    ) {
        mensajeBatalla.innerHTML = '¡Ganaste esta ronda!';
        vidasEnemigo--;
    } else {
        mensajeBatalla.innerHTML = 'Perdiste esta ronda...';
        vidasJugador--;
    }

    actualizarVidas();
    revisarFinJuego();
}

function actualizarVidas() {
    document.getElementById('vidas-jugador').innerHTML = vidasJugador;
    document.getElementById('barra-vida-jugador').value = vidasJugador;
    document.getElementById('vidas-enemigo').innerHTML = vidasEnemigo;
    document.getElementById('barra-vida-enemigo').value = vidasEnemigo;
}

function revisarFinJuego() {
    if (vidasJugador === 0) {
        mostrarMensajeFin('Perdiste el juego... ¡Intenta nuevamente!', 'images/derrota.gif', false);
    } else if (vidasEnemigo === 0) {
        const spanPersonajeJugador = document.getElementById('personaje-jugador').innerHTML;
        const spanPersonajeEnemigo = document.getElementById('personaje-enemigo').innerHTML;
        const mensaje = `¡Ganaste! ${spanPersonajeJugador} derrotó a ${spanPersonajeEnemigo} - CPU`;
        const imagenSrc = `images/${spanPersonajeJugador.toLowerCase()}Feliz.png`;
        mostrarMensajeFin(mensaje, imagenSrc, true);
    }
}

function mostrarMensajeFin(mensaje, imagenSrc, jugadorGana) {
    const textoVictoria = document.getElementById('texto-victoria');
    const imagenVictoria = document.getElementById('imagen-victoria');
    textoVictoria.innerHTML = mensaje;
    imagenVictoria.src = imagenSrc;
    if (jugadorGana) {
        const imagenEnemigo = document.getElementById('imagen-enemigo');
        imagenVictoria.insertAdjacentHTML('afterend', `<img src="${imagenEnemigo.src}" alt="Enemigo derrotado" class="imagen-derrota"/>`);
    }
    document.getElementById('seleccionar-ataque').style.display = 'none';
    document.getElementById('reiniciar').style.display = 'block';
}

function reiniciarJuego() {
    location.reload();
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

window.addEventListener('load', iniciarJuego);
