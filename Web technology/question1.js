// function sumLet(a, b) {
//     let sum = a+b;
//     console.log(sum);
// }
// sumLet(5, 10);

// const result = a*b;
// return result;

// const a = n*n;
// return a
//  or 
 //  return n*n;

// let[a,b]= arr;
// return [a,b];

// let {name,age} = obj;
// return {name,age};

// let a = 10
// return a+b;
 
total = 0;
for(let n of nums){
    total +=n;
}
return total;

return nums.reduce((a,b)=> a+b);

return [...arr1,...arr2];


return arr.map(n => n*2);

return arr.filter(n => n>20);

return Math.max(...arr);

let age} = Object;


return new Promise((resolve, reject)=>{
    setTimeout(()=> {
        resolve("message");
    }, 1000);
} )

return Promise.then( result=> result);

return Promise.reject("error").catch(error => error);