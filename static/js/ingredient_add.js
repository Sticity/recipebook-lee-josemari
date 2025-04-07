function add_ingredient() {
    const container = document.getElementById('ingredients');
    const block = container.firstElementChild.cloneNode(true);
    container.appendChild(block);
}
