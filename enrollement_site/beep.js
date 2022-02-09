var msg = document.getElementById("msg");
msg.addEventListener("keydown", function (e) {
    if (e.key === 'Enter') {
        playSound(e);
        console.log('Validated');
    }
});


var snd = new Audio("beep.mp3");
function playSound(e) {
    setTimeout(function(){
        snd.autoplay = 'true';
        snd.load();
      }, 1000);    
    } 


