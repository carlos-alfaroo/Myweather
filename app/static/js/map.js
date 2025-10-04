// map.js — manejo de Leaflet para seleccionar latitud/longitud

document.addEventListener('DOMContentLoaded', function() {
    console.log('map.js loaded');

    // Intenta obtener inputs por id; si no existen, intenta por name como fallback.
    let latInput = document.getElementById('lat') || document.querySelector('input[name="lat"]') || document.querySelector('input[name$="lat"]');
    let lonInput = document.getElementById('lon') || document.querySelector('input[name="lon"]') || document.querySelector('input[name$="lon"]');
    const mapContainer = document.getElementById('map');

    if (!mapContainer) {
        console.warn('Map container not found (#map).');
        return;
    }
    if (!latInput || !lonInput) {
        console.warn('Lat or Lon input not found. latInput:', latInput, 'lonInput:', lonInput);
        // Continuamos: el mapa funcionará, solo que no actualizará inputs si no existen.
    }

    // Coordenadas iniciales (Mérida, Yucatán)
    const initialLat = 20.9674;
    const initialLon = -89.5926;
    const initialZoom = 12;

    // Crear mapa
    const map = L.map('map').setView([initialLat, initialLon], initialZoom);

    // Agregar capa base
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Marcador inicial
    let marker = L.marker([initialLat, initialLon], {draggable: true}).ad