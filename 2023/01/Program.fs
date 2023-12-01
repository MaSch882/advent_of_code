open System
open System.IO

let allowedExpressions = ["0";"1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"; "one"; "two"; "three"; "four"; "five"; "six"; "seven"; "eight"; "nine"]
let allowedStartChars = ["o"; "t"; "f"; "s"; "e"; "n"; "0"; "1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let allowedNumbers = ["0"; "1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let numberMapping: Collections.Generic.IDictionary<string, int> = dict["one", 1; "two", 2; "three", 3; "four", 4; "five", 5; "six", 6; "seven", 7; "eight", 8; "nine", 9]

let decodeInputToCalibrationValue (input: string) =
    let charArray = input.ToCharArray() |> Array.filter (Char.IsNumber)

    let first : string = string(charArray.GetValue 0)
    let last: string = string(charArray.GetValue (charArray.Length - 1))

    let resultAsString: string = first + last
    int(resultAsString)


let decodeInputToCalibrationValueWithWords (input:string) =
    let inputAsCharArray = input.ToCharArray()
    let mutable foundExpressions: String list = []

    let mutable substring = ""

    for i in 0..input.Length - 1 do
        substring <- String.Concat([substring; string(inputAsCharArray.[i])])

        if substring.Length = 1 && not (List.contains substring allowedStartChars) then
            substring <- ""
        else 
            if List.contains substring allowedNumbers then
                foundExpressions <- [substring] |> List.append foundExpressions
            else 
                let mutable j: int = i+1
                while substring <> "" && j < input.Length do
                    substring <- String.Concat([substring; string(inputAsCharArray.[j])])
                    if List.contains substring allowedExpressions then 
                        foundExpressions <- [substring] |> List.append foundExpressions
                        substring <- ""
                    j <- j+1
        substring <- ""

    let mutable numbers: int list = []
    for element in foundExpressions do
        if element.Length = 1 then 
            numbers <- [int(element)] |> List.append numbers
        else 
            numbers <- [numberMapping[element]] |> List.append numbers

    let first = numbers[0]
    let last = numbers[numbers.Length-1]

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
