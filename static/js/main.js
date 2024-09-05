document.addEventListener('DOMContentLoaded', function() {
    // Example: Mark ticket as green when it's the patient's turn
    const tickets = document.querySelectorAll('.ticket');
    tickets.forEach(ticket => {
        ticket.addEventListener('click', function() {
            this.classList.add('ticket-green');
        });
    });
});

