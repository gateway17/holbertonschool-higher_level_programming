#!/usr/bin/nodejs
'use strict';
/*
Write a function that returns the reversed version of a list:

    Prototype: exports.esrever = function (list)
    You are not allow to use the built-in method reverse

*/
exports.esrever = function (list) {
  let Size = list.length;
  Size--;
  const list2 = [];
  for (let Position = 0; Size > -1; Position++, Size--) {
    list2[Position] = list[Size];
  }
  return list2;
};
