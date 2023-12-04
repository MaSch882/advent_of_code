open System
open System.IO

let numbers = ["0";"1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let delimiter = "."

let buildMatrixFromInput (filepath: string) =
     filepath 
     |> File.ReadAllLines 
     |> Seq.toList 
     |> List.map (fun line -> line.ToCharArray()) 
     |> Seq.toList
    // for i in 0..lines.Length - 1 do 
    //     for j in 0..9 do
    //         printfn "%c " lines.[i].[j]
    //     printfn "Ende Zeile"

let isRelevant (s: string) =
    (not (List.contains s numbers)) && s <> delimiter

let checkEntry (i: int) (j: int) (matrix: char array list) =
    try
        if isRelevant (string matrix.[i].[j]) then
            true
        else 
            false
    with
        _ -> false 

let isRelevantNumber (i: int) ( j: int) (matrix: char array list)  = 
    // links oben
    if matrix |> checkEntry (i-1) (j-1) then 
        true
    // links
    elif matrix |> checkEntry i (j-1)  then 
        true
    // links unten 
    elif matrix |> checkEntry (i+1) (j-1) then 
        true
    // oben
    elif matrix |> checkEntry (i-1) j then
        true
    // unten 
    elif matrix |> checkEntry (i+1) j then 
        true
    // rechts oben
    elif matrix |> checkEntry (i-1) (j+1) then 
        true
    // rechts
    elif matrix |> checkEntry i (j+1) then 
        true 
    // rechts unten
    elif matrix |> checkEntry (i+1) (j+1) then 
        true
    else 
        false 



let sumAllPartNumbers (matrix: char array list) = 
    let mutable sumOfPartNumbers = 0
    let isRelevant = false

    for i in 0..matrix.Length - 1 do
        let mutable currentNumber = ""
        for j in 0..matrix.[0].Length - 1 do
            let currentChar = string(matrix.[i].[j])
            printfn "char = %s, i = %i, j = %i, relevant = %b" currentChar i j (matrix |> isRelevantNumber i j)
            // if List.contains currentChar numbers then
            //     currentNumber <- String.Concat([currentNumber, string(currentChar)])

                

let fileIsGivenAndExists (arguments: String array) (filepath: string) = 
    arguments.Length = 1 && File.Exists filepath

[<EntryPoint>]
let main argv = 
    if argv.Length = 0 then 
        printfn "Please specify a file!"
        1
    elif argv.Length > 1 then
        printfn "More than one file given!"
        2
    else
        let filepath = argv.[0]
        if filepath |> fileIsGivenAndExists argv then 
            printfn "Processing %s" filepath
            let matrix = filepath |> buildMatrixFromInput 
            let sumOfAllPartNumbers = matrix |> sumAllPartNumbers
            0
        else    
            printfn "File does not exist!"
            2   