function showAddplantForm(){
    var addplantForm = document.getElementById('form-container');
    var content = "";
    content+="<div id='form-container' class='flexColumn'>";
    content+="<form class='flexColumn' action='add_plant.py' method='post'>";
    content+="<h3 style='padding-bottom: 20px;'>Add new plant</h3>";
    content+="<label for='price'>price:</label>";
    content+="<input type='text' id='price' name='price'>";
    content+="<br><br>";
    content+="<label for='name'>Name:</label>";
    content+="<input type='text' id='name' name='name'>";
    content+="<br><br><br>";
    content+="<input class='btn' type='button' onclick='addNewplant()' value='Insert'>";
    content+="</form>";
    addplantForm.innerHTML = content;
}

function showEditplantForm(plant_id, price, name){
    var addplantForm = document.getElementById('form-container');
    var content = "";
    content+="<div id='form-container' class='flexColumn'>";
    content+="<form class='flexColumn' action='edit_plant.py' method='post'>";
    content+="<h3 style='padding-bottom: 20px;'>Edit plant</h3>";
    content+="<input type='hidden' id='editId' name='editId' value='" + plant_id + "'>";
    content+="<label for='price'>price:</label>";
    content+="<input type='text' id='editprice' name='editprice' value='" + price + "'>";
    content+="<br><br>";
    content+="<label for='name'>Name:</label>";
    content+="<input type='text' id='editName' name='editName' value='" + name + "'>";
    content+="<br><br><br>";
    content+="<input class='btn' type='button' onclick='editplant()' value='Update'>";
    content+="</form>";
    addplantForm.innerHTML = content;
}

function addNewplant(){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var plants = JSON.parse(xhr.responseText);
            updateAdminplantsTable(plants);
        }
    };
    xhr.open("GET", "add_plant.py?price=" + document.getElementById('price').value + "&name=" + document.getElementById('name').value);
    xhr.send();
}

function editplant(){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var plants = JSON.parse(xhr.responseText);
            updateAdminplantsTable(plants);
        }
    };
    xhr.open("GET", "edit_plant.py?id=" + document.getElementById('editId').value + "&price=" + document.getElementById('editprice').value + "&name=" + document.getElementById('editName').value);
    xhr.send();
}

function deleteplant(plant_id){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var plants = JSON.parse(xhr.responseText);
            updateAdminplantsTable(plants);
        }
    };
    xhr.open("GET", "remove_plant.py?plant_id=" + plant_id);
    xhr.send();
}

function updateAdminplantsTable(plants){
    var table = document.getElementById('plantsTable');
    var content = "<tr><th>ID</th><th>price</th><th>Name</th><th>Action</th></tr>";
    plants.forEach(plant => {
        content+= "<tr>";
        content+="<td>"+plant[0]+"</td><td>"+plant[1]+"</td><td>"+plant[2]+"</td>"
        content+= "<td><a id='edit-plant-btn' onclick=\"showEditplantForm(" + plant[0] + ", '" + plant[1] + "', '" + plant[2] + "')\" class='btn'>Edit</a> <a id='remove-plant-btn' onclick='deleteplant("+plant[0]+")' class='btn'>Delete</a> </td>";
        content+= "</tr>";
    });
    table.innerHTML = content;
    document.getElementById('form-container').innerHTML = "";
}