
var count = document.querySelectorAll(".drum").length
for(var i=0;i<count;i++){
    document.querySelectorAll(".drum")[i].addEventListener("click",function(){
        var audio = new Audio("sounds/tom-1.mp3");
        audio.play();
    });
    
}


