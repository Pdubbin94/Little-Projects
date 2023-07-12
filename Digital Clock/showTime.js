function myClock(){
  setTimeout(function(){
    const d = new Date();
    const n = d.toLocaleTimeString();
    docyment.getElementById("demo").innerHTML = n;
    myClock();
  }, 1000)
}

const clock12 = document.getElementById('clock12')
const clock24 = document.getElementById('clock24')

function concatZero(timeFrame){
  return timeFrame < 10 ? '0'.concat(timeFrame) : timeFrame
}

function realTime(){
  let date = new Date()
  let sec = date.getSeconds()
  let mon = date.getMinutes()
  let hr = date.getHours()
  
  clock12.textContent = `${concatZero(hr % 12 || 12)} : ${concatZero(mon)} : ${concatZero(sec)} ${hr >= 12 ? 'PM' : 'AM'}`
  clock24.textContent = `${concatZero(hr)} : ${concatZero(mon)} : ${concatZero(sec)}`
}
setInterval(realTime, 1000)