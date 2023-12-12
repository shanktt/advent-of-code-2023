import { match } from "assert";

export function part1(inputData: string): number {
    const regex: RegExp = /(\d+) (\w+)/g;
    return inputData.split("\n").reduce((sum,line) => {
        let maxColors: {[key:string]: number} = {"r": 0, "b": 0, "g": 0};
        [...line.matchAll(regex)].forEach((match) => {
            const num = Number(match[0])
            const color = match[1]

            maxColors[color[0]] = Math.max(maxColors[color[0]], num)
        })
        return sum + 
    },0);
}

export function part2(inputData: string): number {
    return 0;
}
