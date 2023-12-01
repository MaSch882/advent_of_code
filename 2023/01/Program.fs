open System
open System.IO

let allowedExpressions = ["0";"1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"; "one"; "two"; "three"; "four"; "five"; "six"; "seven"; "eight"; "nine"]
let allowedStartChars = ["o"; "t"; "f"; "s"; "e"; "n"; "0"; "1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let allowedNumbers = ["0"; "1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let numberMapping: Collections.Generic.IDictionary<string, int> = dict["one", 1; "two", 2; "three", 3; "four", 4; "five", 5; "six", 6; "seven", 7; "eight", 8; "nine", 9]

// Part 1
let decodeInputToCalibrationValue (input: string) =
    let charArray = input.ToCharArray() |> Array.filter (Char.IsNumber)

    let first : string = string(charArray.GetValue 0)
    let last: string = string(charArray.GetValue (charArray.Length - 1))

    let resultAsString: string = first + last
    int(resultAsString)


// Part 2
let concatNextChar (substring: string) (index: int) (chars: char array) = 
    String.Concat([substring; string(chars.[index])])

let substringDoesNotStartWithAllowedChar (substring: string) = 
    substring.Length = 1 && not (List.contains substring allowedStartChars)

let substringStartsWithNumber (substring: string) =
    List.contains substring allowedNumbers

let appendToFoundExpressions (foundExpressions: String list) (expression: string)  = 
    [expression] |> List.append foundExpressions

let isSubstringEmpty (substring: string) =
    substring <> ""

let isAllowedExpression (index: int) (input: string) (substring: string) =
    substring |> isSubstringEmpty && index < input.Length

let decodeInputToCalibrationValueWithWords (input:string) =
    let inputAsCharArray = input.ToCharArray()
    let mutable foundExpressions: String list = []

    let mutable substring = ""

    for i in 0..input.Length - 1 do
        substring <- concatNextChar substring i inputAsCharArray

        if substring |> substringDoesNotStartWithAllowedChar then
            substring <- ""
        
        if substring |> substringStartsWithNumber then
            foundExpressions <- substring |> appendToFoundExpressions foundExpressions
        else 
            // Iteriere durch den Rest der Zeichen und pruefe, ob was passendes dabei ist.
            let mutable j: int = i+1
            while substring |> isAllowedExpression j input do
                substring <- String.Concat([substring; string(inputAsCharArray.[j])])
                if List.contains substring allowedExpressions then 
                    foundExpressions <- substring |> appendToFoundExpressions foundExpressions
                    substring <- ""
                j <- j+1
        substring <- ""

    // Baue aus den gefundenen Ausdruecken Zahlenwerte.
    let mutable numbers: int list = []
    for element in foundExpressions do
        if element.Length = 1 then 
            numbers <- [int(element)] |> List.append numbers
        else 
            numbers <- [numberMapping[element]] |> List.append numbers

    // Hole ersten und letzten Zahlenwert.
    let first = numbers[0]
    let last = numbers[numbers.Length-1]

    // Baue zweistelligen Calibration Value.
    last + 10*first


let processAllInputs (filepath: string)  =
    let rows = File.ReadAllLines filepath
    let mutable sum = 0
    rows 
    // |> Array.map decodeInputToCalibrationValue
    |> Array.map decodeInputToCalibrationValueWithWords
    |> Array.sum


[<EntryPoint>]
let main argv = 
    if argv.Length = 1 then 
        let filePath = argv.[0]
        if File.Exists filePath then
            printfn "Processing %s" filePath
            let result = processAllInputs filePath
            
            printfn "%i" result
            0
        else    
            printfn "File does not exist!"
            2    
    else 
        printfn "Please specify a file!"
        1
