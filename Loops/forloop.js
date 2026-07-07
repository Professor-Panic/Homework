function MathTable(){
    number1=Number(prompt("Enter first Number:"))
    number2=Number(prompt("Enter Second Number:"))
    if(number1>1 && number2>1){
        for(let i=1;i<=number1;i++){
            for(let j=1;j<=number2;j++){
                console.log(`${i}x${j}=${i*j} `)
            }
        }
    }
    else{
        alert("Both Numbers must be greater than 1")
    }
}
MathTable()