let arr = [2,3,1,2,3,6,9];

let s = new Set();
let twice = false;
while (!twice){
    arr.forEach( e =>{
        if (s.has(e)){
            console.log("already in "+e);
            twice = true;
        }
        else{
            console.log("new number "+e);
            s.add(e);
        }
    });
};
for (let item of s)
    console.log(item);

console.log(twice);