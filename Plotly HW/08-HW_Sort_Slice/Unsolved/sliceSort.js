// An unsorted array
numArray = [9.9, 6.1, 17.1, 22.7, 4.6, 8.7, 7.2];

// Sort the array in descending order and assign the results to a variable
numArray.sort(function comparefunction(first,second){
    return second - first;
});

console.log(numArray);

// Print the results to the console

// Sort the array in descending order using an arrow function
// and assign the results to a variable and print to the console
numArray.sort((first, second) => second - first);
console.log(numArray);

// Reverse the array order
var reversedArray = numArray.reverse()
console.log(reversedArray);


// Sort the array in ascending order using an arrow function
var douglas = numArray.sort((first, second) => first - second);
console.log(douglas);

// Slice the first five elements of the sortedAscending array, assign to a variable
var firstfive = douglas.slice(0,5)
console.log(firstfive)