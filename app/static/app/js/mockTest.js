function startMcq1() {
  console.log('start mcq')
  var c = 2;
  var t;
  $(document).ready(function () {

    timedCount1();

  });
  function timedCount1() {
    if (c == 185) {
      return false;
    }

    var hours = parseInt(c / 3600) % 24;
    var minutes = parseInt(c / 60) % 60;
    var seconds = c % 60;
    var result = (hours < 10 ? "0" + hours : hours) + ":" + (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds < 10 ? "0" + seconds : seconds) ;
    // + "Min"  + "Time Left"
    $('#timer1').html(result);
    
    if (c < 0) {
  
      document.getElementById("quizModalBtn").click();
      // $(".quiz-contentBtn").attr('disabled', 'disabled');
      document.getElementById('quizTimer').style.display='none';
      return false;

    }


    c = c - 1;
    t = setTimeout(function () {
      timedCount1()
    }, 1000);
  }
  
}
function quizTimeOut(){
  document.getElementById("quizFormSubmit").click();
}

function quizSubmit(){
  location.href='mockTestAcheivement.html';
}
