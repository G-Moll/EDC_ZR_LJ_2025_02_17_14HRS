var greenElements = document.getElementsByClassName( "green" );
console.log( greenElements );

for( var i = 0; i < greenElements.length; i ++ ) {
    greenElements[ i ].innerHTML = "Green";
    console.log( greenElements[ i ] );
}


// console.log( greenElements[ 0 ] );
// console.log( greenElements[ 1 ] );
// console.log( greenElements[ 2 ] );
// console.log( greenElements[ 3 ] );
