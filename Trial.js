
//Checking the async nature of JS.
async function cookRiceAsync() {
  console.log("Putting rice on to cook... (will be ready in 3 seconds)");
  return 
    setTimeout(() => {
      resolve("Rice is cooked! From Promise after 3sec");
    }, 3000); 
  
}

async function serveMealAsync() {
  console.log("1. Chef: Starting to prepare meal...");
  console.log("2. Chef: While rice is cooking, I can clean the counter or pour drinks!");
  console.log("3. Chef: Waiting for rice to be ready...");
 
  const cookedRice = await cookRiceAsync();

  console.log("4. Chef: " + cookedRice);
  console.log("5. Chef: Meal is ready!");
}

console.log("A. Customer: I've ordered a meal.");
serveMealAsync();
console.log("B. Customer: While I wait, I can read a book or check my phone!");
console.log("C. Customer: Still waiting for the meal...");