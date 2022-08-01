import {CodeDescription, CodesCategory, CodesByCategory} from "./interfaces";

// Source reference: https://hisk.io/javascript-snake-to-camel/
const snakeToCamel = (str: string) => str.replace(
    /([-_][a-z])/g,
    (group: string) => group.toUpperCase()
                    .replace('-', '')
                    .replace('_', '')
);

function transformCodes(sourceCodes: CodesCategory[]): CodesByCategory {

    const outputCodes: CodesByCategory = {};

    sourceCodes.forEach((category: CodesCategory) => {

        const alias: string = snakeToCamel(category.category);
        outputCodes[alias] = {};

        category.values.forEach((item: CodeDescription) => {

            outputCodes[alias][item["short"]] = {
                name: item.long,
                value: item.code
            };
        });

    });

    return outputCodes;
}

export function getCodes(): CodesByCategory {

    const sourceCodes = require('../data/master_codes.json');

    return transformCodes(sourceCodes);
}
