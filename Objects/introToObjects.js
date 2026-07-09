let car={
    brand:"Aston Martin",
    model:"1998 Aston Martin V8 Vantage (V550)",
    color:"Blue",
    top_speed:"20m/s",
    engine_info:{
        cylinder_number:8,
        number:""
    },
    manufacturer:{
        year:1998,
        country:"",
        aka:""
    },
    4.0:"displacement in litres",
    alert_info:function(){
        alert(`Car:${car.name}\n
                ${car.model}\n
                ${car.fun_fact}\n
                ${car[4]}`)
    },
    fun_fact:"idk",
}
console.log(typeof car);
console.table(car);
car.alert_info();