#!/usr/bin/nodejs
'use strict'

/**
 * Write a script that computes and prints a factorial

    The first argument is integer (argument can be cast as integer) used for computing the factorial
    Factorial of NaN is 1
    You must do it recursively
    You must use a function
    You must use console.log(...) to print all output
    You are not allowed to use var


*/

function factorial(i) {

    if (i == 1) {
        return 1
    } else {
        return i * factorial(i - 1)
    }
}

if (process.argv[2] === undefined) {
    process.argv[2] = 1
}

console.log(factorial(parseInt(process.argv[2])))