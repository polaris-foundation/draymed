
function hashFile(fileName: string): string {
    const crypto = require('crypto');
    const fs = require('fs');
    const src_file_buffer = fs.readFileSync(fileName);
    const sum = crypto.createHash('sha256');
    sum.update(src_file_buffer);
    return sum.digest('hex');
}

describe('check that local copy of master codes file ', () => {

    test('is identical with the source file', () => {

        const sourceFile = __dirname + "/../../master_codes.json";
        const hashSource = hashFile(sourceFile);
        console.log(hashSource);

        const targetFile = __dirname + "/../src/data/master_codes.json";
        const hashTarget = hashFile(targetFile);
        console.log(hashTarget);

        expect(hashSource).toEqual(hashTarget);
    });

});
