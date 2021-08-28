#!/usr/bin/nodejs
'use strict';

/**
 * Write a script that prints the addition of 2 integers

    The first argument is the first integer
    The second argument is the second integer
    You have to define a function with this prototype: function add(a, b)
    You must use console.log(...) to print all output
    You are not allowed to use var

*/

function add (a, b) {
  // Convert from string to int and print it
  console.log(parseInt(a) + parseInt(b));
}
// making it better readable
const num1 = process.argv[2];
const num2 = process.argv[3];
// Call function
add(num1, num2);
