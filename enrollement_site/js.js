

function saveFile(){ //Enregistre dans un txt le contenu tapé
   
    var surname = document.getElementById("txtSurname");
    var name = document.getElementById("txtName");
    var msg = document.getElementById("msg");

    
    let data = "\r Surname: " + surname.value + " \r\n " + "Name: " + name.value + " \r\n "  + "Message: " + msg.value;
    console.log(data);
    const textToBLOB = new Blob([data], { type: "text/plain" });
    var filename = "test"

    let newLink = document.createElement("a");
    newLink.download = surname.value+"_text" // Nom du fichier texte

    if (window.webkitURL != null) {
        newLink.href = window.webkitURL.createObjectURL(textToBLOB);
    } else {
        newLink.href = window.URL.createObjectURL(textToBLOB);
        newLink.style.display = "none";
        document.body.appendChild(newLink);
    }
    newLink.click();
    //Remise a 0 des champs aprés l'enregistrement
    document.getElementById("txtSurname").value = '';
    document.getElementById("txtName").value = '';
    document.getElementById("msg").value = '';
};

var audioChunks;
var snd = new Audio("beep.mp3");
startRecord.onclick = e => {
  startRecord.disabled = true;
  stopRecord.disabled=false;
  // This will prompt for permission if not allowed earlier
  navigator.mediaDevices.getUserMedia({audio:true})
    .then(stream => {
      audioChunks = [];
      rec = new MediaRecorder(stream);
      rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive"){
          let blob = new Blob(audioChunks,{type:'audio/wave'});
          recordedAudio.src = URL.createObjectURL(blob);
          recordedAudio.controls=true;
          recordedAudio.autoplay=true;
          audioDownload.href = recordedAudio.src;
          audioDownload.download = document.getElementById("txtSurname").value+"_"+document.getElementById("txtName").value+"_record"
          audioDownload.innerHTML = "Télécharger le fichier audio";
       }
      }
    rec.start();
    setTimeout(function(){
      snd.autoplay = 'true';
      snd.load();
    }, 1000);    
  })
  .catch(e=>console.log(e));
}
stopRecord.onclick = e => {
  snd.autoplay = 'true';
  snd.load();

  setTimeout(function(){
    console.log("Stop");
    startRecord.disabled = false;
    //sendButton.disabled=false;
    //audioDownload.disabled = false;
    stopRecord.disabled=true;
    rec.stop();
  }, 2000);
}

