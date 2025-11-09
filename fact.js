function fact(num){
    if(num==0)
        return 1;
    else 
        return num*fact(num-1);
}
let Factorial=fact(10);
console.log(Factorial);
