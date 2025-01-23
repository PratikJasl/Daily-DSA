

//Apporach: O(n)
//Step1: Create a function to validate palindrome.
//Step2: The function should compare left and right element.
//Step3: If they are equal it should expand outwards.
//Step4: It should store the string which was equal.
//Step5: we will call this function twice for even and odd strings.
//Step6: For even string we need to pass same element in left and right.
//Step7: For odd string pass i and i+1 in left and right.
//Step8: Compare the longest between left, right and longest.

var longestPalindrome = function(s) {
    let longest = ''

    function validPalindrome(left, right, s){
        while(left >= 0 && right < s.length && s[left] === s[right]){
            left--;
            right++;
        }
        return s.slice(left+1, right);
    }

    for(let i = 0; i < s.length; i ++){
        let evenPal = validPalindrome(i, i, s);
        let oddPal = validPalindrome(i, i+1, s);
        console.log(evenPal, oddPal);
        if(evenPal.length > longest.length){
            longest = evenPal
        }
        
        if( oddPal.length > longest.length){
            longest = oddPal
        }
    }
    return longest;
}