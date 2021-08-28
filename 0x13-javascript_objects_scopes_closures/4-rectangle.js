#!/usr/bin/nodejs
'use strict';
/*
Write a class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the character X
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const Character = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(Character.repeat(this.width));
    }
  }

  rotate () {
    this.temporal = this.height;
    this.height = this.width;
    this.width = this.temporal;
    delete (this.temporal);
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
