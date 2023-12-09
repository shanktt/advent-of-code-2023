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
    // const strToInt = {
    //     "one": 1,
    //     "two": 2,
    //     "three": 3,
    //     "four": 4,
    //     "five": 5,
    //     "six": 6,
    //     "seven": 7,
    //     "eight": 8,
    //     "nine": 9,
    // }
    const lines = inputData.split('\n')

    const strToInt = {
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
        let cur_digits = [];
        for (let i = 0; i < line.length; i++) {
            Object.entries(strToInt).forEach((digit,int) => {
                const len_digit = digit.length;

                if (digit.substring(i, i+len_digit) === digit) {
                    cur_digits.push()
                }
            });
        }
    });

    return sum;
}
