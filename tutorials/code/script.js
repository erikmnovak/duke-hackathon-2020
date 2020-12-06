onload = function () {
  if ("speechSynthesis" in window) {
    /* speech synthesis supported */
    var synth = speechSynthesis;
    var flag = false;

    /* references to the buttons */
    var playEle = document.getElementById("play");
    var pauseEle = document.getElementById("pause");
    var stopEle = document.getElementById("stop");

    /* click event handlers for the buttons */
    playEle.addEventListener("click", onClickPlay);
    pauseEle.addEventListener("click", onClickPause);
    stopEle.addEventListener("click", onClickStop);

    function onClickPlay() {
      if (!flag) {
        let str = "";
        var test = document.querySelectorAll(".test");
        for (let i = 0; i < test.length; i++) {
          str += test[i].textContent + " ";
        }
        console.log(str);
        flag = true;
        utterance = new SpeechSynthesisUtterance(str);
        utterance.voice = synth.getVoices()[0];
        utterance.onend = function () {
          flag = false;
          playEle.className = pauseEle.className = "";
          stopEle.className = "stopped";
        };
        playEle.className = "played";
        stopEle.className = "";

        synth.speak(utterance);
        console.log("H");
      }
      if (synth.paused) {
        /* unpause/resume narration */
        playEle.className = "played";
        pauseEle.className = "";
        synth.resume();
      }
    }

    function onClickPause() {
      if (synth.speaking && !synth.paused) {
        /* pause narration */
        pauseEle.className = "paused";
        playEle.className = "";
        synth.pause();
      }
    }

    function onClickStop() {
      if (synth.speaking) {
        /* stop narration */
        /* for safari */
        stopEle.className = "stopped";
        playEle.className = pauseEle.className = "";
        flag = false;
        synth.cancel();
      }
    }
  } else {
    /* speech synthesis not supported */
    console.log("H");
    msg = document.createElement("h5");
    msg.textContent = "Detected no support for Speech Synthesis";
    msg.style.textAlign = "center";
    msg.style.backgroundColor = "red";
    msg.style.color = "white";
    msg.style.marginTop = msg.style.marginBottom = 0;
    document.body.insertBefore(msg, document.querySelector("div"));
  }
};

var arr = [];
function myJsFunction() {
  var text = document.getElementById("email").value;
  arr.push(text);
  console.log(arr);
  document.getElementById("email").value = "";
}
// document.getElementById("btn").addEventListener("click", function () {
//   let email = document.querySelector(".email").textContent;
//   console.log(email);
//   arr.push(email);
//   //document.querySelector(".email").textContent = "";
// });
