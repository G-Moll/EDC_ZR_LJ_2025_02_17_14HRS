// Encontrar los elementos del pagina
var h1 = document.getElementById( "title" );
var imgContainer = document.getElementsByTagName( "div" )[ 0 ];

var imgsArray = [ "grape", "grass", "olive", "snow", "steel" ];

var stringContent = "";
for( var i = 0; i < imgsArray.length; i ++ ) {
    stringContent += "<img class=thumb src=imgs/placeholder-" + imgsArray[ i ] + ".png>";
}
imgContainer.innerHTML = stringContent;
console.log( stringContent );


h1.innerHTML = "DOM & JS";
h1.className = "format";
h1.addEventListener( "click", function() {
    console.log( "Clicking on h1..!" );
});

// console.log( stringContent );
