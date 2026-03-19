// console.log("Hello World");
// let marks = [90, 80, 70, 60];
// console.log(marks);

// Arrow function

// let greet = (name) => {
//     console.log("Hello, " + name + "!");
// }
// greet("vanshi");


// Template literals
 
//  let name = "vanshi";
// console.log(`Hello, ${name}! Welcome to JavaScript.`);


// var a = 10;
// a = 20;
// console.log(a);


// let x = 5;
// if(true){
//     let x= 20;
//     console.log(x);
// }

// console.log(x);
// const y = 10;
// y=20;
// console.log(y);

// question 3
// const square = (n) => n*n;
// console.log(square(5));

// literals

// name = "Vanshika"
// age = "19"
// console.log(`My name is ${name} and I am ${age} year old`);

// Array Destructuring

// Array = [10,20,30];
// let [a,b,c] = Array;
// console.log(a);
// console.log(b);
// console.log(c); 

// object distructuring

// let emp = {
//     id: 101,
//     role: "Developer",

// }
// let{id:empId, role:job} = emp;
// console.log(empId);
// console.log(job);

// Default values in destructuring

// let car = {
// brand: "Toyota",
// }
// let { brand:carBrand, model:carModel = "Unknown" } = car;
// console.log(carBrand);
// console.log(carModel);

// Spread operator

// function sum(...numbers){
//     let total = 0;

//     for(let n of numbers){
//         total += n;
//     }

//     console.log(total);
// }

// sum(1,2,3,4);

// question 4

// let a = [10,20];
// let b = [30,40];
// let c = [...a,...b];
// console.log(c);

// let promise = new Promise(function(resolve,reject){

//     let success = true;

//     if(success){
//         resolve("Task completed");
//     }
//     else{
//         reject("Task failed");
//     }

// });

// promise
// .then(function(result){
//     console.log(result);
// })
// .catch(function(error){
//     console.log(error);
// });

// let promise = new Promise(function(resolve,reject){
//     let number = 5;
//     if(number>0){
//         resolve("Number is positive");
//     }
//     else{
//         reject("Number is negative");
//     }

// });
// promise
// .then(function(result){
//     console.log(result);
// })
// .catch(function(error){
//     console.log(error);
// });
