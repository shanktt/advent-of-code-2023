export function part1(inputData: string): number {
    const lines = inputData.split('\n')

    let sum = 0;
    lines.forEach(line => {
        const digits = line.split('')
            .filter((char) => char >= "0" && char <= "9")
            .map(Number)
        sum += ((digits[0]*10) + digits[digits.length - 1]);
    });
    
    return sum;
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


    let sum = 0
    lines.forEach((line) => {
        let cur_digits: number[] = [];
        for (let i = 0; i < line.length; i++) {
            Object.keys(strToInt)
                .map((str) => [str,strToInt[str]] as [string,number])
                .forEach((digit_int) => {
                    const digit = digit_int[0]
                    if (line.substring(i,i+digit.length) == digit) {
                        cur_digits.push(Number(strToInt[line.substring(i,i+digit.length)]))
                    } else if (line[i] >= "0" && line[i] <= "9") {
                        cur_digits.push(Number(line[i]))
                    }
                })
        };
        sum += ((cur_digits[0]*10) + cur_digits[cur_digits.length - 1]);
    });

    return sum;
}
