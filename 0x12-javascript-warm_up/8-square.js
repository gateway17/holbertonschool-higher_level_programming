#!/usr/bin/nodejs
'use strict'

/**
 * Write a script that prints a square

    The first argument is the size of the square
    If the first argument can’t be converted to an integer, print “Missing size”
    You must use the character X to print the square
    You must use console.log(...) to print all output
    You are not allowed to use var
    You must use a loop (while, for, etc.)

 */

if (isNaN(process.argv[2])) {

    console.log("Missing size");
} else {

    for (let i = 0; i < parseInt(process.argv[2]); i++) {
        
        let char = 'X';
        console.log(char.repeat(parseInt(process.argv[2])))
    }
}