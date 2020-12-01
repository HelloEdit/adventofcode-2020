import { readFileSync } from "fs";

/**
 * Find the two entries that sum to 2020 and then multiply those two numbers together.
 * @param {Array<number>} numbers availables numbers
 */
function ex1(numbers) {
  for (const first of numbers) {
    for (const second of numbers) {
      if (first + second == 2020) return console.log(`1st: ${first * second}`);
    }
  }
}

/**
 * Find the three entries that sum to 2020 and then multiply those three numbers together.
 * @param {Array<number>} numbers availables numbers
 */
function ex1bis(numbers) {
  for (const first of numbers) {
    for (const second of numbers) {
      const middle = first + second;
      if (middle >= 2020) continue;
      for (const third of numbers) {
        if (middle + third == 2020)
          return console.log(`2nd: ${first * second * third}`);
      }
    }
  }
}

const numbers = readFileSync("./day01/input.txt", "utf-8")
  .split("\n")
  .map((i) => Number.parseInt(i));

ex1(numbers);
ex1bis(numbers);
