window.onload = function () {
  startMcq1();
}
cancelled = false
const testTime = JSON.parse(document.getElementById('test-time').textContent);
const testId = JSON.parse(document.getElementById('test-id').textContent);
function startMcq1() {
  
  var c = testTime;
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
      if (cancelled) {
        return;
      }
      else {
        //document.getElementById("quiz-form").submit();
        document.getElementById("quizModalBtn").click();
        // $(".quiz-contentBtn").attr('disabled', 'disabled');
        document.getElementById('quizTimer').style.display = 'none';
        return false;
      }
      
      

    }


    c = c - 1;
    t = setTimeout(function () {
      timedCount1()
      $.ajax({
        url: "/mocktest/timeCount",
        data: {
          id: testId,
          time: c
        },
        dataType: 'json',
        success: function (res) {
          
        }
      });
    }, 1000);
  }
  
}
function quizTimeOut() {
  cancelled = true;
  document.getElementById("quizModalBtn").click();
  // $(".quiz-contentBtn").attr('disabled', 'disabled');
  document.getElementById('quizTimer').style.display = 'none';
  return false;
}

function quizSubmit(){
  document.getElementById("quiz-form").submit();
}
