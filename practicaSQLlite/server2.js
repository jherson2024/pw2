const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const PORT = process.env.PORT || 3000;

// Conexión a la base de datos SQLite
const db = new sqlite3.Database('imdb.db');

// Ruta para obtener todas las películas
app.get('/movies', (req, res) => {
    db.all('SELECT * FROM movies', (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

// Ruta para agregar una nueva película
app.post('/movies', (req, res) => {
    // Aquí deberías procesar los datos enviados por el cliente y agregar la película a la base de datos
    res.status(501).send('Not implemented');
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
