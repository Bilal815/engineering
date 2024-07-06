window.onload = function() {
    var links = document.getElementsByTagName('a');
    for (var i = 0; i < links.length; i++) {
        links[i].onclick = function() {
            // remove active class from all links
            for (var j = 0; j < links.length; j++) {
                links[j].classList.remove('active');
            }
            // add active class to the clicked link
            this.classList.add('active');
        }
    }
}