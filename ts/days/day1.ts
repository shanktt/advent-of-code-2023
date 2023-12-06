export function part1(inputData: string): number {
    const numbers = inputData.split('\n').map(Number);
    let count = 0;

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > numbers[i - 1]) {
            count++;
        }
    }

    return count;
}

export function part2(inputData: string): number {
    const numbers = inputData.split('\n').map(Number);
    return numbers.reduce((sum, current) => sum + current, 0);
}
