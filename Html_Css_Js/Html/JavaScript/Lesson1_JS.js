// Basics, Variables, Arithmetic Operators, User Input, type conversions, Consts

// console.log(`Hello World`)
// console.log(`I like Pizza 🍕`)

// window.alert(`This is an alert`);
// window.alert(`I like Pizza 🍕`);
/*
This is a multi-line
comment 
*/

// document.getElementById("myH1").textContent = `Hello`;
// document.getElementById("myP1").textContent = `I love pizza 🍕`

/* Variable = A container that stores a value
            - Behaves as if it were the value it contains
1. Declaration - let x;
2. Assignment - x = 100;
*/
// Numbers
// let age = 21;
// let price = 11.99;
// let gpa = 4.1;

// console.log(typeof price);
// console.log(`You are ${age} years old`);
// console.log(`You have a gpa of ${gpa}`);
// console.log(`The price is $${price}`);

// // Strings
// let first_name = "Ferda";
// let favorite_food = "Pizza";
// let email = "FerdaV@gmail.com"

// console.log(typeof first_name);
// console.log(`Your first name is ${first_name}`);
// console.log(`Your like ${favorite_food}`);
// console.log(`Your email is ${email}`);

// Booleans
// let online = true;
// let for_sale = false;
// let is_student = true;

// console.log(`Luri is online: ${online}`);
// console.log(`Is this car for sale: ${for_sale}`)
// console.log(`Enrolled: ${is_student}`)

// let full_name = "Ferda Valdrova";
// let age = "21";
// let is_student = true;

// document.getElementById("myP1").textContent = `Your name is ${full_name}`;
// document.getElementById("myP2").textContent = `Your are ${age} years old`;
// document.getElementById("myP3").textContent = `Are you still in school: ${is_student}`;

// Arithmetic Operators
/* Arithmetic Operators = Operands (values, variables, etc)
                        - operators include but not limited to (+ - * /)
                        - eg. 11 = x + 5;
*/

// let students = 30;
// students += 1;
// students -= 1;
// students *= 2;
// students /= 2;
// students **= 2;
// students %= 2 *;
// let extra_students = students %= 2;
// students ++;
// students --;
// console.log(students);

/*  Operator Precedence
    1. Parenthesis ()
    2. Exponents
    3. Multiplication, division and Modulo
    4. Addition and subtraction
*/

// let result = 1 + 2 * 3 + 4 ** 2;
// let result = 12 % 5 + 8 / 2;
// let result = 6 / 2 ** (5 + 2);

// console.log(result);

/*  User Input
    Easy way - window prompt
    Professional way - html textbox
*/

// let username;

// username = window.prompt(`What is your username?`);

// console.log(username);

// let username;
// document.getElementById("my_submit_btn").onclick = function() {
//     username = document.getElementById("my_text").value;
//     document.getElementById("myH1_2").textContent = `Welcome, ${username}`;
// }

// Type Conversion = Changes the datatype of a value to another
//                  (strings, numbers, booleans)

// let age = window.prompt(`What is your age?`);

// age = Number(age);
// age += 23;

// console.log(age, typeof age);

// let x = `Pizza`, y = `Pizza`, z = `Pizza`;

// x = Number(x)
// console.log(x, typeof x)
// y = String(y)

// console.log(y, typeof y)
// z = Boolean(z)

// console.log(z, typeof z)

// Constants
// Const = a variable that can't be changed

// let pi = 3.14159;
// let radius;
// let circumference;

const Pi = 3.14159;
let radius;
let circumference;

// radius = window.prompt(`Enter the radius of the circle`)
// radius = Number(radius)

// circumference = 2 * pi * radius

// console.log(circumference)


// radius = Number(radius);

// document.getElementById("my_submit_btn_2").onclick = function () {
//     radius = document.getElementById("my_radius").value;
//     circumference = 2 * Pi * radius;
//     console.log(`The circumference is ${circumference}`);
//     document.getElementById("my_circumference").textContent = `The Circumference is ${circumference} cm`;
// }
