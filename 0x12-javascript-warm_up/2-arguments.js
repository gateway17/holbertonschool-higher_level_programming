#!/usr/bin/nodejs


if (process.argv.lenght === 2) {
    console.log('No argument');
}
else if (process.argv.lenght === 3) {
    console.log('Argument found');
}
else if (process.argv.lenght > 4) {
    console.log('Arguments found');
}