// Timeline interactive
document.addEventListener('DOMContentLoaded', function() {
    // Animation au scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observer tous les événements de la timeline
    document.querySelectorAll('.timeline-event, .schema-box').forEach(el => {
        observer.observe(el);
    });

    // Effet hover sur les événements
    document.querySelectorAll('.timeline-event').forEach(event => {
        event.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        event.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});