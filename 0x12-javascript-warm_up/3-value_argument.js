#!/usr/bin/nodejs

/**
 * Write a script that prints the first argument passed to it:

    If no arguments are passed to the script, print “No argument”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use length

*/

if (process.argv) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
