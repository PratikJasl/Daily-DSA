//Approach1: O(1)
//Step1: Convert string to lowercase.
//Step2: Remove all alphanumeric characters from it.
//Step3: store it in a varibale.
//Step4: reverse the string and compare both strings.

// var isPalindrome = function(s) {
//     let s1 = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, "");
//     let s2 = s1.split('').reverse().join('');
//     console.log(s1, s2);
//     if(s1 == s2){
//         return true;
//     }else{
//         return false;
//     }
// };

// let s = "String@$";
// isPalindrome(s);

