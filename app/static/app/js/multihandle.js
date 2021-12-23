window.onload = function(){
  slideOne1();
  slideTwo1();
  slideOne();
  slideTwo();
}

//MultiHandle range Desktop

let sliderOne1 = document.getElementById("sliderb-1");
let sliderTwo1 = document.getElementById("sliderb-2");
let displayValOne1 = document.getElementById("multiHandleRangeb1");
let displayValTwo1 = document.getElementById("multiHandleRangeb2");
let minGap1 = 0;
let sliderTrack1 = document.querySelector(".RangeSliderb-track");
let sliderMaxValue1 = document.getElementById("sliderb-1").max;

function slideOne1(){
  if(parseInt(sliderTwo1.value) - parseInt(sliderOne1.value) <= minGap1){
      sliderOne1.value = parseInt(sliderTwo1.value) - minGap1;
  }
  displayValOne1.textContent = sliderOne1.value;
  fillColor1();
}
function slideTwo1(){
  if(parseInt(sliderTwo1.value) - parseInt(sliderOne1.value) <= minGap1){
      sliderTwo1.value = parseInt(sliderOne1.value) + minGap1;
  }
  displayValTwo1.textContent = sliderTwo1.value;
  fillColor1();
}
function fillColor1(){
  percent1 = (sliderOne1.value / sliderMaxValue1) * 100;
  percent2 = (sliderTwo1.value / sliderMaxValue1) * 100;
  sliderTrack1.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #380e86 ${percent1}% , #380e86 ${percent2}%, #dadae5 ${percent2}%)`;
}

//MultiHandle range mobile

let sliderOne = document.getElementById("slider-1");
let sliderTwo = document.getElementById("slider-2");
let displayValOne = document.getElementById("multiHandleRange1");
let displayValTwo = document.getElementById("multiHandleRange2");
let minGap = 0;
let sliderTrack = document.querySelector(".RangeSlider-track");
let sliderMaxValue = document.getElementById("slider-1").max;

function slideOne(){
  if(parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap){
      sliderOne.value = parseInt(sliderTwo.value) - minGap;
  }
  displayValOne.textContent = sliderOne.value;
  fillColor();
}
function slideTwo(){
  if(parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap){
      sliderTwo.value = parseInt(sliderOne.value) + minGap;
  }
  displayValTwo.textContent = sliderTwo.value;
  fillColor();
}
function fillColor(){
  percent1 = (sliderOne.value / sliderMaxValue) * 100;
  percent2 = (sliderTwo.value / sliderMaxValue) * 100;
  sliderTrack.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #380e86 ${percent1}% , #380e86 ${percent2}%, #dadae5 ${percent2}%)`;
}