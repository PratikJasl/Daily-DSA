//Quesiton: Return The Element that is the first reoccuring.

//Arr1 = [2,5,1,2,3,5,1,2,4]
//Output = 2 since it was the first to re-occur.

//Arr2 = [2,1,1,2,3,5,1,2,4]
//Output = 1 since it was the first to re-occur.

//Approach1: O(n)
//Step1: Create a new Object.
//Step2: Iterate through the original array.
//Step3: Check if that element already exists in the new Object.
//Step4: If it does return the element.
//Step5: If it does not add the element to the new array.

function FindReoccuring(arr){
    if(arr.length > 1){
        let Obj = {};
        for(let i = 0; i < arr.length; i ++){
            if(Obj[arr[i]] !== undefined){
                return arr[i];
            }
            else{
                Obj[arr[i]] = i
            }
            console.log(Obj);
        }
        return "no re-occuring element"
    }
    return "invalid array length"
}

console.log(FindReoccuring([2,5,1,2,3,5,1,2,4]));



