
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.add-btn');
    if (buttons.length === 0) {
        console.error("No 'Add' buttons found.");
    } else {
        buttons.forEach(function(button) {
            button.addEventListener('click', function() {
                try {
                    console.log("Hello");
                    const sspId = this.dataset.sspId;
                    const quantityInput = document.querySelector(`#quantity_${sspId}`);
                    const addButton = this;
                } catch (error) {
                    console.error("Error in click event:", error);
                }
                            // Show the quantity input and hide the "Add" button
            quantityInput.style.display = 'block';  
            addButton.style.display = 'none';  // Hide the "Add" button once clicked
            // Set the initial quantity to 1
            quantityInput.value = 1; 
            });
        });
    }
});