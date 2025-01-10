function CreateCar(brand, model, color){
    this.brand = brand
    this.model = model
    this.color = color
}
//We added a new method inside the prototype of constructor function.
CreateCar.prototype.getCarInfo = function(){
    console.log(`${this.brand}, ${this.model}, ${this.color}`);
}
//All objects created using the constructor function will have this method.
const Car1 = new CreateCar('Tata', 'Curve', 'Orange');
Car1.getCarInfo();

