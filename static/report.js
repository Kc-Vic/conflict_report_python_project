
document.addEventListener('DOMContentLoaded', function() {
    // Get the delete button and modal elements
    const deleteReportButton = document.getElementById('deleteReportButton');
    const deleteReportModal = document.getElementById('deleteReportModal');
    
    if (deleteReportButton && deleteReportModal) {
        // Initialize Bootstrap modal
        const deleteModal = new bootstrap.Modal(deleteReportModal);
        
        // Add click event to delete button
        deleteReportButton.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Get report ID from button attribute
            const reportId = this.getAttribute('report_id');
            
            // Set the report ID in the hidden input field
            document.getElementById('report_id').value = reportId;
            
            // Get the current slug from URL
            const pathParts = window.location.pathname.split('/');
            const slug = pathParts[pathParts.length - 2]; // Gets slug from URL like /slug/
            
            // Set the form action URL
            const deleteForm = document.getElementById('deleteReportForm');
            deleteForm.action = `/report_delete/${slug}/`;
            
            // Show the modal
            deleteModal.show();
        });
        
        // Handle modal close buttons
        const modalCloseButtons = deleteReportModal.querySelectorAll('[data-dismiss="modal"]');
        modalCloseButtons.forEach(button => {
            button.addEventListener('click', function() {
                deleteModal.hide();
            });
        });
    }
    
    // Handle comment form submission if it exists
    const submitButton = document.getElementById("submitButton");
    if (submitButton) {
        // Add any comment form handling here if needed
    }
});