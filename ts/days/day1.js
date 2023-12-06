"use strict";
// day1.ts
Object.defineProperty(exports, "__esModule", { value: true });
exports.part2 = exports.part1 = void 0;
/**
 * Counts how many numbers in the input are greater than the previous number.
 *
 * @param inputData - The raw input data as a string.
 * @returns The count of numbers greater than their predecessor.
 */
function part1(inputData) {
    const numbers = inputData.split('\n').map(Number);
    let count = 0;
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > numbers[i - 1]) {
            count++;
        }
    }
    return count;
}
exports.part1 = part1;
/**
 * Calculates the sum of all numbers in the input.
 *
 * @param inputData - The raw input data as a string.
 * @returns The sum of all numbers.
 */
function part2(inputData) {
    const numbers = inputData.split('\n').map(Number);
    return numbers.reduce((sum, current) => sum + current, 0);
}
exports.part2 = part2;
