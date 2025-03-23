// Obtener el campo de búsqueda y los elementos a filtrar
const searchInput = document.getElementById("searchInput");
const container = document.querySelector(".container"); // Ajusta este selector según los elementos a buscar
const items = container.querySelectorAll(".izquierda p, .derecha ul li"); // Ajusta según tu contenido

// Agregar un evento para detectar cambios en el campo de búsqueda
searchInput.addEventListener("input", function () {
    const searchText = searchInput.value.toLowerCase();

    items.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(searchText)) {
            item.style.display = "block"; // Mostrar si coincide
        } else {
            item.style.display = "none"; // Ocultar si no coincide
        }
    });
});
