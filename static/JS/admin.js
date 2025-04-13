function addDish() {
    const category = document.getElementById("category").value;
    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const price = document.getElementById("price").value;
    const image = document.getElementById("image").value;

    const newDish = {
        category: category,
        name: name,
        description: description,
        price: parseInt(price),
        image: image
    };

    fetch('/static/data/menu.json')
        .then(response => response.json())
        .then(data => {
            data.push(newDish);
            saveUpdatedMenu(data);
        });
}

function saveUpdatedMenu(updatedData) {
    fetch('/save-menu', {
        method: 'POST',
        body: JSON.stringify(updatedData),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(() => alert("Блюдо добавлено!"));
}
