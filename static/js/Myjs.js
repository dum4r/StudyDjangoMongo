window.onload = (event) =>{
  var rnd = Math.random() * (4000 - 2000) + 2000;
  // var rnd=0
  document.getElementById("progress").style.animation="loading " + rnd + "ms linear";
  setTimeout(function(){
    document.getElementById("loader").style.display = "none";
    document.getElementById("page").style.visibility="visible";
    typeWriter()
  }, rnd);
};

var i = 0;
var txt = "Hola mi nombre es "+name+", estoy aprendiendo FullStack c:";
var speed = 50;
function typeWriter() {
  if (i < txt.length) {
    document.getElementById("h1Text").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
