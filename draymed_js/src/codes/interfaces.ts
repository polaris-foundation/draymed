
export interface CodeDescription {
    code: string;
    short: string;
    long: string;
}

export interface CodesCategory {
    category: string;
    values: readonly CodeDescription[];
}

export interface Code {
    name: string;
    value: string;
}
export interface Codes {
    [key: string]: Code;
}

export interface CodesByCategory {
    [key: string]: Codes;
}
