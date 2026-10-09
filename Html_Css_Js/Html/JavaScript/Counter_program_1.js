// Counter Program

// let counter;
// counter = document.getElementById("counter_label").textContent = 0;
// counter = Number(counter);

// // Decrease btn function
// document.getElementById("decrease_btn").onclick = function () {
//     counter --
//     counter = document.getElementById("counter_label").textContent = counter;
//     console.log(counter, typeof counter)
// }
// // Reset btn function
// document.getElementById("reset_btn").onclick = function () {
//     counter = 0
//     counter = document.getElementById("counter_label").textContent = counter;
//     console.log(counter, typeof counter)
// }
// // Increase btn function
// document.getElementById("increase_btn").onclick = function () {
//     counter ++
//     counter = document.getElementById("counter_label").textContent = counter;
//     console.log(counter, typeof counter)
// }


const decrease_btn = document.getElementById("decrease_btn");
const reset_btn = document.getElementById("reset_btn");
const increase_btn = document.getElementById("increase_btn");
const counter_label = document.getElementById("counter_label")

let count = 0;

// Increase button function
increase_btn.onclick = function () {
    count ++;
    counter_label.textContent = count;
}
// Decrease button function
decrease_btn.onclick = function () {
    count --;
    counter_label.textContent = count;
}
// reset button function
reset_btn.onclick = function () {
    count = 0;
    counter_label.textContent = count;
}
