export function part1(inputData: string): number {
    const lines = inputData.split('\n')

    return lines.reduce((sum,line) => {
        const digits = line.split('')
            .filter((char) => char >= "0" && char <= "9")
            .map(Number)
        return sum+((digits[0]*10) + digits[digits.length - 1]);
    },0);
    
}
export function part2(inputData: string): number {
    const lines = inputData.split('\n')

    const strToInt: { [key: string]: number } = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    };

    return lines.reduce((sum,line) => {
        let cur_digits: number[] = [];
        for (let i = 0; i < line.length; i++) {
            Object.entries(strToInt).forEach(([str,int]) => {
                if (line.substring(i,i+str.length) == str) {
                    cur_digits.push(int)
                } else if (line[i] >= "0" && line[i] <= "9") {
                    cur_digits.push(Number(line[i]))
                }
            });
        };
        return sum+((cur_digits[0]*10) + cur_digits[cur_digits.length - 1]);
    },0);
}
