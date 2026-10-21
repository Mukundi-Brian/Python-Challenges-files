// Simple Area of a circle calculator

/* 
****************************
Exercise 1: Calculate area of a circle
***********
*/

// const Pi = 3.14159;
// const my_button = document.getElementById("submit_btn");
// const my_header = document.getElementById("my_h1");

// let radius;
// let area_of_circle;

// // Calculation
// my_button.onclick = function () {
//     radius = document.getElementById("my_radius").value;
//     area_of_circle = Pi * radius ** 2
//     my_header.textContent = `The area of the circle is: ${area_of_circle} cm^2`
// }


/* 
****************************
Exercise 2: Generate random latitude (-90, 90) and longitude (-180, 180)
***********
*/

// const my_h1 = document.getElementById("my_h1");
// const my_results = document.getElementById("my_results");
// const submit_btn = document.getElementById("submit_btn");

// let generated_longitude;
// let generated_latitude;

// let max_longitude = 90;
// let min_longitude = -90;

// let max_latitude = 180;
// let min_latitude = -180;

// // Function to calculate after the button is pressed
// submit_btn.onclick = function () {
//     generated_latitude = Math.floor(Math.random() * (max_latitude - min_latitude) + min_latitude);
//     generated_longitude = Math.floor(Math.random() * (max_longitude - min_longitude) + min_longitude);

//     my_results.textContent = `Longitude: ${generated_longitude}, Latitude: ${generated_latitude}`;
// }


/* 
****************************
Exercise 3: interactive web-form validator
***********
*/

// const my_button = document.getElementById("submit_btn");
// const user_level = document.getElementById("user_level");
// const my_display = document.getElementById("my_display")

// let user_clearance;

// my_button.onclick = function () {
//     user_clearance = user_level.value;

//     if (user_clearance > 100 || user_clearance < 0) {
//          my_display.textContent = `Invalid input! Clearance level can't be less than 0 or greater than 100`;
//     }
//     else if (user_clearance > 80) {
//         my_display.textContent = `Access Granted: Senior Geomatics Engineer`;
//     }
//     else if (user_clearance < 80 && user_clearance > 40) {
//         my_display.textContent = `Access Granted: Junior Geomatics Engineer`;
//     }
//     else if (user_clearance < 40 && user_clearance >= 0) {
//         my_display.textContent = `Access Granted: Intern`;
//     }
//     else {
//         my_display.textContent = `Invalid input! Try again`;
//     }
// }


/* 
****************************
Exercise 4: The Coordinate Distance Calculator
***********
*/

const value1 = document.getElementById("x1");
const value2 = document.getElementById("y1");
const value3 = document.getElementById("x2");
const value4 = document.getElementById("y2");
const submit_btn = document.getElementById("submit_btn");
const my_display = document.getElementById("my_display");

let euclidean_distance_result;

submit_btn.onclick = function () {

    // Always pay attention to user input and type conversion
    x1 = parseFloat(value1.value);
    y1 = parseFloat(value2.value);
    x2 = parseFloat(value3.value);
    y2 = parseFloat(value4.value);

    euclidean_distance_result = (Math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2 )));
    euclidean_distance_result = Math.round(euclidean_distance_result)
    my_display.textContent = `The euclidean distance is: ${euclidean_distance_result} cm`;

}
