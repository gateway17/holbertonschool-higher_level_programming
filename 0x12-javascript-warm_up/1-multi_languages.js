#!/usr/bin/node

/*
Write a script that prints 3 lines:

    The first line: “C is fun”
    The second line: “Python is cool”
    The third line: “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var

*/

const List = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let Index;
for (Index in List) {
  console.log(List[Index]);
}
