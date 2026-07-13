let car={
    brand:"Aston Martin",
    model:"1998 Aston Martin V8 Vantage (V550)",
    color:"Blue",
    top_speed:"83m/s",
    engine_info:{
        cylinder_number:8,
    },
    manufacturer:{
        year:null,
        country:"England",
        aka:"Aston Martin V8 Vantage"
    },
    alert_info:function(){
        window.alert(`Car:${car.name}\n
                ${car.model}\n
                ${car.fun_fact}\n`)
    },
    fun_fact:"idk",
}
console.log(typeof car);
console.table(car);
function PrintObjectValues(obj){
    for(const key of Object.keys(obj)){
        console.log(`${key}: contains data of the type ${typeof obj[key]}`);
        //for some reason null is an object????
        if(obj[key]!=null &&typeof obj[key]=="object"){
            PrintObjectValues(obj[key]);
        }
        else{
            console.log(`${key}:${obj[key]}`);
        }
    }
}
PrintObjectValues(car);