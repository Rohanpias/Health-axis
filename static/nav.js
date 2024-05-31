document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginToggle').addEventListener('click', function() {
        document.getElementById('loginForm').classList.add('active');
        document.getElementById('signupForm').classList.remove('active');
        this.classList.add('active');
        document.getElementById('signupToggle').classList.remove('active');
    });

    document.getElementById('signupToggle').addEventListener('click', function() {
        document.getElementById('signupForm').classList.add('active');
        document.getElementById('loginForm').classList.remove('active');
        this.classList.add('active');
        document.getElementById('loginToggle').classList.remove('active');
    });
});
