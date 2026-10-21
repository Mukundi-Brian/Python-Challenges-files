// IF STATEMENTS, .checked, ternary operator, switches, String methods, String slicing,
// Method chaining, logical operators, strict equality

/* 
**************************************************
    IF STATEMENTS = if a condition is true, execute some code
                   if not, do something else
*************
*/

// let age = 10;

// if (age >= 18) {
//     console.log(`You are an adult!`)
// }
// else {
//     console.log(`Go home Kid!`)
// }

// let time = 14;

// if (time < 12) {
//     console.log(`Good Morning!`)
// }
// else{
//     console.log(`Goof Afternoon!`)
// }

// let is_student = true

// if (is_student) {
//     console.log(`You are a Student`)
// }
// else {
//     console.log(`You are not a Student`)
// }

// let age = 0;
// let has_license = false;

// if (age >= 16) {
//     console.log(`You are old enough to drive!`);

//     if (has_license) {
//         console.log(`You have your License`);
//     }
//     else {
//         console.log(`You do not have your License yet!`);
//     }
// }
// else {
//     console.log(`You must be 16 plus to have a license`);
// }

// Order of clauses matter
// if (age >= 100) {
//     console.log(`You are too OLD to enter this site!`)
// }
// else if (age == 0) {
//     console.log(`You were just born, so you can't enter this site!`)
// }
// else if (age >= 18) {
//     console.log(`You are old enough to enter this site!`)
// }
// else if (age < 0) {
//     console.log(`You can't have negative age, Alien!`)
// }

// else {
//     console.log(`You must be 18 plus to enter this site!`)
// }

/* Exercise = Show different messages based on what the user enters */

// const my_age_text = document.getElementById("my_age_text");
// const my_submit = document.getElementById("my_submit");
// const show_result = document.getElementById("show_result");
// let age;

// my_submit.onclick = function () {

//     age = my_age_text.value;
//     age = Number(age);

//     if (age >= 100) {
//         show_result.textContent = `You are too OLD to enter this site!`
//     }
//     else if (age == 0) {
//         show_result.textContent = `You were just born, so you can't enter this site!`
//     }
//     else if (age >= 18) {
//         show_result.textContent = `You are old enough to enter this site!`
//     }
//     else if (age < 0) {
//         show_result.textContent = `You can't have negative age, Alien!`
//     }
//     else {
//         show_result.textContent = `You must be 18 plus to enter this site!`
//     }
// }



/* 
**************************************************
    .checked = property that determines the checked state of an HTML checkbox or radio button element
*************
*/

// const my_checkbox = document.getElementById("my_checkbox");
// const visa_btn = document.getElementById("visa_btn");
// const master_card_btn = document.getElementById("master_card_btn");
// const paypal_btn = document.getElementById("paypal_btn");
// const submit_btn = document.getElementById("submit_btn");
// const sub_result = document.getElementById("sub_result");
// const pay_result = document.getElementById("pay_result");

// submit_btn.onclick = function () {
    
//     if (my_checkbox.checked) {
//         sub_result.textContent = `You are subscribed!`;
//     }
//     else {
//         sub_result.textContent = `You are NOT subscribed!`;
//     }

//     if (visa_btn.checked) {
//         pay_result.textContent = `You are paying with Visa`;
//     }
//     else if (master_card_btn.checked) {
//         pay_result.textContent = `You are paying with MasterCard`;
//     }
//     else if (paypal_btn.checked) {
//         pay_result.textContent = `You are paying with PayPal`;
//     }
//     else {
//         pay_result.textContent = `You must select a payment method`;
//     }
    
// }



/* 
**************************************************
    ternary operator = a shortcut to if{} and else {} statements
                     it helps to assign a variable based on a condition
                     condition ? codeIfTrue : codeIfFalse;
*************
*/

// let age = 21;

// let message = age >= 18 ? `You are an adult!` : `You are a minor!`;

// console.log(message)

// let time = 9;

// let greeting = time < 12 ? `Good Morning!` : `Good Afternoon`

// console.log(greeting);

// let is_student = true;
// let message = is_student ? `You are a Student` : `You are not a Student`;
// console.log(message)

// let purchase_amount = 125;
// let discount = purchase_amount >= 100 ? 10 : 0;
// console.log(`Your total is $${purchase_amount - purchase_amount * (discount/100)}`)



/*
**************************************************
    SWITCH = can be an efficient replacement to many else if statements
*************
*/

// let day = "pizza";

// switch(day) {
//     case 1:
//         console.log(`It is Sunday`)
//         break
//     case 2:
//         console.log(`It is Monday`)
//         break
//     case 3:
//         console.log(`It is Tuesday`)
//         break
//     case 4:
//         console.log(`It is Wednesday`)
//         break
//     case 5:
//         console.log(`It is Thursday`)
//         break
//     case 6:
//         console.log(`It is Friday`)
//         break
//     case 7:
//         console.log(`It is Saturday`)
//         break 
//     default:
//         console.log(`${day} is not a day!`);
// }

// let test_score = 95;
// let letter_grade;

// switch(true) {
//     case test_score >= 90:
//         letter_grade = "A";
//         break;
//     case test_score >= 80:
//         letter_grade = "B";
//         break;
//     case test_score >= 70:
//         letter_grade = "C";
//         break;
//     case test_score >= 60:
//         letter_grade = "D";
//         break;
//     default:
//         letter_grade = "F";
// }

// console.log(letter_grade)

/* 
**************************************************
    String Methods = allow you to manipulate and work with text (strings)
*************
*/

// let username = " Goat Panda ";

// console.log(username.charAt(0));
// console.log(username.indexOf("a"))
// console.log(username.lastIndexOf("a")
// console.log(username.length);
// console.log(username.trim());
// console.log(username.toUpperCase());
// console.log(username.toLowerCase());
// console.log(username.repeat(3));
// let result = username.startsWith(" ")
// let result = username.endsWith(" ")
// let result = username.includes(" ")

// console.log(result);
// if(result){
//     console.log(`Username cannot begin with space ' '`)
// }
// else {
//     console.log(username)
// }

// let phone_number = "123-456-7890";

// phone_number = phone_number.replaceAll("-", " Panda ");
// phone_number = phone_number.padStart(25, "0");
// phone_number = phone_number.padEnd(25, 0)
// console.log(phone_number);


/* 
**************************************************
    String slicing = creating a substring from a portion of another string
                     string.slice(start, end)
                     it doesn't alter the original
*************
*/

// const full_name = "Goat Panda"

// // let first_name = full_name.slice(0, 4);
// // let last_name = full_name.slice(5);
// // let first_char = full_name.slice(0, 1);
// // let last_char = full_name.slice(-1);

// let first_name = full_name.slice(0, full_name.indexOf(" "));
// let last_name = full_name.slice(full_name.indexOf(" ") + 1);

// console.log(first_name)
// console.log(last_name)
// // console.log(first_char)
// // console.log(last_char)

// const email = "danielbryan62f@gmail.com"

// let username = email.slice(0, email.indexOf("@"));
// let extension = email.slice(email.indexOf("@") + 1);

// console.log(username);
// console.log(extension)




/* 
**************************************************
    Method Chaining = calling one method after another in one continuous line of code.
*************
*/

// No method chaining
// let username = window.prompt(`Enter your username: `);

// username = username.trim();

// let letter = username.charAt(0);
// letter = letter.toUpperCase();

// let extra_chars = username.slice(1);
// extra_chars = extra_chars.toLowerCase();

// username = letter + extra_chars;

// console.log(username);


// Method chaining
// let username = window.prompt(`Enter your username: `);

// username = username.trim().charAt(0).toUpperCase() + username.trim().slice(1).toLowerCase()

// console.log(username)




/* 
**************************************************
    logical operators = used to combine or manipulate boolean values (true or false)

    AND = &&
    OR = ||
    NOT = !
*************
*/

// const temp = 200000;

// if(temp > 0 && temp <= 30) {
//     console.log(`The weather is good!`)
// }

// else {
//     console.log(`The weather is bad!!!`)
// }

// const temp = 200000;

// if(temp <= 0 && temp > 30) {
//     console.log(`The weather is good!`)
// }

// else {
//     console.log(`The weather is bad!!!`)
// }

// const is_sunny = true;

// if (!is_sunny) {
//     console.log(`It is sunny!`)
// }
// else {
//     console.log(`It is Cloudy`)
// }




/* 
**************************************************
    Strict Equality operators

    = assignment operator
    == comparison operator (compare if values are equal)
    === strict equality operator (compare if values & datatype are equal)
    != inequality operator
    !== strict inequality operator

*************
*/

// const PI = 3.14;

// if (PI === "3.14") {
//     console.log(`That is PI`)
// }
// else {
//     console.log(`That is not PI`)
// }

// if (PI !== "3.14") {
//     console.log(`This is not PI`)
// }
// else {
//     console.log(`That is PI`)
// }

