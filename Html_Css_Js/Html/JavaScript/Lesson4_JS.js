/* 
************
While loops, for loops, No guessing game, functions, variable scope, temp conversion program, arrays, spread operator
***********
*/

// While loop - repeats some code WHILE some condition is true

// // let username = "";
// let username;

// // while (username === "" || username === null){
// //     username = window.prompt("Enter your name: ");
// // }

// // There's another way to variation of it using do
// do{
//     username = window.prompt("Enter your username: ")
// } while (username === "" || username === null)

// console.log(`Hello, ${username}`);

// let logged_in = false
// let username;
// let password;

// while (!logged_in){
//     username = window.prompt("Enter your username: ")
//     password = window.prompt("Enter your password: ")

//     if (username === "myusername" && password === "mypassword"){
//         logged_in = true;
//         console.log(`You are logged in`);
//     }
//     else{
//         console.log(`Invalid credentials! Please try again`)
//     }
// }

// It does the same thing but with one exception
// // Do enters the while loop at least once
// do{
//     username = window.prompt("Enter your username: ")
//     password = window.prompt("Enter your password: ")

//     if (username === "myusername" && password === "mypassword"){
//         logged_in = true;
//         console.log(`You are logged in`);
//     }
//     else{
//         console.log(`Invalid credentials! Please try again`)
//     }
// }while (!logged_in)




/* For loops *********************
// for loop = repeat a code some LIMITED number of times
*/

// for (let i = 10; i > 0; i--) {
//     console.log(i)
// }

// console.log(`Happy New Year🎊`)

// for(let i = 1; i <= 20; i++){
    
//     if(i == 13){
//         continue;
//     }
//     else{
//         console.log(i);
//     }
// }





/* Number Guessing Game *********************
*/
// const min_num = 1;
// const max_num = 100;
// const answer = Math.floor(Math.random() * (max_num - min_num + 1)) + min_num;

// let attempts = 0;
// let guess;
// let is_running = true;

// while(is_running){
//     guess = window.prompt(`Guess a number between (${min_num} - ${max_num})`);
//     guess = Number(guess);

//     if(isNaN(guess)){
//         window.alert(`Please enter a valid number`)
//     }
//     else if(guess < min_num || guess > max_num){
//         window.alert(`Please enter a valid number`)
//     }
//     else{
//         attempts ++
//         if(guess < answer){
//             window.alert(`Guess too low try again!`)
//         }
//         else if(guess > answer){
//             window.alert(`Guess too high try again!`)
//         }
//         else{
//             window.alert(`Excellent work, the answer was: ${answer}. It took you ${attempts} attempts.`)
//             is_running = false
//         }
//     }   
// }

// console.log(answer)






/* Functions *********************
// function = a set of reusable code.
//            declare code once, use it whenever you want.
//            call the function to execute that code.
*/

// function happy_birthday(username, age){
//     console.log(`Happy Birthday to you!`)
//     console.log(`Miam, miam, miam, miam`)
//     console.log(`Happy Birthday dear ${username}!`)
//     console.log(`Happy Birthday to you!!!`)
//     console.log(`You are ${age} years old now!`)
// }

// happy_birthday("Spider-man", 18);

// function add(x, y){
//     // let result = x + y;
//     // return result;
//     return x + y;
// }

// function subtract(x, y){
//     // let result = x - y;
//     // return result;
//     return x - y;
// }

// let answer = subtract(9, 4)

// console.log(answer)

// function is_even(number){
//     // if(number % 2 === 0){
//     //     return true;
//     // }
//     // else{
//     //     return false
//     // }
//     return number % 2 === 0 ? true : false;
// }

// console.log(is_even(11))

// function is_valid_email(email){
//     // if(email.includes("@")){
//     //     return true
//     // }
//     // else {
//     //     return false
//     // }

//     return email.includes("@") ? true : false;
// }

// console.log(is_valid_email("Miamfake.com"))
// console.log(is_valid_email("Miamfake@.com"))
// console.log(is_valid_email("miamnotfake.com"))






/* variable scope *********************
// variable scope = where a variable scope is recognized and accessible (local vs global)
*/

// function func_1(){
//     x = 1
//     console.log(x);
// }

// // we can have two variables with the same name as long as they have different scopes
// function func_2(){
//     // local scope variable
//     x = 2
//     console.log(x);
// }

// functions can't see inside other functions
// if two variables have different scopes but same name, local takes priority






/* Temp conversion Program *********************
*************************
*/
const text_box = document.getElementById("text_box");
const to_fahrenheit = document.getElementById("to_fahrenheit");
const to_celsius = document.getElementById("to_celsius");
const result = document.getElementById("result");

let temp;

function convert(){
    if(to_fahrenheit.checked){
        temp = Number(text_box.value);
        temp = temp * 9 / 5 + 32;
        result.textContent = temp.toFixed(1) + `°F`;
    }
    else if(to_celsius.checked){
        temp = Number(text_box.value);
        temp = (temp - 32) * (5/9);
        result.textContent = temp.toFixed(1) + `°C`;
    }
    else{
        result.textContent = `Select a unit`;
    }
}
