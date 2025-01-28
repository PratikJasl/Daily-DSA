// function CreateCar(brand, model, color){
//     this.brand = brand
//     this.model = model
//     this.color = color
// }
// //We added a new method inside the prototype of constructor function.
// CreateCar.prototype.getCarInfo = function(){
//     console.log(`${this.brand}, ${this.model}, ${this.color}`);
// }
// //All objects created using the constructor function will have this method.
// const Car1 = new CreateCar('Tata', 'Curve', 'Orange');
// Car1.getCarInfo();

// class Car{
//     #userCount; // Private property

//     constructor(brand, model, color){
//         this.brand = brand;
//         this.model = model;
//         this.color = color;
//         this.#userCount = 20000; // Setting the private property inside the constructor
//     }
//     getModel(){
//         console.log(`Car Model: ${this.model}`)
//     }
//     // Public method to access the private property
//     getUserCount(){
//         console.log(`Car User Count: ${this.#userCount}`);
//     }
// }

// let Car1 = new Car('Tata', 'Curve', 'Orange');
// Car1.getUserCount();


// class Car{
//     static userCount; // Statice property

//     constructor(brand, model, color){
//         this.brand = brand;
//         this.model = model;
//         this.color = color;
//         this.userCount = 20000; // Setting the static property inside the constructor
//     }
//     getDetails(){
//         console.log(`Car Model: ${this.model}, Car Users: ${this.userCount}`);
//     }
// }

// let Car1 = new Car('Tata', 'Curve', 'Orange');
// Car1.getDetails();


//Parent Class
// class Car{
//     constructor(brand, model, color){
//         this.brand = brand;
//         this.model = model;
//         this.color = color;
//     }
//     get CarDetails(){ //getter function
//         console.log(`${this.brand}, ${this.model}, ${this.color}`);
//     }
    
// }
// //Sub-class child Class
// class Bike extends Car{
//     constructor(brand, model, color){
//         super(brand, model, color);
//     }
//     get GetBikeDetails(){
//         console.log(`${this.brand}, ${this.model}, ${this.color}`);
//     }
// }
// let Car1 = new Car();
// const bike1 = new Bike('Honda', 'sp125', 'darkblue');
// bike1.GetBikeDetails;
// Car1.CarDetails;


const unique = new Set([1,2,3]);
const iterator = unique.values(); //both keys and values give same output.
console.log(iterator); // {1,2,3}