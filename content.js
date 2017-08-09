// interval for refreshing the cleaning in milliseconds
var refreshInterval = 5000;

setInterval(function () {   
    var hiddenDivsCount = 0;
    var allAnchors = document.getElementsByTagName("a")
    for (var i = 0; i < allAnchors.length; i++) {
        var linkText = allAnchors[i].href.toLowerCase();
        if (linkText.indexOf("sarahah") >= 0) {
            hideUserPost(allAnchors[i]);
            hiddenDivsCount++;
        }
    }

    // well some divs might be calculated twice
    console.log("Divs hidden: " + hiddenDivsCount);
}, refreshInterval);



// hide the user post by recurring through its parents till the main post div is encountered
function hideUserPost(element)
{
    if (element) {
        if(element.className && element.className.indexOf("fbUserPost")>= 0)
        {
            element.style.display = 'none';            
        }
        else {
            hideUserPost(element.parentNode);
        }
    }
}