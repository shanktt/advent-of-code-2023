import fs from 'fs';
import path from 'path';
import yargs from 'yargs';

async function main() {
    const argv = yargs
        .option('days', {
            alias: 'd',
            describe: 'Days to run',
            type: 'array',
            demandOption: true
        })
        .option('sample', {
            alias: 's',
            describe: 'Use sample input',
            type: 'boolean',
            default: false
        })
        .help()
        .argv as { days: number[]; sample: boolean };;

    for (const day of argv.days as number[]) {
        try {
            // Dynamically import the day module using template literals
            const dayModule = await import(`./days/day${day}`);
            // Construct the input path using template literals
            const inputPath = path.join(__dirname, `inputs/day${day}${argv.sample ? '.sample' : ''}.txt`);
            // Read the input data
            const inputData = fs.readFileSync(inputPath, 'utf8');

            console.log(`Results for Day ${day}:`);
            console.log('Part 1:', dayModule.part1(inputData));
            console.log('Part 2:', dayModule.part2(inputData));

        } catch (error) {
            console.error(`Day ${day} is not available or there was an error:`, error);
        }
    }
}

main();
