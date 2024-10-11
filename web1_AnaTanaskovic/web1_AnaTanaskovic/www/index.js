src="https://code.jquery.com/jquery-3.6.0.min.js"

document.addEventListener('DOMContentLoaded', function() {
    var modalOverlay = document.getElementsByClassName("modal-overlay");
    var modalDialog = document.getElementsByClassName("modal-dialog");

    document.querySelector(".modal-close-btn").addEventListener("click", function() {
        modalOverlay[0].style.display = "none";
        modalDialog[0].style.display = "none";
    });

    var purchaseBtns = document.querySelectorAll(".purchase-btn");

    purchaseBtns.forEach((purchaseBtn) => {
        purchaseBtn.addEventListener("click", function() {
            modalOverlay[0].style.display = "block";
            modalDialog[0].style.display = "block";
        });
    });

});

function purchaseplant(plant_id){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var plants = JSON.parse(xhr.responseText);
            updateCustomerplantsGrid(plants);
        }
    };
    xhr.open("GET", "remove_plant.py?plant_id=" + plant_id);
    xhr.send();
}

function updateCustomerplantsGrid(plants){
    var grid = document.getElementById('plantsGrid');
    var content = "";
    plants.forEach(plant => {
        content+="<div class='plant-card' id=plant-"+plant[0]+">";
        content+="<div class='plant-price'>"+plant[1]+"</div>";
        content+="<div class='plant-name'>"+plant[2]+"</div>";
        content+="<div class='card-image'><img src='/plant.jpeg' alt='"+plant[1]+" "+plant[2]+"'></div>";
        content+="<button onclick='purchaseplant("+plant[0]+")' class='purchase-btn' id='"+plant[0]+"'>Purchase</button>"
        content+="</div>"
    });
    grid.innerHTML = content;
}
