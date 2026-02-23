// // const data= [5];
// // const [x,y=10] = data;
// // console.log(x)
// // console.log(y)
// const data = {x: 5, y: 15}
// const {x , y =10 }  = data

// console.log(x) // 5
// console.log(y) // 15

// person = {
//     name: "vanshi",
//     age : 30,
//     occupation : "Software Engineer",
// };

// const { name = "Anonymous", age = 30, occupation } = person;
// console.log(person);
const m=[1,[2,3]];
const [a,[b,c]]=m;
console.log(a);
console.log(b);
console.log(c);
const data =[5];
const [x=12,y="hello"]=data;
console.log(x);
console.log(y);

let person = {
    name: "vanshi",
    //age: 12,
    salary: 50000
};
console.log(person);

// Destructuring
//let { name, age=10, salary } = person;

//console.log("name:"+name);
//console.log("age:"+age);w
//console.log("salary:"+salary);
let { name, salary } = person;

console.log("name:"+name);
//console.log("age:"+age);
console.log("salary:"+salary);



