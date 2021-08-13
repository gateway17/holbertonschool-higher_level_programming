#!/usr/bin/nodejs
'use strict'
/**
 * Write a script that prints x times “C is fun”

    Where x is the first argument of the script
    If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You can use only two console.log
    You must use a loop (while, for, etc.)

*/

if (isNaN(process.argv[2])) {

    console.log("Missing number of occurrences");
} else {
 
    for (let ctr = 0; ctr < parseInt(process.argv[2]); ctr++) {
    
        console.log("C is fun");
   
    }
}