var spanElements = document.getElementsByTagName( "div" )[ 3 ];
spanElements = spanElements.getElementsByTagName( "span" );

for( var i = 0; i < spanElements.length; i ++ ) {
    spanElements[ i ].className = "orange";
    spanElements[ i ].innerHTML = "orange";
}

// 
var spansGold = document.getElementById( "holderTwo" );
spansGold = spansGold.getElementsByClassName( "gold" )

for( var i = 0; i < spansGold.length; i ++ ) {
    spansGold[ i ].innerHTML = "Gold Class Element";
}

console.log( spansGold );
// console.log( spanElements[ 3 ] );
