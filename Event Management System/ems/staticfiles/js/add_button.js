document.addEventListener('DOMContentLoaded', function() {
    // Handle add button click
    document.querySelectorAll('.add-btn').forEach(button => {
        button.addEventListener('click', function() {
            const sspId = this.dataset.sspId;  // Get the SSP ID
            const quantityInput = document.querySelector(`#quantity_${sspId}`); // Get the corresponding quantity input
            const addButton = this; // Get the "Add" button

            // Show the quantity input and hide the "Add" button
            quantityInput.style.display = 'block';  
            addButton.style.display = 'none';  // Hide the "Add" button once clicked

            // Set the initial quantity to 1
            quantityInput.value = 1;  
        });
    });
});
