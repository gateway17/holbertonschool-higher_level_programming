#!/usr/bin/nodejs
'use strict';
/*
Write a function that returns the number of occurrences in a list:

    Prototype: exports.nbOccurences = function (list, searchElement)

*/
exports.nbOccurences = function (list, searchElement) {
  let Counter = 0;

  for (const Iterator in list) {
    if (list[Iterator] === searchElement) {
      Counter++;
    }
  }
  return Counter;
};
