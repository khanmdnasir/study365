
/***What New Banner****/
$(".homeWhatsNewcarousel").owlCarousel({
  margin: 20,
  loop: true,
  autoplay: true,
  autoplayTimeout: 2000,
  autoplayHoverPause: true,
  responsive: {
    0: {
      items: 1,
      nav: false,
      // dots: false
    },
    600: {
      items: 2,
      nav: false,
      // dots: false
    },
    1000: {
      items: 3,
      nav: false
    },
    1100: {
      items: 4,
      nav: false
    }
  }
});

/***Popular Course*/
$('#carousel0').owlCarousel({
  // loop: true,
  margin: 15,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 3,
      dots: false,
      // nav: true
    },
    1100: {
      items: 3,
      dots: false,
      // nav: true
    },
    1700: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})


// Top rated teacher
$('#carousel1').owlCarousel({
  // loop: true,
  margin: 10,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 2,
      dots: false,
      // nav: true
    },
    1100: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})
$('#carousel2').owlCarousel({
  // loop: true,
  margin: 10,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 2,
      dots: false,
      // nav: true
    },
    1100: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})
$('#carousel3').owlCarousel({
  // loop: true,
  margin: 10,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 2,
      dots: false,
      // nav: true
    },
    1100: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})
$('#carousel4').owlCarousel({
  // loop: true,
  margin: 10,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 2,
      dots: false,
      // nav: true
    },
    1100: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})
$('#carousel5').owlCarousel({
  // loop: true,
  margin: 10,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 2,
      dots: false,
      // nav: true
    },
    1100: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})
$('#carousel6').owlCarousel({
  // loop: true,
  margin: 10,
  autoplay: true,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<span class='fas fa-arrow-circle-left' </span>", "<span class='fas fa-arrow-circle-right' </span>"
  ],
  responsive: {
    0: {
      items: 1,
      dots: false,
      // nav: false
    },
    600: {
      items: 2,
      dots: false,
      // nav: false
    },
    1000: {
      items: 2,
      dots: false,
      // nav: true
    },
    1100: {
      items: 4,
      dots: false,
      // nav: true
    }
  }
})



// Otp-Verification
function clickEvent(first, last) {
  if (first.value.length) {
    document.getElementById(last).focus();
  }
}


//hide toggle
$(".toggle-password").click(function () {
  $(this).toggleClass("fa fa-eye-slash");
  input = $(this).parent().find("input");
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});

// Accordian Active
// .accordion .cursor
var selector = '.cursor';

$(selector).on('click', function () {
  $(selector).removeClass('active');
  $(this).addClass('active');
});

var selector2 = '.cursor2';

$(selector2).on('click', function () {
  $(selector2).removeClass('active');
  $(this).addClass('active');
});

// Course Playlist Accordian button click change

function btnCheck(check) {
  // document.querySelector('.demo').style.display = "none";
  var demos=document.getElementsByClassName('demo')
  for (var i = 0; i < demos.length; i++){
    demos[i].style.display = "none";
}
  
  $.ajax({
      url:"/Course_PlayList_Json",

      data:{
      lesson_id:check
      },
      dataType:'json',
      success:function(res){
      
      
          if (res.lesson_type == "A") {
            
          document.querySelector('.a'+res.id).style.display = "block";
          
          }
          else if (res.lesson_type == "V") {
            
              document.querySelector('.v'+res.id).style.display = "block";
              
          }
          else if (res.lesson_type == "Q") {
            
              document.querySelector('.q'+res.id).style.display = "block";
              
              
          }
          else if (res.lesson_type == 'I'){
            
            document.querySelector('.i'+res.id).style.display = "block";
          }
          
       

        
         
      
      
      }
      });
  
  }

function btnCheck2(check2) {
  if (check2 == "instruction") {
    document.querySelector('.uploadVideo').style.display = "none";
    document.querySelector('.assignment').style.display = "none";
    document.querySelector('.quiz').style.display = "none";
    document.querySelector('.instruction').style.display = "block";
    document.getElementById('lesson_type').value="I";
  }
  else if (check2 == "quiz") {
    document.querySelector('.uploadVideo').style.display = "none";
    document.querySelector('.assignment').style.display = "none";
    document.querySelector('.quiz').style.display = "block";
    document.querySelector('.instruction').style.display = "none";
    document.getElementById('lesson_type').value="Q";
  }
  else if (check2 == "assignment") {
    document.querySelector('.uploadVideo').style.display = "none";
    document.querySelector('.assignment').style.display = "block";
    document.querySelector('.quiz').style.display = "none";
    document.querySelector('.instruction').style.display = "none";
    document.getElementById('lesson_type').value="A";
  }
  else if (check2 == "uploadVideo") {
    document.querySelector('.uploadVideo').style.display = "block";
    document.querySelector('.assignment').style.display = "none";
    document.querySelector('.quiz').style.display = "none";
    document.querySelector('.instruction').style.display = "none";
    document.getElementById('lesson_type').value="V";
  }

}

// add a cource custom file upload
const realFileBtn = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");

customBtn.addEventListener("click", function () {
  realFileBtn.click();
});

realFileBtn.addEventListener("change", function () {
  if (realFileBtn.value) {
    customTxt.innerHTML = realFileBtn.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt.innerHTML = "No file chosen, yet.";
  }
});

//Student profile Replace Div

function toggleChange(change, name) {
  if (change == "change") {
    document.querySelector(".none-" + name).style.display = "none";
    document.querySelector(".block-" + name).style.display = "block";
  }
  else if (change == "unchange") {
    document.querySelector(".none-" + name).style.display = "block";
    document.querySelector(".block-" + name).style.display = "none";
  }
  // its only for teacher profile payment3 or where 3 divs need to toggle
  else if (change == "tchProfile") {
    document.querySelector(".none-" + name).style.display = "none";
    document.querySelector(".block2-" + name).style.display = "block";
  }

}


//Image Upload

function readURL(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function (e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      // $('.image-title').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}

function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
  $('.image-upload-wrap').addClass('image-dropping1');
});
$('.image-upload-wrap').bind('dragleave', function () {
  $('.image-upload-wrap').removeClass('image-dropping1');
});

function read2(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function (e) {
      $('.image-upload-wrap2').hide();

      $('.file-upload-image2').attr('src', e.target.result);
      $('.file-upload-content2').show();

      // $('.image-title').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload2();
  }
}


function removeUpload2() {
  $('.file-upload-input2').replaceWith($('.file-upload-input2').clone());
  $('.file-upload-content2').hide();
  $('.image-upload-wrap2').show();
}
$('.image-upload-wrap2').bind('dragover', function () {
  $('.image-upload-wrap2').addClass('image-dropping2');
});
$('.image-upload-wrap2').bind('dragleave', function () {
  $('.image-upload-wrap2').removeClass('image-dropping2');
});


//Reply And Comment

function submit_comment() {
  var comment = $('.commentar').val();
  el = document.createElement('li');
  el.className = "box_result row";
  el.innerHTML =
    '<div class=\"col-md-1\">' +
    // user image link
    '<div class=\"avatar_comment\">' +
    '<img src=\"Assets/Images/SingleCourse/2authorLogo.png\" alt=\"avatar\"/>' +
    '</div>' +
    '</div>' +
    '<div class=\"result_comment col-md-11 ms-3\">' +
    '<h4 class=\"tools_comment\">Anonimous <span aria-hidden=\"true\"> · </span><span>1m</span></h4>' +
    '<p>' + comment + '</p>' +
    '<div class=\"tools_comment\">' +
    '<a class=\"replay\" href=\"#\">Reply</a>' +
    '</div>' +
    '<ul class="child_replay"></ul>' +
    '</div>';
  document.getElementById('list_comment').prepend(el);
  $('.commentar').val('');
}

$(document).ready(function () {

  // $('#list_comment').on('click', '.replay', function (e) {
  //     cancel_reply();
  //     $current = $(this);
  //     el = document.createElement('li');
  //     el.className = "box_reply row";
  //     el.innerHTML =
  //     '<div class=\"col-md-12 reply_comment\">' +
  //        '<div class=\"row\">' +
  //             '<div class=\"col-md-1\">' + 

  //                '<div class=\"avatar_comment\">'+
  //                   '<img src=\"https://images.unsplash.com/photo-1592492152545-9695d3f473f4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=80\" alt=\"avatar\"/>' +
  //                '</div>' +
  //             '</div>' +
  //             '<div class=\" d-flex gx-0 col-md-10\">' +
  //                  '<textarea class=\"box_comment comment_replay w-50\" placeholder=\"Add a comment...\"></textarea>' +
  //                 '<div class=\"box_post\">' +
  //                    '<button class=\"cancel btn btn3 bg-cl-pm mx-1 px-1\" onclick=\"cancel_reply()\" type=\"button\">Cancel</button>' +
  //                    '<button class=\"btn btn3 bg-cl-pm  px-1" onclick=\"submit_reply()\" type=\"button\" value=\"1\">Reply</button>' +
  //                '</div>' +
  //            '</div>' +
  //         '</div>' +
  //     '</div>';
  //     $current.closest('li').find('.child_replay').prepend(el);
  // });
});

function submit_reply() {
  var comment_replay = $('.comment_replay').val();
  el = document.createElement('li');
  el.className = "box_reply row";
  el.innerHTML =
    '<div class=\"col-md-1\">' +
    '<div class=\"avatar_comment\">' +
    '<img src=\"https://static.xx.fbcdn.net/rsrc.php/v1/yi/r/odA9sNLrE86.jpg\" alt=\"avatar\"/>' +
    '</div>' +
    '</div>' +
    '<div class=\"result_comment col-md-11\">' +
    '<h4 class=\"tools_comment\">Anonimous <span aria-hidden=\"true\"> · </span><span>1m</span></h4>' +
    '<p>' + comment_replay + '</p>' +
    '<div class=\"tools_comment\">' +
    '<a class=\"replay\" href=\"#\">Reply</a>' +
    '</div>' +
    '<ul class="child_replay"></ul>' +
    '</div>';
  $current.closest('li').find('.child_replay').prepend(el);
  $('.comment_replay').val('');
  cancel_reply();
}

function cancel_reply() {
  $('.reply_comment').remove();
}

function startMcq(check) {
  // disappear1.innerHTML = "";
  $.ajax({
    url:"/mcq_json",

    data:{
    lesson_id:check
    },
    dataType:'json',
    success:function(res){
  document.querySelector('.disappear1'+check).style.display = "none";
  document.querySelector('.appear1'+check).style.display = "block";
  var questions=res.quizes
   
    
  


  var currentQuestion = 0;
  var viewingAns = 0;
  var correctAnswers = 0;
  var quizOver = false;
  var iSelectedAnswer = [];
  var mcqTime = res.lesson.quiz_time;
  var c = mcqTime;
  var t;
  $(document).ready(function () {
    // Display the first question
    displayCurrentQuestion();
    $(this).find(".quizMessage").hide();
    $(this).find(".preButton").attr('disabled', 'disabled');

    timedCount();

    $(this).find(".preButton").on("click", function () {

      if (!quizOver) {
        if (currentQuestion == 0) { return false; }

        if (currentQuestion == 1) {
          $(".preButton").attr('disabled', 'disabled');
        }

        currentQuestion--; // Since we have already displayed the first question on DOM ready
        if (currentQuestion < questions.length) {
          displayCurrentQuestion();

        }
      } else {
        if (viewingAns == 3) { return false; }
        currentQuestion = 0; viewingAns = 3;
        viewResults();
      }
    });


    // On clicking next, display the next question
    $(this).find(".nextButton").on("click", function () {
      if (!quizOver) {

        var val = $("input[type='radio']:checked").val();

        if (val == undefined) {
          $(document).find(".quizMessage").text("Please select an answer");
          $(document).find(".quizMessage").show();
        }
        else {
          // TODO: Remove any message -> not sure if this is efficient to call this each time....
          $(document).find(".quizMessage").hide();
          if (val == questions[currentQuestion].correct_answer) {
            correctAnswers++;
          }
          iSelectedAnswer[currentQuestion] = val;

          currentQuestion++; // Since we have already displayed the first question on DOM ready
          if (currentQuestion >= 1) {
            $('.preButton').prop("disabled", false);
          }
          if (currentQuestion < questions.length) {
            displayCurrentQuestion();

          }
          else {
            displayScore();
            $('#iTimeShow'+check).html('Quiz Time Completed!');
            // $('#timer').html("You scored: " + correctAnswers + " out of: " + questions.length);
            c = 185;
            $(document).find(".preButton").text("Previous Question").attr('disabled', 'disabled');
            $(document).find(".nextButton").text("Submit");
            quizOver = true;
            return false;
          }
        }

      }
      else {

        if (viewingAns == 3) {
          return false;
        }
        currentQuestion = 0;
        viewingAns = 3;
        viewResults();

      }
    });
  });



  function timedCount() {
    if (c == 185) {
      return false;
    }

    var hours = parseInt(c / 3600) % 24;
    var minutes = parseInt(c / 60) % 60;
    var seconds = c % 60;
    var result = (hours < 10 ? "0" + hours : hours) + ":" + (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds < 10 ? "0" + seconds : seconds);
    $('#timer'+check).html(result);

    if (c == 0) {
      displayScore();
      $('#iTimeShow'+check).html('Quiz Time Completed!');
      // $('#timer').html("You scored: " + correctAnswers + " out of: " + questions.length);
      c = 185;
      $(document).find(".preButton").text("Previous Question").attr('disabled', 'disabled');
      $(document).find(".nextButton").text("Submit");
      quizOver = true;
      return false;

    }


    c = c - 1;
    t = setTimeout(function () {
      timedCount()
    }, 1000);
  }


  // This displays the current question AND the choices
  function displayCurrentQuestion() {

    if (c == 185) {
      c = mcqTime;
      timedCount();
    }
    var question = questions[currentQuestion].question;
    var questionClass = $(document).find(".quizJScontainer > .question");
    var choiceList = $(document).find(".quizJScontainer > .choiceList");
    var numChoices = questions[currentQuestion].option.length;
    // Set the questionClass text to the current question
    $(questionClass).text(question);
    // Remove all current <li> elements (if any)
    $(choiceList).find("li").remove();
    var choice;


    for (i = 0; i < numChoices; i++) {
      choice = questions[currentQuestion].option[i];

      if (iSelectedAnswer[currentQuestion] == i) {
        $('<li><input type="radio" class="radio-inline" checked="checked"  value=' + i + ' name="dynradio" />' + ' ' + choice + '</li>').appendTo(choiceList);
      } else {
        $('<li><input type="radio" class="radio-inline" value=' + i + ' name="dynradio" />' + ' ' + choice + '</li>').appendTo(choiceList);
      }
    }
  }

  function displayScore() {
    $(document).find(".quizJScontainer > .result").text("You scored: " + correctAnswers + " out of: " + questions.length);
    $(document).find(".quizJScontainer > .result").show();
    // Answer for backend
    // console.log(correctAnswers);
  }

  // function hideScore() {
  //   $(document).find(".result").hide();
  // }

  // Result option redirect another page
  function viewResults() {
    document.getElementById('correctAnswer'+check).innerText = correctAnswers;
    document.querySelector('.disappear2'+check).style.display = "block";
    document.querySelector('.appear1'+check).style.display = "none";
    $.ajax({
      url:"/submit_quiz",
  
      data:{
      lesson_id:check,
      mark:correctAnswers
      },
      dataType:'json',
      success:function(res){

      }
    });

    
  }

}
  });
}




//Teacher Profile help And Support FAQ

function tchBtnCheck(check) {
  if (check == "tchFaqAccordian") {
    document.querySelector('.searchTopic-footer').style.display = "none";
    document.querySelector('.tchFaqAccordian').style.display = "block";
  }
  else if (check == "searchTopic-footer") {
    document.querySelector('.searchTopic-footer').style.display = "block";
    document.querySelector('.tchFaqAccordian').style.display = "none";
  }
  //Cart Coupon
  else if (check == "cartInput") {
    document.querySelector('.cartCoupon').style.display = "none";
    document.querySelector('.cartInput').style.display = "block";
  }
}



//using selectors inside the element
const mockTestViewRslts = document.querySelectorAll(".mockTestViewRslt");
     
mockTestViewRslts.forEach(function (mockTestViewRslt) {
    const btn = mockTestViewRslt.querySelector(".mockTestViewRslt-btn");
    // console.log(btn);

    btn.addEventListener("click", function () {
        // console.log(mockTestViewRslt);

        mockTestViewRslts.forEach(function (item) {
            if (item !== mockTestViewRslt) {
                item.classList.remove("mocktestShow-text");
            }
        });

        mockTestViewRslt.classList.toggle("mocktestShow-text");
    });
});


        

           
           

              
   
    
        
      