//Questions on patterns.

//Question:1

// for (let i = 0; i < 4; i++){
//     for(let j = 0; j < 4; j++){
//         console.log("*");
//     }
//     console.log("\n");
// }console.log(string);

let n = 5
let s = ""
for (let i = 0; i < n; i++){
    for(let j = 0; j <= i; j++){
        s += " "
    }
    for(let j=0; j < (n*2-i+1); j++){
        s += "*"
    }
    for(let j = 0; j <= i; j++){
        s += " "
    }
    s += '/n'
}
console.log(s);