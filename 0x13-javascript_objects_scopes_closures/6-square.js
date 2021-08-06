#!/usr/bin/nodejs
'use strict'
/*
Write a class Square that defines a square and inherits from Square of 5-square.js:

    You must use the class notation for defining your class and extends
    Create an instance method called charPrint(c) that prints the rectangle using the character c
        If c is undefined, use the character X

*/
let SecondSquare = require('./5-square.js');


class Square extends SecondSquare {

    charPrint(c) {

        if (c === undefined || c === 'X') {
            this.print()
        } else {
            
            for (let i = 0; i < this.height;i++) {
                console.log(c.repeat(this.width));
            }
        }
        
    }
}

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

