#!/usr/bin/nodejs
'use strict'
/**
 * Write a script that searches the second biggest integer in the list of arguments.

    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
    You must use console.log(...) to print all output
    You are not allowed to use var

 */

let new_list = process.argv.slice(2, -1);
console.log(new_list)