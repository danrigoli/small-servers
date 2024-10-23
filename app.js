const express = require('express');
const app = express();

// Lista de frases
const frases = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "La paciencia es un árbol de raíz amarga, pero de frutos muy dulces.",
    "No hay viento favorable para el que no sabe a dónde va.",
    "La vida es lo que hacemos de ella.",
    "El conocimiento es poder."
];

// Endpoint para devolver una frase al azar
app.get('/frase', (req, res) => {
    const frase = frases[Math.floor(Math.random() * frases.length)];
    res.json({ frase: frase });
});

// Endpoint para devolver el mayor de dos parámetros
app.get('/mayor', (req, res) => {
    const a = parseInt(req.query.a);
    const b = parseInt(req.query.b);
    const mayor = a > b ? a : b;
    res.json({ mayor: mayor });
});

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000');
});
