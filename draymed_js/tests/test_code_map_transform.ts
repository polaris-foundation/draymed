import {getCodes} from "../src/codes";

describe('matching descriptive names with code from real data', () => {

    const actualCodes = getCodes();

    test('Short name "dietAndExercise" has long name "Diet and exercise"', () => {
        expect(actualCodes.managementType.dietAndExercise.name).toEqual("Diet and Exercise");
    });

    test('Short name "mixedAfrican" has long name "White and Black African"', () => {
        expect(actualCodes.ethnicity.mixedAfrican.name).toEqual("White and Black African");
    });

    test('Short name "movedOutOfArea" has code "D0000029"', () => {
        expect(actualCodes.closedReason.movedOutOfArea.value).toEqual("D0000029");
    });

    test('Short name "oralMeds" has code "386359008"', () => {
        expect(actualCodes.managementType.oralMeds.value).toEqual("386359008");
    });
});
